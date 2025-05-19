# # import os
# # import streamlit as st
# # from PIL import Image

# # # Set page layout (must be first Streamlit command)
# # st.set_page_config(layout="wide")

# # # Title
# # st.title("📂 Input vs Predicted Image Viewer")

# # # Set base folder path
# # base_folder_path = r'C:\Users\pc\Downloads\Bucket\Bucket'

# # # Get all folder names sorted
# # folders = sorted([f for f in os.listdir(base_folder_path) if os.path.isdir(os.path.join(base_folder_path, f))])

# # # Initialize session state for folder index
# # if 'folder_index' not in st.session_state:
# #     st.session_state.folder_index = 0

# # # Navigation buttons
# # col_nav1, col_nav2, col_nav3 = st.columns([1, 4, 1])
# # with col_nav1:
# #     if st.button("⬅️ Back (A)") and st.session_state.folder_index > 0:
# #         st.session_state.folder_index -= 1
# # with col_nav3:
# #     if st.button("Next (D) ➡️") and st.session_state.folder_index < len(folders) - 1:
# #         st.session_state.folder_index += 1

# # # Get current folder
# # current_folder = folders[st.session_state.folder_index]
# # st.subheader(f"🗂 Folder: `{current_folder}`")

# # # Paths for input and predicted folders
# # input_folder = os.path.join(base_folder_path, current_folder, 'input')
# # predicted_folder = os.path.join(base_folder_path, current_folder, 'predicted')

# # # Function to load images from folder
# # def load_images_from_folder(folder_path):
# #     images = []
# #     if not os.path.exists(folder_path):
# #         return images
# #     for filename in sorted(os.listdir(folder_path)):
# #         if filename.lower().endswith('.jpg'):
# #             img_path = os.path.join(folder_path, filename)
# #             try:
# #                 img = Image.open(img_path)
# #                 images.append((filename, img))
# #             except Exception as e:
# #                 st.error(f"Error loading image {filename}: {e}")
# #     return images

# # # Load images
# # input_images = load_images_from_folder(input_folder)
# # predicted_images = load_images_from_folder(predicted_folder)

# # # Display images
# # if not input_images and not predicted_images:
# #     st.warning("No images found in either 'input' or 'predicted' for this folder.")
# # else:
# #     st.markdown("### 📸 Input vs Predicted")
# #     for (input_name, input_img), (pred_name, pred_img) in zip(input_images, predicted_images):
# #         col1, col2 = st.columns(2)
# #         with col1:
# #             st.markdown("**Input Image**")
# #             st.image(input_img, caption=input_name, use_column_width=True)
# #         with col2:
# #             st.markdown("**Predicted Image**")
# #             st.image(pred_img, caption=pred_name, use_column_width=True)
# # //////////////////////////////////////////////////////////////////////

# import os
# import shutil
# import streamlit as st
# from PIL import Image

# # Set page layout
# st.set_page_config(layout="wide")

# # Base folder path
# base_folder_path = r'C:\Users\pc\Downloads\Bucket\Bucket'

# # Get all folder names sorted
# folders = sorted([f for f in os.listdir(base_folder_path) if os.path.isdir(os.path.join(base_folder_path, f))])

# # Search for folders
# search_query = st.text_input("Search for a folder:")
# filtered_folders = [f for f in folders if search_query.lower() in f.lower()]

# # Initialize session state for folder index
# if 'folder_index' not in st.session_state:
#     st.session_state.folder_index = 0

# # Navigation buttons
# col_nav1, col_nav2, col_nav3 = st.columns([1, 4, 1])
# with col_nav1:
#     if st.button("⬅️ Back (A)") and st.session_state.folder_index > 0:
#         st.session_state.folder_index -= 1
# with col_nav3:
#     if st.button("Next (D) ➡️") and st.session_state.folder_index < len(filtered_folders) - 1:
#         st.session_state.folder_index += 1

# # Get current folder
# current_folder = filtered_folders[st.session_state.folder_index]
# st.subheader(f"🗂 Folder: `{current_folder}`")

# # Paths for input and predicted folders
# input_folder = os.path.join(base_folder_path, current_folder, 'input')
# predicted_folder = os.path.join(base_folder_path, current_folder, 'predicted')

