import os
import random
import shutil

# Đường dẫn đến thư mục chứa ảnh và nhãn
image_folder = './train/images'
label_folder = './train/labels'

# Đường dẫn đến thư mục tạo ra để chứa tập train và val
image_val_folder = './val/images'
label_val_folder = './val/labels'


image_test_folder = './test/images'
label_test_folder = './test/labels'
# Tỉ lệ chia dữ liệu giữa tập train và val (vd: 80% train, 20% val)
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

# Lấy danh sách tên các file ảnh
image_files = os.listdir(image_folder)

# Số lượng file ảnh dùng cho tập train
num_train = int(train_ratio * len(image_files))
num_val = int(train_ratio * len(image_files)) + int(val_ratio * len(image_files))
# Xáo trộn danh sách tên file ảnh
random.shuffle(image_files)

# Chia danh sách file ảnh thành tập train và val
val_files = image_files[num_train: num_val]
test_files = image_files[num_val:]

# Di chuyển các file ảnh và nhãn vào thư mục tương ứng

for file_name in val_files:
    image_src = os.path.join(image_folder, file_name)
    image_dst = os.path.join(image_val_folder, file_name)
    shutil.move(image_src, image_dst)
    
    # Di chuyển nhãn tương ứng
    label_file = file_name[:-4] + '.txt'
    label_src = os.path.join(label_folder, label_file)
    label_dst = os.path.join(label_val_folder, label_file)
    shutil.move(label_src, label_dst)


for file_name in test_files:
    image_src = os.path.join(image_folder, file_name)
    image_dst = os.path.join(image_test_folder, file_name)
    shutil.move(image_src, image_dst)
    
    # Di chuyển nhãn tương ứng
    label_file = file_name[:-4] + '.txt'
    label_src = os.path.join(label_folder, label_file)
    label_dst = os.path.join(label_test_folder, label_file)
    shutil.move(label_src, label_dst)
print("Chia tập dữ liệu thành công!")
