---
title: قم بتصفية مشروع VBA أثناء تحميل مصنف
type: docs
weight: 140
url: /ar/net/filter-vba-project-while-loading-a-workbook/
---
## **قم بتصفية مشروع VBA أثناء تحميل مصنف Excel في C#**

تحتوي بعض ملفات .xlsm / .xslb على كمية كبيرة جدًا من وحدات الماكرو (أو وحدات ماكرو طويلة جدًا). سيقوم Aspose.Cells بتحميل هذه البيانات (التعريفية) دون قيد أو شرط عند فتح مثل هذه المصنفات. قد تحتاج إلى التحكم في هذا بالرغم من ذلك[**LoadDataFilterOptions**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) عندما تحتاج حقًا فقط إلى استخراج أسماء الأوراق لعدد كبير من المصنفات ، وبالتالي تخطي هذا المحتوى غير الضروري. يتم توفير هذا الفلتر من خلال تقديم خيار جديد ،[**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions).

## **عينة من الرموز**

يقوم نموذج التعليمات البرمجية التالي بتحميل مصنف بحيث يتم تصفية VBA فقط. يمكن تنزيل نموذج ملف لاختبار هذه الميزة من الرابط التالي:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
