---
title: تصفية الأسماء المعرفة أثناء تحميل المصنف
type: docs
weight: 50
url: /ar/net/filter-defined-names-while-loading-workbook/
---
## **سيناريوهات الاستخدام الممكنة**

Aspose.Cells يسمح لك بترشيح أو إزالة الأسماء المعرفة الموجودة داخل مصنف العمل. الرجاء استخدام[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)لتحميل الأسماء المعرفة واستخدام ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)لإزالتها أثناء تحميل المصنف. يرجى ملاحظة أنه إذا قمت بإزالة الأسماء المعرفة ، فقد تنفصل الصيغ الموجودة داخل المصنف.

## **تصفية الأسماء المعرفة أثناء تحميل المصنف**

 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](61767860.xlsx) التي لها صيغة في الخلية**C1** تحتوي على الأسماء المعرفة أي*= SUM (MyName1، MyName2)*. بما أننا نستخدم ملفات ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) لإزالة الأسماء المعرفة أثناء تحميل المصنف ، فإن الصيغة الموجودة في الخلية C1 بتنسيق[إخراج ملف Excel](61767861.xlsx) تفكك وترى*#NAME?*بدلاً من. يرجى الاطلاع على لقطة الشاشة التالية التي توضح تأثير الكود على نموذج ملف Excel.

![ما يجب القيام به: image_بديل_نص](filter-defined-names-while-loading-workbook_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.cs" >}}
