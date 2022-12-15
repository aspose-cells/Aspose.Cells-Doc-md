---
title: Volets divisés en PHP
type: docs
weight: 70
url: /fr/java/split-panes-in-php/
---
## **Aspose.Cells - Vitres fractionnées**
 Pour diviser les volets à l'aide de**Aspose.Cells Java for PHP** , invoquez simplement**SplitPanes** module.

**Code PHP**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

//Instantiate a new workbook

//Open a template file

$book = new Workbook($dataDir . "book.xls");

//Set the active cell

$book->getWorksheets()->get(0)->setActiveCell("A20");

//Split the worksheet window

$book->getWorksheets()->get(0)->split();

//Save the excel file

$book->save($dataDir . "book.out.xls", $saveFormat->EXCEL_97_TO_2003);

{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Vitres divisées (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/SplitPanes.php)
