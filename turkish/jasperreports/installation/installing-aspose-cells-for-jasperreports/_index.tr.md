---
title: Aspose.Cells for JasperReports ü Yükleme
type: docs
weight: 20
url: /tr/jasperreports/installing-aspose-cells-for-jasperreports/
---

Uygulamanızdan **Aspose.Cells for JasperReports**'ü kullanmak için, Aspose.Cells.JasperReports.zip dosyasının \lib klasöründen **aspose.cells.jasperreports.jar** dosyasını JasperReports\lib dizinine veya uygulamanızın kütüphane klasörüne kopyalayın. Bundan sonra dışa aktarıcları programlı şekilde kullanabilirsiniz.

Aşağıdaki örnek, Aspose.Cells for JasperReports'ü kullanarak bir raporu XLS dosyasına dışa aktarmak için gerekli tipik kodu göstermektedir. Daha fazla örnek ürün arşivinde bulunan demo raporlarda bulunabilir.

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
