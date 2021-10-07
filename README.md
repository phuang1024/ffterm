# Termvideo

Play videos in the terminal (stdout).

`python main.py /path/to/video.mp4`

Terminal size: `-x output_width`, `-y output_height`.
Default autodetects and adapts if terminal is scaled.

Warning: If you redirect output to a file, the file may become
very large. Default behavior stops if redirecting. Add `--redirect` to allow.

Add `--cpp` to compile and load a C++ library. This will greatly improve the speed.

![](https://github.com/phuang1024/termvideo/blob/main/examples/piano.png?raw=true)
