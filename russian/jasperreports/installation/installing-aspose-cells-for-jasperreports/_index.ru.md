---
title: Установка Aspose.Cells for JasperReports
type: docs
weight: 20
url: /ru/jasperreports/installing-aspose-cells-for-jasperreports/
---
 Использовать**Aspose.Cells for JasperReports** из вашего приложения скопируйте**aspose.cells.jasperreports.jar** из папки \lib файла Aspose.Cells.JasperReports.zip в каталог JasperReports\lib или в папку библиотеки вашего приложения. После этого вы можете получить доступ к экспортерам программно.

В следующем примере показан стандартный код, необходимый для экспорта отчета в файл XLS с использованием Aspose.Cells for JasperReports. Дополнительные примеры можно найти в демонстрационных отчетах, включенных в архив продукта.

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
