---
title: Blocca i riquadri in Php
type: docs
weight: 40
url: /it/java/freeze-panes-in-php/
---
## **Aspose.Cells - Congelamento Riquadri**
 Per bloccare i riquadri nel documento del foglio di calcolo utilizzando**Aspose.Cells Java per PHP** , semplicemente invocare**FreezePanes** modulo.

**Codice PHP**

{{< highlight "php" >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Applying freeze panes settings

$worksheet->freezePanes(3,2,3,2);

//Saving the modified Excel file in default format

$workbook->save($dataDir . "book.out.xls");

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica**Blocca riquadri (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/FreezePanes.php)
