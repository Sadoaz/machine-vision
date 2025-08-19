import cv2


def print_image_information(image):
    img = cv2.imread(image)

    if img is None:
        print("kunne ikke laste bildet.")
    else:
        height, width, channels = img.shape
        print("height:", height)
        print("width:", width)
        print("channels:", channels)
        print("size:", img.size)
        print("data type:", img.dtype)


def generate_camera_details():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        fps, width, height = 0, 0, 0
    else:
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        cap.release()

    file_path = "solutions/camera_outputs.txt"

    with open(file_path, "w") as f:
        f.write(f"fps: {fps}\n")
        f.write(f"width: {int(width)}\n")
        f.write(f"height: {int(height)}\n")


def main():
    print_image_information("lena.png")
    generate_camera_details()


main()
