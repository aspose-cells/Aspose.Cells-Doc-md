---
title: إزالة إعدادات الطابعة الحالية لورقة العمل في ملف Excel
type: docs
weight: 40
url: /ar/java/remove-existing-printersettings-of-worksheets-in-excel-file/
---

## **سيناريوهات الاستخدام المحتملة**
أحيانًا يرغب المطورون في منع إكسيل من تضمين ملفات * .bin * لإعدادات الطابعة في ملفات XLSX المحفوظة. تُوجد ملفات إعدادات الطابعة تحت * "[ملف "الجذر"] \ xl \ printerSettings" *. يشرح هذا المستند كيفية إزالة إعدادات الطابعة الحالية باستخدام واجهات برمجة التطبيقات لـ Aspose.Cells.
## **إزالة إعدادات الطابعة الحالية لورقات العمل في ملف Excel**
تُسمح Aspose.Cells لك بإزالة إعدادات الطابعة الحالية المحددة لأوراق مختلفة في ملف إكسيل. يوضح الكود المثالي التالي كيفية إزالة إعدادات الطابعة الحالية لجميع ورقات العمل في سجل العمل. يرجى الاطلاع على [ملف إكسيل عيني](45056023.xlsx) ، [ملف إكسيل الناتج](45056024.xlsx) ، الإخراج على وحدة التحكم بالإضافة إلى لقطة الشاشة للرجوع إليها.
## **لقطة شاشة**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.java" >}}
## **مخرجات الوحدة**
{{< highlight java >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: 5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: 34

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: 70

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: 8

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
