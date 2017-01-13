#Copyright (C) 2016 Paolo Galeone <nessuno@nerdz.eu>
#
#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, you can obtain one at http://mozilla.org/MPL/2.0/.
#Exhibit B is not attached; this software is compatible with the
#licenses expressed under Section 1.12 of the MPL v2.
"""Define the interface to implement to work with detectors"""

import abc


class Detector(object, metaclass=abc.ABCMeta):
    """Detector is the interface that detectors must implement"""

    @abc.abstractmethod
    def get(self, images, num_classes, train_phase=False, l2_penalty=0.0):
        """ define the model with its inputs.
        Use this function to define the model in training and when exporting the model
        in the protobuf format.

        Args:
            images: model input
            num_classes: number of classes to predict
            train_phase: set it to True when defining the model, during train
            l2_penalty: float value, weight decay (l2) penalty

        Returns:
            is_training_: tf.bool placeholder enable/disable training ops at run time
            logits: the unscaled prediction for a class specific detector
            bboxes: the predicted coordinates for every detected object in the input image
                    this must have the same number of rows of logits

        """
        raise NotImplementedError(
            'users must define get_model to use this base class')

    @abc.abstractmethod
    def loss(self, logits, bboxes, labels, coordinates):
        """Return the loss operation between logits and labels
        Args:
            logits: Logits from inference().
            bboxes: Bboxes from inference().
            labels: Labels from distorted_inputs or inputs(). 1-D tensor
                    of shape [batch_size]
            coordinates: Ground truth coordinates from distorted_inputs or inputs().
        Returns:
            Loss tensor of type float.
        """
        raise NotImplementedError(
            'users must define loss to use this base class')
