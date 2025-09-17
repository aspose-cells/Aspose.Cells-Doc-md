##Convert XLS with Images and Charts to PDF
The Java code to convert Excel files with images and charts to PDF format by using the Aspose.Cells for Java API.
Aspose.Cells supports converting XLS files that contain images and charts to PDF documents. Aspose.Cells for Java can work independently to convert a spreadsheet to PDF: Aspose.PDF APIs are not required for the conversion.
The process can be done in memory as the process does not depend on temporary or intermediary XML files. This means that large Excel files, for example, ones containing images, charts, and other drawing objects, can be converted quickly and efficiently.
If the spreadsheet contains formulas, it is best to call the [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) method just before rendering to PDF. Doing so ensures that formula dependent values are recalculated, and the correct values are rendered in the PDF.
## Related Articles
- [Convert Excel file to PDF format compatible with PDFA-1a](https://docs.aspose.com/cells/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Chart Rendering](https://docs.aspose.com/cells/java/chart-rendering/)
