---
title: Conversion de fichiers Excel en PDF en PHP
type: docs
weight: 30
url: /fr/java/converting-excel-to-pdf-files-in-php/
---

## **Aspose.Cells - Conversion de fichiers Excel en PDF**
Pour convertir un fichier Excel en PDF à l'aide du Aspose.Cells for Java en PHP, il suffit d'appeler la méthode excel_to_pdf() du module Converter.

**Code PHP**

{{< highlight php >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

        //Save the document in PDF format

$workbook->save($dataDir . "OutBook1.pdf", $saveFormat->PDF);

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Converting Excel to PDF Files (Aspose.Cells)** depuis l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PdfConversion.php)
