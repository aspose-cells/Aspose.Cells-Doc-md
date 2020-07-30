---
title : "Configuring Alignment Settings" 
description : "" 
weight : 12200 
toc : false
type: docs
url: /net/developerguide/data/configuring+alignment+settings/
---

# Aspose.Cells for .NET : Configuring Alignment Settings


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Configuring Alignment Settings](#configuring-alignment-settings)
    *   1.1 [Alignment settings in Microsoft Excel](#alignment-settings-in-microsoft-excel)
    *   1.2 [Alignment settings in Aspose.Cells](#alignment-settings-in-aspose.cells)
        *   1.2.1 [Horizontal Alignment](#horizontal-alignment)
        *   1.2.2 [Vertical Alignment](#vertical-alignment)
        *   1.2.3 [Indentation](#indentation)
        *   1.2.4 [Orientation](#orientation)
        *   1.2.5 [Text Control](#text-control)
            *   1.2.5.1 [Wrapping Text](#wrapping-text)
            *   1.2.5.2 [Shrinking to Fit](#shrinking-to-fit)
            *   1.2.5.3 [Merging Cells](#merging-cells)
            *   1.2.5.4 [Text Direction](#text-direction)
{{< /panel >}}
 

## Configuring Alignment Settings

### Alignment settings in Microsoft Excel

Anyone who has used Microsoft Excel to format cells will be familiar with the alignment settings in Microsoft Excel.

As you can see from the above figure, there are different kinds of alignment options:

*   Text alignment(horizontal & vertical)
*   Indentation.
*   Orientation.
*   Text control.
*   Text direction.

All of these alignment settings are fully supported by Aspose.Cells and are discussed in more detail below.

### Alignment settings in Aspose.Cells

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook), that represents an Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook)class contains a [Worksheets](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class. The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides a [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection. Each item in the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection represents an object of the [Cell](https://apireference.aspose.com/net/cells/aspose.cells/cell) class.

Aspose.Cells provides [GetStyle](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/getstyle) and [SetStyle](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/setstyle) methods for the [Cell](https://apireference.aspose.com/net/cells/aspose.cells/cell) class that are used to get and set a cell's formatting. The [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) class provides useful properties for configuring alignment settings.

Select any text alignment type using the [TextAlignmentType](https://apireference.aspose.com/net/cells/aspose.cells/textalignmenttype) enumeration. The pre-defined text alignment types in the [TextAlignmentType](https://apireference.aspose.com/net/cells/aspose.cells/textalignmenttype) enumeration are:

{{< table style="table-striped" >}}
|Text Alignment Types|Description|
|:----|:----|
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
{{< /table >}}

You can also apply the justify distributed setting using the [Style.IsJustifyDistributed](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/isjustifydistributed) property.

#### Horizontal Alignment

Use the [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object's [HorizontalAlignment](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/horizontalalignment) property to align the text horizontally.

#### Vertical Alignment

Similar to horizontal alignment, use the [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object's [VerticalAlignment](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/verticalalignment) property to align the text vertically.

#### Indentation

It is possible to set the indentation level of the text in a cell with the [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object's [IndentLevel](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/indentlevel) property.

#### Orientation

Set the orientation (rotation) of the text in a cell with the [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object's [RotationAngle](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/rotationangle) property.

#### Text Control

The following section discusses how to control text by setting text wrapping, shrink to fit and other formatting options.

##### Wrapping Text

Wrapping text in a cell makes it easier to read: the height of the cell adjusts to fit all the text, instead of cutting it off or spilling over into adjacent cells. Set text wrapping on or off with the [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object's [IsTextWrapped](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/istextwrapped) property.

##### Shrinking to Fit

An option to wrapping text in a field is to shrink the text size to fit a cell's dimensions. This is done by setting the [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object's [IsTextWrapped](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/istextwrapped) property to **true**.

##### Merging Cells

Like Microsoft Excel, Aspose.Cells supports merging several cells into one. Aspose.Cells provides two approaches to this task. One way is to call the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection's [Merge](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/merge/index) method. The [Merge](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/merge/index) method takes the following parameters to merge the cells:

*   First row: the first row from where to start merging.
*   First column: the first column from where to start merging.
*   Number of rows: the number of rows to merge.
*   Number of columns: the number of columns to merge.

  
The other way is to first call the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection's [CreateRange](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/createrange/index) method to create a range of the cells to be merged. The [CreateRange](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/createrange/index) method takes the same set of parameters as that of the [Merge](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/merge/index) method discussed above and returns a [Range](https://apireference.aspose.com/net/cells/aspose.cells/range) object. The [Range](https://apireference.aspose.com/net/cells/aspose.cells/range) object also provides a [Merge](https://apireference.aspose.com/net/cells/aspose.cells/range/methods/merge) method that merges the range specified in the [Range](https://apireference.aspose.com/net/cells/aspose.cells/range) object.

##### Text Direction

It is possible to set the reading order of text in cells. The reading order is the visual order in which characters, words, etc. are displayed. For example, English is a left to right language while Arabic is a right to left language.

The reading order is set with the [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object's [TextDirection](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/textdirection) property. Aspose.Cells provides pre-defined text direction types in the [TextDirectionType](https://apireference.aspose.com/net/cells/aspose.cells/textdirectiontype) enumeration.

{{< table style="table-striped" >}}
|Text Direction Types|Description|
|:----|:----|
|Context|The reading order consistent with the language of the first entered character|
|LeftToRight|Left to right reading order|
|RightToLeft|Right to left reading order|
{{< /table >}}

  
  

