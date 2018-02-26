# coding:utf-8
import os
import shutil
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# print os.getcwd()
# 有些文件夹下面有很多文件夹，每个文件夹下面有很多视频文件，现在通过脚本，将文件夹下面的所有文件转移到一个目录下面

# 统计访问的文件夹数量及文件数量
countNum = [0, ]
countFile = [0, ]
# 选择全部移除或者指定后缀名文件


# 查找文件
def move_all_files(dir_path):
    if os.path.exists(dir_path):
        countNum[0] += 1
        # 输出遍历的文件夹数量
        print "*****", countNum[0], "*****"+dir_path
        # 指定文件夹下的所有文件和文件夹
        path_list = os.listdir(dir_path)
        # 遍历
        for each_path in path_list:
            # 如果是文件夹就继续遍历
            print each_path
            if os.path.isdir(dir_path+"\\"+each_path):
                # 移动所有文件到指定目录下面
                src=dir_path+"\\"+each_path
                move_all_files(src)
            else:
                # 如果是指定文件类型，则复制文件
                file_type = os.path.splitext(each_path)[1]
                # 判断是否为选择的文件类型
                selected = False
                if file_type == select_type or select_type == 'All':
                    selected = True
                if selected:
                    # 复制文件
                    src_file = dir_path + "\\" + each_path
                    des_file = des_pos + "\\" + each_path
                    print "正在复制", each_path
                    shutil.copyfile(src_file, des_file)
                    # 文件+1
                    countFile[0] += 1
    else:
        print "指定路径不存在"


# 需要复制文件的文件夹位置
give_pos = r"C:\Users\lance\Downloads\Java Web编程相关"
# 需要复制到的位置
des_pos = r"C:\Users\lance\Downloads\测试"
# All 或者 指定文件后缀名
select_type = 'All'
# 如果不存在，创建
if not os.path.exists(unicode(des_pos, 'utf-8')):
    os.mkdir(unicode(des_pos, "utf-8"))
# 移动文件
move_all_files(unicode(give_pos, "utf-8"))
print "将文件从****'", give_pos, "'复制到****'", des_pos, "'"
print "共访问了", countNum[0], "个文件夹"
print "共复制了 ", countFile[0], " 个文件"