---
title: تصفية الكائنات أثناء تحميل المصنف أو ورقة العمل
type: docs
weight: 330
url: /ar/python-net/filter-objects-while-loading-workbook-or-worksheet/
---

## **سيناريوهات الاستخدام المحتملة**
يرجى استخدام خاصية [LoadOptions.load_filter](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) أثناء تصفية البيانات من ملف العمل. وإذا أردت تصفية البيانات من أوراق عمل فردية، فسيتعين عليك تجاوز طريقة [LoadFilter.start_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter/start_sheet). يرجى تقديم قيمة مناسبة من تعداد [LoadDataFilterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) أثناء إنشاء أو العمل مع [LoadFilter](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter).

تحتوي [LoadDataFilterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) على القيم المحتملة التالية.

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilteringObjectsAtLoadTime-FilteringObjects.py" >}}

{{< app/cells/assistant language="python-net" >}}
