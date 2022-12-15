---
title: Vista previa de salto de página en Php
type: docs
weight: 60
url: /es/java/page-break-preview-in-php/
---
## **Aspose.Cells - Vista previa de salto de página**
 Para configurar la hoja de trabajo para la vista previa de salto de página usando**Aspose.Cells Java for PHP** , simplemente invocar**La previsualización del salto de página** módulo.

**Código PHP**

{{< highlight "php" >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Adding a new worksheet to the Workbook object

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Displaying the worksheet in page break preview

$worksheet->setPageBreakPreview(true);

//Saving the modified Excel file in default format

$workbook->save($dataDir . "output.xls");

{{< /highlight >}}
## **Descargar código de ejecución**
Descargar**Vista previa de salto de página (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/PageBreakPreview.php)
