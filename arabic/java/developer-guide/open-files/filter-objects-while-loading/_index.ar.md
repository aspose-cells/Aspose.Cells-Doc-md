---
title: تصفية الكائنات أثناء تحميل المصنف أو ورقة العمل
type: docs
weight: 1060
url: /ar/java/filter-objects-while-loading-workbook-or-worksheet/
---

## **سيناريوهات الاستخدام المحتملة**
يرجى استخدام خاصية [LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter) أثناء تصفية البيانات من دفتر العمل. ولكن إذا كنت ترغب في تصفية البيانات من أوراق العمل الفردية، فيجب عليك تجاوز خاصية [LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet\(com.aspose.cells.Worksheet\)) . يُرجى تقديم القيمة المناسبة من تعداد [LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) أثناء الإنشاء أو العمل مع [LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter).

تعداد [LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) يحتوي على القيم التالية.

- [بلا](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [الكل](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [خلية فارغة](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BLANK)
- [نص الخلية](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_STRING)
- [القيمة الرقمية للخلية](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_NUMERIC)
- [خطأ الخلية](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_ERROR)
- [قيمة منطقية للخلية](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BOOL)
- [قيمة الخلية](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_VALUE)
- [صيغة](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [بيانات الخلية](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_DATA)
- [رسم بياني](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [شكل](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [منطقة مدموجة](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED_AREA)
- [تنسيق مشروط](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL_FORMATTING)
- [التحقق من البيانات](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA_VALIDATION)
- [جدول محوري](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT_TABLE)
- [جدول](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
- [روابط تشعبية](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#HYPERLINKS)
- [إعدادات الورقة](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_SETTINGS)
- [بيانات الورقة](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_DATA)
- [إعدادات الكتاب](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#BOOK_SETTINGS)
- [الإعدادات](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SETTINGS)
- [خريطة XML](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#XML_MAP)
- [الهيكل](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STRUCTURE)
- [خصائص المستند](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DOCUMENT_PROPERTIES)
- [الأسماء المحددة](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)
- [VBA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#VBA)
- [النمط](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STYLE)
## **كائنات تصفية أثناء تحميل السجل**
يوضح الكود النموذجي التالي كيفية تصفية الرسوم البيانية من السجل. يرجى التحقق من [ملف Excel النموذجي](5472489.xlsx) المستخدم في هذا الكود و[ملف الـPDF الناتج](5472488.pdf) عن طريقه. كما يمكنك رؤية في ملف الـPDF الناتج أن جميع الرسوم البيانية قد تم تصفيتها من السجل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **كائنات تصفية أثناء تحميل ورقة العمل**
يقوم الكود النموذجي التالي بتحميل [ملف الـExcel المصدري](5472492.xlsx) وتصفية البيانات التالية من صفحات العمل باستخدام عملية تصفية مخصصة.

- يتم تصفية الرسوم البيانية من ورقة العمل التي تحمل اسم لا توجد فيها رسوم بيانية.
- يتم تصفية الأشكال من ورقة العمل التي تحمل اسم لا توجد فيها أشكال.
- يتم تصفية التنسيق الشرطي من ورقة العمل التي تحمل اسم لا توجد فيها تنسيق شرطي.

بمجرد أن يتم تحميل [ملف الـExcel المصدري](5472492.xlsx) بتصفية مخصصة، يتم أخذ صور كل صفحات العمل واحدة تلو الأخرى. فيما يلي الصور الناتجة للرجوع إليها. كما يمكنك أن ترى، الصورة الأولى ليست بها رسوم بيانية، الصورة الثانية ليست بها أشكال، والصورة الثالثة ليست بها تنسيق شرطي.

- [NoCharts.png](5472493.png)
- [NoShapes.png](5472491.png)
- [NoConditionalFormatting.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}
