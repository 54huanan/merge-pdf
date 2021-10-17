import getopt
import os
import sys
from PyPDF2 import PdfFileMerger

if __name__ == "__main__":
    try:
        options, args = getopt.getopt(sys.argv[1:], None)
    except getopt.GetoptError as e:
        print("Error => {}", e)
        sys.exit()
    target_dir = args[0]
    pdf_lst = [os.path.join(root, file) for root, dirs, files in os.walk(target_dir) for file in files if
               file.endswith(".pdf")]
    print("文件列表：", pdf_lst)

    file_merger = PdfFileMerger()
    for pdf in pdf_lst:
        file_merger.append(pdf, bookmark=os.path.basename(pdf), import_bookmarks=False)  # 合并pdf文件

    file_merger.write(target_dir + "/merge.pdf")
    print("合并成功")
