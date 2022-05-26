#导入需要的包

import tensorflow_hub as hub
import tensorflow_text as text
import os
import tensorflow as tf

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
GRAND_DIR_PATH = os.path.dirname(DIR_PATH)

class BertvecModel():

    def __init__(self):
        self.embedding_model = tf.saved_model.load("E:\gitHome\github\QCNLP\qcnlp\word_embedding\BERT-Model")

    def tf_cosine_distance(tensor1, tensor2):
        """
        consine相似度：用两个向量的夹角判断两个向量的相似度，夹角越小，相似度越高，得到的consine相似度数值越大
        数值范围[-1,1],数值越大越相似。
        :param tensor1:
        :param tensor2:
        :return:
        """
        # 把张量拉成矢量，这是我自己的应用需求
        tensor1 = tf.reshape(tensor1, shape=(1, -1))
        tensor2 = tf.reshape(tensor2, shape=(1, -1))

        # 求模长
        tensor1_norm = tf.sqrt(tf.reduce_sum(tf.square(tensor1)))
        tensor2_norm = tf.sqrt(tf.reduce_sum(tf.square(tensor2)))

        # 内积
        tensor1_tensor2 = tf.reduce_sum(tf.multiply(tensor1, tensor2))
        cosin = tensor1_tensor2 / (tensor1_norm * tensor2_norm)

        return cosin

    def __call__(self):
        return self.embedding_model
