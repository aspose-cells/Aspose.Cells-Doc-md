---
title: Copiar y Mover Hojas de Cálculo en Php
type: docs
weight: 10
url: /es/java/copying-and-moving-worksheets-in-php/
---

## **Aspose.Cells - Copiar y Mover hojas de cálculo**
### **Copiar Hojas de Cálculo dentro de un Libro de Trabajo**
Para copiar una hoja de cálculo usando **Aspose.Cells for Java en PHP**, llama al método **copy_worksheet** del módulo **copyworksheets**. A continuación se muestra un ejemplo de código.

**Código PHP**

{{< highlight php >}}

 # Create a Worksheets object with reference to the sheets of the Workbook.

$sheets = $workbook->getWorksheets();

\# Copy data to a new sheet from an existing sheet within the Workbook.

$sheets->addCopy("Sheet1");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Copy Worksheet.xls");


{{< /highlight >}}
### **Mover hojas de cálculo dentro de un libro de trabajo**
Para mover una hoja de cálculo usando **Aspose.Cells for Java en PHP**, llama al método **move_worksheet** del módulo **copyworksheets**. A continuación se muestra un ejemplo de código.

**Código PHP**

{{< highlight php >}}

 # Get the first worksheet in the book.

$sheet = $workbook->getWorksheets()->get(0);

\# Move the first sheet to the third position in the workbook.

$sheet->moveTo(2);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Move Worksheet.xls");

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Copiando y Moviendo Hojas de Cálculo (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/CopyingAndMovingWorksheets.php)
