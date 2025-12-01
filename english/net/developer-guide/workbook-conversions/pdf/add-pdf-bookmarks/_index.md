---
title: Add PDF Bookmarks
type: docs
weight: 10
url: /net/add-pdf-bookmarks/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

This article provides information on how to insert PDF bookmarks when converting a spreadsheet to PDF.

Aspose.Cells allows you to add bookmarks on the fly. PDF bookmarks can drastically improve the navigability of long documents. When adding bookmark links to PDF document, you can have precise control over the exact view you want, you're not limited to linking to a page. You can set up the precise view by positioning the target page, and then create the bookmark.

{{% /alert %}}

Please see the following sample code to find out how to add PDF bookmarks. The code generates a simple workbook, specifies PDF bookmarks with destination locations and generates the PDF file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddPDFBookmarks-1.cs" >}}

{{% alert color="primary" %}}

If your spreadsheet has formulas, it is best to call [**Workbook.CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are refreshed & rendered correctly in PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
