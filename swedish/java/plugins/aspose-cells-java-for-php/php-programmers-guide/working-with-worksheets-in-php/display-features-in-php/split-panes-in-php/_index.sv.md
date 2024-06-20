---
title: Dela rutor i Php
type: docs
weight: 70
url: /sv/java/split-panes-in-php/
---

## **Aspose.Cells - Dela fönster**
För att dela rutor med **Aspose.Cells Java for PHP**, helt enkelt anropa **SplitPanes**-modulen.

**PHP-kod**

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
## **Ladda ned körbar kod**
Ladda ner **Delade rutor (Aspose.Cells)** från någon av nedan nämnda sociala kodbaser:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/SplitPanes.php)
