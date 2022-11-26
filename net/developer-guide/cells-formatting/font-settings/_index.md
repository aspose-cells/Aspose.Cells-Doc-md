---
title: Font Settings
type: docs
weight: 30
url: /net/cells-font-settings/
aliases: [/net/dealing-with-font-settings/,/net/fonts/]
---

{{% alert color="primary" %}}

The look and feel of a text can be controlled by changing font settings. The font settings may include the name, style, size, color and other effects of the fonts. Just like Microsoft Excel, Aspose.Cells also supports configuring the font settings of the cells.

{{% /alert %}}

## **Configuring Font Settings**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) class.

Aspose.Cells provides the [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) class' [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) and [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) methods which are used to get and set a cell's formatting style. The [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) class provides properties for configuring font settings.

### **Setting Font Name**

Developers can apply any font to text inside a cell by using the [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) object's [Name](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name) property.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **Setting Font Style to Bold**

Developers can make text bold by setting the [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) object's [**IsBold**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold) property to **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **Setting Font Size**

Set the font size with the [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) object's [**Size**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size) property.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **Setting Font Color**

Use the [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) object's [**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color) property to set the font color. Select any color from the Color enumeration (part of the .NET framework) and assign it to the [**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color) property.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **Setting Font Underline Type**

Use the [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) object's [**Underline**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline) property to underline text. Aspose.Cells offers various pre-defined font underline types in the [**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype) enumeration.

|**Font Underline Types**|**Description**|
| :- | :- |
|Accounting|A single accounting underline|
|Double|Double underline|
|DoubleAccounting|Double accounting underline|
|None|No underline|
|Single|A single underline|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **Setting Strikeout Effect**

Apply strikeout by setting the [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) object's [**IsStrikeout**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout) property to **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **Setting Subscript Effect**

Apply subscript by setting the [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) object's [**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript) property to **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **Setting Superscript Effect on Font**

Developers can apply the superscript effect on the font by setting the [**IsSuperscript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) property of the [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) object to **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **Advance topics**
- [Apply Superscript and Subscript Effects on Fonts](/cells/net/apply-superscript-and-subscript-effects-on-fonts/)
- [Configuring Fonts for Rendering Spreadsheets](/cells/net/configuring-fonts-for-rendering-spreadsheets/)
- [Get a List of Fonts used in a Spreadsheet or Workbook](/cells/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
- [Set DefaultFont property of PdfSaveOptions and ImageOrPrintOptions to have priority](/cells/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Specify Individual or Private Set of Fonts for Workbook Rendering](/cells/net/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
- [Supported Font Formats](/cells/net/supported-font-formats/)
