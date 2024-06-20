---
title: .jrprintファイルをXLS形式にエクスポートする
type: docs
weight: 20
url: /ja/jasperreports/exporting-jrprint-files-to-xls-formats/
---

{{% alert color="primary" %}} 

Aspose.Cells for JasperReports は、.jrprint ファイルまたは JasperPrint オブジェクトを入力として受け取り、それを XLS ファイルにエクスポートするための ACXlsExporter というクラスを提供します。 

{{% /alert %}} 

次のコードスニペットは、例えばdestFileにJasperPrintオブジェクトをエクスポートする方法を示しています。

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
