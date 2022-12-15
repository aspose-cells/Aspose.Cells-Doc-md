---
title: Mostrar u ocultar pestañas en Php
type: docs
weight: 30
url: /es/java/display-or-hide-tabs-in-php/
---
## **Aspose.Cells - Mostrar u ocultar pestañas**
### **Ocultar pestañas**
 Para ocultar pestañas usando**Aspose.Cells Java for PHP** , llamar**Mostrar ocultar pestañas** módulo.

**Código PHP**

{{< highlight "php" >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the tabs of the Excel file

$workbook->getSettings()->setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir + "output.xls");

{{< /highlight >}}
## **Descargar código de ejecución**
Descargar**Ocultar o mostrar u ocultar pestañas (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideTabs.php)
