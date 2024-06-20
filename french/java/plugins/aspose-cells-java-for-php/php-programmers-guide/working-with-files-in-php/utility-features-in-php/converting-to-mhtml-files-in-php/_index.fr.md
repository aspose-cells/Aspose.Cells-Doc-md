---
title: Conversion en fichiers MHTML en PHP
type: docs
weight: 40
url: /fr/java/converting-to-mhtml-files-in-php/
---

## **Aspose.Cells - Conversion en fichiers MHTML**
Pour convertir une feuille de calcul en fichier MHTML à l'aide du Aspose.Cells for Java en PHP, il suffit d'appeler la méthode worksheet_to_mhtml() du module Converter.

**Code PHP**

{{< highlight php >}}

 $sveFormat = new SaveFormat();

//Specify the file path

$filePath = $dataDir . "Book1.xlsx";

//Specify the HTML saving options

$sv = new HtmlSaveOptions($sveFormat->M_HTML);

//Instantiate a workbook and open the template XLSX file

$wb = new Workbook($filePath);

//Save the MHT file

$wb->save($filePath . ".out.mht", $sv);

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Converting to MHTML Files (Aspose.Cells)** depuis l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingToMhtmlFiles.php)
