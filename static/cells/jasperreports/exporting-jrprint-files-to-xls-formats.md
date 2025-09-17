##Exporting .jrprint Files to XLS Formats
Aspose.Cells for JasperReports provides a class named ACXlsExporter for exporting reports to XLS files. It takes a .jrprint file or a JasperPrint object as its input, and exports it to an XLS file.
The following code snippet demonstrates how to export the jasperPrint object to some file path, for example, destFile.
**Java**
import com.aspose.cells.jasperreports. ACXlsExporter;
.................
ACXlsExporter exporter = new ACXlsExporter ();
exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);
exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());
exporter.setParameter(JRXlsExporterParameter.IS_ONE_PAGE_PER_SHEET, Boolean.TRUE);
exporter.setParameter(ACXlsExporterParameter.IS_USE_EXCEL_CHART, Boolean.FALSE);
exporter.exportReport();
