import tensorflow as tf
import re
import json
from data_process import preprocess_img, preprocess_img_from_Url
from models.resnet50 import ResNet50
from keras.layers import Dense, Dropout, BatchNormalization, GlobalAveragePooling2D
from keras.models import Model
import numpy as np
from keras import regularizers
from tensorflow.python.keras.backend import set_session

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
config.gpu_options.per_process_gpu_memory_fraction = 0.7
sess = tf.Session(config=config)

# 全局配置文件
tf.app.flags.DEFINE_integer('num_classes', 40, '垃圾分类数目')
tf.app.flags.DEFINE_integer('input_size', 224, '模型输入图片大小')
tf.app.flags.DEFINE_integer('batch_size', 16, '图片批处理大小')

FLAGS = tf.app.flags.FLAGS
h5_weights_path = './output/best.h5'


## 增加最后输出层
def add_new_last_layer(base_model, num_classes):
    x = base_model.output
    x = GlobalAveragePooling2D(name='avg_pool')(x)
    x = Dropout(0.5, name='dropout1')(x)
    # x = Dense(1024,activation='relu',kernel_regularizer= regularizers.l2(0.0001),name='fc1')(x)
    # x = BatchNormalization(name='bn_fc_00')(x)
    x = Dense(512, activation='relu', kernel_regularizer=regularizers.l2(0.0001), name='fc2')(x)
    x = BatchNormalization(name='bn_fc_01')(x)
    x = Dropout(0.5, name='dropout2')(x)
    x = Dense(num_classes, activation='softmax')(x)
    model = Model(inputs=base_model.input, outputs=x)
    return model


# 加载模型
def model_fn(FLAGS):
    # K.set_learning_phase(0)
    # setup model
    base_model = ResNet50(weights="imagenet",
                          include_top=False,
                          pooling=None,
                          input_shape=(FLAGS.input_size, FLAGS.input_size, 3),
                          classes=FLAGS.num_classes)
    for layer in base_model.layers:
        layer.trainable = False

    # if FLAGS.mode == 'train':
    # K.set_learning_phase(1)
    model = add_new_last_layer(base_model, FLAGS.num_classes)

    # print(model.summary())
    # print(model.layers[84].name)
    # exit()

    # Adam = adam(lr=FLAGS.learning_rate,clipnorm=0.001)
    model.compile(optimizer="adam", loss='categorical_crossentropy', metrics=['accuracy'])
    return model


# 加载封装测试模型
def init_artificial_neural_network(sess):
    set_session(sess)
    model = model_fn(FLAGS)
    model.load_weights(h5_weights_path, by_name=True)
    return model


## 测试图片
def prediction_result_from_img(model, imgurl):
    # 加载分类数据
    try:
        with open("./garbage_classify/garbage_classify_rule.json", 'r', encoding='utf-8') as load_f:
            load_dict = json.load(load_f)
        if re.match(r'^https?:/{2}\w.+$', imgurl):
            test_data = preprocess_img_from_Url(imgurl, FLAGS.input_size)
        else:
            test_data = preprocess_img(imgurl, FLAGS.input_size)

        if test_data != 0:
            tta_num = 5
            predictions = [0 * tta_num]
            for i in range(tta_num):
                x_test = test_data[i]
                x_test = x_test[np.newaxis, :, :, :]
                prediction = model.predict(x_test)[0]
                # print(prediction)
                predictions += prediction
            pred_label = np.argmax(predictions, axis=0)
            print('-------深度学习垃圾分类预测结果----------')
            print(pred_label)
            print(load_dict[str(pred_label)])
            print('-------深度学习垃圾分类预测结果--------')
            return load_dict[str(pred_label)]
        else:
            print('-------文件读取错误----------')
            return False
    except Exception as e:
        print('发生了异常-prediction：', e)

# if __name__ == "__main__":

# test_img('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1572815106329&di=bf107149c926f3114c25e74ef3b79275&imgtype=0&src=http%3A%2F%2Fwww.yejs.com.cn%2Fuserfiles%2FDSC05339.JPG')
# test_img('./test_data/new_img1835.jpg')
