import subprocess
import time
import os

# Base directory for compressed and decompressed files
base_dir = "compressed"

# Compression commands with corrected archive paths
compress_commands = {
    "gzip": f"tar --gzip -cf {base_dir}/archive.tar.gz -T filelist.txt",
    "bzip2": f"tar --bzip2 -cf {base_dir}/archive.tar.bz2 -T filelist.txt",
    "xz": f"tar --xz -cf {base_dir}/archive.tar.xz -T filelist.txt",
    "lz4": f"tar --lz4 -cf {base_dir}/archive.tar.lz4 -T filelist.txt",
    "zstd": f"tar --zstd -cf {base_dir}/archive.tar.zst -T filelist.txt",
    "zip9": f"zip -9 -o -q {base_dir}/archive9.zip -@ < filelist.txt",
    "zip0": f"zip -0 -o -q {base_dir}/archive0.zip -@ < filelist.txt",
}

# Decompression commands with corrected paths
decompress_commands = {
    "gzip": f"tar --gzip -xf {base_dir}/archive.tar.gz -C ",
    "bzip2": f"tar --bzip2 -xf {base_dir}/archive.tar.bz2 -C ",
    "xz": f"tar --xz -xf {base_dir}/archive.tar.xz -C ",
    "lz4": f"tar --lz4 -xf {base_dir}/archive.tar.lz4 -C ",
    "zstd": f"tar --zstd -xf {base_dir}/archive.tar.zst -C ",
    "zip9": f"unzip -o -q {base_dir}/archive9.zip -d ",
    "zip0": f"unzip -o -q {base_dir}/archive0.zip -d ",
}


def benchmark(compress_command, decompress_command, method):
    # Create directories where archives will be decompressed
    decompress_dir = os.path.join(base_dir, method)
    os.makedirs(decompress_dir, exist_ok=True)

    # Compression
    print(compress_command)
    start_compress = time.time()
    subprocess.run(compress_command, shell=True)
    end_compress = time.time()

    # Decompression with corrected command
    full_decompress_command = decompress_command + decompress_dir
    print(full_decompress_command)
    start_decompress = time.time()
    subprocess.run(full_decompress_command, shell=True)
    end_decompress = time.time()

    return (end_compress - start_compress, end_decompress - start_decompress)


# Benchmarking
results = {}
for method, compress_command in compress_commands.items():
    decompress_command = decompress_commands[method]
    compress_time, decompress_time = benchmark(
        compress_command, decompress_command, method
    )
    results[method] = {
        "Compression Time": compress_time,
        "Decompression Time": decompress_time,
    }

# Output results
for method, times in results.items():
    print(
        f"{method}: Compression Time = {times['Compression Time']}s, Decompression Time = {times['Decompression Time']}s"
    )
