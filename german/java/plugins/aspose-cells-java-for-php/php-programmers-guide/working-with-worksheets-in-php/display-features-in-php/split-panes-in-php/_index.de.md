---
title: Panes in Php splitten
type: docs
weight: 70
url: /de/java/split-panes-in-php/
---

## **Aspose.Cells - Panes aufteilen**
Um Panes mit **Aspose.Cells Java for PHP** zu splitten, rufe einfach das Modul **SplitPanes** auf.

**PHP-Code**

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
## **Laufenden Code herunterladen**
Downloaden **Panes splitten (Aspose.Cells)** von einer der unten genannten sozialen Coding-Seiten:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/SplitPanes.php)
