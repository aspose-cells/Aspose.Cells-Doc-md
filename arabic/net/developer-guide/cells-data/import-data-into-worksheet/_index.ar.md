---
title: استيراد البيانات إلى ورقة العمل
type: docs
weight: 170
url: /ar/net/import-data-into-worksheet/
description: تعرف على كيفية استيراد البيانات إلى ورقة العمل من خلال Aspose.Cells for .NET API.
keywords: C# Import Data into Worksheet, Import data into Excel with ICellsDataTable interface, Import data from Array, Import Data from ArrayList, Import Data from Custom Objects, Import Data from Custom Objects to merged area, Import Data from DataTable, Import Data from dynamic object as data source, Import Data from DataColumn, Import Data from DataView, Import Data from DataGrid, Import Data from GridView, Import HTML formatted data, Import Data Data from JSON
---
{{% alert color="primary" %}}

تتناول هذه المقالة بعض تقنيات استيراد البيانات التي يمكن للمطورين الوصول إليها من خلال Aspose.Cells.

{{% /alert %}}

##  **كيفية استيراد البيانات إلى ورقة العمل**

عند فتح ملف Excel بالرقم Aspose.Cells، يتم استيراد جميع البيانات الموجودة في الملف تلقائيًا. يمكن لـ Aspose.Cells أيضًا استيراد البيانات من مصادر البيانات الأخرى.

Aspose.Cells يوفر أ[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)فئة تمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)يحتوي الفصل على أ[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فصل. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) يوفر الفصل أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)مجموعة.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)توفر المجموعة طرقًا مفيدة لاستيراد البيانات من مصادر بيانات مختلفة. تشرح هذه المقالة كيفية استخدام هذه الأساليب.

##  **كيفية استيراد البيانات إلى Excel باستخدام واجهة ICellsDataTable**
 ينفذ[IcellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) لتغليف مصادر البيانات المختلفة، ثم استخدمها[Cells.استيراد البيانات ()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) لاستيراد البيانات إلى ورقة عمل Excel.
###  **عينة من الرموز**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

تنفيذ*CustomerDataSource*، و*Customer*، و*CustomerList* وترد الطبقات أدناه

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


##  **كيفية استيراد البيانات إلى Excel من صفيف**

 لاستيراد البيانات إلى جدول بيانات من مصفوفة، قم باستدعاء[**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)مجموعة. هناك العديد من الإصدارات المحملة بشكل زائد من[**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)الطريقة ولكن التحميل الزائد النموذجي يأخذ المعلمات التالية:

- *Array**، كائن المصفوفة الذي تستورد المحتوى منه.
- *رقم الصف**، رقم صف الخلية الأولى التي سيتم استيراد البيانات إليها.
- *رقم العمود**، رقم عمود الخلية الأولى التي سيتم استيراد البيانات إليها.
- *عمودية**، وهي قيمة منطقية تحدد ما إذا كان سيتم استيراد البيانات رأسيًا أم أفقيًا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

##  **كيفية استيراد البيانات إلى Excel من ArrayList**

 لاستيراد البيانات من*ArrayList* إلى أوراق العمل، اتصل بـ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) المجموعة[**ImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)طريقة. تأخذ طريقة ImportArray المعلمات التالية:

-  *قائمة المصفوفات**، تمثل*ArrayList*الكائن الذي تقوم باستيراده.
- *رقم الصف**، يمثل رقم صف الخلية الأولى التي سيتم استيراد البيانات إليها.
- *رقم العمود**، يمثل رقم عمود الخلية الأولى التي سيتم استيراد البيانات إليها.
- *عمودية**، وهي قيمة منطقية تحدد ما إذا كان سيتم استيراد البيانات رأسيًا أم أفقيًا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

##  **كيفية استيراد البيانات إلى Excel من كائنات مخصصة**

 لاستيراد بيانات من مجموعة كائنات إلى ورقة عمل، استخدم[**ImportCustomObjects**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). قم بتوفير قائمة من الأعمدة/الخصائص للطريقة لعرض قائمة الكائنات المطلوبة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

##  **كيفية استيراد البيانات إلى Excel من الكائنات المخصصة إلى المنطقة المدمجة**

