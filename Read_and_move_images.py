# import os
# import shutil
# import tkinter as tk
# from tkinter import filedialog
# from tkinter.simpledialog import askstring
# from PIL import Image, ImageTk, ImageDraw, ImageFont

# # === Configuration ===
# BUCKET_PATH = r"C:\Users\pc\Downloads\Bucket\Bucket"

# # === Get all timestamp folders ===
# timestamp_folders = sorted([
#     f for f in os.listdir(BUCKET_PATH)
#     if os.path.isdir(os.path.join(BUCKET_PATH, f))
# ])


# class ImageViewer:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Timestamp Image Viewer")
#         self.current_index = 0
#         self.selected_paths = []
#         self.tk_images = []
#         self.image_boxes = []

#         # === UI ===
#         self.canvas = tk.Canvas(root, bg='black')
#         self.canvas.pack(fill=tk.BOTH, expand=True)

#         self.search_frame = tk.Frame(root)
#         self.search_frame.pack(fill=tk.X, padx=5, pady=5)

#         self.search_entry = tk.Entry(self.search_frame)
#         self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

#         self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_folder)
#         self.search_button.pack(side=tk.LEFT)

#         self.button_frame = tk.Frame(root)
#         self.button_frame.pack(fill=tk.X, pady=10)

#         self.prev_button = tk.Button(self.button_frame, text="⟵ Previous", command=self.prev_folder)
#         self.prev_button.pack(side=tk.LEFT, padx=10)

#         self.next_button = tk.Button(self.button_frame, text="Next ⟶", command=self.next_folder)
#         self.next_button.pack(side=tk.RIGHT, padx=10)

#         self.move_button = tk.Button(root, text="Copy Selected Images", command=self.copy_selected_images)
#         self.move_button.pack(pady=5)

#         self.rename_button = tk.Button(root, text="Rename Images in Folder", command=self.rename_images_in_folder)
#         self.rename_button.pack(pady=5)

#         self.root.bind('<KeyPress>', self.key_handler)
#         self.root.bind("<Button-1>", self.on_root_click)

#         self.display_images()

#     def key_handler(self, event):
#         if self.root.focus_get() in (self.search_entry,):
#             return
#         if event.keysym.lower() == 'd':
#             self.next_folder()
#         elif event.keysym.lower() == 'a':
#             self.prev_folder()

#     def on_root_click(self, event):
#         if event.widget not in (self.search_entry,):
#             self.root.focus()

#     def get_image_row(self, folder_path):
#         if not os.path.exists(folder_path):
#             return []
#         return sorted([os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith('.jpg')])[:5]

#     def label_row(self, text, width):
#         img = Image.new("RGB", (width, 30), color="gray")
#         draw = ImageDraw.Draw(img)
#         font = ImageFont.load_default()
#         bbox = draw.textbbox((0, 0), text, font=font)
#         w = bbox[2] - bbox[0]
#         h = bbox[3] - bbox[1]
#         draw.text(((width - w) / 2, (30 - h) / 2), text, fill="white", font=font)
#         return img

#     def display_images(self):
#         self.canvas.delete("all")
#         self.tk_images.clear()
#         self.image_boxes.clear()

#         if not timestamp_folders:
#             self.root.title("No timestamp folders found")
#             return

#         folder_name = timestamp_folders[self.current_index]
#         folder_path = os.path.join(BUCKET_PATH, folder_name)

#         input_images = self.get_image_row(os.path.join(folder_path, "input"))
#         predicted_images = self.get_image_row(os.path.join(folder_path, "predicted"))

#         y_offset = 0
#         for label, paths in zip(["Input Images", "Predicted Images"], [input_images, predicted_images]):
#             images = []
#             for path in paths:
#                 img = Image.open(path).resize((200, 200))
#                 if path in self.selected_paths:
#                     draw = ImageDraw.Draw(img)
#                     draw.rectangle([0, 0, img.width - 1, img.height - 1], outline="red", width=4)
#                 images.append((img, path))

#             if images:
#                 row_width = len(images) * 200
#                 row_image = Image.new("RGB", (row_width, 200))
#                 for i, (img, _) in enumerate(images):
#                     row_image.paste(img, (i * 200, 0))

#                 label_image = self.label_row(label, row_width)
#                 combined = Image.new("RGB", (row_width, 230))
#                 combined.paste(label_image, (0, 0))
#                 combined.paste(row_image, (0, 30))

