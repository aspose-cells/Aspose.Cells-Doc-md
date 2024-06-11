---
title: 字体设置
description: Aspose.Cells 是用于处理电子表格文件的 .NET 库。它支持设置单元格的字体设置，允许用户自定义单元格的字体样式和属性。本文将介绍如何使用 Aspose.Cells 库来设置单元格的字体设置。
keywords: Aspose.Cells, Cells, 字体设置, 样式, 属性
type: docs
weight: 30
url: /zh/net/cells-font-settings/
---

{{% alert color="primary" %}}

通过更改字体设置可以控制文本的外观。字体设置可能包括字体的名称、样式、大小、颜色和其他效果。就像 Microsoft Excel 一样，Aspose.Cells 也支持配置单元格的字体设置。

{{% /alert %}}

## **配置字体设置**

Aspose.Cells提供了一个类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，它代表了一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合中的每个项代表了[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类的对象。

Aspose.Cells提供了[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类的[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)和[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)方法，用于获取和设置单元格的格式样式。[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)类提供了用于配置字体设置的属性。

### **设置字体名称**

开发人员可以通过使用{Name}属性将任何字体应用于单元格内的文本。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **将字体样式设置为粗体**

开发人员通过将[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[**IsBold**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold)属性设置为**true**来使文本加粗。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **设置字体大小**

使用[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[**Size**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)属性设置字体大小。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **设置字体颜色**

使用[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)属性设置字体颜色。从Color枚举（.NET框架的一部分）中选择任何颜色，并将其分配给[**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **设置字体下划线类型**

使用[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[**Underline**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline)属性给文本添加下划线。Aspose.Cells在[**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype)枚举中提供了各种预定义的字体下划线类型。

|**字体下划线类型**|**描述**|
| :- | :- |
|Accounting| 单下划线|
|Double| 双下划线|
|DoubleAccounting| 双帐目下划线|
|None| 无下划线|
|Single| 单下划线|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **设置删除线效果**

通过将[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[**IsStrikeout**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout)属性设置为**true**应用删除线。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **设置下标效果**

通过将[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript)属性设置为**true**应用下标。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **在字体上设置上标效果**

开发人员可以通过将[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[**IsSuperscript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript)属性设置为**true**在字体上应用上标效果。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **高级主题**
- [在字体上应用上标和下标效果](/cells/zh/net/apply-superscript-and-subscript-effects-on-fonts/)
- [获取电子表格或工作簿中使用的字体列表](/cells/zh/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

