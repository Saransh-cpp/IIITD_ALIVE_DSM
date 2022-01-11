#
# Task 2
#
import cv2
import time
import numpy as np
from keras.models import load_model


def detect():
    """
    Detects if the eyes are closed or open.
    """

    # load the model trained in `train.ipynb`
    model = load_model("./model.h5")

    # labels
    classes = {0: "Drowsiness detected", 1: "Drowsiness not detected"}

    # variables for detecting FPS
    prev_frame_time = 0
    new_frame_time = 0

    # start capturing video
    cap = cv2.VideoCapture(3)
    while cap.isOpened():
        # read a frame, resize it, and convert it to RGB
        _, img = cap.read()
        img = cv2.resize(img, (224, 224))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img = img / 255.0

        # redict if open or closed
        y_pred = model.predict(np.array([img]))
        label = classes[np.argmax(y_pred.flatten())]
        print(label)

        # calculate FPS
        new_frame_time = time.time()
        fps = 1 / (new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time

        fps = str(int(fps))

        # putting the FPS count and label on the frame
        cv2.putText(img, fps, (4, 30), cv2.FONT_HERSHEY_COMPLEX,
                    1, (255, 255, 255), 3)
        cv2.putText(img, label, (7, 200),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

        cv2.imshow('Webcam', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    detect()
