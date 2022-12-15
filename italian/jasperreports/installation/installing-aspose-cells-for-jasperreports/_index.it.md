---
title: Installazione Aspose.Cells for JasperReports
type: docs
weight: 20
url: /it/jasperreports/installing-aspose-cells-for-jasperreports/
---
 Usare**Aspose.Cells for JasperReports** dalla tua applicazione, copia**aspose.cells.jasperreports.jar** dalla cartella \lib di Aspose.Cells.JasperReports.zip alla directory JasperReports\lib o a una cartella della libreria dell'applicazione. Successivamente, puoi accedere agli esportatori in modo programmatico.

L'esempio seguente mostra il codice tipico necessario per esportare un report in un file XLS utilizzando Aspose.Cells for JasperReports. Altri esempi possono essere trovati nei report demo inclusi nell'archivio del prodotto.

**Giava**

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
