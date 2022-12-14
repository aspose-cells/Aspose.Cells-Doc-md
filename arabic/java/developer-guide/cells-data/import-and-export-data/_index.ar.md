---
title: استيراد وتصدير البيانات
type: docs
weight: 130
url: /ar/java/import-and-export-data/
---
{{% alert color="primary" %}}

تتناول هذه المقالة بعض تقنيات استيراد وتصدير البيانات التي يمكن للمطورين الوصول إليها من خلال Aspose.Cells.

{{% /alert %}}

## استيراد البيانات إلى ورقة العمل

البيانات تمثل العالم كما هو. لفهم البيانات ، نقوم بتحليلها وفهم العالم. تتحول البيانات إلى معلومات.

هناك العديد من الطرق لإجراء التحليل: يعد وضع البيانات في جداول البيانات ومعالجتها بطرق مختلفة إحدى الطرق الشائعة. مع Aspose.Cells ، من السهل إنشاء جداول بيانات تأخذ البيانات من مجموعة من المصادر الخارجية وتجهزها للتحليل.

تتناول هذه المقالة بعض تقنيات استيراد البيانات التي يمكن للمطورين الوصول إليها من خلال Aspose.Cells.

### استيراد البيانات باستخدام Aspose.Cells

عند فتح ملف Excel باستخدام Aspose.Cells ، يتم استيراد كافة البيانات الموجودة في الملف تلقائيًا. يمكن Aspose.Cells أيضًا استيراد البيانات من مصادر البيانات الأخرى:

- [مجموعة مصفوفة](/cells/ar/java/import-and-export-data/).
- [قائمة الصفيف](/cells/ar/java/import-and-export-data/).
- [مجموعة النتائج](/cells/ar/java/import-and-export-data/).
- [جسون](/cells/ar/java/import-and-export-data/)

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على المجموعة[**ورقة العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) مما يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) مجموعة.[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)يوفر التجميع طرقًا مفيدة للغاية لاستيراد البيانات من مصادر البيانات الأخرى. تشرح هذه المقالة كيف يمكن استخدام هذه الطرق.

#### الاستيراد من Array

 لاستيراد البيانات إلى جدول بيانات من مصفوفة ، قم باستدعاء طريقة importArray الخاصة بامتداد[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)مجموعة. هناك العديد من الإصدارات المحملة بشكل زائد من طريقة importArray ولكن الحمل الزائد النموذجي يأخذ المعلمات التالية:

- **مجموعة مصفوفة**، كائن المصفوفة الذي تقوم باستيراد المحتوى منه.
- **رقم الصف**، رقم صف الخلية الأولى التي سيتم استيراد البيانات إليها.
- **رقم العمود**، رقم عمود الخلية الأولى التي سيتم استيراد البيانات إليها.
- **عمودي**، قيمة منطقية تحدد ما إذا كان سيتم استيراد البيانات رأسيًا أو أفقيًا.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### الاستيراد من المصفوفات متعددة الأبعاد

 لاستيراد البيانات إلى جدول بيانات من مصفوفات متعددة الأبعاد ، قم باستدعاء importArray ذي الصلة الزائد من ملف[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)مجموعة:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### الاستيراد من ArrayList

 لاستيراد البيانات من ملف*ArrayList* لأوراق العمل ، اتصل بـ[**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean) ) طريقة ال[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) مجموعة. ال[**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean)) تأخذ الطريقة المعلمات التالية:

- **ArrayList** ، ال*ArrayList*الكائن الذي سيتم استيراد محتوياته.
- **رقم الصف**، رقم صف الخلية الأولى في نطاق الخلايا الذي سيتم استيراد المحتويات منه.
- **رقم العمود**، رقم عمود الخلية الأولى التي سيتم استيراد البيانات منها.
- **عمودي**، هي قيمة منطقية تحدد ما إذا كان سيتم استيراد البيانات عموديًا أو أفقيًا.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### الاستيراد من كائنات مخصصة إلى منطقة مدمجة

