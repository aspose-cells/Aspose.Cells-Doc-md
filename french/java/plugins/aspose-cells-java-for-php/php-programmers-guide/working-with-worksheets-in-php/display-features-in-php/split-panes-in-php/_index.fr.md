---
title: Fractionnement des volets en Php
type: docs
weight: 70
url: /fr/java/split-panes-in-php/
---

## **Aspose.Cells - Diviser les volets**
Pour fractionner des volets en utilisant **Aspose.Cells Java for PHP**, il suffit d'appeler le module **SplitPanes**.

**Code PHP**

{{< highlight php >}}

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
## **Télécharger le code en cours d'exécution**
Téléchargez **Split Panes (Aspose.Cells)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/SplitPanes.php)
