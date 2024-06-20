---
title: إظهار أو إخفاء التابز في PHP
type: docs
weight: 30
url: /ar/java/display-or-hide-tabs-in-php/
---

## **Aspose.Cells - عرض أو إخفاء علامات التبويب**
### **إخفاء علامات التبويب**
لإخفاء علامات التابز باستخدام **Aspose.Cells Java for PHP**, قم بالاتصال بوحدة **displayhidetabs**.

**كود PHP**

{{< highlight php >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the tabs of the Excel file

$workbook->getSettings()->setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir + "output.xls");

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **إخفاء أو عرض أو إخفاء علامات التبويب (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideTabs.php)
