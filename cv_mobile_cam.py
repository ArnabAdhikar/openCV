import cv2
class Camera:
    def vid(self, camera):
        self.camera = camera
        capture = cv2.VideoCapture(self.camera)
        while True:
            success, frame = capture.read()
            frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            cv2.imshow("Mobile Camera", frame)
            if cv2.waitKey(1) == ord('q'):
                break
        capture.release()
        cv2.destroyAllWindows()
camera1 = Camera()
camera1.vid("http://10.80.130.20:8080/video")
