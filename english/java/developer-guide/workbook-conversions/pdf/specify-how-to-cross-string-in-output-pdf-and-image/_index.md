---
title: Specify how to cross a string in output PDF and image
type: docs
weight: 110
url: /java/specify-how-to-cross-string-in-output-pdf-and-image/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When a cell contains text or a string that is larger than the width of the cell, the text overflows if the next cell in the next column is null or empty. When you save your Excel file to PDF/Image, you can control this overflow by specifying the cross‑type using the [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType) enumeration. It has the following values:

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT): Displays like MS Excel, depending on the next cell. If the next cell is null, the string will cross; otherwise, it will be truncated.

- [**TextCrossType.CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS-KEEP): Displays the string like MS Excel when exporting to PDF/Image.

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS-OVERRIDE): Displays all the text by crossing other cells and overriding the text of crossed cells.

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT-IN-CELL): Displays the string only within the width of the cell.

## **Specify how to cross a string in output PDF/Image using TextCrossType**

The following sample code loads the sample Excel file and saves it to PDF/Image format by specifying different [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType). The sample Excel file and output files can be downloaded from the following links:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}
{{< app/cells/assistant language="java" >}}
