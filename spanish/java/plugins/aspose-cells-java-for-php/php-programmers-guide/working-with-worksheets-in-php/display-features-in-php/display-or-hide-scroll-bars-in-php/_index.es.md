---
title: Mostrar u ocultar barras de desplazamiento en Php
type: docs
weight: 20
url: /es/java/display-or-hide-scroll-bars-in-php/
---
## **Aspose.Cells - Mostrar u ocultar barras de desplazamiento**
### **Ocultar barras de desplazamiento**
 Para ocultar las barras de desplazamiento usando**Aspose.Cells Java for PHP** , llamada**mostrar ocultar barras de desplazamiento** módulo.

**Código PHP**

{{< highlight "php" >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the vertical scroll bar of the Excel file

$workbook->getSettings()->setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

$workbook->getSettings()->setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");

{{< /highlight >}}
## **Descargar código de ejecución**
Descargar**Mostrar u ocultar barras de desplazamiento (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideScrollBars.php)
