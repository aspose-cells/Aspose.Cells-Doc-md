---
title: Copiare e spostare fogli di lavoro in Php
type: docs
weight: 10
url: /it/java/copying-and-moving-worksheets-in-php/
---
## **Aspose.Cells - Copia e spostamento fogli di lavoro**
### **Copia i fogli di lavoro all'interno di una cartella di lavoro**
 Per copiare il foglio di lavoro utilizzando**Aspose.Cells for Java in PHP** , chiamata**copy_worksheet** metodo di**fogli di lavoro** modulo. Di seguito puoi vedere un esempio di codice.

**Codice PHP**

{{< highlight "php" >}}

 # Create a Worksheets object with reference to the sheets of the Workbook.

$sheets = $workbook->getWorksheets();

\# Copy data to a new sheet from an existing sheet within the Workbook.

$sheets->addCopy("Sheet1");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Copy Worksheet.xls");


{{< /highlight >}}
### **Sposta i fogli di lavoro all'interno di una cartella di lavoro**
 Per spostare il foglio di lavoro utilizzando**Aspose.Cells for Java in PHP** , chiamata**move_worksheet** metodo di**fogli di lavoro** modulo. Di seguito puoi vedere un esempio di codice.

**Codice PHP**

{{< highlight "php" >}}

 # Get the first worksheet in the book.

$sheet = $workbook->getWorksheets()->get(0);

\# Move the first sheet to the third position in the workbook.

$sheet->moveTo(2);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Move Worksheet.xls");

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica**Copiare e spostare fogli di lavoro (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/CopyingAndMovingWorksheets.php)
