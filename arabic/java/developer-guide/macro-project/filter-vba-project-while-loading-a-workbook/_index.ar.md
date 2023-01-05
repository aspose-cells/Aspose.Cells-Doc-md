---
title: قم بتصفية مشروع VBA أثناء تحميل مصنف
type: docs
weight: 70
url: /ar/java/filter-vba-project-while-loading-a-workbook/
---
## **سيناريوهات الاستخدام الممكنة**
تحتوي بعض ملفات .xlsm / .xslb على كمية كبيرة جدًا من وحدات الماكرو (أو وحدات ماكرو طويلة جدًا). سيقوم Aspose.Cells بتحميل هذه البيانات (التعريفية) دون قيد أو شرط عند فتح مثل هذه المصنفات. قد تحتاج إلى التحكم في هذا من خلال LoadDataFilterOptions ، عندما تحتاج حقًا فقط إلى استخراج أسماء الأوراق لعدد كبير من المصنفات وبالتالي تخطي هذا المحتوى غير الضروري. يتم توفير عامل التصفية هذا من خلال إدخال خيار جديد LoadDataFilterOptions.VBA.
## **عينة من الرموز**
يقوم نموذج التعليمات البرمجية التالي بتحميل مصنف بحيث يتم تصفية VBA فقط. يمكن تنزيل ملف نموذج لاختبار هذه الميزة من الرابط التالي:

[sampleMacroEnabledWorkbook.xlsm](79527951.xlsm)

// اضبط خيارات التحميل ، لا نريد تحميل VBA
LoadOptions loadOptions = جديد LoadOptions (LoadFormat.AUTO) ؛
loadOptions.setLoadFilter (LoadFilter جديد (LoadDataFilterOptions.ALL & ~ LoadDataFilterOptions.VBA)) ؛

// إنشاء كائن مصنف من نموذج ملف Excel باستخدام خيارات التحميل
كتاب المصنف = مصنف جديد (srcDir + "sampleMacroEnabledWorkbook.xlsm" ، loadOptions) ؛

// احفظ الإخراج بتنسيق pdf
book.save (outDir + "OutputSampleMacroEnabledWorkbook.xlsm"، SaveFormat.XLSM) ؛
