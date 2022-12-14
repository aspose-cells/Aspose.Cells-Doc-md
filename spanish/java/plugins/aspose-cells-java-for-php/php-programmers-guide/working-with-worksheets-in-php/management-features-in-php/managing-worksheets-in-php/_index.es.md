---
title: Manejo de hojas de trabajo en Php
type: docs
weight: 10
url: /es/java/managing-worksheets-in-php/
---
## **Aspose.Cells - Gestión de hojas de trabajo**
### **Agregar hojas de trabajo a un nuevo archivo de Excel**
Para agregar una hoja de trabajo a un nuevo archivo de Excel usando**Aspose.Cells Java para PHP** , simplemente llama**añadir_hoja de trabajo** método de**Gestión de hojas de trabajo** módulo.

**Código PHP**

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
### **Eliminación de hojas de trabajo usando el nombre de la hoja**
 Para eliminar la hoja de trabajo por nombre de hoja usando**Aspose.Cells Java para PHP** , simplemente llama**remove_worksheet_by_name** método de**Gestión de hojas de trabajo** módulo.

**Código PHP**

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
### **Eliminación de hojas de cálculo mediante el índice de hojas**
 Para eliminar hoja de trabajo por índice de hoja usando**Aspose.Cells Java para PHP** , simplemente llama**remove_worksheet_by_index** método de**Gestión de hojas de trabajo** módulo.

**Código PHP**

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
## **Descargar código de ejecución**
Descargar**Gestión de hojas de trabajo (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
