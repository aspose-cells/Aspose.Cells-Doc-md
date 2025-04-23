---
title: 使用 Python.NET 设置打印标题
linktitle: 设置打印标题
type: docs
weight: 200
url: /zh/python-net/how-to-set-print-titles/
description: 学习如何使用 Aspose.Cells for Python via .NET 配置打印页面上的重复行/列标题。
keywords: Python 重复打印标题、设置打印标题、清除打印标题、Excel 页面设置 Python、Python.NET 电子表格打印
---

## **可能的使用场景**

在Excel中设置打印标题，确保每个打印页面重复特定的行或列，这对于跨多页的大型电子表格尤为有用。以下是设置打印标题的一些原因：

1. 改善可读性：打印标题帮助读者理解数据，通过在每页保留标题，容易解读每页的信息，而无需回到第一页。

1. 专业表现：在每一页上持续显示标题或标签，使打印的文档看起来更专业、更有条理。

1. 改进导航：对于包含大量数据的文档，在每页重复显示标题有助于更快地进行导航和引用，减少来回翻页的次数。

1. 减少错误：当每页都显示标题时，可以最大限度减少误解或数据录入错误的可能性，因为用户可以轻松查看数据的上下文。

1. 一致性：确保重要信息（如列标题或行标签）始终可见，保持整个文档的一致性和清晰度。

## **在 Excel 设置打印标题的方法**

在 Excel 中设置打印标题，请按照以下步骤操作：

1. 打开页面布局选项卡：点击 Excel 窗口顶部功能区中的“页面布局”。
1. 访问打印标题：在“页面设置”组中，点击“打印标题”。
1. 设置重复行：在“页面设置”对话框中，切换到“工作表”选项卡。在“打印标题”部分，点击“顶端重复的行”旁的框并选择要重复的行。
1. 设置重复列（如需要）：类似地，你可以点击“左侧重复的列”旁的框，并选择要在每页重复的列。
<br>
<img src="3.png" width=60% />

1. 确认并打印：点击“确定”以应用设置。在打印工作表时，指定的行或列将出现在每一页上。

## **在 Excel 中清除打印标题的方法**

要清除 Excel 中的打印标题，需要删除每页都设置为重复的行或列。操作如下：

1. 打开页面布局选项卡：点击 Excel 窗口顶部功能区中的“页面布局”。
1. 访问打印标题：在“页面设置”组中，点击“打印标题”。
1. 清除打印标题：在“页面设置”对话框中，切换到“工作表”选项卡。删除“顶端重复的行”及“左侧重复的列”文本框中的内容。
<br>
<img src="4.png" width=60% />

1. 确认并关闭：点击“确定”以应用更改。

## **使用 Aspose.Cells 设置打印标题的方法**

在特定工作表中设置打印标题：首先，加载[示例文件](input.xlsx)，然后修改 [**Worksheet.page_setup.print_title_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_rows/) 和 [**Worksheet.page_setup.print_title_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_columns/) 属性。将这些属性设置为范围字符串即可配置打印标题。

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Set row 1 as repeating header
worksheet.page_setup.print_title_rows = "$1:$1"

# Save modified workbook
workbook.save("output.xlsx")
```

输出结果：
<br>
<img src="1.png" width=60% />

## **使用 Aspose.Cells 清除打印标题的方法**

要清除打印标题，将打印标题属性设置为空字符串：

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Clear existing print titles
worksheet.page_setup.print_title_rows = ""
worksheet.page_setup.print_title_columns = ""

# Save modified workbook
workbook.save("output.xlsx")
```

输出结果：
<br>
<img src="2.png" width=60% />

```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Set rows to repeat at the top (e.g., rows 1 and 2)
worksheet.page_setup.print_title_rows = "$1:$2"

# Set columns to repeat at the left (e.g., columns A and B)
worksheet.page_setup.print_title_columns = "$A:$B"

# Save the workbook
workbook.save("set_print_titles.pdf")
```
```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Clear the rows and columns set to repeat
worksheet.page_setup.print_title_rows = ""
worksheet.page_setup.print_title_columns = ""

# Save the workbook
workbook.save("clear_print_titles.pdf")
```
