## freesound

freesound is a dataset of 5000000 audio and caption.

### Download the metadata

`wget https://huggingface.co/datasets/Chr0my/freesound.org/resolve/main/freesound_parquet.parquet`

### Download the audios with audio2dataset

Run this command. It will download the cc3m dataset as subsampled audios in the webdataset format.

```
audio2dataset --url_list freesound_parquet.parquet --input_format "parquet"\
         --url_col "download_url" --caption_col "description" --output_format webdataset\
           --output_folder freesound --processes_count 16 --thread_count 64\
             --enable_wandb True
```

### Benchmark
