import cv2

video_path = r"C:\Users\Raffel\Downloads\kecilin\beyblade.mp4"
cap = cv2.VideoCapture(video_path)

frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)

seconds = round(frames/fps)

frame_total = 150
i = 0

while (cap.isOpened()):
  cap.set(cv2.CAP_PROP_POS_MSEC, (i * ((seconds/frame_total)*1000)))
  flag, frame = cap.read()

  if flag == False:
    break

  # change the path to where you want to save the image
  image_path = rf"C:\Users\Raffel\Downloads\kecilin\image\img_{i}.jpg"
  cv2.imwrite(image_path, frame)

  i += 1

cap.release()
cv2.destroyAllWindows()