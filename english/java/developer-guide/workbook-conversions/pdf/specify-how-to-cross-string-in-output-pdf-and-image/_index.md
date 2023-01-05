---
title: Specify how to cross string in output PDF and image
type: docs
weight: 110
url: /java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Possible Usage Scenarios**

When a cell contains text or string but it is larger than the width of the cell, then the string overflows if the next cell in next column is null or empty. When you save your Excel file into PDF/Image, you can control this overflow by specifying the cross-type using the [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType) enumeration. It has the following values

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT): Display like MS Excel, depends on the next cell. If the next cell is null, the string will cross or it will be truncated.

- [**TextCrossType. CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_KEEP): Display the string like MS Excel exporting PDF/Image

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_OVERRIDE): Display all the text by crossing other cells and override text of crossed cells

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT_IN_CELL): Only displaying the string within the width of cell.

## **Specify how to cross string in output PDF/Image using TextCrossType**

The following sample code loads the sample Excel file and saves it to PDF/Image format by specifying different [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType). The sample Excel file and output files can be downloaded from the following links:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}
