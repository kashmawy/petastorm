#  Copyright (c) 2017-2018 Uber Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import division

import argparse
import glob
import json
import os

import cv2
from pyspark.sql import SparkSession
from six.moves.urllib.request import urlopen  # pylint: disable=import-error

from examples.imagenet.schema import ImagenetSchema
from petastorm.etl.dataset_metadata import materialize_dataset
from petastorm.unischema import dict_to_spark_row
from petastorm.reader import Reader
from petastorm.tf_utils import tf_tensors


def _arg_parser():
    parser = argparse.ArgumentParser(description=__doc__, add_help=False,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--dataset-path', type=str, required=True,
                        help='The dataset path.')

    return parser

def read_dataset(path):
    with Reader(schema_fields=[ImagenetSchema.noun_id, ImagenetSchema.text, ImagenetSchema.image],
                dataset_url=path,
                shuffle=True) as reader:
        reader_tensors = tf_tensors(reader)
        print("Here")

if __name__ == '__main__':
    args = _arg_parser().parse_args()
    read_dataset(args.dataset_path)
