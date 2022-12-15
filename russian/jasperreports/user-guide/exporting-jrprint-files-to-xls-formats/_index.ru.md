---
title: Экспорт файлов .jrprint в форматы XLS
type: docs
weight: 20
url: /ru/jasperreports/exporting-jrprint-files-to-xls-formats/
---
{{% alert color="primary" %}} 

 Aspose.Cells for JasperReports предоставляет класс ACXlsExporter для экспорта отчетов в файлы XLS. Он принимает файл .jrprint или объект JasperPrint в качестве входных данных и экспортирует его в файл XLS.

{{% /alert %}} 

Следующий фрагмент кода демонстрирует, как экспортировать объект jasperPrint по некоторому пути к файлу, например, destFile.

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
