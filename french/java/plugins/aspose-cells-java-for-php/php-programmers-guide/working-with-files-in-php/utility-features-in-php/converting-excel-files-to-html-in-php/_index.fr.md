---
title: Conversion de fichiers Excel en HTML en PHP
type: docs
weight: 20
url: /fr/java/converting-excel-files-to-html-in-php/
---
## **Aspose.Cells - Conversion de fichiers Excel en HTML**
Pour convertir Excel en HTML en utilisant Aspose.Cells for Java en PHP, appelez simplement la feuille de calcul_à_méthode html() du module Convertisseur.

**Code PHP**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

//Save the document in PDF format

$workbook->save($dataDir . "OutBook1.html", $saveFormat->HTML);

{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Conversion de fichiers Excel en HTML (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingExcelFilesToHtml.php)
