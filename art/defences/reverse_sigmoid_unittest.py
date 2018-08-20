from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

import numpy as np
from keras.models import Model
from keras.layers import Input, Activation

from art.defences.reverse_sigmoid import ReverseSigmoid
from art.classifiers import KerasClassifier


class TestReverseSigmoid(unittest.TestCase):
    def test_keras_reverse_sigmoid(self):
        xval = np.array([[0, 1.0, 0, 0, 0]])
        x = Input([5])
        y = Activation("softmax")(x)
        m0 = KerasClassifier(clip_values=[0, 1.0], model=Model(inputs=[x], outputs=[y]))
        rs = ReverseSigmoid()
        m1 = rs(m0)
        yval = m1.predict(xval)
        self.assertTrue(xval.argmax(axis=1)==yval.argmax(axis=1))
        self.assertTrue(np.all(xval != yval))


if __name__ == '__main__':
    unittest.main()

