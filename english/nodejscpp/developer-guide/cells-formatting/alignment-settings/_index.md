---
title: Alignment Settings
linktitle: Alignment Settings
description: In the Aspose.Cells library, you can use cell alignment settings to adjust the layout and display of text using Node.js via C++. This document provides detailed steps and sample code for using Aspose.Cells for cell alignment settings.
keywords: Aspose.Cells, cell alignment, horizontal alignment, vertical alignment, text wrapping Node.js via C++
type: docs
weight: 20
url: /nodejs-cpp/cells-alignment-settings/
---

## **Configuring Alignment Settings**

### **Alignment settings in Microsoft Excel**

Anyone who has used Microsoft Excel to format cells will be familiar with the alignment settings in Microsoft Excel.

As you can see from the above figure, there are different kinds of alignment options:

- Text alignment(horizontal & vertical)
- Indentation.
- Orientation.
- Text control.
- Text direction.

All of these alignment settings are fully supported by Aspose.Cells and are discussed in more detail below.

### **Alignment settings in Aspose.Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class.

Aspose.Cells provides [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) and [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) methods for the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class that are used to get and set a cell's formatting. The [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) class provides useful properties for configuring alignment settings.

Select any text alignment type using the [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype) enumeration. The pre-defined text alignment types in the [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype) enumeration are:

|**Text Alignment Types**|**Description**|
| :- | :- |
|Bottom|Represents bottom text alignment|
|Center|Represents center text alignment|
|CenterAcross|Represents center across text alignment|
|Distributed|Represents distributed text alignment|
|Fill|Represents fill text alignment|
|General|Represents general text alignment|
|Justify|Represents justify text alignment|
|Left|Represents left text alignment|
|Right|Represents right text alignment|
|Top|Represents top text alignment|
|JustifiedLow|Aligns the text with an adjusted kashida length for Arabic text.|
|ThaiDistributed|Distributes Thai text especially, because each character is treated as a word.|

{{% alert color="primary" %}}

You can also apply the justify distributed setting using the [**Style.setIsJustifyDistributed(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsJustifyDistributed-boolean-) method.

{{% /alert %}}

#### **Horizontal Alignment**

Use the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object's [**setHorizontalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setHorizontalAlignment-textalignmenttype-) method to align the text horizontally.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-HorizontalAlignment.js" >}}



#### **Vertical Alignment**

Similar to horizontal alignment, use the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object's [**setVerticalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setVerticalAlignment-textalignmenttype-) method to align the text vertically.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-VerticalAlignment.js" >}}


#### **Indentation**

It is possible to set the indentation level of the text in a cell with the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object's [**setIndentLevel**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIndentLevel-number-) method.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Indentation.js" >}}



#### **Orientation**

Set the orientation (rotation) of the text in a cell with the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object's [**setRotationAngle**](https://reference.aspose.com/cells/nodejs-cpp/style/#setRotationAngle-number-) method.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Orientation.js" >}}

#### **Text Control**

The following section discusses how to control text by setting text wrapping, shrink to fit and other formatting options.

##### **Wrapping Text**

Wrapping text in a cell makes it easier to read: the height of the cell adjusts to fit all the text, instead of cutting it off or spilling over into adjacent cells. Set text wrapping on or off with the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object's [**setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-) method.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapText.js" >}}


##### **Shrinking to Fit**

An option to wrapping text in a field is to shrink the text size to fit a cell's dimensions. This is done by setting the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object's [**setShrinkToFit(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setShrinkToFit-boolean-) method to **true**.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ShrinkToFit.js" >}}


##### **Merging Cells**

Like Microsoft Excel, Aspose.Cells supports merging several cells into one. Aspose.Cells provides two approaches to this task. One way is to call the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) collection's [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) method. The [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) method takes the following parameters to merge the cells:

- First row: the first row from where to start merging.
- First column: the first column from where to start merging.
- Number of rows: the number of rows to merge.
- Number of columns: the number of columns to merge.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-MergeCells.js" >}}


The other way is to first call the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) collection's [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) method to create a range of the cells to be merged. The [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) method takes the same set of parameters as that of the [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) method discussed above and returns a [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) object. The [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) object also provides a [**merge**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) method that merges the range specified in the [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) object.

##### **Text Direction**

It is possible to set the reading order of text in cells. The reading order is the visual order in which characters, words, etc. are displayed. For example, English is a left to right language while Arabic is a right to left language.

The reading order is set with the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object's [**TextDirection**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTextDirection-textdirectiontype-) property. Aspose.Cells provides pre-defined text direction types in the [**TextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/textdirectiontype) enumeration.

|**Text Direction Types**|**Description**|
| :- | :- |
|Context|The reading order consistent with the language of the first entered character|
|LeftToRight|Left to right reading order|
|RightToLeft|Right to left reading order|

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-TextDirection.js" >}}


## **Advance topics**
- [Change Cells Alignment and Keep Existing Formatting](/cells/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Line Breaks and Text Wrapping](/cells/nodejs-cpp/line-breaks-and-text-wrapping/)

{{< app/cells/assistant language="nodejs-cpp" >}}