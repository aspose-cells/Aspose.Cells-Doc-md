---
title: 字体设置
description: Aspose.Cells 是一个用于处理电子表格文件的 .NET 库。它支持设置单元格的字体设置，允许用户自定义单元格的字体样式和属性。本文将介绍如何使用Aspose.Cells库来设置单元格字体设置。
keywords: Aspose.Cells, Cells, Font Settings, Styles, Properties
type: docs
weight: 30
url: /zh/net/cells-font-settings/
---
{{% alert color="primary" %}}

文本的外观和感觉可以通过更改字体设置来控制。字体设置可以包括字体的名称、样式、大小、颜色和其他效果。就像Microsoft Excel一样，Aspose.Cells也支持配置单元格的字体设置。

{{% /alert %}}

##  **配置字体设置**

Aspose.Cells提供一堂课，[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)代表 Microsoft Excel 文件。这[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中的每个工作表的集合。工作表由以下形式表示[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。中的每一项[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合代表一个对象[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级。

 Aspose.Cells 提供[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级'[**获取样式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)和[**设置样式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)用于获取和设置单元格格式样式的方法。这[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)类提供用于配置字体设置的属性。

###  **设置字体名称**

开发人员可以使用以下命令将任何字体应用于单元格内的文本[**样式.字体**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[姓名](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name)财产。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

###  **将字体样式设置为粗体**

开发人员可以通过设置将文本加粗[**样式.字体**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[**是粗体**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold)属性为 *true**。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

###  **设置字体大小**

设置字体大小[**样式.字体**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[**尺寸**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)财产。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

###  **设置字体颜色**

使用[**样式.字体**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[**颜色**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)属性来设置字体颜色。从 Color 枚举（.NET 框架的一部分）中选择任何颜色并将其分配给[**颜色**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)财产。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

###  **设置字体下划线类型**

使用[**样式.字体**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[**强调**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline)属性为文本添加下划线。 Aspose.Cells 提供了各种预定义字体下划线类型[**字体下划线类型**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype)枚举。

|**字体下划线类型**|**描述**|
| :- | :- |
|会计|单一会计下划线|
|双倍的|双下划线|
|双重会计|双会计下划线|
|没有任何|无下划线|
|单身的|单下划线|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

###  **设置三振效果**

通过设置应用删除线[**样式.字体**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[**被三振**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout)属性为 *true**。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

###  **设置下标效果**

通过设置应用下标[**样式.字体**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[**是下标**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript)属性为 *true**。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

###  **设置字体上标效果**

开发者可以通过设置在字体上应用上标效果[**是上标**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript)的财产[**样式.字体**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)反对*true**。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

##  **高级主题**
- [对字体应用上标和下标效果](/cells/zh/net/apply-superscript-and-subscript-effects-on-fonts/)
- [获取电子表格或工作簿中使用的字体列表](/cells/zh/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

