---
title : "Set Print Titles" 
description : "" 
weight : 20651 
toc : false
type: docs
url: /java/plugins/aph-hssf-xssf/featuresmissinginaph/miscellaneousexamples/set+print+titles/
---

# Aspose.Cells for Java : Set Print Titles


## Aspose.Cells - Set Print Titles

Aspose.Cells allows you to designate row and column headers to repeat on all pages of a printed worksheet. To do so, use the [PageSetup](http://docs.aspose.com:8082/docs/display/cellsjava/PageSetup) class'`setPrintTitleColumns` and `setPrintTitleRows` properties.

The rows or columns that will be repeated are defined by passing their row or column numbers. For example, rows are defined as $1:$2 and columns are defined as $A:$B.

**Java**

{{< code lang="java" >}}
//Obtaining the reference of the PageSetup of the worksheet
PageSetup pageSetup = sheet.getPageSetup();

//Defining column numbers A & B as title columns
pageSetup.setPrintTitleColumns("$A:$B");

//Defining row numbers 1 & 2 as title rows
pageSetup.setPrintTitleRows("$1:$2");
{{< /code >}}

## Download Running Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintTitles.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintTitles.java)

For more details, visit [Setting Print Options](http://docs.aspose.com:8082/docs/display/cellsjava/Setting+Print+Options).

