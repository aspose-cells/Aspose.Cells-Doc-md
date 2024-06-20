---
title: تصفية مشروع VBA أثناء تحميل جدول عمل
type: docs
weight: 70
url: /ar/java/filter-vba-project-while-loading-a-workbook/
---

## **سيناريوهات الاستخدام المحتملة**
بعض ملفات .xlsm/.xslb تحتوي على كميات كبيرة للغاية من الماكرو (أو ماكروهات طويلة جدًا جدًا). ستقوم Aspose.Cells بتحميل هذه البيانات (الفرعية) بشكل لا قاطع عند فتح مثل هذه المصنفات. قد تحتاج إلى التحكم في هذا من خلال LoadDataFilterOptions عندما تحتاج حقًا إلى استخراج أسماء الأوراق مثلاً لعدد كبير من المصنفات والتخطي فوق مثل هذا المحتوى غير المرغوب فيه. يتم توفير هذا المرشح من خلال إدخال خيار جديد LoadDataFilterOptions.VBA.
## **الكود المثالي**
يحمل الكود العينة التالي دفتر عمل حيث تتم تصفية VBA فقط. يمكن تنزيل الملف عينة لاختبار هذه الميزة من الرابط التالي:

[sampleMacroEnabledWorkbook.xlsm](79527951.xlsm)

// تعيين خيارات التحميل، نريد عدم تحميل VBA
LoadOptions loadOptions = new LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// إنشاء كائن دفتر عمل من ملف إكسل عينة باستخدام خيارات التحميل
Workbook book = new Workbook(srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// حفظ الناتج في تنسيق PDF
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
