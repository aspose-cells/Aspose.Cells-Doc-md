---
title: JasperReports için Aspose.Cells'i yükleme
type: docs
weight: 20
url: /tr/jasperreports/installing-aspose-cells-for-jasperreports/
---
 Kullanmak**Jasper Raporları için Aspose.Cells** uygulamanızdan kopyalayın**aspose.cells.jasperreports.jar** Aspose.Cells.JasperReports.zip dosyasının \lib klasöründen JasperReports\lib dizinine veya uygulamanızın bir kitaplık klasörüne. Bundan sonra, ihracatçılara programlı olarak erişebilirsiniz.

Aşağıdaki örnek, JasperReports için Aspose.Cells kullanarak bir raporu bir XLS dosyasına dışa aktarmak için gereken tipik kodu gösterir. Ürün arşivinde yer alan demo raporlarında daha fazla örnek bulunabilir.

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
