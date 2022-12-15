---
title: Esportazione di file .jrprint in formati XLS
type: docs
weight: 20
url: /it/jasperreports/exporting-jrprint-files-to-xls-formats/
---
{{% alert color="primary" %}} 

 Aspose.Cells for JasperReports fornisce una classe denominata ACXlsExporter per l'esportazione di report in file XLS. Prende un file .jrprint o un oggetto JasperPrint come input e lo esporta in un file XLS.

{{% /alert %}} 

Il seguente frammento di codice mostra come esportare l'oggetto jasperPrint in un percorso file, ad esempio destFile.

**Giava**

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
