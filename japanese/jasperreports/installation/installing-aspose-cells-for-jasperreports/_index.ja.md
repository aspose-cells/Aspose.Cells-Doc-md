---
title: インストール Aspose.Cells for JasperReports
type: docs
weight: 20
url: /ja/jasperreports/installing-aspose-cells-for-jasperreports/
---
使用するには**Aspose.Cells for JasperReports**アプリケーションから、コピー**aspose.cells.jasperreports.jar**Aspose.Cells.JasperReports.zip の \lib フォルダから JasperReports\lib ディレクトリまたはアプリケーションのライブラリ フォルダにコピーします。その後、プログラムでエクスポーターにアクセスできます。

次の例は、Aspose.Cells for JasperReports を使用してレポートを XLS ファイルにエクスポートするために必要な一般的なコードを示しています。製品アーカイブに含まれるデモ レポートには、さらに多くの例があります。

**Java**

{{< highlight "csharp" >}}

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
