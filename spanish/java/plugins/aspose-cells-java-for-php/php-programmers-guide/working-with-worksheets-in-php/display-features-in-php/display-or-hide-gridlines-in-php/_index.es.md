---
title: Mostrar u Ocultar Rejillas en Php
type: docs
weight: 10
url: /es/java/display-or-hide-gridlines-in-php/
---

## **Aspose.Cells - Mostrar u ocultar líneas de cuadrícula**
### **Ocultar líneas de cuadrícula**
Para ocultar la hoja de trabajo usando **Aspose.Cells Java para PHP**, llame al módulo **displayhidegridlines**.

**Código PHP**

{{< highlight php >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

//Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Hiding the grid lines of the first worksheet of the Excel file

$worksheet->setGridlinesVisible(false);

//Saving the modified Excel file in default (that is Excel 2000) format

$workbook->save($dataDir . "output.xls");


{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Mostrar u ocultar líneas de cuadrícula (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideGridlines.php)
