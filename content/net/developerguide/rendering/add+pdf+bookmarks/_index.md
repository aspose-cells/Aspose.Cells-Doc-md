---
title : "Add PDF Bookmarks" 
description : "" 
weight : 12088 
toc : false
type: docs
url: /net/developerguide/rendering/add+pdf+bookmarks/
---

# Aspose.Cells for .NET : Add PDF Bookmarks


This article provides information on how to insert PDF bookmarks when converting a spreadsheet to PDF.

Aspose.Cells allows you to add bookmarks on the fly. PDF bookmarks can drastically improve the navigability of long documents. When adding bookmark links to PDF document, you can have precise control over the exact view you want, you're not limited to linking to a page. You can set up the precise view by positioning the target page, and then create the bookmark.

Please see the following sample code to find out how to add PDF bookmarks. The code generates a simple workbook, specifies PDF bookmarks with destination locations and generates the PDF file.

If your spreadsheet has formulas, it is best to call [Workbook.CalculateFormula](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/calculateformula/index) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are refreshed & rendered correctly in PDF.

