---
title: استيراد البيانات إلى ورقة العمل
type: docs
weight: 170
url: /ar/net/import-data-into-worksheet/
---
{{% alert color="primary" %}}

تتناول هذه المقالة بعض تقنيات استيراد البيانات التي يمكن للمطورين الوصول إليها من خلال Aspose.Cells.

{{% /alert %}}

## **استيراد البيانات إلى ورقة العمل**

عند فتح ملف Excel باستخدام Aspose.Cells ، يتم استيراد كافة البيانات الموجودة في الملف تلقائيًا. يمكن Aspose.Cells أيضًا استقبال البيانات من مصادر البيانات الأخرى.

يوفر Aspose.Cells أ[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)فئة تمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)مجموعة.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)يوفر التجميع طرقًا مفيدة لاستيراد البيانات من مصادر بيانات مختلفة. تشرح هذه المقالة كيف يمكن استخدام هذه الطرق.

## **استيراد البيانات في Excel بواجهة ICellsDataTable**
 ينفذ[ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) لالتفاف مصادر البيانات المختلفة ، ثم استخدم[Cells. بيانات الاستيراد ()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) لاستيراد البيانات إلى ورقة عمل Excel.
### **عينة من الرموز**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

تنفيذ*CustomerDataSource*, *عميل*، و*قائمة العملاء* يتم إعطاء الفئات أدناه

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


## **الاستيراد من Array**

 لاستيراد البيانات إلى جدول بيانات من مصفوفة ، قم باستدعاء[**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. هناك العديد من الإصدارات المحملة بشكل زائد من[**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)طريقة ولكن الحمل الزائد النموذجي يأخذ المعلمات التالية:

- **مجموعة مصفوفة**، كائن المصفوفة الذي تقوم باستيراد المحتوى منه.
- **رقم الصف**، رقم صف الخلية الأولى التي سيتم استيراد البيانات إليها.
- **رقم العمود**، رقم عمود الخلية الأولى التي سيتم استيراد البيانات إليها.
- **عمودي**، قيمة منطقية تحدد ما إذا كان سيتم استيراد البيانات رأسيًا أو أفقيًا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

## **الاستيراد من ArrayList**

 لاستيراد البيانات من ملف*ArrayList* لأوراق العمل ، اتصل بـ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) المجموعة[**ImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)طريقة. تأخذ طريقة ImportArray المعلمات التالية:

- **قائمة الصفيف** ، يمثل*ArrayList*الكائن الذي تقوم باستيراده.
- **رقم الصف**، يمثل رقم صف الخلية الأولى التي سيتم استيراد البيانات إليها.
- **رقم العمود**، يمثل رقم عمود الخلية الأولى التي سيتم استيراد البيانات إليها.
- **عمودي**، قيمة منطقية تحدد ما إذا كان سيتم استيراد البيانات رأسيًا أو أفقيًا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

## **الاستيراد من كائنات مخصصة**

 لاستيراد البيانات من مجموعة كائنات إلى ورقة عمل ، استخدم[**ImportCustomObjects**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). قم بتوفير قائمة بالأعمدة / الخصائص للطريقة لعرض قائمة الكائنات التي تريدها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

## **الاستيراد من كائنات مخصصة إلى منطقة مدمجة**

لاستيراد بيانات من مجموعة كائنات إلى ورقة عمل تحتوي على خلايا مدمجة ، استخدم[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) خاصية. إذا كان قالب Excel يحتوي على خلايا مدمجة ، فقم بتعيين قيمة[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)الملكية على صواب. مرر ال[**خيارات ImportTable**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) كائن مع قائمة الأعمدة / الخصائص لطريقة عرض قائمة الكائنات التي تريدها. يوضح نموذج التعليمات البرمجية التالي استخدام[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) لاستيراد البيانات من الكائنات المخصصة إلى الخلايا المدمجة. يرجى الاطلاع على المرفق[مصدر Excel](90112033.xlsx) ملف و[الإخراج إكسل](90112034.xlsx) ملف كمرجع.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

## **الاستيراد من DataTable**

 لاستيراد البيانات من ملف*جدول البيانات* ، اتصل ب[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) المجموعة[**إيمبورداتاتابلي**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) طريقة. هناك العديد من الإصدارات المحملة بشكل زائد من[**إيمبورداتاتابلي**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)طريقة ولكن الحمل الزائد النموذجي يأخذ المعلمات التالية:

- **جدول البيانات** ، ال*جدول البيانات* الكائن الذي تقوم باستيراد المحتوى منه.
- **هو اسم الحقل المعروض** ، يحدد ما إذا كانت أسماء ملفات*جدول البيانات*يجب استيراد الأعمدة إلى ورقة العمل كصف أول أم لا.
- **خلية البداية** ، يمثل اسم خلية البداية (على سبيل المثال "A1") من مكان استيراد محتويات ملف*جدول البيانات*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

## **الاستيراد من كائن ديناميكي كمصدر بيانات**

يوفر Aspose.Cells ميزات للعمل مع العناصر الديناميكية كمصدر بيانات. يساعد في استخدام مصدر البيانات حيث تتم إضافة الخصائص ديناميكيًا إلى الكائنات. بمجرد إضافة الخصائص إلى العنصر ، يعتبر Aspose.Cells الإدخال الأول كقالب ويتعامل مع الباقي وفقًا لذلك. هذا يعني أنه إذا تمت إضافة بعض الخصائص الديناميكية إلى عنصر أول فقط وليس إلى كائنات أخرى ، فإن Aspose.Cells يعتبر أن جميع العناصر في المجموعة يجب أن تكون متطابقة.

