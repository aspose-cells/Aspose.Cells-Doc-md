---
title: Esportazione dei file .jrprint nei formati XLS
type: docs
weight: 20
url: /it/jasperreports/exporting-jrprint-files-to-xls-formats/
---

{{% alert color="primary" %}} 

Aspose.Cells for JasperReports fornisce una classe chiamata ACXlsExporter per esportare i report in file XLS. Prende un file .jrprint o un oggetto JasperPrint come input e lo esporta in un file XLS. 

{{% /alert %}} 

Il seguente snippet di codice dimostra come esportare l'oggetto jasperPrint in un percorso file, ad esempio destFile.

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
