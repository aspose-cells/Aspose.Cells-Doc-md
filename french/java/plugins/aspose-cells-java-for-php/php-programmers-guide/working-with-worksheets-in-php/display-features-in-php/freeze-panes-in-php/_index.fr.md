---
title: Figer les volets en PHP
type: docs
weight: 40
url: /fr/java/freeze-panes-in-php/
---
## **Aspose.Cells - Figer les volets**
 Pour figer des volets dans le document de feuille de calcul à l'aide de**Aspose.Cells Java pour PHP** , invoquez simplement**FreezePanes** module.

**Code PHP**

{{< highlight "php" >}}

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
## **Télécharger le code d'exécution**
Télécharger**Figer les volets (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/FreezePanes.php)
