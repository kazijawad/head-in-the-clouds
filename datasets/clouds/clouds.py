import tensorflow_datasets as tfds

class Clouds(tfds.core.GeneratorBasedBuilder):
    VERSION = tfds.core.Version("1.0.0")
    RELEASE_NOTES = {"1.0.0": "Initial release."}

    def _info(self) -> tfds.core.DatasetInfo:
        """Returns the dataset metadata."""
        # TODO(clouds): Specifies the tfds.core.DatasetInfo object
        return tfds.core.DatasetInfo(
            builder=self,
            features=tfds.features.FeaturesDict({
                "image": tfds.features.Image(shape=(512, 512, 3)),
            }),
            supervised_keys=None
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        """Returns SplitGenerators."""
        path = dl_manager.download_and_extract("https://datasets.kazijawad.com/clouds.zip")
        return {
            "train": self._generate_examples(path / "clouds"),
        }

    def _generate_examples(self, path):
        """Yields examples."""
        for p in path.glob("*.jpg"):
            yield p.name, {"image": p}
