﻿---
title: الملء التلقائي لبيانات العلامات الذكية في أوراق عمل أخرى إذا كانت البيانات كبيرة جدًا
type: docs
weight: 10
url: /ar/java/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---
## **سيناريوهات الاستخدام الممكنة**

في بعض الأحيان ، تريد ملء بيانات العلامة الذكية تلقائيًا في أوراق عمل أخرى إذا كانت كبيرة جدًا. لنفترض أن مصدر البيانات الخاص بك يحتوي على 1500000 سجل. هذه سجلات كثيرة جدًا لورقة عمل واحدة ، ثم يمكنك نقل بقية السجلات إلى ورقة العمل التالية.

## **الملء التلقائي لبيانات العلامات الذكية في أوراق عمل أخرى إذا كانت البيانات كبيرة جدًا**

يحتوي نموذج التعليمات البرمجية التالي على مصدر بيانات يحتوي على 21 سجلاً. نريد عرض 15 سجلاً فقط في ورقة عمل واحدة ، ثم تنتقل بقية السجلات تلقائيًا إلى ورقة العمل الثانية. يرجى ملاحظة أن ورقة العمل الثانية يجب أن تحتوي أيضًا على نفس علامة العلامة الذكية ويجب عليك الاتصال[**WorkbookDesigner.process (sheetIndex، isPreserved)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process(int,%20boolean) ) طريقة لكل من الأوراق. رجاء تاكد من[Microsoft ملف قاعدة بيانات Access](60489777.accdb) المستخدمة في هذا الرمز وكذلك[إخراج ملف Excel](60489786.xlsx)تم إنشاؤها بواسطة رمز كمرجع.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.java" >}}
