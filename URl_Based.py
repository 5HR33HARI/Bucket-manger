# import tkinter as tk
# import pymongo
# import requests
# from PIL import Image, ImageTk
# from io import BytesIO

# # MongoDB connection setup
# client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI
# db = client["FACTREE"]  # Replace with your database name
# collection = db["677d54d91a244a474eeca4b0"]  # Replace with your collection name

# class ImageViewer:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("MongoDB Image Viewer")
#         self.current_index = 0
#         self.data = self.fetch_data_from_mongo()

#         # === GUI Layout ===
#         self.search_frame = tk.Frame(root)
#         self.search_frame.pack(fill=tk.X, padx=5, pady=5)

#         self.search_entry = tk.Entry(self.search_frame)
#         self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

#         self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_entry)
#         self.search_button.pack(side=tk.LEFT, padx=5)

#         self.canvas = tk.Canvas(root, bg='white')
#         self.canvas.pack(fill=tk.BOTH, expand=True)

#         self.button_frame = tk.Frame(root)
#         self.button_frame.pack(fill=tk.X, pady=10)

#         self.prev_button = tk.Button(self.button_frame, text="⟵ Previous", command=self.prev_image)
#         self.prev_button.pack(side=tk.LEFT, padx=10)

#         self.next_button = tk.Button(self.button_frame, text="Next ⟶", command=self.next_image)
#         self.next_button.pack(side=tk.RIGHT, padx=10)

#         self.status_label = tk.Label(root, text="Enter Status:")
#         self.status_label.pack(pady=5)

#         self.status_entry = tk.Entry(root)
#         self.status_entry.pack(fill=tk.X, padx=5, pady=5)
#         self.status_entry.bind("<Return>", lambda e: self.save_status())

#         self.save_button = tk.Button(root, text="Save Status", command=self.save_status)
#         self.save_button.pack(pady=5)

#         self.display_images()

#     def fetch_data_from_mongo(self):
#         """ Fetch data from MongoDB collection """
#         data = []
#         for doc in collection.find():
#             # Directly extract the required fields from each document
#             input_image_url = doc.get('input_image')
#             predicted_image_url = doc.get('predicted_image')
#             if input_image_url and predicted_image_url:
#                 data.append({"input_image": input_image_url, "predicted_image": predicted_image_url})
#         return data

#     def display_images(self):
#         """ Display the input and predicted images of the current document """
#         self.canvas.delete("all")
        
#         if not self.data:
#             self.canvas.create_text(10, 10, anchor='nw', text="No data available.", font=("Helvetica", 12), fill="red")
#             return

#         # Fetch current document's images
#         current_data = self.data[self.current_index]
#         input_image_url = current_data['input_image']
#         predicted_image_url = current_data['predicted_image']

#         # Load and display images
#         self.load_and_display_image(input_image_url, y_offset=0)  # Display input image
#         self.load_and_display_image(predicted_image_url, y_offset=250)  # Display predicted image (250px below)

#         # Update status
#         self.root.title(f"Viewing Image Pair {self.current_index + 1}/{len(self.data)}")

#     def load_and_display_image(self, url, y_offset=0):
#         """ Fetch image from URL and display in Tkinter """
#         try:
#             response = requests.get(url)
#             img_data = response.content
#             pil_img = Image.open(BytesIO(img_data))

#             # Resize image to fit canvas
#             canvas_width = max(1, self.canvas.winfo_width())
#             canvas_height = max(1, self.canvas.winfo_height())
#             scale_w = canvas_width / pil_img.width
#             scale_h = canvas_height / pil_img.height
#             scale = min(scale_w, scale_h, 1.0)
#             new_size = (max(1, int(pil_img.width * scale)), max(1, int(pil_img.height * scale)))
#             pil_img = pil_img.resize(new_size, Image.Resampling.LANCZOS)

#             # Convert image to Tkinter format
#             self.tk_image = ImageTk.PhotoImage(pil_img)
#             self.canvas.create_image(0, y_offset, anchor='nw', image=self.tk_image)
#             self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

#         except Exception as e:
#             print(f"Error loading image from URL: {url}. Error: {e}")
#             self.canvas.create_text(10, 10, anchor='nw', text="Error loading image.", font=("Helvetica", 12), fill="red")

#     def next_image(self):
#         """ Navigate to the next image """
#         if self.current_index < len(self.data) - 1:
#             self.current_index += 1
#             self.display_images()

#     def prev_image(self):
#         """ Navigate to the previous image """
#         if self.current_index > 0:
#             self.current_index -= 1
#             self.display_images()

#     def search_entry(self):
#         """ Search for a folder by name (no longer applicable with this structure) """
#         self.display_images()

#     def save_status(self):
#         """ Save the current status to MongoDB """
#         # Your existing save functionality
#         pass

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry("800x600")
#     viewer = ImageViewer(root)
#     root.mainloop()



# import tkinter as tk
# import pymongo
# import requests
# from PIL import Image, ImageTk
# from io import BytesIO

