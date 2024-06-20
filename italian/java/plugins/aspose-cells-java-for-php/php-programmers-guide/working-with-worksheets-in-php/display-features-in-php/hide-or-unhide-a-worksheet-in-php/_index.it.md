---
title: Nascondi o mostra un foglio di lavoro in Php
type: docs
weight: 50
url: /it/java/hide-or-unhide-a-worksheet-in-php/
---

## **Aspose.Cells - Nascondi o Mostra un Foglio**
### **Nascondere un foglio di lavoro**
Per nascondere il foglio di lavoro utilizzando Aspose.Cells Java per PHP, chiama il modulo **hideunhideworksheet**.

**Codice PHP**

{{< highlight php >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Hiding the first worksheet of the Excel file

$worksheet->setVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");


{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Nascondi o Mostra un Foglio (Aspose.Cells)** da uno dei siti di codice sociale sotto indicati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/HideUnhideWorksheet.php)
