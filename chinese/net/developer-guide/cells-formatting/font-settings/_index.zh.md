---
title: 字体设置
type: docs
weight: 30
url: /zh/net/cells-font-settings/
---
{{% alert color="primary" %}}

可以通过更改字体设置来控制文本的外观。字体设置可以包括字体的名称、样式、大小、颜色和其他效果。与Microsoft Excel一样，Aspose.Cells也支持配置单元格的字体设置。

{{% /alert %}}

## **配置字体设置**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。中的每一项[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合代表一个对象[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级。

Aspose.Cells 提供了[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级'[**获取样式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)和[**设置样式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)用于获取和设置单元格格式样式的方法。这[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)类提供用于配置字体设置的属性。

### **设置字体名称**

开发人员可以通过使用[**样式.字体**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[姓名](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name)财产。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **将字体样式设置为粗体**

开发人员可以通过设置[**样式.字体**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[**加粗**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold)财产给**真的**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **设置字体大小**

设置字体大小[**样式.字体**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[**尺寸**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)财产。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **设置字体颜色**

使用[**样式.字体**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[**颜色**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)属性来设置字体颜色。从 Color 枚举（.NET 框架的一部分）中选择任何颜色并将其分配给[**颜色**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)财产。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **设置字体下划线类型**

使用[**样式.字体**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[**强调**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline)给文本加下划线的属性。 Aspose.Cells 提供各种预定义的字体下划线类型[**字体下划线类型**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype)枚举。

|**字体下划线类型**|**描述**|
|:- |:- |
|会计|单个会计下划线|
|双倍的|双下划线|
|双重会计|双会计下划线|
|没有任何|无下划线|
|单身的|单下划线|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **设置删除线效果**

通过设置应用删除线[**样式.字体**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[**是三振**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout)财产给**真的**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **设置下标效果**

通过设置应用下标[**样式.字体**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)对象的[**下标**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript)财产给**真的**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **设置字体上标效果**

开发者可以通过设置[**是上标**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript)的财产[**样式.字体**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)反对**真的**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **推进主题**
- [对字体应用上标和下标效果](/cells/zh/net/apply-superscript-and-subscript-effects-on-fonts/)
- [获取电子表格或工作簿中使用的字体列表](/cells/zh/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

