---
title: Installerar Aspose.Cells for JasperReports
type: docs
weight: 20
url: /sv/jasperreports/installing-aspose-cells-for-jasperreports/
---
 Att använda**Aspose.Cells for JasperReports** från din ansökan, kopiera**aspose.cells.jasperreports.jar** från mappen \lib i Aspose.Cells.JasperReports.zip till katalogen JasperReports\lib eller till en biblioteksmapp i ditt program. Efter det kan du komma åt exportörerna programmatiskt.

Följande exempel visar den typiska koden som behövs för att exportera en rapport till en XLS-fil med Aspose.Cells for JasperReports. Fler exempel finns i demorapporterna som ingår i produktarkivet.

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
