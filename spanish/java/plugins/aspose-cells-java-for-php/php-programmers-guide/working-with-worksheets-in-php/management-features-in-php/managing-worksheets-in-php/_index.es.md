---
title: Gestión de hojas de cálculo en Php
type: docs
weight: 10
url: /es/java/managing-worksheets-in-php/
---

## **Aspose.Cells - Gestionar Hojas de Cálculo**
### **Añadir hojas de cálculo a un nuevo archivo de Excel**
Para agregar una hoja de cálculo a un nuevo archivo de Excel usando **Aspose.Cells Java para PHP**, simplemente llame al método **add_worksheet** del módulo **MangingWorksheets**.

**Código PHP**

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
### **Eliminar hojas de cálculo utilizando el nombre de la hoja**
Para eliminar una hoja de cálculo por nombre de hoja utilizando **Aspose.Cells Java para PHP**, simplemente llame al método **remove_worksheet_by_name** del módulo **MangingWorksheets**.

**Código PHP**

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
### **Eliminar hojas de cálculo utilizando el índice de la hoja**
Para eliminar una hoja de cálculo por índice de hoja utilizando **Aspose.Cells Java para PHP**, simplemente llame al método **remove_worksheet_by_index** del módulo **MangingWorksheets**.

**Código PHP**

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
## **Descargar Código en Ejecución**
Descargar **Gestión de Hojas de Cálculo (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