في هذا المثال ، يتم استخدام نموذج نموذج يحتوي مبدئيًا على متغيرين فقط. يتم تحويل هذه القائمة إلى قائمة الكائنات الديناميكية. ثم يتم إضافة بعض الحقول الإضافية إليه وتحميله أخيرًا في المصنف. يختار المصنف القيم الموجودة في ملف القالب XLSX فقط. يستخدم مصنف القالب هذا العلامات الذكية التي تحتوي أيضًا على معلمات. تسمح لك المعلمات بتعديل كيفية وضع المعلومات. يمكن الحصول على تفاصيل حول العلامات الذكية من المقالة التالية:

[استخدام العلامات الذكية](/cells/ar/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

## **الاستيراد من DataColumn (.NET)**

أ*جدول البيانات*أو*عرض البيانات*يتكون الكائن من عمود واحد أو أكثر. يمكن للمطورين أيضًا استيراد البيانات من أي عمود / أعمدة في*جدول البيانات*أو*عرض البيانات*من خلال استدعاء[**بيانات الاستيراد**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)مجموعة. ال[**بيانات الاستيراد**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)الأسلوب يقبل معلمة من النوع[**خيارات ImportTable**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions). ال[**خيارات ImportTable**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) فئة توفر أ[**العمود الفهارس**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)الخاصية التي تقبل مصفوفة من فهارس الأعمدة.

يوضح نموذج التعليمات البرمجية الوارد أدناه استخدام[**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) لاستيراد الأعمدة الانتقائية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

## **الاستيراد من DataView (.NET)**

 لاستيراد البيانات من ملف*عرض البيانات* ، اتصل ب[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) المجموعة[**بيانات الاستيراد**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) طريقة. هناك العديد من الإصدارات المحملة بشكل زائد من[**بيانات الاستيراد**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)الطريقة ولكن طريقة DataView تأخذ المعلمات التالية:

- **عرض البيانات:** ال*عرض البيانات*الذي أنت على وشك استيراد المحتوى منه.
- **السطر الاول:**رقم صف الخلية الأولى التي سيتم استيراد البيانات إليها.
- **العمود الأول:**رقم عمود الخلية الأولى التي سيتم استيراد البيانات إليها.
- **خيارات ImportTable:**خيارات الاستيراد.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

## **الاستيراد من DataGrid (.NET)**

 من الممكن استيراد البيانات من ملف*شبكة بيانات* من خلال استدعاء[**إيمبورداتاتجريد**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. هناك العديد من الإصدارات المحملة بشكل زائد من[**إيمبورداتاتجريد**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)طريقة ولكن الحمل الزائد النموذجي يأخذ المعلمات التالية:

- **شبكة بيانات** ، ال*شبكة بيانات*الذي تقوم باستيراد المحتوى منه.
- **رقم الصف**، رقم صف الخلية الأولى التي سيتم استيراد البيانات إليها.
- **رقم العمود**، رقم عمود الخلية الأولى التي سيتم استيراد البيانات إليها.
- **إدراج صفوف**، خاصية منطقية تشير إلى ما إذا كان يجب إضافة صفوف إضافية إلى ورقة العمل لاحتواء البيانات أم لا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

## **الاستيراد من GridView**

 لاستيراد البيانات من ملف*عرض شبكي* السيطرة ، استدعاء[**إيمبورتجريدفيو**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)مجموعة.

Aspose.Cells يسمح لنا باحترام HTML القيم المنسقة أثناء استيراد البيانات إلى جدول البيانات. عند اتاحة التوزيع HTML أثناء استيراد البيانات ، يقوم Aspose.Cells بتحويل HTML إلى تنسيق الخلية المقابل.

## **استيراد HTML بيانات منسقة**

 يوفر Aspose.Cells أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)فئة توفر طرقًا مفيدة للغاية لاستيراد البيانات من مصادر البيانات الخارجية. يوضح هذا المقال كيفية تحليل HTML نص منسق أثناء استيراد البيانات وتحويل HTML إلى قيم خلية منسقة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

## **استيراد البيانات من JSON**

يوفر Aspose.Cells أ[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) فئة المعالجة JSON.[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) الصف لديه[**بيانات الاستيراد**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) طريقة لاستيراد بيانات JSON. يوفر Aspose.Cells أيضًا أ[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) فئة تمثل خيارات تخطيط JSON. ال[**بيانات الاستيراد**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)طريقة تقبل[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)كمعامل. ال[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)فئة توفر الخصائص التالية.

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): يجب معالجة الإشارات في المصفوفة كجدول أم لا.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): الحصول على أو تحديد قيمة تشير إلى ما إذا كان سيتم تحويل السلسلة في JSON إلى رقم أو تاريخ.
- [**صيغة التاريخ**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): الحصول على تنسيق قيمة التاريخ وتعيينه.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): يشير إلى ما إذا كان سيتم تجاهل العنوان إذا كانت خاصية الكائن عبارة عن مصفوفة
- [**تجاهل**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): يشير إلى ما إذا كان يجب تجاهل القيمة الخالية أم لا.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): يشير إلى ما إذا كان سيتم تجاهل العنوان إذا كانت خاصية الكائن هي كائن.
- [**رقم**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): الحصول على تنسيق القيمة الرقمية وتعيينه.
- [**العنوان**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): الحصول على نمط العنوان وتحديده.

يوضح نموذج التعليمة البرمجية أدناه استخدام ملحق[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) و[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) فئات لاستيراد JSON البيانات.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

## **موضوعات مسبقة**
- [حدد حقول الصيغة أثناء استيراد البيانات إلى ورقة العمل](/cells/ar/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [نقل الصف الأول لأسفل عند ادخال Cells صفوف جدول البيانات](/cells/ar/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
