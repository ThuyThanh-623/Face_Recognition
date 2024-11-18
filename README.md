# Nhận dạng khuôn mặt dựa theo tên

## Giới thiệu

Báo cáo này trình bày việc ứng dụng thư viện `face_recognition` để nhận dạng khuôn mặt và dự đoán tên trong thời gian thực từ video hoặc camera. Mục tiêu của bài toán là phát hiện khuôn mặt, mã hóa khuôn mặt và so sánh để nhận diện danh tính của người trong các bức ảnh hoặc video.

### Phương pháp
Ứng dụng sử dụng các phương pháp học sâu như:

1. **Phát hiện khuôn mặt**:
   - Sử dụng **Histogram of Oriented Gradients (HOG)** và **Convolutional Neural Network (CNN)** để phát hiện khuôn mặt.

2. **Mã hóa khuôn mặt**:
   - Áp dụng **Deep Metric Learning** để chuyển đổi khuôn mặt thành một vector đặc trưng (face encoding), cho phép so sánh và nhận diện khuôn mặt.

3. **So sánh khuôn mặt**:
   - Sử dụng **Euclidean Distance** để xác định mức độ tương đồng giữa các khuôn mặt.

4. **Xác định các đặc điểm trên khuôn mặt**:
   - Phát hiện các điểm đặc trưng trên khuôn mặt như mắt, mũi, miệng, và cằm.

## Cài đặt và Chạy Chương Trình

### Cài đặt thư viện

Trước khi bắt đầu, bạn cần cài đặt các thư viện cần thiết:

```bash
pip install face_recognition opencv-python numpy
```

### Lớp SimpleFacerec

Lớp `SimpleFacerec` cung cấp các phương thức để tải và mã hóa khuôn mặt, cũng như nhận diện khuôn mặt từ video hoặc hình ảnh. Các phương thức chính bao gồm:

- **Khởi tạo**:
  - `self.known_face_encodings`: Danh sách mã hóa khuôn mặt đã biết.
  - `self.known_face_names`: Danh sách tên tương ứng với các mã hóa khuôn mặt.

- **Phương thức `load_encoding_images`**:
  - Tải và mã hóa các hình ảnh khuôn mặt đã biết từ thư mục.

- **Phương thức `detect_known_faces`**:
  - Phát hiện và nhận diện các khuôn mặt trong một khung hình.

### Chạy chương trình

- Tạo một đối tượng từ lớp `SimpleFacerec`.
- Tải các mã hóa khuôn mặt từ thư mục chứa ảnh đã biết.
- Sử dụng webcam hoặc video để phát hiện và nhận diện khuôn mặt theo thời gian thực.
- Hiển thị tên của người trong khuôn mặt hoặc nhãn "Unknown" nếu khuôn mặt không có trong tập dữ liệu đã biết.

## Kết quả Đạt được

- Chương trình nhận diện được 3 khuôn mặt đã được mã hóa và gán nhãn tên. 
- Các khuôn mặt không có trong tập dữ liệu sẽ được gán nhãn "Unknown".

## Ưu điểm và Hạn chế

### Ưu điểm:
- **Tính đơn giản và dễ hiểu**: Mã nguồn rõ ràng, dễ dàng mở rộng và tùy chỉnh cho các dự án khác.
- **Hiệu suất tốt**: Hệ thống nhận diện khuôn mặt nhanh chóng, đặc biệt trong các video từ webcam.
- **Dễ tích hợp**: Có thể dễ dàng tích hợp vào các ứng dụng khác với lớp `SimpleFacerec`.

### Hạn chế:
- **Độ chính xác**: Việc thay đổi kích thước khung hình có thể làm giảm độ chính xác của việc phát hiện khuôn mặt.
- **Phụ thuộc vào dữ liệu huấn luyện**: Nếu dữ liệu huấn luyện không đủ đa dạng, hệ thống có thể gặp khó khăn trong việc nhận diện khuôn mặt trong các tình huống khác nhau.
- **Cần phần cứng mạnh**: Việc xử lý video và nhận diện khuôn mặt yêu cầu máy tính có cấu hình mạnh mẽ.

---

Mong nhận được thêm đóng góp của bạn!