لاستيراد بيانات من مجموعة كائنات إلى ورقة عمل تحتوي على خلايا مدمجة، استخدم[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) ملكية. إذا كان قالب Excel يحتوي على خلايا مدمجة، فقم بتعيين قيمة[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)الملكية إلى صحيح. مرر ال[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) كائن مع قائمة الأعمدة/الخصائص إلى طريقة عرض قائمة الكائنات المطلوبة. يوضح نموذج التعليمات البرمجية التالي استخدام[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) خاصية استيراد البيانات من الكائنات المخصصة إلى الخلايا المدمجة. يرجى الاطلاع على المرفق[المصدر اكسل](90112033.xlsx) الملف و[اكسل الإخراج](90112034.xlsx) ملف للرجوع إليه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

##  **كيفية استيراد البيانات إلى Excel من DataTable**

لاستيراد البيانات من *DataTable*، اتصل بـ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) المجموعة[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) طريقة. هناك العديد من الإصدارات المحملة بشكل زائد من[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)الطريقة ولكن التحميل الزائد النموذجي يأخذ المعلمات التالية:

-  *جدول البيانات**،*جدول البيانات* الكائن الذي تقوم باستيراد المحتوى منه.
-  *هل يظهر اسم الحقل**، يحدد ما إذا كانت أسماء*جدول البيانات*يجب استيراد الأعمدة إلى ورقة العمل كصف أول أم لا.
- *خلية البداية**، تمثل اسم خلية البداية (على سبيل المثال "A1") حيث سيتم استيراد محتويات *DataTable*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

##  **كيفية استيراد البيانات إلى Excel من كائن ديناميكي كمصدر للبيانات**

يوفر Aspose.Cells ميزات للعمل مع الكائنات الديناميكية كمصدر بيانات. يساعد في استخدام مصدر البيانات حيث تتم إضافة الخصائص ديناميكيًا إلى الكائنات. بمجرد إضافة الخصائص إلى الكائن، يعتبر Aspose.Cells الإدخال الأول بمثابة القالب ويتعامل مع الباقي وفقًا لذلك. وهذا يعني أنه إذا تمت إضافة بعض الخصائص الديناميكية إلى العنصر الأول فقط وليس إلى كائنات أخرى، فإن Aspose.Cells يعتبر أن جميع العناصر في المجموعة يجب أن تكون هي نفسها.

في هذا المثال، يتم استخدام نموذج القالب الذي يحتوي في البداية على متغيرين فقط. يتم تحويل هذه القائمة إلى قائمة الكائنات الديناميكية. ثم تتم إضافة بعض الحقول الإضافية إليه ويتم تحميلها أخيرًا في المصنف. يختار المصنف فقط تلك القيم الموجودة في ملف القالب XLSX. يستخدم مصنف القالب هذا العلامات الذكية التي تحتوي أيضًا على معلمات. تسمح لك المعلمات بتعديل كيفية عرض المعلومات. يمكن الحصول على تفاصيل حول العلامات الذكية من المقالة التالية:

[استخدام العلامات الذكية](/cells/ar/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

##  **كيفية استيراد البيانات إلى Excel من DataColumn (.NET)**

A *جدول البيانات*أو*عرض البيانات*يتكون الكائن من عمود واحد أو أكثر. يمكن للمطورين أيضًا استيراد البيانات من أي عمود/أعمدة من الملف*جدول البيانات*أو*عرض البيانات*عن طريق الاتصال ب[**بيانات الاستيراد**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)مجموعة. ال[**بيانات الاستيراد**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)تقبل الطريقة معلمة من النوع[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions). ال[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) يوفر الفصل أ[**فهارس الأعمدة**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)الخاصية التي تقبل مجموعة من فهارس الأعمدة.

يوضح نموذج التعليمات البرمجية الوارد أدناه استخدام[**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)لاستيراد أعمدة انتقائية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

##  **كيفية استيراد البيانات إلى Excel من DataView (.NET)**

 لاستيراد البيانات من *DataView*، اتصل بـ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) المجموعة[**بيانات الاستيراد**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) طريقة. هناك العديد من الإصدارات المحملة بشكل زائد من[**بيانات الاستيراد**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)الطريقة ولكن الطريقة الخاصة بـ DataView تأخذ المعلمات التالية:

