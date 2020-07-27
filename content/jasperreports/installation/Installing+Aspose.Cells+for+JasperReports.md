+++
title = "Installing Aspose.Cells for JasperReports" 
description = "" 
weight = 8019 
+++

Aspose.Cells for JasperReports : Installing Aspose.Cells for JasperReports  

# Aspose.Cells for JasperReports : Installing Aspose.Cells for JasperReports


To use **Aspose.Cells for JasperReports** from your application, copy **aspose.cells.jasperreports.jar** from the \\lib folder of Aspose.Cells.JasperReports.zip to the JasperReports\\lib directory or to a library folder of your application. After that, you can access the exporters programmatically.

The following example shows the typical code needed to export a report to an XLS file using Aspose.Cells for JasperReports. More examples can be found in the demo reports included in the product archive.

**Java**

{{< code lang="java" >}}
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
 
{{< /code >}}

