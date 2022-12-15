---
title: Afficher ou masquer les onglets en PHP
type: docs
weight: 30
url: /fr/java/display-or-hide-tabs-in-php/
---
## **Aspose.Cells - Afficher ou masquer les onglets**
### **Masquer les onglets**
 Pour masquer les onglets à l'aide de**Aspose.Cells Java for PHP** , appel**afficher les onglets masqués** module.

**Code PHP**

{{< highlight "php" >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the tabs of the Excel file

$workbook->getSettings()->setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir + "output.xls");

{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Masquer ou afficher ou masquer les onglets (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideTabs.php)
