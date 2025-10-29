---
title: إزالة إعدادات الطابعة الحالية لورقة العمل في ملف Excel
type: docs
weight: 60
url: /ar/python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: تشرح هذه المقالة كيفية إزالة إعدادات الطابعة الحالية لورقة العمل داخل ملف إكسل من خلال كائن إعداد الصفحة برمجياً مع رمز عينة باستخدام مكتبة Aspose.Cells للبايثون إكسل.
keywords: مكتبة إكسل بلغة بايثون، إزالة إعدادات الطابعة لورقة العمل، إزالة إعدادات الطابعة لورقة عمل إكسل باستخدام بايثون.
---

## **سيناريوهات الاستخدام المحتملة**
أحيانًا يرغب المطورون في منع إكسل من تضمين ملفات *.bin* الخاصة بإعدادات الطابعة في ملفات XLSX المحفوظة. تقع ملفات إعدادات الطابعة تحت *“[ملف "الجذر"]\xl\printerSettings”.* يوضح هذا المستند كيفية إزالة إعدادات الطابعة الحالية باستخدام API الخاصة بـ Aspose.Cells للبايثون via .NET.

## **إزالة إعدادات الطابعة الحالية لورقات العمل في ملف Excel**
يسمح Aspose.Cells للبايثون via .NET بإزالة إعدادات الطابعة الحالية المحددة لورقات مختلفة في ملف إكسل. يوضح رمز العينة التالي كيفية إزالة إعدادات الطابعة الحالية لجميع أوراق العمل في المصنف. يرجى مراجعة [ملف إكسل العينة](45056020.xlsx)، [ملف إكسل الناتج](45056021.xlsx)، الإخراج في وحدة التحكم بالإضافة إلى لقطة الشاشة للرجوع.

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
{{< app/cells/assistant language="python-net" >}}
