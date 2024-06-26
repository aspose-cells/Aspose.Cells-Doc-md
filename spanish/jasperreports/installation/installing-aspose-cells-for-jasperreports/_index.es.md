---
title: Instalación de Aspose.Cells for JasperReports
type: docs
weight: 20
url: /es/jasperreports/installing-aspose-cells-for-jasperreports/
---

Para usar **Aspose.Cells for JasperReports** desde su aplicación, copie **aspose.cells.jasperreports.jar** de la carpeta \lib de Aspose.Cells.JasperReports.zip al directorio JasperReports\lib o a una carpeta de biblioteca de su aplicación. Después de eso, podrá acceder a los exportadores programáticamente.

El siguiente ejemplo muestra el código típico necesario para exportar un informe a un archivo XLS utilizando Aspose.Cells for JasperReports. Se pueden encontrar más ejemplos en los informes de demostración incluidos en el archivo del producto.

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
