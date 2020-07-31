---
title : "Specify how to cross string in output PDF and image" 
description : "" 
weight : 12083 
toc : false
type: docs
url: /java/developerguide/rendering/specify+how+to+cross+string+in+output+pdf+and+image/
---

# Aspose.Cells for Java : Specify how to cross string in output PDF and image


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Specify how to cross string in output PDF/Image using TextCrossType](#specify-how-to-cross-string-in-output-pdf/image-using-textcrosstype)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

When a cell contains text or string but it is larger than the width of the cell, then the string overflows if the next cell in next column is null or empty. When you save your Excel file into PDF/Image, you can control this overflow by specifying the cross-type using the [TextCrossType](https://apireference.aspose.com/java/cells/com.aspose.cells/TextCrossType) enumeration. It has the following values

*   **[TextCrossType.DEFAULT](https://apireference.aspose.com/java/cells/com.aspose.cells/textcrosstype#DEFAULT)**

Display like MS Excel, depends on the next cell. If the next cell is null, the string will cross or it will be truncated.

*   **[TextCrossType.CROSS\_KEEP](https://apireference.aspose.com/java/cells/com.aspose.cells/textcrosstype#CROSS_KEEP)**

Display the string like MS Excel exporting PDF/Image

*   **[TextCrossType.CROSS\_OVERRIDE](https://apireference.aspose.com/java/cells/com.aspose.cells/textcrosstype#CROSS_OVERRIDE)**

Display all the text by crossing other cells and override text of crossed cells

*   **[TextCrossType.STRICT\_IN\_CELL](https://apireference.aspose.com/java/cells/com.aspose.cells/textcrosstype#STRICT_IN_CELL)**

Only displaying the string within the width of cell.

## Specify how to cross string in output PDF/Image using TextCrossType

The following sample code loads the sample Excel file and saves it to PDF/Image format by specifying different [TextCrossType](https://apireference.aspose.com/java/cells/com.aspose.cells/TextCrossType). The sample Excel file and output files can be downloaded from the following links:

[sampleCrossType.xlsx](https://docs.aspose.com/download/attachments/81690955/sampleCrossType.xlsx?version=1&modificationDate=1549116106058&api=v2)

[outputCrossType.pdf](https://docs.aspose.com/download/attachments/81690955/outputCrossType.pdf?version=1&modificationDate=1549116106051&api=v2)

[outputCrossType.png](https://docs.aspose.com/download/attachments/81690955/outputCrossType.png?version=1&modificationDate=1549116106054&api=v2)

## Sample Code

