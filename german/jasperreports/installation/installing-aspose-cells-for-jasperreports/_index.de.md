---
title: Aspose.Cells for JasperReports installieren
type: docs
weight: 20
url: /de/jasperreports/installing-aspose-cells-for-jasperreports/
---

Um **Aspose.Cells for JasperReports** aus Ihrer Anwendung zu verwenden, kopieren Sie **aspose.cells.jasperreports.jar** aus dem \lib-Ordner von Aspose.Cells.JasperReports.zip in das JasperReports\lib-Verzeichnis oder in einen Bibliotheksordner Ihrer Anwendung. Danach können Sie auf die Exporter programmgesteuert zugreifen.

Das folgende Beispiel zeigt den typischen Code, um einen Bericht mithilfe von Aspose.Cells for JasperReports in eine XLS-Datei zu exportieren. Weitere Beispiele finden Sie in den mit dem Produktarchiv gelieferten Demoberichten.

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
