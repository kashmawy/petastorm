# ImageNet Example

This is an example of how to use Petastorm with ImageNet. This will show how to extract the dataset, use schema and use tensorflow with petastorm.

## Getting the data

Get the dataset from ImageNet at http://www.image-net.org/.
The format of the dataset should be folders, each starting with n and under that folder there will be a images for that specific noun.


## Generating the dataset from ImageNet

Following that, the following command should be run in order to extract the dataset and define the schema to be used:
```python examples/imagenet/generate_petastorm_imagenet.py -i /home/kash/image_net/ImageNet-downloader/sample/ -o file:///tmp/imagenet_dataset```

This will extract the dataset from ImageNet as defined by the following schema:
```
ImagenetSchema = Unischema('ImagenetSchema', [
    UnischemaField('noun_id', np.string_, (), ScalarCodec(StringType()), False),
    UnischemaField('text', np.string_, (), ScalarCodec(StringType()), False),
    UnischemaField('image', np.uint8, (None, None, 3), CompressedImageCodec('png'), False),
])
```

In this schema, we have three fields for each entry. The noun_id which is a string, the text which is a string and the image which is a PNG of shape (None, None, 3).

## Reading the dataset

