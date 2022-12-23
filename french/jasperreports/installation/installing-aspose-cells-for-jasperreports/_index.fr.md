---
title: Installation Aspose.Cells for JasperReports
type: docs
weight: 20
url: /fr/jasperreports/installing-aspose-cells-for-jasperreports/
---
 Utiliser**Aspose.Cells for JasperReports** depuis votre application, copiez**aspose.cells.jasperreports.jar** du dossier \lib de Aspose.Cells.JasperReports.zip vers le répertoire JasperReports\lib ou vers un dossier de bibliothèque de votre application. Après cela, vous pouvez accéder aux exportateurs par programmation.

L'exemple suivant montre le code typique nécessaire pour exporter un rapport vers un fichier XLS en utilisant Aspose.Cells for JasperReports. D'autres exemples peuvent être trouvés dans les rapports de démonstration inclus dans l'archive du produit.

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
