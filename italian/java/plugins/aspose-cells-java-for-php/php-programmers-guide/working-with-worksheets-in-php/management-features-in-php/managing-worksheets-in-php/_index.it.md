---
title: Gestione dei fogli di lavoro in Php
type: docs
weight: 10
url: /it/java/managing-worksheets-in-php/
---

## **Aspose.Cells - Gestione dei fogli di lavoro**
### **Aggiungere fogli di lavoro a un nuovo file Excel**
Per aggiungere un foglio di lavoro a un nuovo file Excel utilizzando **Aspose.Cells Java per PHP**, chiama semplicemente il metodo **add_worksheet** del modulo **MangingWorksheets**.

**Codice PHP**

{{< highlight php >}}

 //Instantiating a Workbook object

$workbook = new Workbook();

//Adding a new worksheet to the Workbook object

$worksheets = $workbook->getWorksheets();

$sheetIndex = $worksheets->add();

$worksheet = $worksheets->get($sheetIndex);

//Setting the name of the newly added worksheet

$worksheet->setName("My Worksheet");

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

{{< /highlight >}}
### **Rimozione dei fogli di lavoro utilizzando il nome del foglio**
Per rimuovere il foglio di lavoro per nome utilizzando **Aspose.Cells Java per PHP**, chiama semplicemente il metodo **remove_worksheet_by_name** del modulo **MangingWorksheets**.

**Codice PHP**

{{< highlight php >}}

 //Creating a file stream containing the Excel file to be opened

$fstream = new FileInputStream($dataDir . "book.xls");

//Instantiating a Workbook object with the stream

$workbook = new Workbook($fstream);

//Removing a worksheet using its sheet name

$workbook->getWorksheets()->removeAt("Sheet1");

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

//Closing the file stream to free all resources

$fstream->close();

{{< /highlight >}}
### **Rimozione dei fogli di lavoro utilizzando l'indice del foglio**
Per rimuovere il foglio di lavoro per indice utilizzando **Aspose.Cells Java per PHP**, chiama semplicemente il metodo **remove_worksheet_by_index** del modulo **MangingWorksheets**.

**Codice PHP**

{{< highlight php >}}

 //Creating a file stream containing the Excel file to be opened

$fstream=new FileInputStream($dataDir . "book.xls");

//Instantiating a Workbook object with the stream

$workbook = new Workbook($fstream);

//Removing a worksheet using its sheet index

$workbook->getWorksheets()->removeAt(0);

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

//Closing the file stream to free all resources

$fstream->close();

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Gestione dei fogli di lavoro (Aspose.Cells)** da uno qualsiasi dei siti di codici sociali menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