# # MongoDB connection setup
# client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI
# db = client["FACTREE"]  # Replace with your database name
# collection = db["677d54d91a244a474eeca4b0"]  # Replace with your collection name

# class ImageViewer:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("MongoDB Image Viewer")
#         self.current_index = 0
#         self.data = self.fetch_data_from_mongo()

#         # === GUI Layout ===
#         self.search_frame = tk.Frame(root)
#         self.search_frame.pack(fill=tk.X, padx=5, pady=5)

#         self.search_entry = tk.Entry(self.search_frame)
#         self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

#         self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_folder)
#         self.search_button.pack(side=tk.LEFT, padx=5)

#         self.canvas = tk.Canvas(root, bg='white')
#         self.canvas.pack(fill=tk.BOTH, expand=True)

#         self.button_frame = tk.Frame(root)
#         self.button_frame.pack(fill=tk.X, pady=10)

#         self.status_label = tk.Label(root, text="Enter Status:")
#         self.status_label.pack(pady=5)

#         self.status_entry = tk.Entry(root)
#         self.status_entry.pack(fill=tk.X, padx=5, pady=5)
#         self.status_entry.bind("<Return>", lambda e: self.save_status())

#         self.save_button = tk.Button(root, text="Save Status", command=self.save_status)
#         self.save_button.pack(pady=5)

#         # Display images
#         self.display_images()

#         # Bind keys for navigation
#         self.root.bind('d', lambda event: self.next_image())  # "D" for next
#         self.root.bind('a', lambda event: self.prev_image())  # "A" for previous

#     #     return data
#     def fetch_data_from_mongo(self):
#     # """Fetch data from MongoDB collection"""
#         data = []
#         for doc in collection.find():
#             input_images = doc.get("input_image", {})
#             predicted_images = doc.get("predicted_image", {})
#             if input_images and predicted_images:
#                 data.append({
#                     "input_images": input_images,
#                     "predicted_images": predicted_images
#                 })
#         return data

#     def display_images(self):
#         """ Display the input and predicted images of the current document """
#         self.canvas.delete("all")
        
#         if not self.data:
#             self.canvas.create_text(10, 10, anchor='nw', text="No data available.", font=("Helvetica", 12), fill="red")
#             return

#         # Fetch current document's images
#         current_data = self.data[self.current_index]
#         input_image_url = current_data['input_image']
#         predicted_image_url = current_data['predicted_image']

#         # Load and display images
#         self.load_and_display_image(input_image_url, y_offset=0)  # Display input image
#         self.load_and_display_image(predicted_image_url, y_offset=250)  # Display predicted image (250px below)

#         # Update status
#         self.root.title(f"Viewing Image Pair {self.current_index + 1}/{len(self.data)}")

#     def load_and_display_image(self, url, y_offset=0):
#         """ Fetch image from URL and display in Tkinter """
#         try:
#             response = requests.get(url)
#             img_data = response.content
#             pil_img = Image.open(BytesIO(img_data))

#             # Resize image to fit canvas
#             canvas_width = max(1, self.canvas.winfo_width())
#             canvas_height = max(1, self.canvas.winfo_height())
#             scale_w = canvas_width / pil_img.width
#             scale_h = canvas_height / pil_img.height
#             scale = min(scale_w, scale_h, 1.0)
#             new_size = (max(1, int(pil_img.width * scale)), max(1, int(pil_img.height * scale)))
#             pil_img = pil_img.resize(new_size, Image.Resampling.LANCZOS)

#             # Convert image to Tkinter format
#             self.tk_image = ImageTk.PhotoImage(pil_img)
#             self.canvas.create_image(0, y_offset, anchor='nw', image=self.tk_image)
#             self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

#         except Exception as e:
#             print(f"Error loading image from URL: {url}. Error: {e}")
#             self.canvas.create_text(10, 10, anchor='nw', text="Error loading image.", font=("Helvetica", 12), fill="red")

#     def next_image(self):
#         """ Navigate to the next image """
#         if self.current_index < len(self.data) - 1:
#             self.current_index += 1
#             self.display_images()

#     def prev_image(self):
#         """ Navigate to the previous image """
#         if self.current_index > 0:
#             self.current_index -= 1
#             self.display_images()

#     def search_folder(self):
#         """ Search for a folder by name """
#         folder_name = self.search_entry.get().strip()
#         # In this example, we will match by index, since no folder names exist in your data.
#         # Modify this if you have a 'folder_name' field or a structure that allows searching
#         if folder_name.isnumeric() and int(folder_name) < len(self.data):
#             self.current_index = int(folder_name) - 1  # Folder names are numeric in this example
#             self.display_images()
#         else:
#             self.root.title(f"Folder '{folder_name}' not found")

#     def save_status(self):
#         """ Save the current status to MongoDB """
#         # Your existing save functionality
#         pass


# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry("800x600")
#     viewer = ImageViewer(root)
#     root.mainloop()





# //////////////////////////
# import pymongo

# # MongoDB connection setup
# client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI
# db = client["FACTREE"]  # Replace with your database name
# collection = db["your_collection_name"]  # Replace with your collection name

