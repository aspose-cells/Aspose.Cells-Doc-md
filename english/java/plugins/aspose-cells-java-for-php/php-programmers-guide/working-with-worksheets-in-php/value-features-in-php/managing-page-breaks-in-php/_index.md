---
title: Managing Page Breaks in Php
type: docs
weight: 20
url: /java/managing-page-breaks-in-php/
---

## **Aspose.Cells - Managing Page Breaks**
### **Adding Page Breaks**
To add page breaks using **Aspose.Cells Java for PHP**, call **add_page_breaks** method of **pagebreaks** module. Below you can see code example.

**PHP Code**

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
### **Clearing All Page Breaks**
To clear all page breaks using **Aspose.Cells Java for PHP**, call **clear_all_page_breaks** method of **pagebreaks** module. Below you can see code example.

**PHP Code**

{{< highlight php >}}

 $workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();

$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Clear All Page Breaks.xls");

{{< /highlight >}}
### **Removeing Specific Page Break**
To remove specific page break using **Aspose.Cells Java for PHP**, call **remove_page_break** method of **pagebreaks** module. Below you can see code example.

**PHP Code**

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
## **Download Running Code**
Download **Managing Page Breaks (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)