# # Function to load images from folder
# def load_images_from_folder(folder_path):
#     images = []
#     if not os.path.exists(folder_path):
#         return images
#     for filename in sorted(os.listdir(folder_path)):
#         if filename.lower().endswith('.jpg'):
#             img_path = os.path.join(folder_path, filename)
#             try:
#                 img = Image.open(img_path)
#                 images.append((filename, img))
#             except Exception as e:
#                 st.error(f"Error loading image {filename}: {e}")
#     return images

# # Load images
# input_images = load_images_from_folder(input_folder)
# predicted_images = load_images_from_folder(predicted_folder)

# # Display images
# if not input_images and not predicted_images:
#     st.warning("No images found in either 'input' or 'predicted' for this folder.")
# else:
#     st.markdown("### 📸 Input vs Predicted")
#     for idx, ((input_name, input_img), (pred_name, pred_img)) in enumerate(zip(input_images, predicted_images)):
#         col1, col2 = st.columns(2)
#         with col1:
#             st.markdown("**Input Image**")
#             zoom_factor_input = st.slider(f"Zoom Input Image {input_name}", 1, 5, 1, key=f"zoom_input_{idx}")
#             input_img_resized = input_img.resize((input_img.width * zoom_factor_input, input_img.height * zoom_factor_input))
#             st.image(input_img_resized, caption=input_name, use_column_width=True)
#         with col2:
#             st.markdown("**Predicted Image**")
#             zoom_factor_pred = st.slider(f"Zoom Predicted Image {pred_name}", 1, 5, 1, key=f"zoom_pred_{idx}")
#             pred_img_resized = pred_img.resize((pred_img.width * zoom_factor_pred, pred_img.height * zoom_factor_pred))
#             st.image(pred_img_resized, caption=pred_name, use_column_width=True)

# # Copy selected images
# if st.button("Copy Selected Images"):
#     destination_folder = st.text_input("Enter destination folder path:")
#     if destination_folder:
#         for input_name, input_img in input_images:
#             shutil.copy(input_img, destination_folder)

# # Rename images
# base_name = st.text_input("Enter base name for renaming:")
# if st.button("Rename Images"):
#     for idx, (input_name, input_img) in enumerate(input_images):
#         new_name = f"{base_name}_{idx+1}.jpg"
#         os.rename(input_img, os.path.join(input_folder, new_name))
# ////
import os
import shutil
import uuid
from PIL import Image, ImageOps
import streamlit as st

# Set page layout
st.set_page_config(layout="wide")

# Base folder path
base_folder_path = r'C:\Users\pc\Downloads\Bucket\Bucket'

# Get all folder names sorted
folders = sorted([f for f in os.listdir(base_folder_path) if os.path.isdir(os.path.join(base_folder_path, f))])

# Search for folders
search_query = st.text_input("Search for a folder:")
filtered_folders = [f for f in folders if search_query.lower() in f.lower()]

# Handle no folders match
if not filtered_folders:
    st.warning("No folders match your search.")
    st.stop()

# Session state initialization
if 'folder_index' not in st.session_state:
    st.session_state.folder_index = 0
if 'last_search' not in st.session_state:
    st.session_state.last_search = ''

# Reset index on new search
if st.session_state.last_search != search_query:
    st.session_state.folder_index = 0
    st.session_state.last_search = search_query

# Navigation
col_nav1, col_nav2, col_nav3 = st.columns([1, 4, 1])
with col_nav1:
    if st.button("⬅️ Back (A)") and st.session_state.folder_index > 0:
        st.session_state.folder_index -= 1
with col_nav3:
    if st.button("Next (D) ➡️") and st.session_state.folder_index < len(filtered_folders) - 1:
        st.session_state.folder_index += 1

# Current folder
current_folder = filtered_folders[st.session_state.folder_index]
st.subheader(f"🗂 Folder: `{current_folder}`")

# Paths
input_folder = os.path.join(base_folder_path, current_folder, 'input')
predicted_folder = os.path.join(base_folder_path, current_folder, 'predicted')

# Load images
def load_images_from_folder(folder_path):
    images = []
    if not os.path.exists(folder_path):
        return images
    for filename in sorted(os.listdir(folder_path)):
        if filename.lower().endswith('.jpg'):
            img_path = os.path.join(folder_path, filename)
            try:
                img = Image.open(img_path)
                images.append((filename, img.copy(), img_path))
            except Exception as e:
                st.error(f"Error loading image {filename}: {e}")
    return images

# Add border to selected image
def add_border(img, color='red', border=10):
    return ImageOps.expand(img, border=border, fill=color)

