---
title: عرض أو إخفاء أشرطة التمرير في PHP
type: docs
weight: 20
url: /ar/java/display-or-hide-scroll-bars-in-php/
---

## **Aspose.Cells - عرض أو إخفاء أشرطة التمرير**
### **إخفاء أشرطة التمرير**
لإخفاء أشرطة التمرير باستخدام **Aspose.Cells Java for PHP** ، اتصل بوحدة **displayhidescrollbars**.

**كود PHP**

{{< highlight php >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the vertical scroll bar of the Excel file

$workbook->getSettings()->setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

$workbook->getSettings()->setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **إظهار أو إخفاء أشرطة التمرير (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideScrollBars.php)
