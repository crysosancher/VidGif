# Video to GIF Converter

![Example GIF](https://github.com/crysosancher/VidGif/blob/main/test.gif) *Example GIF created with this tool*

A lightweight, high-quality video to GIF converter using FFmpeg. Perfect for creating smooth, optimized GIFs from 1080p or 4K video sources while maintaining small file sizes.

## Features

- 🎞️ High-quality conversion with smooth frame transitions
- ⚡ Optimized compression using FFmpeg's two-pass palette method
- ⏱️ Precise timing control with start/end time selection
- 📏 Customizable dimensions (width with aspect ratio preservation)
- 🐇 Lightweight (only requires Python and FFmpeg)
- 🧹 Automatic cleanup of temporary files

## Installation

### Prerequisites

- FFmpeg installed and in system PATH
- Python 3.9+

### Setup

```bash
# Create conda environment
conda create -n gif_env -c conda-forge python=3.9 ffmpeg -y

# Activate environment
conda activate gif_env

# Clone repository
git clone https://github.com/yourusername/video-to-gif.git
cd video-to-gif
```

## Usage

### Basic Conversion

```bash
python video_to_gif.py input.mp4 00:05 00:10
```

Converts 5-10 seconds of video to GIF with default settings (480px width, 15 FPS)

### Advanced Options

```bash
python video_to_gif.py input.mp4 00:15 00:25 \
  --output my_animation.gif \
  --width 720 \
  --fps 20
```

### Recommended Settings

| Scenario | Width | FPS | Command Example |
|----------|-------|-----|-----------------|
| Web sharing | 480 | 15 | `--width 480 --fps 15` |
| HD presentation | 720 | 20 | `--width 720 --fps 20` |
| Mobile optimized | 320 | 12 | `--width 320 --fps 12` |
| High-quality demo | 960 | 24 | `--width 960 --fps 24` |

## Customization
## Customization

Modify these parameters in the command line:

- `--width`: Output width in pixels (maintains aspect ratio)
- `--fps`: Frame rate (15-24 recommended)
- `--output`: Custom output filename

## Performance Notes

Typical output sizes for a 10-second clip:

- 480p: 1-2MB
- 720p: 2-3MB
- 1080p: 3-5MB

For best results:

- Keep clips under 15 seconds
- Use darker backgrounds for better compression
- Lower FPS for smaller file sizes
- Reduce width for mobile optimization

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Made with ❤️ and FFmpeg magic. Perfect for creating GIFs for GitHub READMEs, product demos, and social media!