input_images = load_images_from_folder(input_folder)
predicted_images = load_images_from_folder(predicted_folder)

# Display
if not input_images and not predicted_images:
    st.warning("No images found in either 'input' or 'predicted' for this folder.")
    st.stop()
else:
    st.markdown("### 📸 Input vs Predicted")
    st.markdown(f"**Total:** {len(input_images)} input images | {len(predicted_images)} predicted images")

# Image selection
if 'selected_images' not in st.session_state:
    st.session_state.selected_images = []

selected_image = None

for idx, ((input_name, input_img, input_path), (pred_name, pred_img, pred_path)) in enumerate(zip(input_images, predicted_images)):
    col1, col2 = st.columns(2)

    with col1:
        select_input = st.checkbox(f"Select {input_name}", key=f"input_select_{idx}")
        zoom_input = st.slider(f"Zoom Input Image {input_name}", 1, 5, 1, key=f"zoom_input_{idx}")
        if select_input:
            input_img = add_border(input_img)
            selected_image = input_img
        input_img_resized = input_img.resize((input_img.width * zoom_input, input_img.height * zoom_input))
        st.image(input_img_resized, caption=input_name, use_column_width=True)

    with col2:
        select_pred = st.checkbox(f"Select {pred_name}", key=f"pred_select_{idx}")
        zoom_pred = st.slider(f"Zoom Predicted Image {pred_name}", 1, 5, 1, key=f"zoom_pred_{idx}")
        if select_pred:
            pred_img = add_border(pred_img)
            selected_image = pred_img
        pred_img_resized = pred_img.resize((pred_img.width * zoom_pred, pred_img.height * zoom_pred))
        st.image(pred_img_resized, caption=pred_name, use_column_width=True)

# Global zoomed image
if selected_image:
    st.markdown("### 🔍 Zoomed Image")
    zoom_factor = st.slider("Zoom Level", 1, 5, 1)
    zoomed_image = selected_image.resize((selected_image.width * zoom_factor, selected_image.height * zoom_factor))
    st.image(zoomed_image, caption="Zoomed Image", use_column_width=True)

# List selected image names
selected_names = [input_name for idx, (input_name, _, _) in enumerate(input_images) if st.session_state.get(f"input_select_{idx}")]
selected_names += [pred_name for idx, (pred_name, _, _) in enumerate(predicted_images) if st.session_state.get(f"pred_select_{idx}")]

if selected_names:
    st.markdown("### 📝 Selected Images")
    for name in selected_names:
        st.write(name)

# Copy selected images
destination_folder = st.text_input("Enter destination folder path to copy selected images:")
if destination_folder:
    if not os.path.exists(destination_folder):
        st.error("Destination folder does not exist.")
    elif st.button("📥 Copy Selected Images"):
        paths_to_copy = [path for idx, (_, _, path) in enumerate(input_images) if st.session_state.get(f"input_select_{idx}")]
        paths_to_copy += [path for idx, (_, _, path) in enumerate(predicted_images) if st.session_state.get(f"pred_select_{idx}")]
        
        if not paths_to_copy:
            st.warning("No images selected to copy.")
        else:
            for path in paths_to_copy:
                try:
                    shutil.copy(path, destination_folder)
                    st.success(f"Copied: {os.path.basename(path)}")
                except Exception as e:
                    st.error(f"Failed to copy {path}: {e}")

# Rename selected images
base_name = st.text_input("Enter base name for renaming:")
if st.button("✏️ Rename Selected Images"):
    renamed_count = 1
    for idx, (input_name, _, input_path) in enumerate(input_images):
        if st.session_state.get(f"input_select_{idx}"):
            new_name = f"{base_name}_{uuid.uuid4().hex[:6]}.jpg"
            try:
                new_path = os.path.join(input_folder, new_name)
                os.rename(input_path, new_path)
                st.success(f"Renamed {input_name} → {new_name}")
            except Exception as e:
                st.error(f"Error renaming {input_name}: {e}")

    for idx, (pred_name, _, pred_path) in enumerate(predicted_images):
        if st.session_state.get(f"pred_select_{idx}"):
            new_name = f"{base_name}_{uuid.uuid4().hex[:6]}.jpg"
            try:
                new_path = os.path.join(predicted_folder, new_name)
                os.rename(pred_path, new_path)
                st.success(f"Renamed {pred_name} → {new_name}")
            except Exception as e:
                st.error(f"Error renaming {pred_name}: {e}")
