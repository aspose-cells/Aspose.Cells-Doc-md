---
title: إدارة كسور الصفحة في PHP
type: docs
weight: 20
url: /ar/java/managing-page-breaks-in-php/
---

## **Aspose.Cells - إدارة فواصل الصفحات**
### **إضافة فواصل الصفحات**
لإضافة كسور الصفحة باستخدام **Aspose.Cells Java for PHP**، اتصل بطريقة **add_page_breaks** في وحدة **pagebreaks**. يمكنك رؤية مثال على الكود أدناه.

**كود PHP**

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
### **مسح كافة فواصل الصفحات**
لمسح كل كسور الصفحة باستخدام **Aspose.Cells Java for PHP**، اتصل بطريقة **clear_all_page_breaks** في وحدة **pagebreaks**. يمكنك رؤية مثال على الكود أدناه.

**كود PHP**

{{< highlight php >}}

 $workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();

$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Clear All Page Breaks.xls");

{{< /highlight >}}
### **إزالة فاصل صفحة محدد**
لإزالة كسر الصفحة المحدد باستخدام **Aspose.Cells Java for PHP**، اتصل بطريقة **remove_page_break** في وحدة **pagebreaks**. يمكنك رؤية مثال على الكود أدناه.

**كود PHP**

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
## **تحميل رمز التشغيل**
تنزيل **إدارة فواصل الصفحات (Aspose.Cells)** من أي من مواقع التعاون الاجتماعي التالية:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)
