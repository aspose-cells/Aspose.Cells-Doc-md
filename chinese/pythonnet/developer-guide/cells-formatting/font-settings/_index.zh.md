---
title: 字体设置
description: Aspose.Cells 是一个用于处理电子表格文件的 Python 库。它支持设置单元格的字体属性，允许用户自定义单元格的字体样式和属性。本文将介绍如何使用 Aspose.Cells for Python via .NET 库设置单元格字体。
keywords: Aspose.Cells for Python via .NET，单元格，字体设置，样式，属性
type: docs
weight: 30
url: /zh/python-net/cells-font-settings/
---

{{% alert color="primary" %}}

文本的外观可以通过更改字体设置来控制。字体设置可能包括字体名称、样式、大小、颜色及其他效果。就像微软 Excel 一样，Aspose.Cells for Python via .NET 也支持配置单元格的字体设置。

{{% /alert %}}

## **配置字体设置**

Aspose.Cells for Python via .NET 提供了一个类 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)，代表微软 Excel 文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类包含一个 [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) 集合，可以访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类提供一个 [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) 集合。[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) 集合中的每个项目表示 [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) 类的对象。

Aspose.Cells提供了[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)类的[**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style)和[**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style)方法，用于获取和设置单元格的格式样式。[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)类提供了用于配置字体设置的属性。

### **设置字体名称**

开发者可以使用 [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) 对象的 [**name**](https://reference.aspose.com/cells/python-net/aspose.cells/font/name/) 属性，将任何字体应用于单元格内的文本。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontName-1.py" >}}

### **将字体样式设置为粗体**

开发人员通过将[**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)对象的[**is_bold**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_bold)属性设置为**true**来使文本加粗。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontStyle.py" >}}

### **设置字体大小**

使用[**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)对象的[**size**](https://reference.aspose.com/cells/python-net/aspose.cells/font/size)属性设置字体大小。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontSize.py" >}}

### **设置字体颜色**

使用[**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)对象的[**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color)属性设置字体颜色。从Color枚举（.NET框架的一部分）中选择任何颜色，并将其分配给[**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color)属性。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontColor.py" >}}

### **设置字体下划线类型**

使用 [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) 对象的 [**underline**](https://reference.aspose.com/cells/python-net/aspose.cells/font/underline) 属性为文本添加下划线。Aspose.Cells for Python via .NET 提供了在 [**FontUnderlineType**](https://reference.aspose.com/cells/python-net/aspose.cells/fontunderlinetype) 枚举中的各种预定义字体下划线类型。

|**字体下划线类型**|**描述**|
| :- | :- |
|ACCOUNTING|单一会计下划线|
|DOUBLE|双下划线|
|DOUBLE_ACCOUNTING|双重会计下划线|
|NONE|无下划线|
|SINGLE|单一下划线|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontUnderlineType-1.py" >}}

### **设置删除线效果**

通过将[**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)对象的[**is_strikeout**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_strikeout)属性设置为**true**应用删除线。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetStrikeout.py" >}}

### **设置下标效果**

通过将[**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)对象的[**is_subscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_subscript/)属性设置为**true**应用下标。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetSubscript.py" >}}

### **在字体上设置上标效果**

开发人员可以通过将[**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)对象的[**is_superscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_superscript)属性设置为**true**在字体上应用上标效果。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetSuperscript.py" >}}

## **高级主题**
- [在字体上应用上标和下标效果](/cells/zh/python-net/apply-superscript-and-subscript-effects-on-fonts/)
- [获取电子表格或工作簿中使用的字体列表](/cells/zh/python-net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)


{{< app/cells/assistant language="python-net" >}}
