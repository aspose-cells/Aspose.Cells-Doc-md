---
title: Mostrar u Ocultar Barras de Desplazamiento en Php
type: docs
weight: 20
url: /es/java/display-or-hide-scroll-bars-in-php/
---

## **Aspose.Cells - Mostrar u Ocultar Barras de Desplazamiento**
### **Ocultar Barras de Desplazamiento**
Para ocultar las barras de desplazamiento usando **Aspose.Cells Java para PHP**, llame al módulo **displayhidescrollbars**.

**Código PHP**

{{< highlight php >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the vertical scroll bar of the Excel file

$workbook->getSettings()->setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

$workbook->getSettings()->setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Mostrar u Ocultar Barras de Desplazamiento (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideScrollBars.php)
