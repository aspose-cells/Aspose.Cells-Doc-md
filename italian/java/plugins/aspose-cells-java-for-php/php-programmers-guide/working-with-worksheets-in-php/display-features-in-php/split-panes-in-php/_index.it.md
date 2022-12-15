---
title: Dividi riquadri in Php
type: docs
weight: 70
url: /it/java/split-panes-in-php/
---
## **Aspose.Cells - Riquadri divisi**
 Per dividere i riquadri utilizzando**Aspose.Cells Giava for PHP** , semplicemente invocare**SplitPanes** modulo.

**Codice PHP**

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
## **Scarica il codice in esecuzione**
Scarica**Riquadri divisi (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/SplitPanes.php)
