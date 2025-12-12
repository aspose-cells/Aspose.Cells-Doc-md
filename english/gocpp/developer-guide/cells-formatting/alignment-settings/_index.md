---
title: Alignment Settings with Golang via C++
linktitle: Alignment Settings
description: In the Aspose.Cells library, you can use cell alignment settings to adjust the layout and display of text. By adjusting settings such as horizontal alignment, vertical alignment, and text wrapping, you have more control over how text flows in cells. This document will provide you with detailed steps and sample code to help you quickly grasp how to use Aspose.Cells for cell alignment settings.
keywords: Aspose.Cells, cell alignment, horizontal alignment, vertical alignment, text wrapping
type: docs
weight: 20
url: /go-cpp/cells-alignment-settings/
---

## **Configuring Alignment Settings**

### **Alignment settings in Microsoft Excel**

Anyone who has used Microsoft Excel to format cells will be familiar with the alignment settings in Microsoft Excel.

As you can see from the above figure, there are different kinds of alignment options:

- Text alignment (horizontal & vertical)
- Indentation.
- Orientation.
- Text control.
- Text direction.

All of these alignment settings are fully supported by Aspose.Cells and are discussed in more detail below.

### **Alignment settings in Aspose.Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class provides a [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) collection. Each item in the [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class.

Aspose.Cells provides [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) and [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) methods for the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class that are used to get and set a cell's formatting. The [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) class provides useful properties for configuring alignment settings.

Select any text alignment type using the [**TextAlignmentType**](https://reference.aspose.com/cells/go-cpp/textalignmenttype/) enumeration. The predefined text alignment types in the [**TextAlignmentType**](https://reference.aspose.com/cells/go-cpp/textalignmenttype/) enumeration are:

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
|ThaiDistributed|Distributes Thai text because each character is treated as a word.|

{{% alert color="primary" %}}

You can also apply the justify distributed setting using the [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/go-cpp/style/isjustifydistributed/) property.

{{% /alert %}}

#### **Horizontal Alignment**

Use the [**Style**](https://reference.aspose.com/cells/go-cpp/style/) object's [**GetHorizontalAlignment()**](https://reference.aspose.com/cells/go-cpp/style/gethorizontalalignment/) property to align the text horizontally.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings.go" >}}
#### **Vertical Alignment**

Similar to horizontal alignment, use the [**Style**](https://reference.aspose.com/cells/go-cpp/style/) object's [**GetVerticalAlignment()**](https://reference.aspose.com/cells/go-cpp/style/getverticalalignment/) property to align the text vertically.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-1.go" >}}
#### **Indentation**

It is possible to set the indentation level of the text in a cell with the [**Style**](https://reference.aspose.com/cells/go-cpp/style/) object's [**GetIndentLevel()**](https://reference.aspose.com/cells/go-cpp/style/getindentlevel/) property.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-2.go" >}}
#### **Orientation**

Set the orientation (rotation) of the text in a cell with the [**Style**](https://reference.aspose.com/cells/go-cpp/style/) object's [**GetRotationAngle()**](https://reference.aspose.com/cells/go-cpp/style/getrotationangle/) property.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-3.go" >}}
#### **Text Control**

The following section discusses how to control text by setting text wrapping, shrink‑to‑fit and other formatting options.

##### **Wrapping Text**

Wrapping text in a cell makes it easier to read: the height of the cell adjusts to fit all the text, instead of cutting it off or spilling over into adjacent cells. Set text wrapping on or off with the [**Style**](https://reference.aspose.com/cells/go-cpp/style/) object's [**IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/) property.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-4.go" >}}
##### **Shrinking to Fit**

An alternative to wrapping text in a cell is to shrink the text size to fit the cell's dimensions. This is done by setting the [**Style**](https://reference.aspose.com/cells/go-cpp/style/) object's **IsShrinkToFit** property to **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-5.go" >}}
##### **Merging Cells**

Like Microsoft Excel, Aspose.Cells supports merging several cells into one. Aspose.Cells provides two approaches to this task. One way is to call the [**GetCells()**](https://reference.aspose.com/cells/go-cpp/worksheet/getcells/) collection's [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) method. The [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) method takes the following parameters to merge the cells:

- First row: the first row from which to start merging.
- First column: the first column from which to start merging.
- Number of rows: the number of rows to merge.
- Number of columns: the number of columns to merge.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-6.go" >}}
The other way is to first call the [**GetCells()**](https://reference.aspose.com/cells/go-cpp/worksheet/getcells/) collection's [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) method to create a range of the cells to be merged. The [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) method takes the same set of parameters as that of the [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) method discussed above and returns a [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) object. The [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) object also provides a [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) method that merges the range specified in the [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) object.

##### **Text Direction**

It is possible to set the reading order of text in cells. The reading order is the visual order in which characters, words, etc. are displayed. For example, English is a left‑to‑right language while Arabic is a right‑to‑left language.

The reading order is set with the [**Style**](https://reference.aspose.com/cells/go-cpp/style/) object's [**GetTextDirection()**](https://reference.aspose.com/cells/go-cpp/style/gettextdirection/) property. Aspose.Cells provides pre‑defined text direction types in the [**TextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/textdirectiontype/) enumeration.

|**Text Direction Types**|**Description**|
| :- | :- |
|Context|The reading order consistent with the language of the first entered character|
|LeftToRight|Left to right reading order|
|RightToLeft|Right to left reading order|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-7.go" >}}
## **Advanced topics**
- [Change Cells Alignment and Keep Existing Formatting](/cells/cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Line Breaks and Text Wrapping](/cells/cpp/line-breaks-and-text-wrapping/)