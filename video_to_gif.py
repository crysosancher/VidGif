import argparse
import subprocess
import os
import re

def time_to_seconds(time_str):
    """Convert time string to seconds (supports MM:SS and seconds)"""
    if re.match(r'^\d+:\d+', time_str):
        parts = time_str.split(':')
        return int(parts[0]) * 60 + float(parts[1])
    try:
        return float(time_str)
    except ValueError:
        raise SystemExit(f"Invalid time format: {time_str}. Use MM:SS or seconds")

def convert_video_to_gif(input_path, start_time, end_time, output_path=None, width=480, fps=20):
    start_sec = time_to_seconds(start_time)
    end_sec = time_to_seconds(end_time)
    duration = end_sec - start_sec
    
    if not output_path:
        base_name = os.path.splitext(input_path)[0]
        output_path = f"{base_name}.gif"
    
    palette_file = "palette_temp.png"
    
    try:
        # Generate palette
        subprocess.run([
            'ffmpeg', '-ss', str(start_sec), '-t', str(duration),
            '-i', input_path,
            '-vf', f'fps={fps},scale={width}:-1:flags=lanczos,palettegen=stats_mode=diff',
            '-y', palette_file
        ], check=True)
        
        # Create GIF
        subprocess.run([
            'ffmpeg', '-ss', str(start_sec), '-t', str(duration),
            '-i', input_path, '-i', palette_file,
            '-lavfi', f'fps={fps},scale={width}:-1:flags=lanczos [x]; [x][1:v] paletteuse=dither=bayer:bayer_scale=3',
            '-y', output_path
        ], check=True)
        
        print(f"✅ GIF created: {output_path}")
        print(f"   Dimensions: {width}px width, {fps} FPS, Duration: {duration:.1f}s")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during conversion: {e}")
        return False
    finally:
        if os.path.exists(palette_file):
            os.remove(palette_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert video to optimized GIF')
    parser.add_argument('input', help='Input video file path')
    parser.add_argument('start', help='Start time (MM:SS or seconds)')
    parser.add_argument('end', help='End time (MM:SS or seconds)')
    parser.add_argument('--output', help='Output file path (optional)')
    parser.add_argument('--width', type=int, default=480, help='Output width in pixels (default: 480)')
    parser.add_argument('--fps', type=int, default=15, help='Frames per second (default: 15)')
    
    args = parser.parse_args()
    convert_video_to_gif(
        args.input,
        args.start,
        args.end,
        args.output,
        args.width,
        args.fps
    )