---
title: Afficher ou masquer le quadrillage en php
type: docs
weight: 10
url: /fr/java/display-or-hide-gridlines-in-php/
---
## **Aspose.Cells - Afficher ou masquer le quadrillage**
### **Masquer le quadrillage**
 Pour masquer la feuille de calcul à l'aide de**Aspose.Cells Java for PHP** , téléphoner à**affichermasquerleslignesdegrille** module.

**Code PHP**

{{< highlight "php" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

//Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Hiding the grid lines of the first worksheet of the Excel file

$worksheet->setGridlinesVisible(false);

//Saving the modified Excel file in default (that is Excel 2000) format

$workbook->save($dataDir . "output.xls");


{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Afficher ou masquer le quadrillage (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideGridlines.php)
