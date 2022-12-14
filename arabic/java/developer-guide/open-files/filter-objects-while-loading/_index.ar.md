---
title: تصفية الكائنات أثناء تحميل المصنف أو ورقة العمل
type: docs
weight: 1060
url: /ar/java/filter-objects-while-loading-workbook-or-worksheet/
---
## **سيناريوهات الاستخدام الممكنة**
 يرجى استخدام[LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter) الخاصية أثناء تصفية البيانات من المصنف. ولكن إذا كنت ترغب في تصفية البيانات من أوراق العمل الفردية ، فسيتعين عليك تجاوز[LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet\(com.aspose.cells.Worksheet\) ) طريقة. يرجى تقديم القيمة المناسبة من[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) التعداد أثناء الإنشاء أو العمل مع[LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter).

 ال[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions)التعداد له القيم التالية.

- [لا أحد](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [الكل](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [CELL_BLANK](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BLANK)
- [CELL_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_STRING)
- [CELL_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_NUMERIC)
- [CELL_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_ERROR)
- [CELL_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BOOL)
- [CELL_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_VALUE)
- [معادلة](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [CELL_DATA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_DATA)
- [جدول](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [شكل](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [MERGED_AREA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED_AREA)
- [تنسيق مشروط](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL_FORMATTING)
- [تأكيد صحة البيانات](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA_VALIDATION)
- [جدول محوري](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT_TABLE)
- [الطاولة](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
- [روابط تشعبية](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#HYPERLINKS)
- [SHEET_SETTINGS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_SETTINGS)
- [SHEET_DATA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_DATA)
- [BOOK_SETTINGS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#BOOK_SETTINGS)
- [الإعدادات](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SETTINGS)
- [XML_MAP](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#XML_MAP)
- [بنية](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STRUCTURE)
- [خصائص المستند](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DOCUMENT_PROPERTIES)
- [DEFINED_NAMES](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)
- [VBA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#VBA)
- [نمط](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STYLE)
## **تصفية الكائنات أثناء تحميل المصنف**
 يوضح نموذج التعليمات البرمجية التالي كيفية تصفية المخططات من المصنف. رجاء تاكد من[نموذج ملف اكسل](5472489.xlsx) المستخدمة في هذا الرمز و[إخراج PDF](5472488.pdf)ولدت به. كما ترى في ملف PDF الناتج ، تمت تصفية جميع المخططات من المصنف.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **تصفية الكائنات أثناء تحميل ورقة العمل**
 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[ملف اكسل المصدر](5472492.xlsx) وتصفية البيانات التالية من أوراق العمل الخاصة بها باستخدام مرشح مخصص.

- يقوم بتصفية المخططات من ورقة العمل المسماة NoCharts.
- يقوم بتصفية الأشكال من ورقة العمل المسماة NoShapes.
- يقوم بتصفية التنسيق الشرطي من ورقة العمل المسماة NoConditionalFormatting.

 مرة واحدة ، يتم تحميل ملف[ملف اكسل المصدر](5472492.xlsx) باستخدام مرشح مخصص ، فإنه يأخذ صور جميع أوراق العمل واحدة تلو الأخرى. ها هي الصور الناتجة للرجوع اليها. كما ترى ، لا تحتوي الصورة الأولى على مخططات ، ولا تحتوي الصورة الثانية على أشكال ، ولا تحتوي الصورة الثالثة على تنسيق شرطي.

- [NoCharts.png](5472493.png)
- [NoShapes.png](5472491.png)
- [NoConditionalFormatting.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}
