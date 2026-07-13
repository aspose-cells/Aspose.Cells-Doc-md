---
title: 将 Excel 转换为 OFD 格式
linktitle: 将 Excel 转换为 OFD 格式
description: Aspose.Cells for Python via .NET 是一个电子表格处理库，支持将 Excel 工作簿转换为 OFD（开放版式文档）格式。本文演示如何创建 Excel 内容并将其导出为 OFD，以及如何使用 Aspose.Cells 将现有的 Excel 文件转换为 OFD。
keywords: Aspose.Cells, Python via .NET 库, 电子表格, Excel 转 OFD, OFD 转换, SaveFormat.Ofd, 固定版式文档, 工作簿导出
type: docs
weight: 195
url: /zh/python-net/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持使用 `SaveFormat.Ofd` 枚举值将 Excel 工作簿直接转换为 OFD（开放版式文档）格式。生成的 OFD 文档保留了工作簿的可见布局、内容、合并单元格、列宽、行高、字体、颜色、边框和数字格式。这使得 Aspose.Cells 适用于需要固定版式输出的归档、打印、监管申报和政府提交等工作流程。

{{% /alert %}}
## **简介**
OFD（开放版式文档，Open Fixed-layout Document）是中国的一项国家标准（GB/T 33190-2016），用于以固定的、基于页面的版式表示数字文档。在需要准确保留源文档视觉外观的用例中，它的作用类似于 PDF。OFD 广泛应用于中华人民共和国的政府提交、监管申报、电子发票和长期归档。

在需要将电子表格内容作为只读的、版式锁定的文档进行分发（而不是作为可编辑的电子表格）的场景中，将 Excel 工作簿转换为 OFD 是一个常见的需求。例如向客户发送已确定的发票、归档季度财务报告，或向监管机构提交预算电子表格。Aspose.Cells 通过 `SaveFormat.Ofd` 枚举值满足这一需求，该枚举值可将工作簿直接写入 OFD，无需中间转换步骤。OFD 输出保留了工作簿上配置的单元格值、合并区域、字体、颜色、边框、数字格式和页面设置选项。

{{% alert color="primary" %}}

Aspose.Cells 生成的 OFD 输出保留了源工作簿的可见布局，包括单元格内容、合并单元格、列宽和行高。字体、颜色、边框、对齐方式和数字格式等单元格格式也会在固定版式输出中呈现。工作表上配置的页面设置选项（例如纸张大小、方向和打印区域）会影响生成的 OFD 文档的布局。

{{% /alert %}}
## **创建 Excel 工作簿并保存为 OFD**
Aspose.Cells 允许您以编程方式构建工作簿，向其中填充数据，然后使用 `SaveFormat.Ofd` 枚举将其直接保存为 OFD 格式。以下示例从头开始创建一张发票。它添加公司徽标、抬头信息、收款方部分、明细项目以及计算得出的总额，然后将工作簿导出为 OFD 文档。
### **构建带有徽标的发票**
该示例通过在左上角插入徽标图像来构建发票工作表，填写公司名称和联系信息，在合并的单元格中添加"INVOICE"标题，记录发票编号和日期，列出收款方客户，构建包含描述、数量、单价和合计列的明细项目表，并使用单元格公式计算小计、税额和总计。使用 `Style` 和 `Font` 对象应用加粗标题、价格货币格式、边框和列宽等格式。最后，使用 `SaveFormat.Ofd` 以 `.ofd` 扩展名保存工作簿。

