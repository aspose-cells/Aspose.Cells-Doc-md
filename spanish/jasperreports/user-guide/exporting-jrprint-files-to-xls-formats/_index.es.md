---
title: Exportar archivos .jrprint a formatos XLS
type: docs
weight: 20
url: /es/jasperreports/exporting-jrprint-files-to-xls-formats/
---

{{% alert color="primary" %}} 

Aspose.Cells for JasperReports proporciona una clase llamada ACXlsExporter para exportar informes a archivos XLS. Recibe como entrada un archivo .jrprint o un objeto JasperPrint y lo exporta a un archivo XLS. 

{{% /alert %}} 

El siguiente fragmento de código demuestra cómo exportar el objeto jasperPrint a una ruta de archivo, por ejemplo, destFile.

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
