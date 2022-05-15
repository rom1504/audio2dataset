"""subsampler module handle audio resizing"""


class Subsampler:
    """
    subsample audios
    Expose a __call__ method to be used as a callable object

    Should be used to subsample one audio at a time

    """

    def __init__(
        self,
        disable_all_reencoding=False,
    ):
        self.disable_all_reencoding = disable_all_reencoding

    def __call__(self, audio_stream):
        """
        input: an audio stream
        output: audio_str, width, height, original_width, original_height, err
        """
        try:
            if self.disable_all_reencoding:
                return audio_stream.read(), None, None, None, None, None

            return audio_stream.read(), None, None, None, None, None

        except Exception as err:  # pylint: disable=broad-except
            return None, None, None, None, None, str(err)
