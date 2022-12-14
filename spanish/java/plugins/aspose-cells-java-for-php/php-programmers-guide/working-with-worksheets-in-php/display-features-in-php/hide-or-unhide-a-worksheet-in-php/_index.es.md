---
title: Ocultar o mostrar una hoja de trabajo en Php
type: docs
weight: 50
url: /es/java/hide-or-unhide-a-worksheet-in-php/
---
## **Aspose.Cells - Ocultar o mostrar una hoja de trabajo**
### **Ocultar una hoja de trabajo**
 Para ocultar la hoja de trabajo usando Aspose.Cells Java para PHP, llame**ocultarunhideworksheet** módulo.

**Código PHP**

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
## **Descargar código de ejecución**
Descargar**Ocultar o mostrar una hoja de trabajo (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/HideUnhideWorksheet.php)
