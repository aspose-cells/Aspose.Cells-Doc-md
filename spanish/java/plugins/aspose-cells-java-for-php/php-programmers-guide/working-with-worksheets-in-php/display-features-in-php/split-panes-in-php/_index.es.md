---
title: Dividir Paneles en Php
type: docs
weight: 70
url: /es/java/split-panes-in-php/
---

## **Aspose.Cells - Dividir paneles**
Para dividir paneles usando **Aspose.Cells Java para PHP**, simplemente invoque el módulo **SplitPanes**.

**Código PHP**

{{< highlight php >}}

 $saveFormat = new SaveFormat();

//Instantiate a new workbook

//Open a template file

$book = new Workbook($dataDir . "book.xls");

//Set the active cell

$book->getWorksheets()->get(0)->setActiveCell("A20");

//Split the worksheet window

$book->getWorksheets()->get(0)->split();

//Save the excel file

$book->save($dataDir . "book.out.xls", $saveFormat->EXCEL_97_TO_2003);

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Dividir paneles (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/SplitPanes.php)
