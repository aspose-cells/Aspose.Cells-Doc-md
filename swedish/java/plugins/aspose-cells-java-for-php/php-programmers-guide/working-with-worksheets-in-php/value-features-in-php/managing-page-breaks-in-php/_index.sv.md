---
title: Hantera sidbrytningar i Php
type: docs
weight: 20
url: /sv/java/managing-page-breaks-in-php/
---

## **Aspose.Cells - Hantera sidbrytningar**
### **Lägga till sidbrytningar**
För att lägga till sidbrytningar med **Aspose.Cells Java för PHP**, anropa **add_page_breaks** metoden för **pagebreaks** modulen. Nedan kan du se kodexemplet.

**PHP-kod**

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
### **Rensa alla sidbrytningar**
För att rensa alla sidbrytningar med **Aspose.Cells Java för PHP**, anropa **clear_all_page_breaks** metoden för **pagebreaks** modulen. Nedan kan du se kodexemplet.

**PHP-kod**

{{< highlight php >}}

 $workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();

$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Clear All Page Breaks.xls");

{{< /highlight >}}
### **Ta bort specifik sidbrytning**
För att ta bort specifik sidbrytning med **Aspose.Cells Java för PHP**, anropa **remove_page_break** metoden för **pagebreaks** modulen. Nedan kan du se kodexemplet.

**PHP-kod**

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
## **Ladda ned körbar kod**
Hämta **Hantera Sidbrytningar (Aspose.Cells)** från någon av de nedan nämnda sociala kodningssidorna:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)
