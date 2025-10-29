---
title: 使用Python.NET在保存为PDF时对特定Unicode字符更改字体
linktitle: 更改特定Unicode字符的字体
type: docs
weight: 260
url: /zh/python-net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: 学习如何在使用Aspose.Cells for Python via .NET进行PDF转换时对特定Unicode字符修改字体。确保字符级字体替换的精确文本渲染。
---

{{% alert color="primary" %}}

 一些Unicode字符被指定字体无法显示。其中之一是**不换行连字符** (U+2011)，Unicode编号为8209。此字符不能用**Times New Roman**显示，但可以用**Arial Unicode MS**等字体显示。

 当此类字符出现在用特定字体（如 Times New Roman）格式的文本中时，Aspose.Cells默认会将整个单词/句子的字体更改为兼容的字体（如 Arial Unicode MS）。如果用户只想更改不可渲染字符的字体，可以通过**PdfSaveOptions.is_font_substitution_char_granularity**属性实现细粒度控制。

{{% /alert %}}

## ** 示例对比**

 下方截图展示了不同设置的输出。第一个PDF显示全文字体替换，第二个PDF仅更改特定字符的字体。

|**全文替换**|**字符级替换**|
| :- | :- |
|![全文字体更改](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|![选择性字体更改](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

## ** 实现步骤**

 要启用字符级字体替换：

 1. 创建一个 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) 对象
 2. 使用 [**Worksheet.cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) 属性访问工作表单元格
 3. 设置包含特殊Unicode字符的单元格值
 4. 配置 [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)：
    - `is_font_substitution_char_granularity = True`
 5. 将工作簿保存为PDF格式

```python
import os
from aspose.cells import Workbook, PdfSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Create workbook object
workbook = Workbook()

# Access the first worksheet
worksheet = workbook.worksheets[0]

# Access cells
cell1 = worksheet.cells.get("A1")
cell2 = worksheet.cells.get("B1")

# Set the styles of both cells to Times New Roman
style = cell1.get_style()
style.font.name = "Times New Roman"
cell1.set_style(style)
cell2.set_style(style)

# Put the values inside the cell
cell1.put_value("Hello without Non-Breaking Hyphen")
cell2.put_value("Hello" + chr(8209) + " with Non-Breaking Hyphen")

# Autofit the columns
worksheet.auto_fit_columns()

# Save to Pdf without setting PdfSaveOptions.is_font_substitution_char_granularity
workbook.save(os.path.join(data_dir, "SampleOutput_out.pdf"))

# Save to Pdf after setting PdfSaveOptions.is_font_substitution_char_granularity to true
opts = PdfSaveOptions()
opts.is_font_substitution_char_granularity = True
workbook.save(os.path.join(data_dir, "SampleOutput2_out.pdf"), opts)
```

## ** 关键配置**

 使用以下必要的API组件：

 - 用于PDF渲染设置的 [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) 类
 - **is_font_substitution_char_granularity** 属性用于字符级字体替换
 - [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/) 方法用于输出生成

{{% alert color="note" %}} 
**API差异说明**：在Python.NET中，布尔属性使用蛇形命名（`is_font_substitution_char_granularity`），而在.NET中使用PascalCase。
{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
