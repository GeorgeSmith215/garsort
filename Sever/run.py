from prediction import prediction_result_from_img,init_artificial_neural_network
import tensorflow as tf
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
config.gpu_options.per_process_gpu_memory_fraction = 0.7
sess = tf.Session(config=config)


if __name__ == '__main__':
    model = init_artificial_neural_network(sess)
    while True:
        try:
            img_url = input("请输入图片地址:")
            print('您输入的图片地址为：' + img_url)
            res = prediction_result_from_img(model, img_url)
        except Exception as e:
            print('发生了异常：', e)
