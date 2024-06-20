---
title: Gestionar Saltos de Página en Php
type: docs
weight: 20
url: /es/java/managing-page-breaks-in-php/
---

## **Aspose.Cells - Gestionar Saltos de Página**
### **Añadir Saltos de Página**
Para agregar saltos de página usando **Aspose.Cells Java para PHP**, llama al método **add_page_breaks** del módulo **pagebreaks**. A continuación se muestra un ejemplo de código.

**Código PHP**

{{< highlight php >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->add("Y30");

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->add("Y30");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Add Page Breaks.xls");   

{{< /highlight >}}
### **Borrar Todos los Saltos de Página**
Para borrar todos los saltos de página usando **Aspose.Cells Java para PHP**, llama al método **clear_all_page_breaks** del módulo **pagebreaks**. A continuación se muestra un ejemplo de código.

**Código PHP**

{{< highlight php >}}

 $workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();

$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Clear All Page Breaks.xls");

{{< /highlight >}}
### **Eliminar Salto de Página Específico**
Para quitar un salto de página específico utilizando **Aspose.Cells Java para PHP**, llama al método **remove_page_break** del módulo **pagebreaks**. A continuación, puedes ver un ejemplo de código.

**Código PHP**

{{< highlight php >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->removeAt(0);

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->removeAt(0);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Remove Page Break.xls");

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Gestionando Saltos de Página (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)
