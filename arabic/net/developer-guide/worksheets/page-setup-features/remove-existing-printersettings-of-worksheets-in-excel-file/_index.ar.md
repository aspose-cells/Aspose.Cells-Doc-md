---
title: إزالة إعدادات الطابعة الحالية لورقة العمل في ملف Excel
type: docs
weight: 60
url: /ar/net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: في هذا المقال، ستتعلم كيفية إزالة إعدادات الطابعة الحالية لورقة العمل داخل ملف Excel بواسطة كائن إعداد الصفحة برمجيًا باستخدام واجهة برمجة التطبيقات C# أو .NET.
keywords: إزالة إعدادات الطابعة لورقة العمل c#، إزالة إعدادات الطابعة لورقة عمل إكسل c#
---

## **سيناريوهات الاستخدام المحتملة**
في بعض الأحيان، يرغب المطورون في منع Excel من تضمين ملفات *.bin* لإعدادات الطابعة في ملفات XLSX المحفوظة. تقع ملفات إعدادات الطابعة تحت *“[file "root"]\xl\printerSettings”.* يوضح هذا المستند كيفية إزالة إعدادات الطابعة الحالية باستخدام واجهة برمجة التطبيقات Aspose.Cells.
## **إزالة إعدادات الطابعة الحالية لورقات العمل في ملف Excel**
تتيح Aspose.Cells إزالة إعدادات الطابعة الحالية المحددة لورقات العمل المختلفة في ملف Excel. يوضح الكود العينات التالية كيفية إزالة إعدادات الطابعة الحالية لجميع ورقات العمل في الدفتر. يرجى الاطلاع على [ملف Excel عينة](45056020.xlsx)، [ملف Excel الناتج](45056021.xlsx)، الإخراج على وحدة التحكم، فضلاً عن اللقطة للإشارة.
## **لقطة شاشة**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
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
