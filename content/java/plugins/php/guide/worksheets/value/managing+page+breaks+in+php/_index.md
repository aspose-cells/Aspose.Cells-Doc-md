---
title : "Managing Page Breaks in Php" 
description : "" 
weight : 24865 
toc : false
type: docs
url: /java/plugins/php/guide/worksheets/value/managing+page+breaks+in+php/
---

# Aspose.Cells for Java : Managing Page Breaks in Php


## Aspose.Cells - Managing Page Breaks

##### Adding Page Breaks

To add page breaks using **Aspose.Cells Java for PHP**, call **add\_page\_breaks** method of **pagebreaks** module. Below you can see code example.

**PHP Code**

{{< code lang="cs" >}}
$worksheets = $workbook->getWorksheets();
$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();
$h_page_breaks->add("Y30");

$v_page_breaks = $worksheet->getVerticalPageBreaks();
$v_page_breaks->add("Y30");

# Saving the modified Excel file in default (that is Excel 2003) format
$workbook->save($dataDir . "Add Page Breaks.xls");   
{{< /code >}}

##### Clearing All Page Breaks

To clear all page breaks using **Aspose.Cells Java for PHP**, call **clear\_all\_page\_breaks** method of **pagebreaks** module. Below you can see code example.

**PHP Code**

{{< code lang="cs" >}}
$workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();
$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

# Saving the modified Excel file in default (that is Excel 2003) format
$workbook->save($dataDir . "Clear All Page Breaks.xls");
{{< /code >}}

##### Removeing Specific Page Break

To remove specific page break using **Aspose.Cells Java for PHP**, call **remove\_page\_break** method of **pagebreaks** module. Below you can see code example.

**PHP Code**

{{< code lang="cs" >}}
$worksheets = $workbook->getWorksheets();
$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();
$h_page_breaks->removeAt(0);

$v_page_breaks = $worksheet->getVerticalPageBreaks();
$v_page_breaks->removeAt(0);

# Saving the modified Excel file in default (that is Excel 2003) format
$workbook->save($dataDir . "Remove Page Break.xls");
{{< /code >}}

## Download Running Code

Download **Managing Page Breaks (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)

