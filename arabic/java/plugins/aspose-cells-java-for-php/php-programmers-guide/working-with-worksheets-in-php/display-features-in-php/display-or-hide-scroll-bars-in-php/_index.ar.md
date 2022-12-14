---
title: عرض أو إخفاء أشرطة التمرير في Php
type: docs
weight: 20
url: /ar/java/display-or-hide-scroll-bars-in-php/
---
## **Aspose.Cells - عرض أو إخفاء أشرطة التمرير**
### **إخفاء أشرطة التمرير**
 لإخفاء أشرطة التمرير باستخدام ملفات**Aspose.Cells Java لـ PHP** ، مكالمة**أشرطة التمرير** وحدة.

**كود PHP**

{{< highlight "php" >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the vertical scroll bar of the Excel file

$workbook->getSettings()->setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

$workbook->getSettings()->setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
تحميل**عرض أو إخفاء أشرطة التمرير (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideScrollBars.php)
