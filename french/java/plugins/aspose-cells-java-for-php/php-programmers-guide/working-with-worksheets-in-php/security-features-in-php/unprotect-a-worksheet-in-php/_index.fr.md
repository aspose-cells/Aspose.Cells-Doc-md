---
title: Déverrouiller une feuille de calcul en Php
type: docs
weight: 20
url: /fr/java/unprotect-a-worksheet-in-php/
---

## **Aspose.Cells - Déverrouiller une feuille de calcul**
Pour protéger une feuille de calcul avec **Aspose.Cells Java pour PHP**, appelez la méthode **unprotect_worksheet** du module **protection**.

**Code PHP**

{{< highlight php >}}

 $filesFormatType = new FileFormatType();

//Instantiating a Workbook object

$workbook = new Workbook($dataDir . "book1.xls");

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$protection = $worksheet->getProtection();

//Unprotecting the worksheet with a password

$worksheet->unprotect("aspose");

// Save the excel file.

$workbook->save($dataDir . "output.xls", $filesFormatType->EXCEL_97_TO_2003); 

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Déverrouiller une feuille de calcul (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/UnprotectingPasswordProtectedWorksheet.php)