لاستيراد بيانات من مجموعة كائنات إلى ورقة عمل تحتوي على خلايا مدمجة ، استخدم[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)منشأه. إذا كان قالب Excel يحتوي على خلايا مدمجة ، فقم بتعيين قيمة[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)الملكية على صواب. مرر ال[**خيارات ImportTable**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions)كائن مع قائمة الأعمدة / الخصائص لطريقة عرض قائمة الكائنات التي تريدها. يوضح نموذج التعليمات البرمجية التالي استخدام[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)لاستيراد البيانات من الكائنات المخصصة إلى الخلايا المدمجة. يرجى الاطلاع على المرفق[مصدر Excel](90112035.xlsx)ملف و[الإخراج إكسل](90112036.xlsx)ملف كمرجع.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### استيراد البيانات من JSON

 يوفر Aspose.Cells أ[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) فئة لمعالجة JSON.[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) الصف لديه[**بيانات الاستيراد**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions) ) طريقة لاستيراد بيانات JSON. يوفر Aspose.Cells أيضًا أ[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)فئة تمثل خيارات تخطيط JSON. ال[**بيانات الاستيراد**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions) ) طريقة تقبل[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) كمعامل. ال[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) فئة توفر الخصائص التالية.

- [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable): يجب معالجة الإشارات في المصفوفة كجدول أم لا.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate): الحصول على أو تعيين قيمة تشير إلى ما إذا كان سيتم تحويل السلسلة في JSON إلى رقم أو تاريخ.
- [**صيغة التاريخ**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat): الحصول على تنسيق قيمة التاريخ وتعيينه.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle): يشير إلى ما إذا كان سيتم تجاهل العنوان إذا كانت خاصية الكائن عبارة عن مصفوفة
- [**تجاهل**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull): يشير إلى ما إذا كان يجب تجاهل القيمة الخالية أم لا.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle): يشير إلى ما إذا كان سيتم تجاهل العنوان إذا كانت خاصية الكائن هي كائن.
- [**رقم**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat): الحصول على تنسيق القيمة الرقمية وتعيينه.
- [**العنوان**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle): الحصول على نمط العنوان وتحديده.

 يوضح نموذج التعليمة البرمجية أدناه استخدام ملحق[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) و[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) فئات لاستيراد بيانات JSON.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## تصدير البيانات من ورقة العمل

لا يتيح Aspose.Cells لمستخدميه استيراد البيانات إلى أوراق العمل من مصادر البيانات الخارجية فحسب ، بل يسمح لهم أيضًا بتصدير بيانات ورقة العمل إلى مصفوفة.

### تصدير البيانات باستخدام Aspose.Cells - تصدير البيانات إلى المصفوفة

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على[**ورقة العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) مجموعة.

 يمكن بسهولة تصدير البيانات إلى كائن Array باستخدام امتداد[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) صف دراسي'[**تصدير**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)) طريقة.

#### الأعمدة التي تحتوي على بيانات مكتوبة بقوة

 تخزن جداول البيانات البيانات كتسلسل من الصفوف والأعمدة. استخدم ال[**تصدير**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) ) لتصدير البيانات من ورقة عمل إلى مصفوفة.[**تصدير**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) ) يأخذ المعلمات التالية لتصدير بيانات ورقة العمل كملف*مجموعة مصفوفة* هدف:

- رقم الصف ، رقم صف الخلية الأولى التي سيتم تصدير البيانات منها.
- رقم العمود ، رقم العمود للخلية الأولى التي سيتم تصدير البيانات منها
- عدد الصفوف ، عدد الصفوف المراد تصديرها.
- عدد الأعمدة ، عدد الأعمدة المراد تصديرها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **موضوعات مسبقة**
- [استيراد البيانات من Microsoft Access Database ResultSet Object إلى ورقة العمل](/cells/ar/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [حدد حقول الصيغة أثناء استيراد البيانات إلى ورقة العمل](/cells/ar/java/specify-formula-fields-while-importing-data-to-worksheet/)
