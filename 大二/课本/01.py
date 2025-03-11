from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import IndirectObject

def delete_even_pages(input_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # 添加奇数页到输出文件
    for i in range(len(reader.pages)):
        if i % 2 == 0:  # 保留奇数页（索引从0开始）
            writer.add_page(reader.pages[i])

    # 手动复制书签，并保留原始目标页码
    def copy_outline(outline, parent=None):
        for item in outline:
            if isinstance(item, dict):  # 处理单个书签
                page_ref = item.get("/Page", None)
                if isinstance(page_ref, IndirectObject):
                    page_obj = page_ref.get_object()  # 获取实际的页面对象
                    original_page_num = reader.get_page_number(page_obj)  # 获取原始页码
                else:
                    original_page_num = reader.get_page_number(page_ref)

                if original_page_num is not None:
                    # 直接使用原始页码作为目标页码
                    writer.add_outline_item(
                        title=item.get("/Title", "Untitled"),
                        page_number=original_page_num,
                        parent=parent
                    )
            elif isinstance(item, list):  # 处理嵌套书签
                parent_item = None  # 初始化父书签
                for sub_item in item:  # 遍历子书签
                    if isinstance(sub_item, dict):
                        page_ref = sub_item.get("/Page", None)
                        if isinstance(page_ref, IndirectObject):
                            page_obj = page_ref.get_object()
                            original_page_num = reader.get_page_number(page_obj)
                        else:
                            original_page_num = reader.get_page_number(page_ref)

                        if original_page_num is not None:
                            if parent_item is None:  # 创建父书签
                                parent_item = writer.add_outline_item(
                                    title=sub_item.get("/Title", "Untitled"),
                                    page_number=original_page_num,
                                    parent=parent
                                )
                            else:  # 添加子书签
                                writer.add_outline_item(
                                    title=sub_item.get("/Title", "Untitled"),
                                    page_number=original_page_num,
                                    parent=parent_item
                                )

    # 检查是否有书签
    if reader.outline:
        copy_outline(reader.outline)

    # 写入输出文件
    with open(output_pdf, "wb") as output_pdf_file:
        writer.write(output_pdf_file)

# 使用示例
delete_even_pages("计算机网络_978-7-121-42506-6.pdf", "output_with_outline.pdf")