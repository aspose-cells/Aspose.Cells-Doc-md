---
title: 将 .jrprint 文件导出为 XLS 格式
type: docs
weight: 20
url: /zh/jasperreports/exporting-jrprint-files-to-xls-formats/
---
{{% alert color="primary" %}} 

Aspose.Cells for JasperReports 提供了一个名为 ACXlsExporter 的类，用于将报告导出到 XLS 文件。它采用 .jrprint 文件或 JasperPrint 对象作为输入，并将其导出到 XLS 文件。

{{% /alert %}} 

以下代码片段演示了如何将 jasperPrint 对象导出到某个文件路径，例如 destFile。

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