```python
from datetime import datetime

data_dir = "C:\\Temp\\"

# 创建一个新的 Workbook
workbook = ac.Workbook()

# 获取第一个工作表
worksheet = workbook.worksheets[0]

# 设置列宽
worksheet.cells.set_column_width(0, 5)
worksheet.cells.set_column_width(1, 35)
worksheet.cells.set_column_width(2, 12)
worksheet.cells.set_column_width(3, 15)
worksheet.cells.set_column_width(4, 15)
worksheet.cells.set_column_width(5, 5)

# 插入公司徽标
worksheet.pictures.add(1, 1, data_dir + "logo.png")

# 公司名称和联系详情
worksheet.cells["B3"].put_value("Acme Corporation")
worksheet.cells["B4"].put_value("123 Business Street")
worksheet.cells["B5"].put_value("City, State 12345")
worksheet.cells["B6"].put_value("Phone: (555) 123-4567")

# INVOICE 标题 - 合并单元格
worksheet.cells.merge(7, 1, 2, 4)
title_cell = worksheet.cells["B8"]
title_cell.put_value("INVOICE")

title_style = workbook.create_style()
title_style.font.is_bold = True
title_style.font.size = 20
title_style.horizontal_alignment = ac.TextAlignmentType.CENTER
title_cell.set_style(title_style)

# 发票编号和日期
worksheet.cells["B11"].put_value("Invoice Number:")
worksheet.cells["C11"].put_value("INV-2024-001")
worksheet.cells["B12"].put_value("Date:")
worksheet.cells["C12"].put_value(datetime.now().strftime("%Y-%m-%d"))

# 收款方信息部分
worksheet.cells["B14"].put_value("Bill To:")
worksheet.cells["B15"].put_value("Client Name")
worksheet.cells["B16"].put_value("Client Address")
worksheet.cells["B17"].put_value("Client City, State")

# 明细项目表头
header_desc = worksheet.cells["B19"]
header_qty = worksheet.cells["C19"]
header_price = worksheet.cells["D19"]
header_total = worksheet.cells["E19"]

header_desc.put_value("Description")
header_qty.put_value("Quantity")
header_price.put_value("Unit Price")
header_total.put_value("Total")

header_style = workbook.create_style()
header_style.font.is_bold = True
header_style.font.color = drawing.Color.white
header_style.background_color = drawing.Color.navy
header_style.horizontal_alignment = ac.TextAlignmentType.CENTER
header_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

header_desc.set_style(header_style)
header_qty.set_style(header_style)
header_price.set_style(header_style)
header_total.set_style(header_style)

# 带边框的货币样式
currency_style = workbook.create_style()
currency_style.custom = "\"$\"#,##0.00"
currency_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

# 用于描述/数量单元格的普通边框样式
border_style = workbook.create_style()
border_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

# 明细项目行
line_items = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
]

for i in range(len(line_items)):
    row = 20 + i
    desc_cell = worksheet.cells[row, 1]
    qty_cell = worksheet.cells[row, 2]
    price_cell = worksheet.cells[row, 3]
    total_cell = worksheet.cells[row, 4]

    desc_cell.put_value(line_items[i][0])
    qty_cell.put_value(line_items[i][1])
    price_cell.put_value(line_items[i][2])
    total_cell.formula = "C" + str(row) + "*D" + str(row)

    desc_cell.set_style(border_style)
    qty_cell.set_style(border_style)
    price_cell.set_style(currency_style)
    total_cell.set_style(currency_style)

# 小计、税金、合计
worksheet.cells["B24"].put_value("Subtotal:")
subtotal_cell = worksheet.cells["E24"]
subtotal_cell.formula = "SUM(E20:E22)"

worksheet.cells["B25"].put_value("Tax (10%):")
tax_cell = worksheet.cells["E25"]
tax_cell.formula = "E24*0.1"

worksheet.cells["B26"].put_value("Grand Total:")
grand_total_cell = worksheet.cells["E26"]
grand_total_cell.formula = "E24+E25"

# 用于合计值的加粗 + 货币样式
total_style = workbook.create_style()
total_style.font.is_bold = True
total_style.custom = "\"$\"#,##0.00"

subtotal_cell.set_style(total_style)
tax_cell.set_style(total_style)
grand_total_cell.set_style(total_style)

# 用于合计标签的加粗样式
bold_style = workbook.create_style()
bold_style.font.is_bold = True

worksheet.cells["B24"].set_style(bold_style)
worksheet.cells["B25"].set_style(bold_style)
worksheet.cells["B26"].set_style(bold_style)

# 将工作簿保存为 OFD 文件
workbook.save(data_dir + "Invoice.ofd", ac.SaveFormat.Ofd)
```
## **将现有 Excel 文件转换为 OFD**
Aspose.Cells 还可以从磁盘加载现有的 Excel 工作簿并将其直接导出为 OFD 格式。这对于批量转换管道、归档工作流程以及源工作簿由其他工具生成且仅需要作为固定版式文档重新发布的场景非常有用。以下示例加载现有的 `.xlsx` 工作簿，从其单元格读取数据，应用可选的页面设置调整，然后将结果保存为 OFD 文档。

```python
from datetime import datetime

dataDir = "C:\\Examples\\"

# 从磁盘打开现有的 Excel 工作簿
workbook = ac.Workbook(dataDir + "SampleBook.xlsx")

# (1) 读取并显示所选单元格的值以确认文件已加载
firstSheet = workbook.worksheets[0]
print("First sheet name: " + firstSheet.name)
print("Cell A1: " + firstSheet.cells["A1"].string_value)
print("Cell B1: " + firstSheet.cells["B1"].string_value)
print("Cell C1: " + firstSheet.cells["C1"].string_value)

# (2) 遍历 Worksheets 集合以枚举可用的工作表
print("\nAvailable worksheets:")
for i in range(workbook.worksheets.count):
    ws = workbook.worksheets[i]
    print("  [" + str(i) + "] " + ws.name)

# (3) 可选择地更新时间戳单元格以反映转换
firstSheet.cells["A1"].put_value("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 在数据块顶部追加一个摘要标题行
firstSheet.cells.insert_row(0)
firstSheet.cells["A1"].put_value("Conversion Summary")
firstSheet.cells["A2"].put_value("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# (4) 在工作表上配置 PageSetup 属性
pageSetup = firstSheet.page_setup
pageSetup.orientation = ac.PageOrientationType.LANDSCAPE
pageSetup.paper_size = ac.PaperSizeType.PAPER_A4
pageSetup.fit_to_pages_tall = 1
pageSetup.fit_to_pages_wide = 1

# (5) 可选择地为 OFD 输出设置打印区域
lastRow = firstSheet.cells.max_data_row
lastCol = firstSheet.cells.max_data_column
lastColLetter = ac.CellsHelper.column_index_to_name(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.page_setup.print_area = printArea
print("\nPrint area set to: " + printArea)

# (6) 将工作簿另存为 OFD 文件
workbook.save(dataDir + "SampleBook.ofd", ac.SaveFormat.Ofd)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")
```

## **相关文章**
- [将 Excel 文件拆分为多个文件](/cells/zh/python-net/splitting-excel-files-into-multiple-files/)
- [在单元格中插入图像](/cells/zh/python-net/inserting-an-image-into-a-cell/)
- [读写 DBF 文件](/cells/zh/python-net/dbf/)
- [在 Aspose.Cells for Python via .NET 中将迷你图转换为图像和 HTML](/cells/zh/python-net/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="python" >}}