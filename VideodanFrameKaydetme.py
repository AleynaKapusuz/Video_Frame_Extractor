import cv2
import os

video_path = "VID-20250313-WA0006.mp4"
output_folder = "video_frames"

os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Save Frame
    frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
    cv2.imwrite(frame_filename, frame)

    frame_count += 1

cap.release()
cv2.destroyAllWindows()

print(f"All frames saved in {output_folder} folder. Total {frame_count} frames processed.")