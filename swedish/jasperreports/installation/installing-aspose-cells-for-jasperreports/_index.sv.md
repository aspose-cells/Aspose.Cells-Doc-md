---
title: Installation av Aspose.Cells for JasperReports
type: docs
weight: 20
url: /sv/jasperreports/installing-aspose-cells-for-jasperreports/
---

För att använda Aspose.Cells for JasperReports från din applikation, kopiera **aspose.cells.jasperreports.jar** från mappen \lib i Aspose.Cells.JasperReports.zip till JasperReports\lib-mappen eller till en biblioteksmapp i din applikation. Därefter kan du få åtkomst till exportörerna programmatiskt.

Följande exempel visar den typiska kod som behövs för att exportera en rapport till en XLS-fil med hjälp av Aspose.Cells for JasperReports. Fler exempel finns i de demorapporter som ingår i produktarkivet.

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
