from PIL import Image

# Bộ ký tự từ đậm -> nhạt (có thể chỉnh sửa tùy thích)
ASCII_CHARS = ["█", "▓", "▒", "░", " "]

def resize_image(image, new_width=100):
    """Resize ảnh giữ tỉ lệ"""
    width, height = image.size
    ratio = height / width / 1.65  # chỉnh cho cân đối khi in ra console
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def grayify(image):
    """Chuyển ảnh sang grayscale"""
    return image.convert("L")

def pixels_to_ascii(image):
    """Chuyển pixel grayscale thành ký tự ASCII"""
    pixels = image.getdata()
    ascii_str = "".join(ASCII_CHARS[pixel // 51] for pixel in pixels)
    return ascii_str

def image_to_ascii(image_path, new_width=100):
    """Main: chuyển ảnh thành ASCII"""
    try:
        image = Image.open(image_path)
    except Exception as e:
        print("❌ Không mở được ảnh:", e)
        return None

    image = resize_image(image, new_width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    img_width = image.width

    ascii_img = "\n".join(
        ascii_str[i:(i+img_width)] for i in range(0, len(ascii_str), img_width)
    )

    return ascii_img

if __name__ == "__main__":
    # Hỏi tên file ảnh
    path = input("📂 Nhập tên file ảnh (ví dụ: IMG_4555.jpeg): ").strip()
    ascii_image = image_to_ascii(path, new_width=80)

    if ascii_image:
        print("\n✅ Kết quả ASCII:\n")
        print(ascii_image)

        # Lưu ra file txt
        with open("output_ascii.txt", "w", encoding="utf-8") as f:
            f.write(ascii_image)
        print("\n💾 ASCII đã lưu vào file: output_ascii.txt")
