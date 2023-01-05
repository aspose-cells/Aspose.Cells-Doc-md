---
title: Exportera .jrprint-filer till XLS-format
type: docs
weight: 20
url: /sv/jasperreports/exporting-jrprint-files-to-xls-formats/
---
{{% alert color="primary" %}} 

 Aspose.Cells for JasperReports tillhandahåller en klass som heter ACXlsExporter för export av rapporter till XLS-filer. Den tar en .jrprint-fil eller ett JasperPrint-objekt som indata och exporterar den till en XLS-fil.

{{% /alert %}} 

Följande kodsnutt visar hur man exporterar jasperPrint-objektet till någon filsökväg, till exempel destFile.

**Java**

{{< highlight "csharp" >}}

 import com.aspose.cells.jasperreports. ACXlsExporter;

.................

ACXlsExporter exporter = new ACXlsExporter ();

exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);

exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());

exporter.setParameter(JRXlsExporterParameter.IS_ONE_PAGE_PER_SHEET, Boolean.TRUE);

exporter.setParameter(ACXlsExporterParameter.IS_USE_EXCEL_CHART, Boolean.FALSE);

exporter.exportReport();



{{< /highlight >}}
