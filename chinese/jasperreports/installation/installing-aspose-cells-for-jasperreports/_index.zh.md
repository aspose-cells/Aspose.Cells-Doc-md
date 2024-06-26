---
title: 安装 Aspose.Cells for JasperReports
type: docs
weight: 20
url: /zh/jasperreports/installing-aspose-cells-for-jasperreports/
---

要在应用程序中使用 **Aspose.Cells for JasperReports**，请从 Aspose.Cells.JasperReports.zip 的 \lib 文件夹中复制 **aspose.cells.jasperreports.jar** 到 JasperReports\lib 目录或应用程序的库文件夹。之后，您可以通过编程方式访问导出器。

以下示例显示了使用 Aspose.Cells for JasperReports 导出报告到 XLS 文件所需的典型代码。更多示例可以在产品存档中包含的演示报告中找到。

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
