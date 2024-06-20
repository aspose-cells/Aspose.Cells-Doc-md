---
title: Aspose.Cells for JasperReportsのインストール
type: docs
weight: 20
url: /ja/jasperreports/installing-aspose-cells-for-jasperreports/
---

アプリケーションから**Aspose.Cells for JasperReports**を使用するには、Aspose.Cells.JasperReports.zipの\libフォルダから**aspose.cells.jasperreports.jar**をJasperReports\libディレクトリまたはアプリケーションのライブラリフォルダにコピーします。その後、プログラムからエクスポータにアクセスできます。

以下の例は、Aspose.Cells for JasperReportsを使用してレポートをXLSファイルにエクスポートするために必要な典型的なコードを示しています。製品アーカイブに含まれるデモレポートには、他の例があります。

**Java**

{{< highlight csharp >}}

    import com.aspose.cells.jasperreports.*;


   ACXlsExporter exporter = new ACXlsExporter ();

   ACXlsReportConfiguration conf = new ACXlsReportConfiguration ();

   File sourceFile = new File(fileName);

   JasperPrint jasperPrint = (JasperPrint)JRLoader.loadObject(sourceFile);

   exporter.setConfiguration(conf);

   exporter.setExporterInput(new SimpleExporterInput(jasperPrint));


   File destFile = new File(sourceFile.getParent(), jasperPrint.getName() + ".xls");

   exporter.setExporterOutput(new SimpleOutputStreamExporterOutput(destFile.toString());

   exporter.exportReport();



{{< /highlight >}}
