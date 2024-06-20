---
title: Vista Previa de Salto de Página en Php
type: docs
weight: 60
url: /es/java/page-break-preview-in-php/
---

## **Aspose.Cells - Vista previa de salto de página**
Para establecer una hoja de cálculo en vista previa de salto de página usando **Aspose.Cells Java para PHP**, simplemente invoque el módulo **PageBreakPreview**.

**Código PHP**

{{< highlight php >}}

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
## **Descargar Código en Ejecución**
Descargar **Vista previa de salto de página (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/PageBreakPreview.php)
