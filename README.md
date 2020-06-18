

Image splitter merger used for splitting the images in to smaller chunks and can be send and downloaded as chunks
having less network bandwidth and can be merger to get a original file.

## Splitter
Splits the images into chunks of smaller sizes and stores the hash value.

## Usage

  ```bash
    python run.py -s -b split size in bytes(default=100MB) binary_file
  ```

  
 ## Merger
Merges the splitted images into the original size.

## Usage

   ```bash
    python run.py -m  -i folder_path(splitted images) - o out_file_name
  ```
