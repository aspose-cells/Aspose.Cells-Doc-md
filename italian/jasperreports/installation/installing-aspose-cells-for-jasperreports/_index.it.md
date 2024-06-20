---
title: Installazione di Aspose.Cells for JasperReports
type: docs
weight: 20
url: /it/jasperreports/installing-aspose-cells-for-jasperreports/
---

Per utilizzare **Aspose.Cells for JasperReports** dalla tua applicazione, copia **aspose.cells.jasperreports.jar** dalla cartella \lib di Aspose.Cells.JasperReports.zip nella directory JasperReports\lib o in una cartella delle librerie della tua applicazione. Dopodiché puoi accedere agli esportatori programmaticamente.

L'esempio seguente mostra il codice tipico necessario per esportare un report in un file XLS utilizzando Aspose.Cells for JasperReports. Altri esempi possono essere trovati nei report dimostrativi inclusi nell'archivio del prodotto.

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
