---
title: Proteger hojas de cálculo en Php
type: docs
weight: 10
url: /es/java/protecting-worksheets-in-php/
---

## **Aspose.Cells - Protección de hojas de cálculo**
Para proteger la hoja de cálculo usando **Aspose.Cells Java para PHP**, llame al método **protect_worksheet** del módulo **protection**.

**Código PHP**

{{< highlight php >}}

 //Instantiating a Excel object by excel file path

$excel = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $excel->getWorksheets();

$worksheet = $worksheets->get(0);

$protection = $worksheet->getProtection();

//The following 3 methods are only for Excel 2000 and earlier formats

$protection->setAllowEditingContent(false);

$protection->setAllowEditingObject(false);

$protection->setAllowEditingScenario(false);

//Protects the first worksheet with a password "1234"

$protection->setPassword("1234");

//Saving the modified Excel file in default format

$excel->save($dataDir . "output.xls");  

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Protección de hojas de cálculo (Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/ProtectingWorksheet.php)
