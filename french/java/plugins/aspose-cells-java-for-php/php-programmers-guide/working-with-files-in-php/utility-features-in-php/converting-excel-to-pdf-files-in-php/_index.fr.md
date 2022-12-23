---
title: Conversion d'Excel en fichiers PDF en PHP
type: docs
weight: 30
url: /fr/java/converting-excel-to-pdf-files-in-php/
---
## **Aspose.Cells - Conversion d'Excel en fichiers PDF**
Pour convertir Excel en fichier Pdf en utilisant Aspose.Cells for Java en PHP, appelez simplement Excel_à_méthode pdf() du module Converter.

**Code PHP**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

        //Save the document in PDF format

$workbook->save($dataDir . "OutBook1.pdf", $saveFormat->PDF);

{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Conversion d'Excel en fichiers PDF (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PdfConversion.php)
