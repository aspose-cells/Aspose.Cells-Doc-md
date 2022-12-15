---
title: إدارة فواصل الصفحات في Php
type: docs
weight: 20
url: /ar/java/managing-page-breaks-in-php/
---
## **Aspose.Cells - إدارة فواصل الصفحات**
### **مضيفا فواصل الصفحات**
 لإضافة فواصل الصفحات باستخدام**Aspose.Cells Java for PHP** ، مكالمة**add_page_breaks** طريقة**فواصل الصفحة** وحدة. أدناه يمكنك مشاهدة مثال رمز.

**كود PHP**

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
### **مسح كافة فواصل الصفحات**
 لمسح كافة فواصل الصفحات باستخدام**Aspose.Cells Java for PHP** ، مكالمة**clear_all_page_breaks** طريقة**فواصل الصفحة** وحدة. أدناه يمكنك مشاهدة مثال رمز.

**كود PHP**

{{< highlight "php" >}}

 $workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();

$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Clear All Page Breaks.xls");

{{< /highlight >}}
### **إزالة فاصل صفحة معين**
 لإزالة فاصل صفحة معين باستخدام**Aspose.Cells Java for PHP** ، مكالمة**remove_page_break** طريقة**فواصل الصفحة** وحدة. أدناه يمكنك مشاهدة مثال رمز.

**كود PHP**

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
## **تحميل كود الجري**
تحميل**إدارة فواصل الصفحات (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)
