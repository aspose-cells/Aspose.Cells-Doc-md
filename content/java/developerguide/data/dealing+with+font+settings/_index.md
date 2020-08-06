---
title : "Dealing with Font Settings" 
description : "" 
weight : 12170 
toc : false
type: docs
url: /java/developerguide/data/dealing+with+font+settings/
---

# Aspose.Cells for Java : Dealing with Font Settings



{{< panel title="Contents Summary" style="primary" >}}
*   1 [Configuring Font Settings](#configuring-font-settings)
    *   1.1 [Setting Font Name](#setting-font-name)
    *   1.2 [Setting Font Style to Bold](#setting-font-style-to-bold)
    *   1.3 [Setting Font Size](#setting-font-size)
    *   1.4 [Setting Font Underline Type](#setting-font-underline-type)
    *   1.5 [Setting Font Color](#setting-font-color)
    *   1.6 [Setting Strikeout Effect on Text](#setting-strikeout-effect-on-text)
    *   1.7 [Setting Subscript](#setting-subscript)
    *   1.8 [Setting Superscript](#setting-superscript)
{{< /panel >}}
 

The look and feel of the text can be controlled by changing its font settings. These font settings may include the name, style, size, color and other effects of the fonts as shown below in the figure:

**Font settings in Microsoft Excel**  
![image](5473162.png)

Just like Microsoft Excel, Aspose.Cells also supports configuring the font settings of the cells.

### Configuring Font Settings

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/Workbook) that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/Workbook) class contains a [WorksheetCollection](https://apireference.aspose.com/java/cells/com.aspose.cells/WorksheetCollection) that allows access to each worksheet in an Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class. The [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class provides a [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection. Each item in the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection represents an object of the [Cell](https://apireference.aspose.com/java/cells/com.aspose.cells/cell) class.

Aspose.Cells provides the [Cell](https://apireference.aspose.com/java/cells/com.aspose.cells/cell) class' [setStyle](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#setStyle(com.aspose.cells.Style)) method, used to set a cell's formatting. Also, the object of the [Style](https://apireference.aspose.com/java/cells/com.aspose.cells/Style) class provides properties for configuring font settings.

This article shows how to:

*   [Apply a specific font to text.](https://docs2.aspose.com/cells/java/developerguide/data/dealing+with+font+settings)
*   [Set text to bold](https://docs2.aspose.com/cells/java/developerguide/data/dealing+with+font+settings).
*   [Set the font size](https://docs2.aspose.com/cells/java/developerguide/data/dealing+with+font+settings).
*   [Set the font color](https://docs2.aspose.com/cells/java/developerguide/data/dealing+with+font+settings).
*   [Underline text](https://docs2.aspose.com/cells/java/developerguide/data/dealing+with+font+settings).
*   [Strikeout text](https://docs2.aspose.com/cells/java/developerguide/data/dealing+with+font+settings).
*   [Set text to subscript](https://docs2.aspose.com/cells/java/developerguide/data/dealing+with+font+settings).
*   [Set text to superscript](https://docs2.aspose.com/cells/java/developerguide/data/dealing+with+font+settings).

#### Setting Font Name

Apply a specific font to text in cells using the [Font](https://apireference.aspose.com/java/cells/com.aspose.cells/Font) object's [setName](https://apireference.aspose.com/java/cells/com.aspose.cells/font#Name) property.

#### Setting Font Style to Bold

Set text to bold by setting the [Font](https://apireference.aspose.com/java/cells/com.aspose.cells/Font) object's [setBold](https://apireference.aspose.com/java/cells/com.aspose.cells/font#IsBold) property to **true**.

#### Setting Font Size

Set the font size using the [Font](https://apireference.aspose.com/java/cells/com.aspose.cells/Font) object's [setSize](https://apireference.aspose.com/java/cells/com.aspose.cells/font#Size) property.

#### Setting Font Underline Type

Underline text with the [Font](https://apireference.aspose.com/java/cells/com.aspose.cells/Font) object's [setUnderline](https://apireference.aspose.com/java/cells/com.aspose.cells/font#Underline) property. Aspose.Cells offers various pre-defined font underline types in the [FontUnderlineType](https://apireference.aspose.com/java/cells/com.aspose.cells/FontUnderlineType) enumeration.

{{< table style="table-striped" >}}
|Font Underline Types|Description|
|:----|:----|
|[NONE](https://apireference.aspose.com/java/cells/com.aspose.cells/fontunderlinetype#NONE)|No underline|
|[SINGLE](https://apireference.aspose.com/java/cells/com.aspose.cells/fontunderlinetype#SINGLE)|A single underline|
|[DOUBLE](https://apireference.aspose.com/java/cells/com.aspose.cells/fontunderlinetype#DOUBLE)|Double underline|
|[ACCOUNTING](https://apireference.aspose.com/java/cells/com.aspose.cells/fontunderlinetype#ACCOUNTING)|A single accounting underline|
|[DOUBLE\_ACCOUNTING](https://apireference.aspose.com/java/cells/com.aspose.cells/fontunderlinetype#DOUBLE_ACCOUNTING)|Double accounting underline|
|[DASH](https://apireference.aspose.com/java/cells/com.aspose.cells/fontunderlinetype#DASH)|Dashed Underline|
|[DASH\_DOT\_DOT\_HEAVY](https://apireference.aspose.com/java/cells/com.aspose.cells/fontunderlinetype#DASH_DOT_DOT_HEAVY)|Thick Dash-Dot-Dot Underline|
|[DASH\_DOT\_HEAVY](https://apireference.aspose.com/java/cells/com.aspose.cells/fontunderlinetype#DASH_DOT_HEAVY)|Thick Dash-Dot Underline|
|[DASHED\_HEAVY](https://apireference.aspose.com/java/cells/com.aspose.cells/fontunderlinetype#DASHED_HEAVY)|Thick Dashed Underline|
|[DASH\_LONG](https://apireference.aspose.com/java/cells/com.aspose.cells/fontunderlinetype#DASH_LONG)|Long Dashed Underline|
|[DASH\_LONG\_HEAVY](https://apireference.aspose.com/java/cells/com.aspose.cells/fontunderlinetype#DASH_LONG_HEAVY)|Thick Long Dashed Underline|
|[DOT\_DASH](https://apireference.aspose.com/java/cells/com.aspose.cells/fontunderlinetype#DOT_DASH)|Dash-Dot Underline|
|[DOT\_DOT\_DASH](https://apireference.aspose.com/java/cells/com.aspose.cells/fontunderlinetype#DOT_DOT_DASH)|Dash-Dot-Dot Underline|
|[DOTTED](https://apireference.aspose.com/java/cells/com.aspose.cells/fontunderlinetype#DOTTED)|Dotted Underline|
|[DOTTED\_HEAVY](https://apireference.aspose.com/java/cells/com.aspose.cells/fontunderlinetype#DOTTED_HEAVY)|Thick Dotted Underline|
|[HEAVY](https://apireference.aspose.com/java/cells/com.aspose.cells/fontunderlinetype#HEAVY)|Thick Underline|
|[WAVE](https://apireference.aspose.com/java/cells/com.aspose.cells/fontunderlinetype#WAVE)|Wave Underline|
|[WAVY\_DOUBLE](https://apireference.aspose.com/java/cells/com.aspose.cells/fontunderlinetype#WAVY_DOUBLE)|Double Wave Underline|
|[WAVY\_HEAVY](https://apireference.aspose.com/java/cells/com.aspose.cells/fontunderlinetype#WAVY_HEAVY)|Heavy Wave Underline|
|[WORDS](https://apireference.aspose.com/java/cells/com.aspose.cells/fontunderlinetype#WORDS)|Underline Non-Space Characters Only|
{{< /table >}}

  

#### Setting Font Color

Set the font color with the [Font](https://apireference.aspose.com/java/cells/com.aspose.cells/Font) object's [setColor](https://apireference.aspose.com/java/cells/com.aspose.cells/font#Color) property. Select any color from the [Color](https://apireference.aspose.com/java/cells/com.aspose.cells/Color) enumeration and assign the selected color to the [Font](https://apireference.aspose.com/java/cells/com.aspose.cells/Font) object's [setColor](https://apireference.aspose.com/java/cells/com.aspose.cells/font#Color).

  

#### Setting Strikeout Effect on Text

Strikeout text with the [Font](https://apireference.aspose.com/java/cells/com.aspose.cells/Font) object's [setStrikeout](https://apireference.aspose.com/java/cells/com.aspose.cells/font#IsStrikeout) property.

  

#### Setting Subscript

Make text superscript by using the [Font](https://apireference.aspose.com/java/cells/com.aspose.cells/Font) object's [setSubscript](https://apireference.aspose.com/java/cells/com.aspose.cells/font#IsSubscript) property.

  

#### Setting Superscript

Apply superscript to text with the [Font](https://apireference.aspose.com/java/cells/com.aspose.cells/Font) object's [setSuperscript](https://apireference.aspose.com/java/cells/com.aspose.cells/font#IsSuperscript) property.