#                 tk_img = ImageTk.PhotoImage(combined)
#                 self.tk_images.append(tk_img)
#                 self.canvas.create_image(0, y_offset, anchor='nw', image=tk_img)

#                 for i, (_, path) in enumerate(images):
#                     box = (i * 200, y_offset + 30, (i + 1) * 200, y_offset + 230, path)
#                     self.image_boxes.append(box)

#                 y_offset += 230

#         self.canvas.bind("<Button-1>", self.on_canvas_click)
#         self.canvas.bind("<Button-3>", self.on_canvas_click)

#         self.root.title(f"Viewing: {folder_name}")

#     def on_canvas_click(self, event):
#         x, y = event.x, event.y
#         for x1, y1, x2, y2, path in self.image_boxes:
#             if x1 <= x <= x2 and y1 <= y <= y2:
#                 if event.num == 3:  # Right-click for zoom
#                     self.zoom_image(path)
#                 else:
#                     if path in self.selected_paths:
#                         self.selected_paths.remove(path)
#                     else:
#                         self.selected_paths.append(path)
#                     self.display_images()
#                 break

#     def zoom_image(self, path):
#         zoom_win = tk.Toplevel(self.root)
#         zoom_win.title(os.path.basename(path))
#         img = Image.open(path)

#         canvas = tk.Canvas(zoom_win, bg="black")
#         canvas.pack(fill=tk.BOTH, expand=True)

#         zoom_factor = 1.0
#         img_width, img_height = img.size
#         canvas_width, canvas_height = zoom_win.winfo_width(), zoom_win.winfo_height()

#         tk_img = ImageTk.PhotoImage(img)
#         image_id = canvas.create_image(0, 0, anchor='nw', image=tk_img)
#         canvas.image = tk_img

#         drag_data = {"x": 0, "y": 0}

#         def redraw():
#             resized = img.resize((int(img.width * zoom_factor), int(img.height * zoom_factor)))
#             tk_img2 = ImageTk.PhotoImage(resized)
#             canvas.itemconfig(image_id, image=tk_img2)
#             canvas.image = tk_img2
#             canvas.config(scrollregion=canvas.bbox(tk.ALL))

#         def on_mousewheel(event):
#             nonlocal zoom_factor
#             if event.delta > 0:
#                 zoom_factor *= 1.1
#             else:
#                 zoom_factor /= 1.1
#             redraw()

#         def on_drag_start(event):
#             drag_data["x"] = event.x
#             drag_data["y"] = event.y

#         def on_drag_motion(event):
#             delta_x = event.x - drag_data["x"]
#             delta_y = event.y - drag_data["y"]
#             canvas.move(image_id, delta_x, delta_y)
#             drag_data["x"] = event.x
#             drag_data["y"] = event.y

#         canvas.bind("<MouseWheel>", on_mousewheel)
#         canvas.bind("<ButtonPress-1>", on_drag_start)
#         canvas.bind("<B1-Motion>", on_drag_motion)
#         zoom_win.bind("<Escape>", lambda e: zoom_win.destroy())

#         redraw()

#     def copy_selected_images(self):
#         if not self.selected_paths:
#             self.root.title("No images selected to copy.")
#             return

#         dest_folder = filedialog.askdirectory(title="Select Destination Folder")
#         if not dest_folder:
#             return

#         copied = 0
#         for path in self.selected_paths:
#             try:
#                 shutil.copy2(path, os.path.join(dest_folder, os.path.basename(path)))
#                 copied += 1
#             except Exception as e:
#                 print(f"Error copying {path}: {e}")

#         self.root.title(f"Copied {copied} images to {dest_folder}")
#         self.selected_paths.clear()
#         self.display_images()

#     def rename_images_in_folder(self):
#         folder_path = filedialog.askdirectory(title="Select Folder to Rename Images")
#         if not folder_path:
#             return

#         new_name = askstring("Rename", "Enter the base name for renaming:")
#         if not new_name:
#             return

#         image_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
#         for i, filename in enumerate(image_files):
#             file_extension = os.path.splitext(filename)[1]
#             new_filename = f"{new_name}_{i + 1}{file_extension}"
#             old_path = os.path.join(folder_path, filename)
#             new_path = os.path.join(folder_path, new_filename)
#             os.rename(old_path, new_path)
#             print(f"Renamed {filename} to {new_filename}")

#         self.root.title(f"Renamed {len(image_files)} images in {folder_path}")

#     def next_folder(self):
#         if self.current_index < len(timestamp_folders) - 1:
#             self.current_index += 1
#             self.display_images()

