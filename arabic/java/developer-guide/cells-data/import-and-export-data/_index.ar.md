---
title: استيراد وتصدير البيانات
type: docs
weight: 130
url: /ar/java/import-and-export-data/
---

{{% alert color="primary" %}}

يناقش هذا المقال بعض تقنيات استيراد البيانات وتصديرها التي يمتلك المطورون الوصول إليها من خلال Aspose.Cells.

{{% /alert %}}

## استيراد البيانات إلى ورقة العمل

تمثل البيانات العالم كما هي. لفهم البيانات، نقوم بتحليلها وكسب فهم للعالم. تتحول البيانات إلى معلومات.

هناك العديد من الطرق لإجراء التحليل: وضع البيانات في جداول البيانات وتلاعب بها بطرق مختلفة هي طريقة شائعة. مع Aspose.Cells، من السهل إنشاء جداول بيانات تأخذ البيانات من مجموعة متنوعة من المصادر الخارجية وتعدّها للتحليل.

يناقش هذا المقال بعض تقنيات استيراد البيانات التي يحصل عليها المطورون من خلال Aspose.Cells.

### استيراد البيانات باستخدام Aspose.Cells

عند فتح ملف Excel باستخدام Aspose.Cells، يتم استيراد جميع البيانات في الملف تلقائياً. يمكن أيضاً لـ Aspose.Cells استيراد البيانات من مصادر بيانات أخرى:

- [مصفوفة](/cells/ar/java/import-and-export-data/).
- [قائمة الصفائف](/cells/ar/java/import-and-export-data/).
- [مجموعة النتائج](/cells/ar/java/import-and-export-data/).
- [JSON](/cells/ar/java/import-and-export-data/)

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) التي تمثل ملف Excel من مايكروسوفت. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على مجموعة [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) التي تسمح بالوصول إلى كل صفحة عمل في ملف Excel. يتم تمثيل صفحة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). توفر مجموعة [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) طرقا مفيدة جدا لاستيراد البيانات من مصادر بيانات أخرى. يشرح هذا المقال كيفية استخدام هذه الطرق.

#### الاستيراد من صفيف

لتوريد البيانات إلى جدول بيانات من صفيف، ادعوا طريقة importArray في مجموعة [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). هناك العديد من الإصدارات المحملة ضعفيا لطريقة importArray ولكن الإصدار النموذجي يأخذ المعلمات التالية:

- مصفوفة، الكائن مصفوفة الذي تقوم باستيراد المحتوى منه.
- رقم الصف، رقم الصف الذي سيتم استيراد البيانات إليه.
- رقم العمود، رقم العمود الذي سيتم استيراد البيانات إليه.
- هَلْ رأسيّ، قيمة بولية تحدد ما إذا كنت ستقوم استيراد البيانات عموديًا أو أفقيًا.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### الاستيراد من صفائف متعددة الأبعاد

لتوريد البيانات إلى جدول بيانات من صفائف متعددة الأبعاد، ادعوا طريقة importArray المحملة ضعفيا ذات الصلة في مجموعة [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells):

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### الاستيراد من ArrayList

لإدخال البيانات من *ArrayList* إلى أوراق العمل ، يتم استدعاء الأسلوب [**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList-java.util.ArrayList-int-int-boolean-) في مجموعة [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). يستغرق الأسلوب [**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList-java.util.ArrayList-int-int-boolean-) التالية المعلمات التالية:

- **الجمعية**, *ArrayList* الذي سيتم توريد محتوياته.
- **رقم الصف**, رقم الصف الأول لنطاق الخلية من الذي سيتم توريد المحتويات.
- **رقم العمود**, رقم العمود الأول من الذي سيتم توريد البيانات.
- **هل هو عمودي**, قيمة بوليانية تحدد ما إذا كان من المناسب توريد البيانات عموديًا أم أفقيًا.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### الاستيراد من الكائنات المخصصة إلى منطقة مدمجة

