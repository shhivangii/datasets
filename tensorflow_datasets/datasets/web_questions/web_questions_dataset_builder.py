# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""WebQuestions Benchmark for Question Answering."""

import json
import re

from etils import epath
import tensorflow_datasets.public_api as tfds
_SPLIT_DOWNLOAD_URL = {
    'train': 'https://worksheets.codalab.org/rest/bundles/0x4a763f8cde224c2da592b75f29e2f5c2/contents/blob/',
    'test': 'https://worksheets.codalab.org/rest/bundles/0xe7bac352fce7448c9ef238fb0a297ec2/contents/blob/',
}


class Builder(tfds.core.GeneratorBasedBuilder):
  """WebQuestions Benchmark for Question Answering."""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'url': tfds.features.Text(),
            'question': tfds.features.Text(),
            'answers': tfds.features.Sequence(tfds.features.Text()),
        }),
        supervised_keys=None,
        homepage='https://worksheets.codalab.org/worksheets/0xba659fe363cb46e7a505c5b6a774dc8a',
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    file_paths = dl_manager.download(_SPLIT_DOWNLOAD_URL)

    return [
        tfds.core.SplitGenerator(
            name=split, gen_kwargs={'file_path': file_path}
        )
        for split, file_path in file_paths.items()
    ]

  def _generate_examples(self, file_path):
    """Parses split file and yields examples."""

    def _target_to_answers(target):
      target = re.sub(r'^\(list |\)$', '', target)
      return [
          ''.join(ans)
          for ans in re.findall(
              r'\(description (?:"([^"]+?)"|([^)]+?))\)\w*', target
          )
      ]

    with epath.Path(file_path).open() as f:
      examples = json.load(f)
      for i, ex in enumerate(examples):
        yield i, {
            'url': ex['url'],
            'question': ex['utterance'],
            'answers': _target_to_answers(ex['targetValue']),
        }