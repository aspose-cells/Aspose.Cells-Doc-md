---
title: Gestión de saltos de página en PHP
type: docs
weight: 20
url: /es/java/managing-page-breaks-in-php/
---
## **Aspose.Cells - Gestión de saltos de página**
### **Adición de saltos de página**
 Para agregar saltos de página usando**Aspose.Cells Java para PHP** , llamar**add_page_breaks** método de**saltos de página** módulo. A continuación puede ver un ejemplo de código.

**Código PHP**

{{< highlight "php" >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->add("Y30");

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->add("Y30");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Add Page Breaks.xls");   

{{< /highlight >}}
### **Borrar todos los saltos de página**
 Para borrar todos los saltos de página usando**Aspose.Cells Java para PHP** , llamar**clear_all_page_breaks** método de**saltos de página** módulo. A continuación puede ver un ejemplo de código.

**Código PHP**

{{< highlight "php" >}}

 $workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();

$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Clear All Page Breaks.xls");

{{< /highlight >}}
### **Eliminación de un salto de página específico**
 Para eliminar un salto de página específico usando**Aspose.Cells Java para PHP** , llamar**remove_page_break** método de**saltos de página** módulo. A continuación puede ver un ejemplo de código.

**Código PHP**

{{< highlight "php" >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->removeAt(0);

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->removeAt(0);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Remove Page Break.xls");

{{< /highlight >}}
## **Descargar código de ejecución**
Descargar**Gestión de saltos de página (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)