لتوريد البيانات من مجموعة من الكائنات إلى صفحة عمل تحتوي على خلايا مدمجة، استخدم خاصية [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells). إذا كان لديك القالب الخاص بإكسل به خلايا مدمجة، ضبط قيمة الخاصية [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells) على صحيح. قم بتمرير كائن [**ImportTableOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions) مع قائمة الأعمدة/الخصائص إلى الطريقة لعرض القائمة المطلوبة من الكائنات الخاصة بك. يُظهر الكود البرمجي التالي استخدام الخاصية [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells) لتوريد البيانات من الكائنات المخصصة إلى الخلايا المدمجة. يُرجى الاطلاع على الملف الإكسل المرفق [المصدر](90112035.xlsx) والملف [إكسل الناتج](90112036.xlsx) للإحالة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### استيراد البيانات من JSON

توفر Aspose.Cells فئة [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) لمعالجة JSON. تحتوي فئة [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) على طريقة [**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData-java.lang.String-com.aspose.cells.Cells-int-int-com.aspose.cells.JsonLayoutOptions-) لاستيراد البيانات ال JSON. كما توفر Aspose.Cells فئة [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) التي تمثل خيارات تخطيط JSON. الطريقة [**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData-java.lang.String-com.aspose.cells.Cells-int-int-com.aspose.cells.JsonLayoutOptions-) تقبل [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) كمعلمة. توفر الفئة [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) الخصائص التالية.

- [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable): يشير ما إذا كان يجب معالجة الصف في مصفوفة كجدول أم لا.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate): يحصل أو يعين قيمة تشير إلى ما إذا كان يجب تحويل السلسلة في JSON إلى رقم أو تاريخ أم لا.
- [**DateFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat): يحصل ويضبط تنسيق قيمة التاريخ.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle): يدل ما إذا كان يتجاهل العنوان في حال كان خصائص الكائن هي مصفوفة.
- [**IgnoreNull**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull): يشير ما إذا كان يجب تجاهل قيمة الـ Null أم لا.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle): يشير ما إذا كان يجب تجاهل العنوان في حال كانت خصائص الكائن هي كائن.
- [**NumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat): يحصل ويضبط تنسيق القيمة الرقمية.
- [**TitleStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle): يحصل ويضبط نمط العنوان.

يلضح الكود النموذجي المعطى أدناه استخدام فئتي [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) و [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) لاستيراد بيانات JSON.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## تصدير بيانات من ورق العمل

تتيح Aspose.Cells لمستخدميها ليس فقط استيراد البيانات إلى أوراق العمل من مصادر بيانات خارجية ولكنها تسمح أيضًا لهم بتصدير بيانات ورق العمل إلى مصفوفة.

### تصدير البيانات باستخدام Aspose.Cells - تصدير البيانات إلى مصفوفة

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)، التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) يسمح بالوصول إلى كل ورق عمل في ملف Excel. يُمثل ورق العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells).

يمكن تصدير البيانات بسهولة إلى كائن مصفوفة باستخدام طريقة [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-) لـ فئة [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells).

#### الأعمدة الحاوية على بيانات مكتوبة بنوعية محددة

تخزن جداول البيانات بيانات كسلسلة من الصفوف والأعمدة. استخدم الطريقة [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-) لتصدير البيانات من ورقة عمل إلى مصفوفة. يأخذ [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-) المعلمات التالية لتصدير بيانات ورقة العمل ككائن *مصفوفة*:

- رقم الصف، رقم الصف الأول الذي سيتم تصدير البيانات منه.
- رقم العمود، رقم العمود الأول حيث سيتم تصدير البيانات منه.
- عدد الصفوف، عدد الصفوف المراد تصديرها.
- عدد الأعمدة، عدد الأعمدة المراد تصديرها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **مواضيع متقدمة**
- [استيراد البيانات من كائن نتائج قاعدة بيانات Microsoft Access إلى ورقة العمل](/cells/ar/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [تحديد حقول الصيغة أثناء استيراد البيانات إلى الورقة العمل](/cells/ar/java/specify-formula-fields-while-importing-data-to-worksheet/)
{{< app/cells/assistant language="java" >}}
