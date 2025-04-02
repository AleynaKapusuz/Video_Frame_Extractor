# Video_Frame_Extractor

This Python script extracts every frame from a video file and saves them as .png image files. Each frame visible in the video playback will be stored in the video_frames folder as a separate image.

📌 Features
✅ Extracts all frames from a video file.
✅ Saves each frame in .png format in a specified folder.
✅ Frames are named sequentially as frame_0000.png, frame_0001.png, frame_0002.png, etc.
✅ Automatically creates the output folder if it doesn't exist.
✅ Stops processing automatically when the video ends.

🛠️ Requirements
This script requires the following libraries:

- opencv-python

- os (included with Python)

If OpenCV is not installed, you can install it using the following command:

```
pip install opencv-python
```

🚀 Usage
1️⃣ Specify your video file
Update the video_path variable in the script with the path to your video file. Example:

```
video_path = "VID-20250313-WA0006.mp4"  # Your video file name or path
```
If you need to specify the full path:
```
video_path = "C:/Users/User/Desktop/video.mp4"
```


2️⃣ Check the output

Once the process is complete, the extracted frames will be saved in the video_frames folder. Example:

video_frames/

│── frame_0000.png

│── frame_0001.png

│── frame_0002.png

│── frame_0003.png

│── ...
At the end of execution, you will see a message like this:
```
All frames have been saved in the video_frames folder. A total of 1500 frames were processed.
```

📂 Output Folder Structure

📁 Working Directory

│── extract_frames.py  # Python script

│── VID-20250313-WA0006.mp4  # Your video file

│── 📂 video_frames

│   │── frame_0000.png

│   │── frame_0001.png

│   │── frame_0002.png

│   │── frame_0003.png

│   │── ...


⚠️ Important Notes
If the video resolution is high and contains many frames, it may consume a large amount of storage.

Processing time can be long for very long videos.

You don't need to manually create the video_frames folder, as the script will automatically generate it.
