---
title: Gestione dei fogli di lavoro in Php
type: docs
weight: 10
url: /it/java/managing-worksheets-in-php/
---
## **Aspose.Cells - Gestione fogli di lavoro**
### **Aggiunta di fogli di lavoro a un nuovo file Excel**
Per aggiungere un foglio di lavoro a un nuovo file Excel utilizzando**Aspose.Cells Giava for PHP** , chiama semplicemente**add_worksheet** metodo di**Gestione dei fogli di lavoro** modulo.

**Codice PHP**

{{< highlight "php" >}}

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
### **Rimozione di fogli di lavoro utilizzando il nome del foglio**
 Per rimuovere il foglio di lavoro per nome del foglio utilizzando**Aspose.Cells Giava for PHP** , chiama semplicemente**remove_worksheet_by_name** metodo di**Gestione dei fogli di lavoro** modulo.

**Codice PHP**

{{< highlight "php" >}}

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
### **Rimozione di fogli di lavoro utilizzando l'indice dei fogli**
 Per rimuovere il foglio di lavoro dall'indice del foglio utilizzando**Aspose.Cells Giava for PHP** , chiama semplicemente**remove_worksheet_by_index** metodo di**Gestione dei fogli di lavoro** modulo.

**Codice PHP**

{{< highlight "php" >}}

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
Scarica**Gestione fogli di lavoro (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
