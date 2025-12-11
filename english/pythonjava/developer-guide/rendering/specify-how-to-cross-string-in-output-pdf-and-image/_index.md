---
title: Specify how to cross string in output PDF and image
type: docs
weight: 20
url: /python-java/specify-how-to-cross-string-in-output-pdf-and-image/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Specify how to cross string in output PDF and image**
When a cell contains text or a string that is larger than the width of the cell, the string overflows if the next cell in the next column is null or empty. When you save your Excel file to PDF/Image, you can control this overflow by specifying the cross‑type using the [TextCrossType](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType) enumeration. It has the following values:

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT): Displays like MS Excel; depends on the next cell. If the next cell is null, the string will cross, otherwise it will be truncated.
- [TextCrossType.CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP): Displays the string similar to MS Excel when exporting to PDF/Image.
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE): Displays all the text by crossing other cells and overrides the text of crossed cells.
- [TextCrossType.STRICT_IN_CELL](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL): Displays the string only within the width of the cell.

The following sample code loads the sample Excel file and saves it to PDF/Image format by specifying different TextCrossType values. The sample Excel file and output files can be downloaded from the following links:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **Sample Code**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}
