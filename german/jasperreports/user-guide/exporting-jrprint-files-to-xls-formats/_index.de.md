---
title: Exportieren von .jrprint Dateien im XLS Format
type: docs
weight: 20
url: /de/jasperreports/exporting-jrprint-files-to-xls-formats/
---

{{% alert color="primary" %}} 

Aspose.Cells for JasperReports bietet eine Klasse namens ACXlsExporter zum Exportieren von Berichten in XLS-Dateien. Es nimmt eine .jrprint-Datei oder ein JasperPrint-Objekt als Eingabe und exportiert sie in eine XLS-Datei. 

{{% /alert %}} 

Der folgende Codeausschnitt zeigt, wie das jasperPrint-Objekt beispielsweise in destFile exportiert wird.

**Java**

{{< highlight csharp >}}

 import com.aspose.cells.jasperreports. ACXlsExporter;

.................

ACXlsExporter exporter = new ACXlsExporter ();

exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);

exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());

exporter.setParameter(JRXlsExporterParameter.IS_ONE_PAGE_PER_SHEET, Boolean.TRUE);

exporter.setParameter(ACXlsExporterParameter.IS_USE_EXCEL_CHART, Boolean.FALSE);

exporter.exportReport();



{{< /highlight >}}
