import customtkinter as ctk
from PIL import Image
import cv2
from tkinter import filedialog

class SevenPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        def back():
            controller.show_page("dots")

        def openImg():
            window_name = "Camera - Press C to Capture | Q to Quit"
            cap = cv2.VideoCapture(0)

            if not cap.isOpened():
                print("Camera not accessible")
                return
            
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

            
            cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
            cv2.resizeWindow(window_name, 1200, 1200)  # 👈 BIG window
            captured_frame = None

            while True:
                if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
                    break

                ret, frame = cap.read()
                if not ret:
                    break

                cv2.imshow(window_name, frame)

                key = cv2.waitKey(1) & 0xFF

                if key == ord('c'):   # Capture
                    captured_frame = frame
                    break
                elif key == ord('q'): # Quit without capture
                    break

            cap.release()
            cv2.destroyAllWindows()

            if captured_frame is not None:
                show_captured_image(captured_frame)


        def show_captured_image(frame):
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame).resize((300, 300))

            ctk_img = ctk.CTkImage(img, size=(300, 300))
            image_label.configure(image=ctk_img)
            image_label.image = ctk_img


        def uploadImg():
            path = filedialog.askopenfilename(
                filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
            )
            if not path:
                return

            img = Image.open(path).resize((300, 300))
            ctk_img = ctk.CTkImage(img, size=(300, 300))
            image_label.configure(image=ctk_img)
            image_label.image = ctk_img


        h1 = ctk.CTkLabel(self, text="Connect The Dots", font=("Arial", 32, "bold"))
        h2 = ctk.CTkLabel(self, text="7x7", font=("Arial", 16))
        h1.pack(pady=(15, 2))
        h2.pack(pady=(2, 20))

        btn1 = ctk.CTkButton(self, height=30, width=120, font=("Roboto", 12, "bold"), text="Open Camera", fg_color="black", hover_color="grey",text_color="white", command=openImg)
        btn2 = ctk.CTkButton(self, height=30, width=120, font=("Roboto", 12, "bold"), text="Upload Image", fg_color="black", hover_color="grey",text_color="white", command=uploadImg)


        btn1.pack(padx=25, pady=(20,5))
        btn2.pack(padx=25, pady=5)

        
        image_label = ctk.CTkLabel(self, text="")
        image_label.pack(pady=20)

        bottom_bar = ctk.CTkFrame(self, height=25)
        bottom_bar.pack(side="bottom", fill="x")

        btnback = ctk.CTkButton(bottom_bar, width=20, font=("Roboto", 16, "bold"), text="Back", fg_color="black", hover_color="grey",text_color="white", command=back)
        btnback.pack(side="left", padx=15, pady=(40,10))