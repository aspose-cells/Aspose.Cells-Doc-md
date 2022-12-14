---
title: تصفية الأسماء المعرفة أثناء تحميل المصنف
type: docs
weight: 50
url: /ar/java/filter-defined-names-while-loading-workbook/
---
## **سيناريوهات الاستخدام الممكنة**

Aspose.Cells يسمح لك بترشيح أو إزالة الأسماء المعرفة الموجودة داخل مصنف العمل. يرجى استخدام[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)لتحميل الأسماء المعرفة واستخدام ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)لإزالتها أثناء تحميل المصنف. يرجى ملاحظة أنه إذا قمت بإزالة الأسماء المعرفة ، فقد تنفصل الصيغ الموجودة داخل المصنف.

## **تصفية الأسماء المعرفة أثناء تحميل المصنف**

يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](61767873.xlsx)التي تحتوي على صيغة في الخلية C1 تحتوي على الأسماء المعرفة مثل*= SUM (MyName1، MyName2)*. منذ ذلك الحين ، نحن نستخدم ملفات ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)لإزالة الأسماء المعرفة أثناء تحميل المصنف ، فإن الصيغة الموجودة في الخلية C1 بتنسيق[إخراج ملف Excel](61767872.xlsx)تفكك وترى*#NAME?*في حين أن. يرجى الاطلاع على لقطة الشاشة التالية التي توضح تأثير الكود على نموذج ملف Excel.

![ما يجب القيام به: image_بديل_نص](filter-defined-names-while-loading-workbook_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.java" >}}
