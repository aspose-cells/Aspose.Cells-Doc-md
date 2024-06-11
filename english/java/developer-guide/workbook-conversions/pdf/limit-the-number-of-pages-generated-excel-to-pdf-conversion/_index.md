---
title: Limit the Number of Pages Generated - Excel to PDF Conversion
type: docs
weight: 60
url: /java/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Sometimes, you want to print a range of pages to an output PDF file. Aspose.Cells has the ability to set a limit on how many pages are generated when converting an Excel spreadsheet to PDF.

{{% /alert %}}

## **Limiting the Number of Pages Generated**

The following example shows how to render a range of pages (3 and 4) in a Microsoft Excel file to PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LimitNumberofPagesGenerated-LimitNumberofPagesGenerated.java" >}}

{{% alert color="primary" %}}

If the spreadsheet contains formulas, it is best to call [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) just before rendering it to PDF format. Doing so ensures that formula dependent values are recalculated, and the correct values are rendered in the output file.

{{% /alert %}}
