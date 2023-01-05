---
title: Installieren von Aspose.Cells for JasperReports
type: docs
weight: 20
url: /de/jasperreports/installing-aspose-cells-for-jasperreports/
---
 Benutzen**Aspose.Cells for JasperReports** aus Ihrer Bewerbung kopieren**aspose.cells.jasperreports.jar** aus dem Ordner \lib von Aspose.Cells.JasperReports.zip in das Verzeichnis JasperReports\lib oder in einen Bibliotheksordner Ihrer Anwendung. Danach können Sie programmgesteuert auf die Exporter zugreifen.

Das folgende Beispiel zeigt den typischen Code, der zum Exportieren eines Berichts in eine XLS-Datei mit Aspose.Cells for JasperReports erforderlich ist. Weitere Beispiele finden Sie in den Demoberichten im Produktarchiv.

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
