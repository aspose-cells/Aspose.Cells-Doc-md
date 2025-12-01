---  
title: Font Settings with Node.js via C++  
linktitle: Font Settings  
description: Aspose.Cells is a Node.js library for working with spreadsheet files. It supports setting the font settings of cells, allowing users to customize the font style and properties of cells. This article will introduce how to use the Aspose.Cells library to set cell font settings.  
keywords: Aspose.Cells, Cells, Font Settings, Styles, Properties, Node.js via C++  
type: docs  
weight: 30  
url: /nodejs-cpp/cells-font-settings/  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  
The look and feel of a text can be controlled by changing font settings. The font settings may include the name, style, size, color and other effects of the fonts. Just like Microsoft Excel, Aspose.Cells also supports configuring the font settings of the cells.  
{{% /alert %}}  

## **Configuring Font Settings**  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class.  

Aspose.Cells provides the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class' [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) and [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) methods which are used to get and set a cell's formatting style. The [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) class provides properties for configuring font settings.  

### **Setting Font Name**  

Developers can apply any font to text inside a cell by using the [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) object's [setName](https://reference.aspose.com/cells/nodejs-cpp/font/#setName-string-) method.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontName.js" >}}


### **Setting Font Style to Bold**  

Developers can make text bold by setting the [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) object's [**setIsBold**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsBold-boolean-) method to **true**.   

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetBoldStyle.js" >}}



### **Setting Font Size**  

Set the font size with the [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) object's [**setSize**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSize-number-) method.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontSize.js" >}}


### **Setting Font Color**  

Use the [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) object's [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-) method to set the font color. Select any color from the Color enumeration (part of Node.js) and assign it to the [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-) method.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontColor.js" >}}


### **Setting Font Underline Type**  

Use the [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) object's [**setUnderline**](https://reference.aspose.com/cells/nodejs-cpp/font/#setUnderline-fontunderlinetype-) method to underline text. Aspose.Cells offers various pre-defined font underline types in the [**FontUnderlineType**](https://reference.aspose.com/cells/nodejs-cpp/fontunderlinetype) enumeration.  

|**Font Underline Types**|**Description**|  
| :- | :- |  
|Accounting|A single accounting underline|  
|Double|Double underline|  
|DoubleAccounting|Double accounting underline|  
|None|No underline|  
|Single|A single underline|  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontUnderline.js" >}}


### **Setting Strikeout Effect**  

Apply strikeout by setting the [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) object's [**setIsStrikeout**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsStrikeout-boolean-) method to **true**.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}


### **Setting Subscript Effect**  

Apply subscript by setting the [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) object's [**setIsSubscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSubscript-boolean-) method to **true**.  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}



### **Setting Superscript Effect on Font**  

Developers can apply the superscript effect on the font by setting the [**setIsSuperscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSuperscript-boolean-) method of the [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) object to **true**.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetSuperscript.js" >}}


## **Advance topics**  
- [Apply Superscript and Subscript Effects on Fonts](/cells/nodejs-cpp/apply-superscript-and-subscript-effects-on-fonts/)  
- [Get a List of Fonts used in a Spreadsheet or Workbook](/cells/nodejs-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)  

  
{{< app/cells/assistant language="nodejs-cpp" >}}
