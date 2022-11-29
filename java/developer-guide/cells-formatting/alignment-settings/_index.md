---
title: Alignment Settings
type: docs
weight: 20
url: /java/cells-alignment-settings/
---

## **Configuring Alignment Settings**

## **Alignment settings in Microsoft Excel**

Anyone who has used Microsoft Excel to format cells will be familiar with the alignment settings in Microsoft Excel.

As you can see from the above figure, there are different kinds of alignment options:

- Text alignment(horizontal & vertical)
- Indentation.
- Orientation.
- Text control.
- Text direction.

All of these alignment settings are fully supported by Aspose.Cells and are discussed in more detail below.

## **Alignment settings in Aspose.Cells**

Aspose.Cells provides [**GetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle) and [**SetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle) methods for the [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) class that are used to get and set a cell's formatting. The [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style) class provides useful properties for configuring alignment settings.

Select any text alignment type using the [**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) enumeration. The pre-defined text alignment types in the [**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) enumeration are:

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

You can also apply the justify distributed setting using the [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed) property.

{{% /alert %}}

## **Horizontal , Vertical Alignment and Indentation**

Use the [**HorizontalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment) property to align the text horizontally and [**VerticalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment) property to align the text vertically.
It is possible to set the indentation level of the text in a cell with the [**IndentLevel**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel) property 
and tt only effects when Horizontal alignment is left or right.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **Orientation**

Set the orientation (rotation) of the text in a cell with the [**RotationAngle**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle) property.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **Text Control**

The following section discusses how to control text by setting text wrapping, shrink to fit and other formatting options.

### **Wrapping Text**

Wrapping text in a cell makes it easier to read: the height of the cell adjusts to fit all the text, instead of cutting it off or spilling over into adjacent cells. Set text wrapping on or off with the [**IsTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped) property.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **Shrinking to Fit**

An option to wrapping text in a field is to shrink the text size to fit a cell's dimensions. This is done by setting the [**ShrinkToFit**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit) property. to **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **Merging Cells**

Like Microsoft Excel, Aspose.Cells supports merging several cells into one. Aspose.Cells provides two approaches to this task. One way is to call the [**Merge**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) method. The method takes the following parameters to merge the cells:

- First row: the first row from where to start merging.
- First column: the first column from where to start merging.
- Number of rows: the number of rows to merge.
- Number of columns: the number of columns to merge.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **Text Direction**

It is possible to set the reading order of text in cells. The reading order is the visual order in which characters, words, etc. are displayed. For example, English is a left to right language while Arabic is a right to left language.

The reading order is set with the [**TextDirection**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection) property. Aspose.Cells provides pre-defined text direction types in the [**TextDirectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection) enumeration.

|**Text Direction Types**|**Description**|
| :- | :- |
|Context|The reading order consistent with the language of the first entered character|
|LeftToRight|Left to right reading order|
|RightToLeft|Right to left reading order|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **Advance topics**
- [Change Cells Alignment and Keep Existing Formatting](/cells/java/change-cells-alignment-and-keep-existing-formatting/)
- [Line Breaks and Text Wrapping](/cells/java/line-breaks-and-text-wrapping/)
