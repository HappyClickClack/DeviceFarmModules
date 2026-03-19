import cv2

DEVICE_HOST_IP = '10.54.198.107'
device_stream_port = 1234
video_path = f"tcp://{DEVICE_HOST_IP}:{device_stream_port}"
cap = cv2.VideoCapture(video_path)


# Check if camera opened successfully
if cap.isOpened()== False:
    print("Error opening video stream or file")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
input_fps = int(cap.get(cv2.CAP_PROP_FPS))

print("Video Path: ", video_path)
print("Source_width", width, "Source_height", height, "input FPS: ", input_fps)

width, height = width//2, height//2
print("Cropped_width", width, "Cropped_height", height)

# Read until video is completed
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        frame_rs = cv2.resize(frame, (width, height))

        # Display the resulting frame
        cv2.imshow('Frame', frame_rs)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
