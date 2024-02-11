# Compression Benchmark
A simple and crude program to benchmark different standard compression methods.
It measures the compression time, decompression time and the compressed filesize

## Setup & Running
1. Setup some sample data similar to the following
```
git clone https://github.com/facebook/react.git src
```

2. Create a file with the name filelist.txt that contains a list of files to be used for sample data
The following will create filelist.txt that points to 300 JavaScript files located within ./src
```
find ./src -name '*.js' | sort | head -n 300 > filelist.txt
```

3. Run the python script

```
python benchmark.py
```

## Note
This was only tested on my personal Macbook Pro running MacOS Sonoma (14.2.1)
