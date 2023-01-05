---
title: Hantera sidbrytningar i Php
type: docs
weight: 20
url: /sv/java/managing-page-breaks-in-php/
---
## **Aspose.Cells - Hantera sidbrytningar**
### **Lägga till sidbrytningar**
 För att lägga till sidbrytningar med hjälp av**Aspose.Cells Java for PHP** , ringa upp**add_page_breaks** metod av**sidbrytningar** modul. Nedan kan du se kodexempel.

**PHP-kod**

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
### **Rensa alla sidbrytningar**
 För att rensa alla sidbrytningar med**Aspose.Cells Java for PHP** , ringa upp**rensa_alla_sidebrytningar** metod av**sidbrytningar** modul. Nedan kan du se kodexempel.

**PHP-kod**

{{< highlight "php" >}}

 $workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();

$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Clear All Page Breaks.xls");

{{< /highlight >}}
### **Ta bort specifik sidbrytning**
 För att ta bort specifik sidbrytning med**Aspose.Cells Java for PHP** , ringa upp**remove_page_break** metod av**sidbrytningar** modul. Nedan kan du se kodexempel.

**PHP-kod**

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
## **Ladda ner Running Code**
Ladda ner**Hantera sidbrytningar (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)
