---
title: Dividi riquadri in Php
type: docs
weight: 70
url: /it/java/split-panes-in-php/
---

## **Aspose.Cells - Dividi riquadri**
Per dividere i riquadri usando **Aspose.Cells Java per PHP**, invoca semplicemente il modulo **SplitPanes**.

**Codice PHP**

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
## **Scarica il codice in esecuzione**
Scarica **Dividere i riquadri (Aspose.Cells)** da uno qualsiasi dei siti di codici sociali menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/SplitPanes.php)
