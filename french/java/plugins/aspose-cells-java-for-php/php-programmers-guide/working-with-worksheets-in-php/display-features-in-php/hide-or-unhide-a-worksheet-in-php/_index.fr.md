---
title: Masquer ou afficher une feuille de calcul en PHP
type: docs
weight: 50
url: /fr/java/hide-or-unhide-a-worksheet-in-php/
---
## **Aspose.Cells - Masquer ou afficher une feuille de calcul**
### **Masquer une feuille de calcul**
 Pour masquer la feuille de calcul à l'aide de Aspose.Cells Java pour PHP, appelez**masquerafficher la feuille de travail** module.

**Code PHP**

{{< highlight "php" >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Hiding the first worksheet of the Excel file

$worksheet->setVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");


{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Masquer ou afficher une feuille de calcul (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/HideUnhideWorksheet.php)
