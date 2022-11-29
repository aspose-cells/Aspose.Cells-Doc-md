---
title: Set Print Titles in xlsx4j
type: docs
weight: 40
url: /java/set-print-titles-in-xlsx4j/
---

## **Aspose.Cells - Set Print Titles**
Aspose.Cells allows you to designate row and column headers to repeat on all pages of a printed worksheet. To do so, use the [PageSetup](/java/PageSetup) class'setPrintTitleColumns and setPrintTitleRows properties.

The rows or columns that will be repeated are defined by passing their row or column numbers. For example, rows are defined as $1:$2 and columns are defined as $A:$B.

**Java**

{{< highlight java >}}

 //Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

//Defining column numbers A & B as title columns

pageSetup.setPrintTitleColumns("$A:$B");

//Defining row numbers 1 & 2 as title rows

pageSetup.setPrintTitleRows("$1:$2");

{{< /highlight >}}
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/setprinttitles/AsposeSetPrintTitles.java)

{{% alert color="primary" %}} 

For more details, visit [Setting Print Options](/cells/java/page-setup-features/#setting-print-options).

{{% /alert %}}
