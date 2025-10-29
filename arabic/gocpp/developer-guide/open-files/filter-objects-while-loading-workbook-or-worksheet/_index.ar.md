---
title: تصفية الكائنات أثناء تحميل دفتر العمل أو ورقة العمل باستخدام Golang عبر C++
linktitle: تصفية الكائنات أثناء تحميل المصنف أو ورقة العمل
type: docs
weight: 330
url: /ar/go-cpp/filter-objects-while-loading-workbook-or-worksheet/
description: تعلم كيفية تصفية الكائنات مثل الرسوم البيانية والأشكال والتنسيق الشرطي أثناء تحميل دفاتر العمل أو أوراق العمل باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**
 يرجى استخدام خاصية [LoadOptions.GetLoadFilter()](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) عند تصفية البيانات من دفتر العمل. وإذا كنت تريد تصفية البيانات من أوراق عمل فردية، فستحتاج إلى تجاوز طريقة [LoadFilter.StartSheet](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/startsheet/) . يرجى توفير القيمة المناسبة من تعداد [LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) أثناء الإنشاء أو العمل مع [LoadFilter](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/).

تعد [LoadDataFilterOptions](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) القيم الممكنة التالية.

- الكل
- إعدادات الكتاب
- خلية فارغة
- خلية مع تخطيط
- بيانات الخلية
- خطأ الخلية
- رقم الخليّة
- سلسلة الخليّة
- قيمة الخلية
- Chart
- تنسيق شرطي
- التحقق من البيانات
- الأسماء المعرفة
- خصائص المستند
- صيغة
- الروابط الفائقة
- منطقة مدمجة
- الجدول المحوري
- الإعدادات
- الشكل
- بيانات الورقة
- إعدادات الورقة
- البنية
- النمط
- الجدول
- VBA
- خريطة Xml

## **تصفية الكائنات أثناء تحميل دفتر العمل**
يوضح الكود المصدري التالي كيفية تصفية الرسوم البيانية من دفتر العمل. يرجى التحقق من [ملف الإكسل العيني](5115258.xlsx) المستخدم في هذا الكود و [ملف PDF الناتج](5115257.pdf) الذي تم إنشاؤه بواسطته. كما يمكنك رؤية في ملف PDF الناتج، تم تصفية جميع الرسوم البيانية من دفتر العمل.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet.go" >}}
## **تصفية الكائنات أثناء تحميل ورقة العمل**
يقوم الكود المصدري التالي بتحميل [ملف الإكسل الأصلي](5115255.xlsx) ويقوم بتصفية البيانات التالية من ورقات العمل باستخدام تصفية مخصصة.

- يتم تصفية الرسوم البيانية من ورقة العمل التي تحمل اسم لا توجد فيها رسوم بيانية.
- يتم تصفية الأشكال من ورقة العمل التي تحمل اسم لا توجد فيها أشكال.
- يتم تصفية التنسيق الشرطي من ورقة العمل التي تحمل اسم لا توجد فيها تنسيق شرطي.

يقوم بتحميل ملف Excel المصدر (5115255.xlsx) بتصفية مخصصة، ثم يأخذ صور جميع ورقات العمل بشكل تتابع. إليك صور الإخراج للإشارة. كما يمكنك أن ترى، الصورة الأولى ليست تحتوي على رسوم بيانية، الصورة الثانية ليست تحتوي على أشكال، والصورة الثالثة ليست تحتوي على تنسيق شرطي.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet-1.go" >}}
هكذا تستخدم فئة CustomLoadFilter حسب أسماء ورقة العمل.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet-2.go" >}}
