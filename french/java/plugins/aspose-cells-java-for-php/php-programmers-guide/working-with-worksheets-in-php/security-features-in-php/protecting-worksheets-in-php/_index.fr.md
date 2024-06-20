---
title: Protection des feuilles de calcul en Php
type: docs
weight: 10
url: /fr/java/protecting-worksheets-in-php/
---

## **Aspose.Cells - Protection des feuilles de calcul**
Pour protéger une feuille de calcul en utilisant **Aspose.Cells Java for PHP**, appelez la méthode **protect_worksheet** du module **protection**.

**Code PHP**

{{< highlight php >}}

 //Instantiating a Excel object by excel file path

$excel = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $excel->getWorksheets();

$worksheet = $worksheets->get(0);

$protection = $worksheet->getProtection();

//The following 3 methods are only for Excel 2000 and earlier formats

$protection->setAllowEditingContent(false);

$protection->setAllowEditingObject(false);

$protection->setAllowEditingScenario(false);

//Protects the first worksheet with a password "1234"

$protection->setPassword("1234");

//Saving the modified Excel file in default format

$excel->save($dataDir . "output.xls");  

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Protecting Worksheets (Aspose.Cells)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/ProtectingWorksheet.php)
