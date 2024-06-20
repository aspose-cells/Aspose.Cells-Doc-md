---
title: Congelar paneles en Php
type: docs
weight: 40
url: /es/java/freeze-panes-in-php/
---

## **Aspose.Cells - Congelar paneles**
Para congelar paneles en el documento de la hoja de cálculo usando **Aspose.Cells Java para PHP**, simplemente invoque el módulo **FreezePanes**.

**Código PHP**

{{< highlight php >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Applying freeze panes settings

$worksheet->freezePanes(3,2,3,2);

//Saving the modified Excel file in default format

$workbook->save($dataDir . "book.out.xls");

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Congelar Paneles (Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/FreezePanes.php)