- **عرض البيانات:** ال*عرض البيانات*الكائن الذي أنت على وشك استيراد المحتوى منه.
- **السطر الاول:**رقم صف الخلية الأولى التي سيتم استيراد البيانات إليها.
- **العمود الأول:**رقم عمود الخلية الأولى التي سيتم استيراد البيانات إليها.
- **خيارات الاستيراد:**خيارات الاستيراد.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

##  **كيفية استيراد البيانات إلى Excel من DataGrid (.NET)**

 من الممكن استيراد البيانات من*شبكة بيانات* عن طريق الاتصال ب[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)مجموعة. هناك العديد من الإصدارات المحملة بشكل زائد من[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)الطريقة ولكن التحميل الزائد النموذجي يأخذ المعلمات التالية:

-  *شبكة البيانات**،*شبكة بيانات*الكائن الذي تقوم باستيراد المحتوى منه.
- *رقم الصف**، رقم صف الخلية الأولى التي سيتم استيراد البيانات إليها.
- *رقم العمود**، رقم عمود الخلية الأولى التي سيتم استيراد البيانات إليها.
- *إدراج صفوف**، وهي خاصية منطقية تشير إلى ما إذا كان يجب إضافة صفوف إضافية إلى ورقة العمل لملاءمة البيانات أم لا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

##  **كيفية استيراد البيانات إلى Excel من GridView**

 لاستيراد البيانات من أ*عرض شبكي* السيطرة، استدعاء[**استيرادGridView**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)مجموعة.

Aspose.Cells يسمح لنا باحترام HTML القيم المنسقة أثناء استيراد البيانات إلى جدول البيانات. عند تمكين تحليل HTML أثناء استيراد البيانات، يقوم Aspose.Cells بتحويل HTML إلى تنسيق الخلية المقابل.

##  **كيفية استيراد البيانات المنسقة HTML إلى Excel**

 Aspose.Cells يوفر أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)فئة توفر طرقًا مفيدة جدًا لاستيراد البيانات من مصادر البيانات الخارجية. توضح هذه المقالة كيفية تحليل النص المنسق HTML أثناء استيراد البيانات وتحويل HTML إلى قيم خلايا منسقة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

##  **كيفية استيراد البيانات إلى Excel من JSON**

Aspose.Cells يوفر أ[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) فئة المعالجة JSON.[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) فئة لديها[**بيانات الاستيراد**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) طريقة استيراد بيانات JSON. Aspose.Cells يوفر أيضًا أ[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) فئة تمثل خيارات تخطيط JSON. ال[**بيانات الاستيراد**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)يقبل الأسلوب[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)كمعلمة. ال[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)توفر الفئة الخصائص التالية.

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): يشير إلى أنه يجب معالجة المصفوفة كجدول أم لا.
- [**تحويلNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): الحصول على أو تعيين قيمة تشير إلى ما إذا كانت السلسلة الموجودة في JSON سيتم تحويلها إلى رقمية أو تاريخ.
- [**صيغة التاريخ**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): الحصول على تنسيق قيمة التاريخ وتعيينه.
- [**تجاهلArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): يشير إلى ما إذا كان سيتم تجاهل العنوان إذا كانت خاصية الكائن عبارة عن مصفوفة
- [**تجاهلNull**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): يشير إلى ما إذا كان يجب تجاهل القيمة الخالية أم لا.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): يشير إلى ما إذا كان سيتم تجاهل العنوان إذا كانت خاصية الكائن كائنًا.
- [**تنسيق الرقم**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): الحصول على تنسيق القيمة الرقمية وتعيينه.
- [**نمط العنوان**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle):الحصول على نمط العنوان وتعيينه.

يوضح نموذج التعليمات البرمجية الوارد أدناه استخدام[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) و[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)فئات لاستيراد البيانات JSON.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

##  **مواضيع متقدمة**
- [تحديد حقول الصيغة أثناء استيراد البيانات إلى ورقة العمل](/cells/ar/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [قم بإزاحة الصف الأول لأسفل عند إدراج صفوف جدول البيانات Cells](/cells/ar/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
