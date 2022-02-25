<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="media_sum" />
  <meta itemprop="description" content="This large-scale media interview dataset contains 463.6K transcripts with&#10;abstractive summaries, collected from interview transcripts and overview /&#10;topic descriptions from NPR and CNN.&#10;&#10;**Please restrict your usage of this dataset to research purpose only.**&#10;&#10;And please cite our paper:&#10;**[MediaSum: A Large-scale Media Interview Dataset for Dialogue Summarization](https://arxiv.org/abs/2103.06410)**&#10;&#10;## Ethics&#10;&#10;We have used only the publicly available transcripts data from the media&#10;sources and adhere to their only-for-research-purpose guideline.&#10;&#10;As media and guests may have biased views, the transcripts and summaries will&#10;likely contain them. The content of the transcripts and summaries only reflect&#10;the views of the media and guests, and should be viewed with discretion.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;media_sum&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/media_sum" />
  <meta itemprop="sameAs" content="https://github.com/zcgzcgzcg1/MediaSum" />
  <meta itemprop="citation" content="@article{zhu2021mediasum,&#10;  title={MediaSum: A Large-scale Media Interview Dataset for Dialogue Summarization},&#10;  author={Zhu, Chenguang and Liu, Yang and Mei, Jie and Zeng, Michael},&#10;  journal={arXiv preprint arXiv:2103.06410},&#10;  year={2021}&#10;}" />
</div>

# `media_sum`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

Warning: Manual download required. See instructions below.

*   **Description**:

This large-scale media interview dataset contains 463.6K transcripts with
abstractive summaries, collected from interview transcripts and overview / topic
descriptions from NPR and CNN.

**Please restrict your usage of this dataset to research purpose only.**

And please cite our paper:
**[MediaSum: A Large-scale Media Interview Dataset for Dialogue Summarization](https://arxiv.org/abs/2103.06410)**

## Ethics

We have used only the publicly available transcripts data from the media sources
and adhere to their only-for-research-purpose guideline.

As media and guests may have biased views, the transcripts and summaries will
likely contain them. The content of the transcripts and summaries only reflect
the views of the media and guests, and should be viewed with discretion.

*   **Homepage**:
    [https://github.com/zcgzcgzcg1/MediaSum](https://github.com/zcgzcgzcg1/MediaSum)

*   **Source code**:
    [`tfds.summarization.media_sum.MediaSum`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/summarization/media_sum/media_sum.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `4.11 GiB`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    manual_dir should contain the files:

    *   news_dialogue.json
    *   train_val_test_split.json

The files can be downloaded and extracted from the dataset's GitHub page:
https://github.com/zcgzcgzcg1/MediaSum/tree/main/data

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 10,000
`'train'` | 443,596
`'val'`   | 10,000

*   **Features**:

```python
FeaturesDict({
    'date': Text(shape=(), dtype=tf.string),
    'id': Text(shape=(), dtype=tf.string),
    'program': Text(shape=(), dtype=tf.string),
    'speaker': Sequence(Text(shape=(), dtype=tf.string)),
    'summary': Text(shape=(), dtype=tf.string),
    'url': Text(shape=(), dtype=tf.string),
    'utt': Sequence(Text(shape=(), dtype=tf.string)),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('utt', 'summary')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

*   **Citation**:

```
@article{zhu2021mediasum,
  title={MediaSum: A Large-scale Media Interview Dataset for Dialogue Summarization},
  author={Zhu, Chenguang and Liu, Yang and Mei, Jie and Zeng, Michael},
  journal={arXiv preprint arXiv:2103.06410},
  year={2021}
}
```
