---
title: Dealing with Font Settings
type: docs
weight: 110
url: /java/dealing-with-font-settings/
---

{{% alert color="primary" %}} 

The look and feel of the text can be controlled by changing its font settings. These font settings may include the name, style, size, color and other effects of the fonts as shown below in the figure:

**Font settings in Microsoft Excel** 

![todo:image_alt_text](dealing-with-font-settings_1.png)

Just like Microsoft Excel, Aspose.Cells also supports configuring the font settings of the cells.

{{% /alert %}} 
## **Configuring Font Settings**
Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/cells/java/com.aspose.cells/Workbook) that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/cells/java/com.aspose.cells/Workbook) class contains a [WorksheetCollection](https://apireference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) that allows access to each worksheet in an Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/cells/java/com.aspose.cells/Worksheet) class. The [Worksheet](https://apireference.aspose.com/cells/java/com.aspose.cells/Worksheet) class provides a [Cells](https://apireference.aspose.com/cells/java/com.aspose.cells/Cells) collection. Each item in the [Cells](https://apireference.aspose.com/cells/java/com.aspose.cells/Cells) collection represents an object of the [Cell](https://apireference.aspose.com/cells/java/com.aspose.cells/cell) class.

Aspose.Cells provides the [Cell](https://apireference.aspose.com/cells/java/com.aspose.cells/cell) class' [setStyle](https://apireference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) method, used to set a cell's formatting. Also, the object of the [Style](https://apireference.aspose.com/cells/java/com.aspose.cells/Style) class provides properties for configuring font settings.

This article shows how to:

- [Apply a specific font to text.](/cells/java/dealing-with-font-settings/)
- [Set text to bold](/cells/java/dealing-with-font-settings/).
- [Set the font size](/cells/java/dealing-with-font-settings/).
- [Set the font color](/cells/java/dealing-with-font-settings/).
- [Underline text](/cells/java/dealing-with-font-settings/).
- [Strikeout text](/cells/java/dealing-with-font-settings/).
- [Set text to subscript](/cells/java/dealing-with-font-settings/).
- [Set text to superscript](/cells/java/dealing-with-font-settings/).
### **Setting Font Name**
Apply a specific font to text in cells using the [Font](https://apireference.aspose.com/cells/java/com.aspose.cells/Font) object's [setName](https://apireference.aspose.com/cells/java/com.aspose.cells/font#Name) property.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **Setting Font Style to Bold**
Set text to bold by setting the [Font](https://apireference.aspose.com/cells/java/com.aspose.cells/Font) object's [setBold](https://apireference.aspose.com/cells/java/com.aspose.cells/font#IsBold) property to **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **Setting Font Size**
Set the font size using the [Font](https://apireference.aspose.com/cells/java/com.aspose.cells/Font) object's [setSize](https://apireference.aspose.com/cells/java/com.aspose.cells/font#Size) property.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **Setting Font Underline Type**
Underline text with the [Font](https://apireference.aspose.com/cells/java/com.aspose.cells/Font) object's [setUnderline](https://apireference.aspose.com/cells/java/com.aspose.cells/font#Underline) property. Aspose.Cells offers various pre-defined font underline types in the [FontUnderlineType](https://apireference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType) enumeration.

|**Font Underline Types**|**Description**|
| :- | :- |
|[NONE](https://apireference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|No underline|
|[SINGLE](https://apireference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|A single underline|
|[DOUBLE](https://apireference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|Double underline|
|[ACCOUNTING](https://apireference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|A single accounting underline|
|[DOUBLE_ACCOUNTING](https://apireference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE_ACCOUNTING)|Double accounting underline|
|[DASH](https://apireference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|Dashed Underline|
|[DASH_DOT_DOT_HEAVY](https://apireference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_DOT_HEAVY)|Thick Dash-Dot-Dot Underline|
|[DASH_DOT_HEAVY](https://apireference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_HEAVY)|Thick Dash-Dot Underline|
|[DASHED_HEAVY](https://apireference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED_HEAVY)|Thick Dashed Underline|
|[DASH_LONG](https://apireference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG)|Long Dashed Underline|
|[DASH_LONG_HEAVY](https://apireference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG_HEAVY)|Thick Long Dashed Underline|
|[DOT_DASH](https://apireference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DASH)|Dash-Dot Underline|
|[DOT_DOT_DASH](https://apireference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DOT_DASH)|Dash-Dot-Dot Underline|
|[DOTTED](https://apireference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|Dotted Underline|
|[DOTTED_HEAVY](https://apireference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED_HEAVY)|Thick Dotted Underline|
|[HEAVY](https://apireference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|Thick Underline|
|[WAVE](https://apireference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|Wave Underline|
|[WAVY_DOUBLE](https://apireference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_DOUBLE)|Double Wave Underline|
|[WAVY_HEAVY](https://apireference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_HEAVY)|Heavy Wave Underline|
|` `[WORDS](https://apireference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|Underline Non-Space Characters Only|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **Setting Font Color**
Set the font color with the [Font](https://apireference.aspose.com/cells/java/com.aspose.cells/Font) object's [setColor](https://apireference.aspose.com/cells/java/com.aspose.cells/font#Color) property. Select any color from the [Color](https://apireference.aspose.com/cells/java/com.aspose.cells/Color) enumeration and assign the selected color to the [Font](https://apireference.aspose.com/cells/java/com.aspose.cells/Font) object's [setColor](https://apireference.aspose.com/cells/java/com.aspose.cells/font#Color).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **Setting Strikeout Effect on Text**
Strikeout text with the [Font](https://apireference.aspose.com/cells/java/com.aspose.cells/Font) object's [setStrikeout](https://apireference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout) property.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **Setting Subscript**
Make text superscript by using the [Font](https://apireference.aspose.com/cells/java/com.aspose.cells/Font) object's [setSubscript](https://apireference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript) property.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **Setting Superscript**
Apply superscript to text with the [Font](https://apireference.aspose.com/cells/java/com.aspose.cells/Font) object's [setSuperscript](https://apireference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript) property.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}
