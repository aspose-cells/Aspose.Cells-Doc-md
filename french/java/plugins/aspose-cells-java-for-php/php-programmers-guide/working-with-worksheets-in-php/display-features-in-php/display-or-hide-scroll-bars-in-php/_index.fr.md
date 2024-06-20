---
title: Afficher ou masquer les barres de défilement en Php
type: docs
weight: 20
url: /fr/java/display-or-hide-scroll-bars-in-php/
---

## **Aspose.Cells - Afficher ou Masquer les barres de défilement**
### **Masquer les barres de défilement**
Pour masquer les barres de défilement en utilisant **Aspose.Cells Java pour PHP**, appelez le module **displayhidescrollbars**.

**Code PHP**

{{< highlight php >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the vertical scroll bar of the Excel file

$workbook->getSettings()->setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

$workbook->getSettings()->setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Afficher ou Masquer les barres de défilement (Aspose.Cells)** sur l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideScrollBars.php)
