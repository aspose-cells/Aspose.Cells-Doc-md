---
title: Nascondere o scoprire un foglio di lavoro in Php
type: docs
weight: 50
url: /it/java/hide-or-unhide-a-worksheet-in-php/
---
## **Aspose.Cells - Nascondi o mostra un foglio di lavoro**
### **Nascondere un foglio di lavoro**
 Per nascondere il foglio di lavoro utilizzando Aspose.Cells Java per PHP, chiama**hideunhideworksheet** modulo.

**Codice PHP**

{{< highlight "php" >}}

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
Scarica**Nascondere o scoprire un foglio di lavoro (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/HideUnhideWorksheet.php)
