---
title: إزالة إعدادات الطابعة الحالية لورقة العمل في ملف Excel
type: docs
weight: 60
url: /ar/python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: في هذا المقال، ستتعلم كيفية إزالة إعدادات الطابعة الحالية للجدول العمل داخل ملف Excel من خلال كائن Page Setup برمجياً باستخدام رمز عينة باستخدام مكتبة Aspose.Cells لـ Python Excel.
keywords: مكتبة Excel الخاصة ببيثون، بيثون إزالة إعدادات الطابعة لجدول العمل، بيثون إزالة إعدادات الطابعة لجدول عمل Excel.
---

## **سيناريوهات الاستخدام المحتملة**
في بعض الأحيان يرغب المطورين في منع Excel من تضمين ملفات *.bin* لإعدادات الطابعة في ملفات XLSX المحفوظة. تقع ملفات إعدادات الطابعة تحت *"[file "root"]\xl\printerSettings”. يشرح هذا المستند كيفية إزالة إعدادات الطابعة الحالية باستخدام APIs Aspose.Cells لـ Python via .NET.

## **إزالة إعدادات الطابعة الحالية لورقات العمل في ملف Excel**
تسمح Aspose.Cells لبيثون via .NET بإزالة إعدادات الطابعة الحالية المحددة للصفحات المختلفة في ملف Excel. يوضح رمز العينة التالي كيفية إزالة إعدادات الطابعة الحالية لجميع أوراق العمل في الدفتر. يرجى رؤية [ملف Excel عينة](45056020.xlsx)، [ملف الإكسل الناتج](45056021.xlsx)، إخراج الوحدة النمطية بالإضافة إلى اللقطة الشاشة للإشارة.

## **لقطة شاشة**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **الكود المثالي**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.py" >}}

## **مخرجات الوحدة**
{{< highlight java >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
