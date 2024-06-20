---
title: Geler les volets en Php
type: docs
weight: 40
url: /fr/java/freeze-panes-in-php/
---

## **Aspose.Cells - Figer les volets**
Pour geler les volets dans le document de feuille de calcul en utilisant **Aspose.Cells Java pour PHP**, il suffit d'invoquer le module **FreezePanes**.

**Code PHP**

{{< highlight php >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Applying freeze panes settings

$worksheet->freezePanes(3,2,3,2);

//Saving the modified Excel file in default format

$workbook->save($dataDir . "book.out.xls");

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Figer les volets (Aspose.Cells)** sur l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/FreezePanes.php)
