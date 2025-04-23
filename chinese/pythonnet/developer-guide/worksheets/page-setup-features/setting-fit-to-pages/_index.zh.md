---
title: 如何使用Python.NET将Excel以适合宽度和高度的页面进行打印
linktitle: 如何将Excel打印为宽度和高度适应的页面
type: docs
weight: 200
url: /zh/python-net/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: 学习使用Aspose.Cells for Python via .NET API设置Excel打印的fit_to_pages_wide和fit_to_pages_tall属性。
keywords: Python Excel打印，Python页面适应设置，Python FitToPagesWide，Python FitToPagesTall，Python将工作表打印为单页，Python打印所有列在一页上
---

## **介绍**

fit_to_pages_wide和fit_to_pages_tall设置控制打印时的电子表格缩放。这些设置确保打印输出适应指定的页面尺寸：

1. **fit_to_pages_wide**：指定水平页面数量以进行打印
1. **fit_to_pages_tall**：指定垂直页面数量以进行打印

## **为什么使用适合页面宽度和高度**
主要优点包括：
1. 精确的打印布局控制
1. 一致的多工作表格式
1. 专业的文件展示

## **如何在Excel中将文件打印为宽度和高度都适合的页面**
在Microsoft Excel中配置方法：
1. 打开工作簿并选择工作表
1. 导航到**页面布局** → **页面设置**对话框
1. 在**页面**选项卡下的**缩放**：
   - 选择“适合”
   - 指定宽（水平）和高（垂直）页数

<br>
<img src="2.png" width=60% />

## **如何使用Aspose.Cells将Excel的宽度和高度适合页面打印**
要以编程方式配置：
1. 加载[示例文件](input.xlsx)
1. 访问工作表的[**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/)对象
1. 设置[**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall/)和[**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide/)属性

```python
from aspose.cells import Workbook

# Instantiating a Workbook object
workbook = Workbook("input.xlsx")

# Accessing the first worksheet in the Excel file
worksheet = workbook.worksheets[0]

# Setting the number of pages to which the length of the worksheet will be spanned
worksheet.page_setup.fit_to_pages_tall = 1

# Setting the number of pages to which the width of the worksheet will be spanned
worksheet.page_setup.fit_to_pages_wide = 1

# Save the workbook
workbook.save("out_net.pdf")
```

输出结果：
<br>
<img src="1.png" width=60% />

## **如何将工作表打印为一页**
要强制输出为单页：
1. 使用 [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)
1. 设置 [**one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/one_page_per_sheet/) 属性

```python
from aspose.cells import Workbook, PdfSaveOptions

# Instantiating a Workbook object
workbook = Workbook("sample.xlsx")

options = PdfSaveOptions()

# Setting OnePagePerSheet option
options.one_page_per_sheet = True

# Save the workbook with options
workbook.save("OnePagePerSheet.pdf", options)
```

输出结果：
<br>
<img src="3.png" width=60% />

## **如何在一页打印所有列**
水平合并列：
1. 配置 [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)
1. 启用 [**all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/all_columns_in_one_page_per_sheet/) 属性

```python
from aspose.cells import Workbook, PdfSaveOptions

# Instantiating a Workbook object
workbook = Workbook("sample.xlsx")

options = PdfSaveOptions()

# Setting all columns in one page per sheet
options.all_columns_in_one_page_per_sheet = True

# Save the workbook
workbook.save("AllColumnsInOnePagePerSheet.pdf", options)
```

输出结果：
<br>
<img src="4.png" width=60% />