#     def prev_folder(self):
#         if self.current_index > 0:
#             self.current_index -= 1
#             self.display_images()

#     def search_folder(self):
#         folder_name = self.search_entry.get().strip()
#         if folder_name in timestamp_folders:
#             self.current_index = timestamp_folders.index(folder_name)
#             self.display_images()
#         else:
#             self.root.title(f"Folder '{folder_name}' not found")


# # === Main App Launch ===
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry("1000x600")
#     viewer = ImageViewer(root)
#     root.mainloop()




import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter.simpledialog import askstring
from PIL import Image, ImageTk, ImageDraw, ImageFont

# === Configuration ===
BUCKET_PATH = r"C:\Users\pc\Downloads\Bucket\Bucket"

# === Get all timestamp folders ===
timestamp_folders = sorted([
    f for f in os.listdir(BUCKET_PATH)
    if os.path.isdir(os.path.join(BUCKET_PATH, f))
])


class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Timestamp Image Viewer")
        self.current_index = 0
        self.selected_paths = []
        self.tk_images = []
        self.image_boxes = []
        self.copy_dest_folder = None  # ← Store copy destination

        # === UI ===
        self.canvas = tk.Canvas(root, bg='black')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.search_frame = tk.Frame(root)
        self.search_frame.pack(fill=tk.X, padx=5, pady=5)

        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_folder)
        self.search_button.pack(side=tk.LEFT)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(fill=tk.X, pady=10)

        self.prev_button = tk.Button(self.button_frame, text="⟵ Previous", command=self.prev_folder)
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.next_button = tk.Button(self.button_frame, text="Next ⟶", command=self.next_folder)
        self.next_button.pack(side=tk.RIGHT, padx=10)

        self.move_button = tk.Button(root, text="Copy Selected Images", command=self.copy_selected_images)
        self.move_button.pack(pady=5)

        self.rename_button = tk.Button(root, text="Rename Images in Folder", command=self.rename_images_in_folder)
        self.rename_button.pack(pady=5)

        self.set_dest_button = tk.Button(root, text="Set Copy Destination", command=self.set_copy_destination)
        self.set_dest_button.pack(pady=5)

        self.root.bind('<KeyPress>', self.key_handler)
        self.root.bind("<Button-1>", self.on_root_click)

        self.display_images()

    def key_handler(self, event):
        if self.root.focus_get() in (self.search_entry,):
            return
        if event.keysym.lower() == 'd':
            self.next_folder()
        elif event.keysym.lower() == 'a':
            self.prev_folder()

    def on_root_click(self, event):
        if event.widget not in (self.search_entry,):
            self.root.focus()

    def get_image_row(self, folder_path):
        if not os.path.exists(folder_path):
            return []
        return sorted([os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith('.jpg')])[:5]

    def label_row(self, text, width):
        img = Image.new("RGB", (width, 30), color="gray")
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        bbox = draw.textbbox((0, 0), text, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        draw.text(((width - w) / 2, (30 - h) / 2), text, fill="white", font=font)
        return img

    def display_images(self):
        self.canvas.delete("all")
        self.tk_images.clear()
        self.image_boxes.clear()

        if not timestamp_folders:
            self.root.title("No timestamp folders found")
            return

        folder_name = timestamp_folders[self.current_index]
        folder_path = os.path.join(BUCKET_PATH, folder_name)

        input_images = self.get_image_row(os.path.join(folder_path, "input"))
        predicted_images = self.get_image_row(os.path.join(folder_path, "predicted"))

        y_offset = 0
        for label, paths in zip(["Input Images", "Predicted Images"], [input_images, predicted_images]):
            images = []
            for path in paths:
                img = Image.open(path).resize((200, 200))
                if path in self.selected_paths:
                    draw = ImageDraw.Draw(img)
                    draw.rectangle([0, 0, img.width - 1, img.height - 1], outline="red", width=4)
                images.append((img, path))

            if images:
                row_width = len(images) * 200
                row_image = Image.new("RGB", (row_width, 200))
                for i, (img, _) in enumerate(images):
                    row_image.paste(img, (i * 200, 0))

                label_image = self.label_row(label, row_width)
                combined = Image.new("RGB", (row_width, 230))
                combined.paste(label_image, (0, 0))
                combined.paste(row_image, (0, 30))

                tk_img = ImageTk.PhotoImage(combined)
                self.tk_images.append(tk_img)
                self.canvas.create_image(0, y_offset, anchor='nw', image=tk_img)

                for i, (_, path) in enumerate(images):
                    box = (i * 200, y_offset + 30, (i + 1) * 200, y_offset + 230, path)
                    self.image_boxes.append(box)

                y_offset += 230

        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<Button-3>", self.on_canvas_click)

        self.root.title(f"Viewing: {folder_name}")

    def on_canvas_click(self, event):
        x, y = event.x, event.y
        for x1, y1, x2, y2, path in self.image_boxes:
            if x1 <= x <= x2 and y1 <= y <= y2:
                if event.num == 3:  # Right-click for zoom
                    self.zoom_image(path)
                else:
                    if path in self.selected_paths:
                        self.selected_paths.remove(path)
                    else:
                        self.selected_paths.append(path)
                    self.display_images()
                break

    def zoom_image(self, path):
        zoom_win = tk.Toplevel(self.root)
        zoom_win.title(os.path.basename(path))
        img = Image.open(path)

        canvas = tk.Canvas(zoom_win, bg="black")
        canvas.pack(fill=tk.BOTH, expand=True)

        zoom_factor = 1.0
        img_width, img_height = img.size

        tk_img = ImageTk.PhotoImage(img)
        image_id = canvas.create_image(0, 0, anchor='nw', image=tk_img)
        canvas.image = tk_img

        drag_data = {"x": 0, "y": 0}

        def redraw():
            resized = img.resize((int(img.width * zoom_factor), int(img.height * zoom_factor)))
            tk_img2 = ImageTk.PhotoImage(resized)
            canvas.itemconfig(image_id, image=tk_img2)
            canvas.image = tk_img2
            canvas.config(scrollregion=canvas.bbox(tk.ALL))

        def on_mousewheel(event):
            nonlocal zoom_factor
            if event.delta > 0:
                zoom_factor *= 1.1
            else:
                zoom_factor /= 1.1
            redraw()

        def on_drag_start(event):
            drag_data["x"] = event.x
            drag_data["y"] = event.y

        def on_drag_motion(event):
            delta_x = event.x - drag_data["x"]
            delta_y = event.y - drag_data["y"]
            canvas.move(image_id, delta_x, delta_y)
            drag_data["x"] = event.x
            drag_data["y"] = event.y

        canvas.bind("<MouseWheel>", on_mousewheel)
        canvas.bind("<ButtonPress-1>", on_drag_start)
        canvas.bind("<B1-Motion>", on_drag_motion)
        zoom_win.bind("<Escape>", lambda e: zoom_win.destroy())

        redraw()

    def copy_selected_images(self):
        if not self.selected_paths:
            self.root.title("No images selected to copy.")
            return

        if not self.copy_dest_folder:
            self.set_copy_destination()
            if not self.copy_dest_folder:
                self.root.title("No destination folder selected.")
                return

        dest_folder = self.copy_dest_folder
        copied = 0
        for path in self.selected_paths:
            try:
                shutil.copy2(path, os.path.join(dest_folder, os.path.basename(path)))
                copied += 1
            except Exception as e:
                print(f"Error copying {path}: {e}")

        self.root.title(f"Copied {copied} images to {dest_folder}")
        self.selected_paths.clear()
        self.display_images()

    def set_copy_destination(self):
        folder = filedialog.askdirectory(title="Select Copy Destination Folder")
        if folder:
            self.copy_dest_folder = folder
            self.root.title(f"Copy destination set to: {folder}")

    def rename_images_in_folder(self):
        folder_path = filedialog.askdirectory(title="Select Folder to Rename Images")
        if not folder_path:
            return

        new_name = askstring("Rename", "Enter the base name for renaming:")
        if not new_name:
            return

        image_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
        for i, filename in enumerate(image_files):
            file_extension = os.path.splitext(filename)[1]
            new_filename = f"{new_name}_{i + 1}{file_extension}"
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed {filename} to {new_filename}")

        self.root.title(f"Renamed {len(image_files)} images in {folder_path}")

    def next_folder(self):
        if self.current_index < len(timestamp_folders) - 1:
            self.current_index += 1
            self.display_images()

    def prev_folder(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.display_images()

    def search_folder(self):
        folder_name = self.search_entry.get().strip()
        if folder_name in timestamp_folders:
            self.current_index = timestamp_folders.index(folder_name)
            self.display_images()
        else:
            self.root.title(f"Folder '{folder_name}' not found")


# === Main App Launch ===
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x600")
    viewer = ImageViewer(root)
    root.mainloop()
