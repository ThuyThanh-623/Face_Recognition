import face_recognition
import cv2
import os
import glob
import numpy as np

class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        # Chọn kích thước khung hình
        self.frame_resizing = 0.25

    def load_encoding_images(self, images_path):

        # Tải ảnh
        images_path = glob.glob(os.path.join(images_path, "*.*"))

        print("{} ảnh được tìm thấy.".format(len(images_path)))

        
        for img_path in images_path:
            # Lặp qua từng ảnh và chuyển thành ảnh xám
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Lấy tên của ảnh
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)
            # Mã hóa ảnh
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

            # Lưu ảnh và tên tương ứng của ảnh
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)
        print("Load ảnh thành công!")

    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        # Nhận dạng tất cả khuôn mặt, bao gồm mặt đã được mã hóa
        # Chuyển hệ màu BGR (OpenCV) khớp RGB (face_recognition)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # So sánh khuôn mặt với khuôn mặt đã được mã hóa
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding, tolerance=0.4)
            name = "Unknown"

            # Chọn khuôn mặt đã biết có khoảng cách nhỏ nhất với khuôn mặt mới
            # được phát hiện và gán tên của khuôn mặt đã biết này cho khuôn mặt mới.
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            face_names.append(name)

        # Trả về mảng các vị trí khuôn mặt đã điều chỉnh và mảng tên tương ứng của khuôn mặt
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names
