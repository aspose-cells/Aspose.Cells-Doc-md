---
title: تصفية الكائنات أثناء تحميل المصنف أو ورقة العمل
type: docs
weight: 330
url: /ar/net/filter-objects-while-loading-workbook-or-worksheet/
---

## **سيناريوهات الاستخدام المحتملة**
يرجى استخدام خاصية [LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) أثناء تصفية البيانات من دفتر العمل. ولكن إذا كنت ترغب في تصفية البيانات من أوراق العمل الفردية، فسيتعين عليك تجاوز الطريقة [LoadFilter.StartSheet](https://reference.aspose.com/cells/net/aspose.cells/loadfilter/methods/startsheet). يرجى توفير قيمة مناسبة من تعداد [LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) أثناء إنشاء أو العمل مع [LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter).

تحتوي تعداد [LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) على القيم الممكنة التالية.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-FilteringObjects.cs" >}}
## **تصفية الكائنات أثناء تحميل ورقة العمل**
يقوم الكود المصدري التالي بتحميل [ملف الإكسل الأصلي](5115255.xlsx) ويقوم بتصفية البيانات التالية من ورقات العمل باستخدام تصفية مخصصة.

- يتم تصفية الرسوم البيانية من ورقة العمل التي تحمل اسم لا توجد فيها رسوم بيانية.
- يتم تصفية الأشكال من ورقة العمل التي تحمل اسم لا توجد فيها أشكال.
- يتم تصفية التنسيق الشرطي من ورقة العمل التي تحمل اسم لا توجد فيها تنسيق شرطي.

يقوم بتحميل ملف Excel المصدر (5115255.xlsx) بتصفية مخصصة، ثم يأخذ صور جميع ورقات العمل بشكل تتابع. إليك صور الإخراج للإشارة. كما يمكنك أن ترى، الصورة الأولى ليست تحتوي على رسوم بيانية، الصورة الثانية ليست تحتوي على أشكال، والصورة الثالثة ليست تحتوي على تنسيق شرطي.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-1.cs" >}}


هكذا تستخدم فئة CustomLoadFilter حسب أسماء ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-2.cs" >}}
{{< app/cells/assistant language="csharp" >}}
