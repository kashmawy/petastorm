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
import pytest

from petastorm.reader import Reader


def test_dataset_url_must_be_string():
    with pytest.raises(ValueError):
        Reader(dataset_url=None)

    with pytest.raises(ValueError):
        Reader(dataset_url=123)

    with pytest.raises(ValueError):
        Reader(dataset_url=[])
