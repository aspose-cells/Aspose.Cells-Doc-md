---
title: Alignment Settings
description: In the Aspose.Cells for Python via .NET library, you can use cell alignment settings to adjust the layout and display of text. By adjusting settings such as horizontal alignment, vertical alignment, and text wrapping, you have more control over how text flows in cells. This document will provide you with detailed steps and sample code to help you quickly grasp how to use Aspose.Cells for Python via .NET for cell alignment settings.
keywords: Aspose.Cells for Python via .NET, cell alignment, horizontal alignment, vertical alignment, text wrapping
type: docs
weight: 20
url: /python-net/cells-alignment-settings/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
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

All of these alignment settings are fully supported by Aspose.Cells for Python via .NET and are discussed in more detail below.

### **Alignment settings in Aspose.Cells for Python via .NET**

Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides a [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) collection. Each item in the [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) class.

Aspose.Cells for Python via .NET provides [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) and [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) methods for the [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) class that are used to get and set a cell's formatting. The [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) class provides useful properties for configuring alignment settings.

Select any text alignment type using the [**TextAlignmentType**](https://reference.aspose.com/cells/python-net/aspose.cells/textalignmenttype) enumeration. The pre-defined text alignment types in the [**TextAlignmentType**](https://reference.aspose.com/cells/python-net/aspose.cells/textalignmenttype) enumeration are:

|**Text Alignment Types**|**Description**|
| :- | :- |
|GENERAL|Represents general text alignment|
|BOTTOM|Represents bottom text alignment|
|CENTER|Represents center text alignment|
|CENTER_ACROSS|Represents center across text alignment|
|DISTRIBUTED|Represents distributed text alignment|
|FILL|Represents fill text alignment|
|JUSTIFY|Represents justify text alignment|
|LEFT|Represents left text alignment|
|RIGHT|Represents right text alignment|
|TOP|Represents top text alignment|
|JUSTIFIED_LOW|Aligns the text with an adjusted kashida length for Arabic text|
|THAI_DISTRIBUTED|Distributes Thai text specially, because each character is treated as a word|

{{% alert color="primary" %}}

You can also apply the justify distributed setting using the [**Style.is_justify_distributed**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_justify_distributed) property.

{{% /alert %}}

#### **Horizontal Alignment**

Use the [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object's [**horizontal_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells/style/horizontal_alignment) property to align the text horizontally.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.py" >}}

#### **Vertical Alignment**

Similar to horizontal alignment, use the [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object's [**vertical_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells/style/vertical_alignment) property to align the text vertically.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.py" >}}

#### **Indentation**

It is possible to set the indentation level of the text in a cell with the [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object's [**indent_level**](https://reference.aspose.com/cells/python-net/aspose.cells/style/indent_level) property.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-Indentation-1.py" >}}

#### **Orientation**

Set the orientation (rotation) of the text in a cell with the [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object's [**rotation_angle**](https://reference.aspose.com/cells/python-net/aspose.cells/style/rotation_angle) property.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-Orientation-1.py" >}}

#### **Text Control**

The following section discusses how to control text by setting text wrapping, shrink to fit and other formatting options.

##### **Wrapping Text**

Wrapping text in a cell makes it easier to read: the height of the cell adjusts to fit all the text, instead of cutting it off or spilling over into adjacent cells. Set text wrapping on or off with the [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object's [**is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) property.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-WrapText-1.py" >}}

##### **Shrinking to Fit**

An option to wrapping text in a field is to shrink the text size to fit a cell's dimensions. This is done by setting the [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object's [**is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) property to **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.py" >}}

##### **Merging Cells**

Like Microsoft Excel, Aspose.Cells for Python via .NET supports merging several cells into one. Aspose.Cells for Python via .NET provides two approaches to this task. One way is to call the [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) collection's [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) method. The [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) method takes the following parameters to merge the cells:

- First row: the first row from where to start merging.
- First column: the first column from where to start merging.
- Number of rows: the number of rows to merge.
- Number of columns: the number of columns to merge.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Merging-MergingCellsInWorksheet.-1.py" >}}

The other way is to first call the [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) collection's [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) method to create a range of the cells to be merged. The [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) method takes the same set of parameters as that of the [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) method discussed above and returns a [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) object. The [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) object also provides a [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge) method that merges the range specified in the [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) object.

##### **Text Direction**

It is possible to set the reading order of text in cells. The reading order is the visual order in which characters, words, etc. are displayed. For example, English is a left to right language while Arabic is a right to left language.

The reading order is set with the [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object's [**text_direction**](https://reference.aspose.com/cells/python-net/aspose.cells/style/text_direction) property. Aspose.Cells for Python via .NET provides pre-defined text direction types in the [**TextDirectionType**](https://reference.aspose.com/cells/python-net/aspose.cells/textdirectiontype) enumeration.

|**Text Direction Types**|**Description**|
| :- | :- |
|CONTEXT|The reading order consistent with the language of the first entered character|
|LEFT_TO_RIGHT|Left to right reading order|
|RIGHT_TO_LEFT|Right to left reading order|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeTextDirection-1.py" >}}

## **Advance topics**
- [Change Cells Alignment and Keep Existing Formatting](/cells/python-net/change-cells-alignment-and-keep-existing-formatting/)
- [Line Breaks and Text Wrapping](/cells/python-net/line-breaks-and-text-wrapping/)


{{< app/cells/assistant language="python-net" >}}