# class ImageViewer:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("MongoDB Image Viewer")
#         self.current_index = 0
#         self.folder_names = []

#         # === Fetch data from MongoDB ===
#         self.data = self.fetch_data_from_mongo()
#         self.folder_names = list(self.data.keys())

#         # === GUI Layout ===
#         # (Your GUI setup code continues here...)

#     def fetch_data_from_mongo(self):
#         """ Fetch data from MongoDB collection """
#         data = {}
#         for doc in collection.find():
#             # Check if 'folder_name' exists in the document
#             folder_name = doc.get('folder_name')
#             if folder_name:
#                 status = doc.get('status', "")
#                 image_urls = doc.get('image_urls', [])
#                 data[folder_name] = {"status": status, "image_urls": image_urls}
#             else:
#                 print("Document does not contain 'folder_name':", doc)
#         return data

#     # (The rest of your code continues here...)

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry("800x600")
#     viewer = ImageViewer(root)
#     root.mainloop()


# /////////////////////////////////
import tkinter as tk
import pymongo
import requests
from PIL import Image, ImageTk
from io import BytesIO
from bson.objectid import ObjectId

# === MongoDB Connection ===
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["FACTREE"]
collection = db["677d54d91a244a474eeca4b0"]

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("MongoDB Image Viewer")
        self.current_index = 0
        self.data = self.fetch_data_from_mongo()

        # === GUI Layout ===
        self.search_frame = tk.Frame(root)
        self.search_frame.pack(pady=5)

        self.search_entry = tk.Entry(self.search_frame, width=50)
        self.search_entry.pack(side=tk.LEFT, padx=5)

        self.search_button = tk.Button(self.search_frame, text="Search by _id", command=self.search_by_id)
        self.search_button.pack(side=tk.LEFT, padx=5)

        self.canvas = tk.Canvas(root, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.doc_id_label = tk.Label(root, text="", font=("Helvetica", 10, "italic"))
        self.doc_id_label.pack(pady=2)

        self.nav_frame = tk.Frame(root)
        self.nav_frame.pack(pady=10)

        tk.Button(self.nav_frame, text="<< Prev", command=self.prev_image).pack(side=tk.LEFT, padx=10)
        tk.Button(self.nav_frame, text="Next >>", command=self.next_image).pack(side=tk.LEFT, padx=10)

        self.root.bind("<KeyPress-d>", lambda event: self.next_image())
        self.root.bind("<KeyPress-a>", lambda event: self.prev_image())

        self.display_images()

    def fetch_data_from_mongo(self):
        data = []
        for doc in collection.find():
            input_images = doc.get("input_image", {})
            predicted_images = doc.get("predicted_image", {})
            if input_images and predicted_images:
                data.append({
                    "_id": str(doc["_id"]),
                    "input_images": input_images,
                    "predicted_images": predicted_images
                })
        return data

    def display_images(self):
        self.canvas.delete("all")
        self.tk_images = []

        if not self.data:
            self.canvas.create_text(10, 10, anchor='nw', text="No data available.", font=("Helvetica", 12), fill="red")
            return

        current_data = self.data[self.current_index]
        input_images = current_data["input_images"]
        predicted_images = current_data["predicted_images"]

        x_input = 10
        x_pred = 350
        y_offset = 10

        for i in range(5):
            input_url = input_images.get(str(i))
            pred_url = predicted_images.get(str(i))

            if input_url:
                img = self.get_tk_image(input_url)
                if img:
                    self.canvas.create_image(x_input, y_offset, anchor='nw', image=img)
                    self.tk_images.append(img)

            if pred_url:
                img = self.get_tk_image(pred_url)
                if img:
                    self.canvas.create_image(x_pred, y_offset, anchor='nw', image=img)
                    self.tk_images.append(img)

            y_offset += 220

        self.root.title(f"MongoDB Image Viewer - Set {self.current_index + 1}/{len(self.data)} - ID: {current_data['_id']}")
        self.doc_id_label.config(text=f"Document ID: {current_data['_id']}")

    def get_tk_image(self, url):
        try:
            response = requests.get(url)
            pil_img = Image.open(BytesIO(response.content)).convert("RGB")
            pil_img = pil_img.resize((300, 200), Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(pil_img)
        except Exception as e:
            print(f"Error loading image from {url}: {e}")
            return None

    def next_image(self):
        if self.current_index < len(self.data) - 1:
            self.current_index += 1
            self.display_images()

    def prev_image(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.display_images()

    def search_by_id(self):
        search_id = self.search_entry.get().strip()
        if not search_id:
            return

        try:
            # Try to match by string _id
            for idx, doc in enumerate(self.data):
                if doc["_id"] == search_id:
                    self.current_index = idx
                    self.display_images()
                    return

            self.root.title(f"Document with _id '{search_id}' not found.")
        except Exception as e:
            print(f"Invalid ObjectId: {e}")
            self.root.title("Invalid _id format")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x1200")
    app = ImageViewer(root)
    root.mainloop()
