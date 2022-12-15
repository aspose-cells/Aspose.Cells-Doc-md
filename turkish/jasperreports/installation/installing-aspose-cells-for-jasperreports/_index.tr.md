---
title: Kurulum Aspose.Cells for JasperReports
type: docs
weight: 20
url: /tr/jasperreports/installing-aspose-cells-for-jasperreports/
---
 Kullanmak**Aspose.Cells for JasperReports** uygulamanızdan kopyalayın**aspose.cells.jasperreports.jar** Aspose.Cells.JasperReports.zip dosyasının \lib klasöründen JasperReports\lib dizinine veya uygulamanızın bir kitaplık klasörüne. Bundan sonra, ihracatçılara programlı olarak erişebilirsiniz.

Aşağıdaki örnek, bir raporu Aspose.Cells for JasperReports kullanarak bir XLS dosyasına dışa aktarmak için gereken tipik kodu göstermektedir. Ürün arşivinde bulunan demo raporlarında daha fazla örnek bulunabilir.

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
