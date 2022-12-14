---
title: قم بإزالة إعدادات PrinterSettings الموجودة من أوراق العمل في ملف Excel
type: docs
weight: 40
url: /ar/java/remove-existing-printersettings-of-worksheets-in-excel-file/
---
## **سيناريوهات الاستخدام الممكنة**
يريد المطورون أحيانًا منع Excel من تضمين ملفات*.سلة مهملات* ملفات إعدادات الطابعة في ملفات XLSX المحفوظة. توجد ملفات إعدادات الطابعة أسفل*"[file" root "] \ xl \ printerSettings"*. يشرح هذا المستند كيفية إزالة إعدادات الطابعة الحالية باستخدام Aspose.Cells APIs.
## **قم بإزالة إعدادات PrinterSettings الموجودة من أوراق العمل في ملف Excel**
يسمح لك Aspose.Cells بإزالة إعدادات الطابعة الموجودة المحددة لأوراق مختلفة في ملف Excel. يوضح نموذج التعليمات البرمجية التالي كيفية إزالة إعدادات الطابعة الموجودة لكافة أوراق العمل في المصنف. يرجى الاطلاع عليها[نموذج لملف Excel](45056023.xlsx), [إخراج ملف Excel](45056024.xlsx)، وإخراج وحدة التحكم وكذلك لقطة شاشة كمرجع.
## **لقطة شاشة**
![ما يجب القيام به: image_بديل_نص](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.java" >}}
## **إخراج وحدة التحكم**
{{< highlight "java" >}}

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
