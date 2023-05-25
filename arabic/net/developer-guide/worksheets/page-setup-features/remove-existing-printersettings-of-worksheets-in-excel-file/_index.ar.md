---
title: قم بإزالة إعدادات PrinterSettings الموجودة من أوراق العمل في ملف Excel
type: docs
weight: 60
url: /ar/net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: في هذه المقالة ، ستتعلم كيفية إزالة PrinterSettings من ورقة العمل الموجودة داخل ملف Excel من خلال كائن إعداد الصفحة برمجيًا باستخدام نموذج التعليمات البرمجية باستخدام C# API أو مكتبة .NET.
keywords: remove printer settings of worksheet c#, remove printer settings of excel worksheet c#
---
##  **سيناريوهات الاستخدام الممكنة**
يريد المطورون أحيانًا منع Excel من تضمين ملفات*.سلة مهملات* ملفات إعدادات الطابعة في ملفات XLSX المحفوظة. توجد ملفات إعدادات الطابعة أسفل*"[ملف" جذر "] \ xl \ إعدادات الطابعة".* يشرح هذا المستند كيفية إزالة إعدادات الطابعة الحالية باستخدام Aspose.Cells APIs.
##  **قم بإزالة إعدادات PrinterSettings الموجودة من أوراق العمل في ملف Excel**
يسمح لك Aspose.Cells بإزالة إعدادات الطابعة الموجودة المحددة لأوراق مختلفة في ملف Excel. يوضح نموذج التعليمات البرمجية التالي كيفية إزالة إعدادات الطابعة الموجودة لكافة أوراق العمل في المصنف. يرجى الاطلاع عليها[نموذج لملف Excel](45056020.xlsx), [إخراج ملف Excel](45056021.xlsx)، إخراج وحدة التحكم وكذلك لقطة الشاشة كمرجع.
##  **لقطة شاشة**
![ما يجب القيام به: image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
##  **عينة من الرموز**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
##  **إخراج وحدة التحكم**
{{< highlight "java" >}}

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
