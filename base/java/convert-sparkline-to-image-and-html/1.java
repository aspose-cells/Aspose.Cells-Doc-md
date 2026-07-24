import com.aspose.cells.*;

Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);