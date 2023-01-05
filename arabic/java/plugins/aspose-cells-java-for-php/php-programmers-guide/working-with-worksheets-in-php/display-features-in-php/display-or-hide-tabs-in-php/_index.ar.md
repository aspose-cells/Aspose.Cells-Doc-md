---
title: عرض أو إخفاء علامات التبويب في Php
type: docs
weight: 30
url: /ar/java/display-or-hide-tabs-in-php/
---
## **Aspose.Cells - عرض أو إخفاء علامات التبويب**
### **علامات التبويب الاختباء**
 لإخفاء علامات التبويب باستخدام ملفات**Aspose.Cells Java for PHP** ، مكالمة**عرض** وحدة.

**كود PHP**

{{< highlight "php" >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the tabs of the Excel file

$workbook->getSettings()->setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir + "output.xls");

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
تحميل**إخفاء أو عرض أو إخفاء علامات التبويب (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideTabs.php)
