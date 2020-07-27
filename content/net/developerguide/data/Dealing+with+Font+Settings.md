+++
title = "Dealing with Font Settings" 
description = "" 
weight = 12203 
+++

Aspose.Cells for .NET : Dealing with Font Settings  

# Aspose.Cells for .NET : Dealing with Font Settings


The look and feel of a text can be controlled by changing font settings. The font settings may include the name, style, size, color and other effects of the fonts. Just like Microsoft Excel, Aspose.Cells also supports configuring the font settings of the cells.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Configuring Font Settings](#DealingwithFontSettings-ConfiguringFontSettings)
    *   1.1 [Setting Font Name](#DealingwithFontSettings-SettingFontName)
    *   1.2 [Setting Font Style to Bold](#DealingwithFontSettings-SettingFontStyletoBold)
    *   1.3 [Setting Font Size](#DealingwithFontSettings-SettingFontSize)
    *   1.4 [Setting Font Color](#DealingwithFontSettings-SettingFontColor)
    *   1.5 [Setting Font Underline Type](#DealingwithFontSettings-SettingFontUnderlineType)
    *   1.6 [Setting Strikeout Effect](#DealingwithFontSettings-SettingStrikeoutEffect)
    *   1.7 [Setting Subscript Effect](#DealingwithFontSettings-SettingSubscriptEffect)
    *   1.8 [Setting Superscript Effect on Font](#DealingwithFontSettings-SettingSuperscriptEffectonFont)
{{< /panel >}}
 

 

## Configuring Font Settings

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class contains a [Worksheets](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class. The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides a [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection. Each item in the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection represents an object of the [Cell](https://apireference.aspose.com/net/cells/aspose.cells/cell) class.

Aspose.Cells provides the [Cell](https://apireference.aspose.com/net/cells/aspose.cells/cell) class' [GetStyle](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/getstyle) and [SetStyle](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/setstyle) methods which are used to get and set a cell's formatting style. The [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) class provides properties for configuring font settings.

### Setting Font Name

Developers can apply any font to text inside a cell by using the [Style.Font](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/font) object's [Name](https://apireference.aspose.com/net/cells/aspose.cells/font/properties/name) property.

### Setting Font Style to Bold

Developers can make text bold by setting the [Style.Font](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/font) object's [IsBold](https://apireference.aspose.com/net/cells/aspose.cells/font/properties/isbold) property to **true**.

### Setting Font Size

Set the font size with the [Style.Font](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/font) object's [Size](https://apireference.aspose.com/net/cells/aspose.cells/font/properties/size) property.

### Setting Font Color

Use the [Style.Font](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/font) object's [Color](https://apireference.aspose.com/net/cells/aspose.cells/font/properties/color) property to set the font color. Select any color from the `Color` enumeration (part of the .NET framework) and assign it to the [Color](https://apireference.aspose.com/net/cells/aspose.cells/font/properties/color) property.

### Setting Font Underline Type

Use the [Style.Font](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/font) object's [Underline](https://apireference.aspose.com/net/cells/aspose.cells/font/properties/underline) property to underline text. Aspose.Cells offers various pre-defined font underline types in the [FontUnderlineType](https://apireference.aspose.com/net/cells/aspose.cells/fontunderlinetype) enumeration.

{{< table style="table-striped" >}}
|Font Underline Types|Description|
|:----|:----|
|Accounting|A single accounting underline|
|Double|Double underline|
|DoubleAccounting|Double accounting underline|
|None|No underline|
|Single|A single underline|
{{< /table >}}

### Setting Strikeout Effect

Apply strikeout by setting the [Style.Font](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/font) object's [IsStrikeout](https://apireference.aspose.com/net/cells/aspose.cells/font/properties/isstrikeout) property to **true**.

### Setting Subscript Effect

Apply subscript by setting the [Style.Font](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/font) object's [IsSubScript](https://apireference.aspose.com/net/cells/aspose.cells/font/properties/issubscript) property to **true**.

### Setting Superscript Effect on Font

Developers can apply the superscript effect on the font by setting the [IsSuperscript](https://apireference.aspose.com/net/cells/aspose.cells/font/properties/issuperscript)  property of the [Style.Font](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/font) object to **true**.

