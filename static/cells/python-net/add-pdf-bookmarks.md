##Add PDF Bookmarks
Learn how to add pdf book marks with Aspose.Cells for Python via .NET API.
This article provides information on how to insert PDF bookmarks when converting a spreadsheet to PDF.
Aspose.Cells for Python via .NET allows you to add bookmarks on the fly. PDF bookmarks can drastically improve the navigability of long documents. When adding bookmark links to PDF document, you can have precise control over the exact view you want, you're not limited to linking to a page. You can set up the precise view by positioning the target page, and then create the bookmark.
Please see the following sample code to find out how to add PDF bookmarks. The code generates a simple workbook, specifies PDF bookmarks with destination locations and generates the PDF file.
If your spreadsheet has formulas, it is best to call [**Workbook.calculate_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are refreshed & rendered correctly in PDF.
