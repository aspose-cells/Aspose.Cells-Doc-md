---
title: Congelar paneles en Php
type: docs
weight: 40
url: /es/java/freeze-panes-in-php/
---
## **Aspose.Cells - Congelar paneles**
 Para congelar paneles en el documento de hoja de cálculo usando**Aspose.Cells Java para PHP** , simplemente invocar**FreezePanes** módulo.

**Código PHP**

{{< highlight "php" >}}

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
## **Descargar código de ejecución**
Descargar**Congelar paneles (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/FreezePanes.php)
