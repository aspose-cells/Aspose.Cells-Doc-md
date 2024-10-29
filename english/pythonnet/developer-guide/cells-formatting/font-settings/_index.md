---
title: Font Settings
description: Aspose.Cells is a .NET library for working with spreadsheet files. It supports setting the font settings of cells, allowing users to customize the font style and properties of cells. This article will introduce how to use the Aspose.Cells library to set cell font settings.
keywords: Aspose.Cells, Cells, Font Settings, Styles, Properties
type: docs
weight: 30
url: /python-net/cells-font-settings/
---

{{% alert color="primary" %}}

The look and feel of a text can be controlled by changing font settings. The font settings may include the name, style, size, color and other effects of the fonts. Just like Microsoft Excel, Aspose.Cells also supports configuring the font settings of the cells.

{{% /alert %}}

## **Configuring Font Settings**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides a [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) collection. Each item in the [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells.worksheet/cells) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) class.

Aspose.Cells provides the [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) class' [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) and [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) methods which are used to get and set a cell's formatting style. The [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) class provides properties for configuring font settings.

### **Setting Font Name**

Developers can apply any font to text inside a cell by using the [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) object's [Name](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name) property.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **Setting Font Style to Bold**

Developers can make text bold by setting the [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) object's [**is_bold**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_bold) property to **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **Setting Font Size**

Set the font size with the [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) object's [**size**](https://reference.aspose.com/cells/python-net/aspose.cells/font/size) property.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **Setting Font Color**

Use the [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) object's [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color) property to set the font color. Select any color from the Color enumeration (part of the .NET framework) and assign it to the [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color) property.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **Setting Font Underline Type**

Use the [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) object's [**underline**](https://reference.aspose.com/cells/python-net/aspose.cells/font/underline) property to underline text. Aspose.Cells offers various pre-defined font underline types in the [**font_underline_type**](https://reference.aspose.com/cells/python-net/aspose.cells/font_underline_type) enumeration.

|**Font Underline Types**|**Description**|
| :- | :- |
|Accounting|A single accounting underline|
|Double|Double underline|
|DoubleAccounting|Double accounting underline|
|None|No underline|
|Single|A single underline|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **Setting Strikeout Effect**

Apply strikeout by setting the [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) object's [**is_strikeout**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_strikeout) property to **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **Setting Subscript Effect**

Apply subscript by setting the [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) object's [**is_sub_script**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_sub_script) property to **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **Setting Superscript Effect on Font**

Developers can apply the superscript effect on the font by setting the [**is_superscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_superscript) property of the [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) object to **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **Advance topics**
- [Apply Superscript and Subscript Effects on Fonts](/cells/python-net/apply-superscript-and-subscript-effects-on-fonts/)
- [Get a List of Fonts used in a Spreadsheet or Workbook](/cells/python-net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

{{< app/cells/assistant language="csharp" >}}
