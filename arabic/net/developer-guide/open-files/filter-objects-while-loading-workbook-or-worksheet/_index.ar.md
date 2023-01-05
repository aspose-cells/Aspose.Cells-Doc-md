---
title: تصفية الكائنات أثناء تحميل المصنف أو ورقة العمل
type: docs
weight: 330
url: /ar/net/filter-objects-while-loading-workbook-or-worksheet/
---
## **سيناريوهات الاستخدام الممكنة**
الرجاء استخدام[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)الخاصية أثناء تصفية البيانات من المصنف. ولكن إذا كنت ترغب في تصفية البيانات من أوراق العمل الفردية ، فسيتعين عليك تجاوز[LoadFilter.StartSheet](https://reference.aspose.com/cells/net/aspose.cells/loadfilter/methods/startsheet)طريقة. يرجى تقديم قيمة مناسبة من[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)التعداد أثناء الإنشاء أو العمل مع[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter).

 ال[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)التعداد لديه القيم المحتملة التالية.

- الجميع
- BookSettings
- سيل بلانك
- CellBool
- CellData
- CellError
- رقم الخلية
- CellString
- CellValue
- جدول
- تنسيق مشروط
- تأكيد صحة البيانات
- الأسماء المعرفة
- خصائص المستند
- معادلة
- الارتباطات التشعبية
- منطقة مدمجة
- جدول محوري
- إعدادات
- شكل
- شيتداتا
- SheetSettings
- بنية
- أسلوب
- الطاولة
- VBA
- XmlMap
## **تصفية الكائنات أثناء تحميل المصنف**
 يوضح نموذج التعليمات البرمجية التالي كيفية تصفية المخططات من المصنف. رجاء تاكد من[نموذج ملف اكسل](5115258.xlsx) المستخدمة في هذا الرمز و[الإخراج PDF](5115257.pdf)ولدت به. كما ترى في الإخراج PDF ، تمت تصفية كافة المخططات من المصنف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-FilteringObjects.cs" >}}
## **تصفية الكائنات أثناء تحميل ورقة العمل**
 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[ملف اكسل المصدر](5115255.xlsx) وتصفية البيانات التالية من أوراق العمل الخاصة بها باستخدام مرشح مخصص.

- يقوم بتصفية المخططات من ورقة العمل المسماة NoCharts.
- يقوم بتصفية الأشكال من ورقة العمل المسماة NoShapes.
- يقوم بتصفية التنسيق الشرطي من ورقة العمل المسماة NoConditionalFormatting.

 مرة واحدة ، يتم تحميل ملف[ملف اكسل المصدر](5115255.xlsx) باستخدام مرشح مخصص ، فإنه يأخذ صور جميع أوراق العمل واحدة تلو الأخرى. ها هي الصور الناتجة للرجوع اليها. كما ترى ، لا تحتوي الصورة الأولى على مخططات ، ولا تحتوي الصورة الثانية على أشكال ، ولا تحتوي الصورة الثالثة على تنسيق شرطي.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-1.cs" >}}


هذه هي طريقة استخدام فئة CustomLoadFilter وفقًا لأسماء ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-2.cs" >}}
