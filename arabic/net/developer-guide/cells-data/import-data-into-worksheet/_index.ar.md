---
title: استيراد البيانات في صفحة العمل
type: docs
weight: 170
url: /ar/net/import-data-into-worksheet/
description: تعلم كيفية استيراد البيانات في صفحة عمل من خلال Aspose.Cells for .NET واجهة برمجة التطبيقات.
keywords: C# استيراد البيانات في صفحة عمل، استيراد البيانات إلى Excel باستخدام واجهة ICellsDataTable، استيراد البيانات من مصفوفة، استيراد البيانات من ArrayList، استيراد البيانات من كائنات مخصصة، استيراد البيانات من كائنات مخصصة إلى منطقة مدمجة، استيراد البيانات من DataTable، استيراد البيانات من كائن ديناميكي كمصدر بيانات، استيراد البيانات من DataColumn، استيراد البيانات من DataView، استيراد البيانات من DataGrid، استيراد البيانات من GridView، استيراد البيانات المنسقة بتنسيق HTML، استيراد البيانات من JSON
---

{{% alert color="primary" %}}

يناقش هذا المقال بعض تقنيات استيراد البيانات التي يحصل عليها المطورون من خلال Aspose.Cells.

{{% /alert %}}

## **كيفية استيراد البيانات إلى ورقة العمل**

عند فتح ملف Excel بـ Aspose.Cells ، يتم استيراد جميع البيانات في الملف تلقائيًا. يمكن لـ Aspose.Cells أيضًا استيراد البيانات من مصادر بيانات أخرى.

توفر Aspose.Cells فئة تمثل ملف Microsoft Excel. تحتوي الفئة على مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة الفئة. توفر الفئة مجموعة. توفر مجموعة وسائل مفيدة لاستيراد البيانات من مصادر بيانات مختلفة. يشرح هذا المقال كيف يمكن استخدام هذه الأساليب.

## **كيفية استيراد البيانات إلى Excel باستخدام واجهة ICellsDataTable**
نفذ [ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) لتغليف مصادر البيانات المختلفة لديك، ثم استخدم [Cells.ImportData()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) لاستيراد البيانات إلى ورقة العمل في Excel.
### **الكود المثالي**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

يتم تقديم تنفيذ *CustomerDataSource*, *Customer*, و *CustomerList* للفئات أدناه

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


## **كيفية استيراد البيانات إلى Excel من مصفوفة**

لِاستيراد البيانات إلى ورقة العمل من مصفوفة، اُنادي بطريقة [**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) في مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). يوجد العديد من الإصدارات المحملة للدالة [**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) ولكن الشحصة الصارية تأخذ المعاملات التالية:

- مصفوفة، الكائن مصفوفة الذي تقوم باستيراد المحتوى منه.
- رقم الصف، رقم الصف الذي سيتم استيراد البيانات إليه.
- رقم العمود، رقم العمود الذي سيتم استيراد البيانات إليه.
- هَلْ رأسيّ، قيمة بولية تحدد ما إذا كنت ستقوم استيراد البيانات عموديًا أو أفقيًا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

## **كيفية استيراد البيانات إلى Excel من ArrayList**

لِاستيراد البيانات من *ArrayList* إلى ورقات العمل، اُنادي بطريقة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) في مجموعة [**ImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist). تأخذ طريقة ImportArray المعاملات التالية:

- *ArrayList*، تمثل كائن *ArrayList* الذي تقوم بإستيراده.
- رقم الصف، تمثل رقم الصف الأول الذي سيتم استيراد البيانات إليه.
- رقم العمود، تمثل رقم العمود الأول الذي سيتم استيراد البيانات إليه.
- هَلْ رأسيّ، قيمة بولية تحدد ما إذا كنت ستقوم استيراد البيانات عموديًا أو أفقيًا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

## **كيفية استيراد البيانات إلى Excel من الكائنات المخصصة**

للاستيراد البيانات من مجموعة من الكائنات إلى ورقة العمل، استخدم [**ImportCustomObjects**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). قدم قائمة من الأعمدة/الخصائص إلى الطريقة لعرض قائمة الكائنات المرغوبة الخاصة بك.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

## **كيفية استيراد البيانات إلى إكسل من الكائنات المخصصة وفحص منطقة الدمج**

للاستيراد البيانات من مجموعة من الكائنات إلى ورقة العمل التي تحتوي على خلايا مدمجة، استخدم خاصية [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells). إذا كان القالب في إكسل يحتوي على خلايا مدمجة، ضبط قيمة الخاصية [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) على القيمة الصحيحة. قم بتمرير الكائن [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) إلى جانب قائمة الأعمدة/الخصائص إلى الطريقة لعرض قائمة الكائنات المرغوبة الخاصة بك. يوضح الكود العيني التالي استخدام الخاصية [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) لاستيراد البيانات من الكائنات المخصصة إلى الخلايا المدمجة. يرجى الرجوع إلى الملف الإكسل المرفق للمرجعية [source Excel](90112033.xlsx) وملف الإكسل الناتج [output Excel](90112034.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

## **كيفية استيراد البيانات إلى إكسل من DataTable**

للاستيراد البيانات من *DataTable*، اتصل بال [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) الخاص بمجموعة [**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index). هناك العديد من النسخ المتعددة من الطريقة [**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) ولكن النسخة النمطية تأخذ معلمات الدخول التالية:

- **جدول البيانات**، كائن *DataTable* الذي تستورد محتواه منه.
- **هل يتم عرض اسم الحقل**، يحدد ما إذا كانت أسماء أعمدة *DataTable* يجب استيرادها إلى ورقة العمل كصف أول أم لا.
- **خلية البداية**, يمثل اسم الخلية البداية (على سبيل المثال "A1") من حيث يجب استيراد محتويات *DataTable*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

## **كيفية استيراد البيانات إلى إكسل من كائن ديناميكي كمصدر بيانات**

توفر Aspose.Cells ميزات للعمل مع الكائنات الديناميكية كمصدر بيانات. يساعد في استخدام مصدر بيانات حيث يتم إضافة الخصائص بشكل ديناميكي إلى الكائنات. بمجرد إضافة الخصائص إلى الكائن، تعتبر Aspose.Cells الإدخال الأول كالقالب وتتعامل بشكل مناسب مع البقية. يعني إذا تمت إضافة خاصية ديناميكية إلى العنصر الأول فقط وليس إلى الكائنات الأخرى، تعتبر Aspose.Cells أن جميع العناصر في المجموعة يجب أن تكون متماثلة.

في هذا المثال، يتم استخدام نموذج قالب يحتوي في البداية على متغيرين فقط. يتم تحويل هذه القائمة إلى قائمة من الكائنات الديناميكية. ثم يتم إضافة بعض الحقول الإضافية إليها وأخيرا تحميلها في مصنف البيانات. يقوم المصنف بأخذ القيم الخاصة بالقالب XLSX فقط. يستخدم مصنف القالب علامات Smart Markers التي تحتوي أيضا على معلمات. تسمح المعلمات لك بتعديل كيفية تخطيط المعلومات. يمكن الحصول على تفاصيل حول علامات Smart Markers من المقالة التالية:

[استخدام علامات Smart Markers](/cells/ar/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

## **كيفية استيراد DataColumn إلى إكسل**

يتكون كائن *DataTable* أو *DataView* من عمود واحد أو أكثر. يمكن للمطورين أيضًا استيراد البيانات من أي عمود/أعمدة من *DataTable* أو *DataView* عن طريق استدعاء [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) في مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). الطريقة [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) تقبل معلمة من نوع [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions). توفر الفئة [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) خاصية [**ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) تقبل مصفوفة من مؤشرات الأعمدة.

يقدم الكود العيني أدناه استخدام [**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) لاستيراد الأعمدة الانتقائية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

## **كيفية استيراد DataView إلى إكسل**

للاستيراد البيانات من *DataView*، اتصل بال [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) الخاص بمجموعة [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index). هناك العديد من النسخ المتعددة من الطريقة [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) ولكن النسخة لـ DataView تأخذ المعلمات التالية:

- **DataView:** ال *DataView* الذي تعتزم استيراد المحتوى منه.
- **الصف الأول:** رقم الصف الذي سيتم استيراد البيانات إليه.
- **العمود الأول:** رقم العمود الذي سيتم استيراد البيانات إليه.
- **خيارات جدول الاستيراد:** خيارات الاستيراد.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

## **كيفية استيراد DataGrid إلى Excel**

من الممكن استيراد البيانات من *DataGrid* عن طريق استدعاء الأسلوب [**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) في مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). هناك العديد من الإصدارات المتعددة للأسلوب [**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) ولكن الإصدار النمطي يأخذ المعلمات التالية:

- **جدول البيانات**، كائن *DataGrid* الذي تقوم باستيراد المحتوى منه.
- **رقم الصف**، رقم الصف للخلية الأولى التي سيتم استيراد البيانات إليها.
- **رقم العمود**، رقم العمود للخلية الأولى التي سيتم استيراد البيانات إليها.
- **إدراج الصفوف**، خاصية بوليانية تشير ما إذا كان يجب إضافة صفوف إضافية إلى ورقة العمل لتناسب البيانات أم لا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

## **كيفية استيراد GridView إلى Excel**

لتستيراد البيانات من عنصر *GridView*، اِستدعِ [**ImportGridView**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) في مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells).

تسمح Aspose.Cells لنا بالاحترام للقيم المهيئة بتنسيق HTML أثناء استيراد البيانات إلى جدول البيانات. عند تمكين تحليل HTML أثناء استيراد البيانات، يحول Aspose.Cells ال HTML إلى تنسيق الخلية المقابل.

## **كيفية استيراد البيانات المهيئة بتنسيق HTML إلى Excel**

توفر Aspose.Cells فئة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) توفر طرقًا مفيدة جدًا لاستيراد البيانات من مصادر بيانات خارجية. يوضح هذا المقال كيفية تحليل النص المهيئ بتنسيق HTML أثناء استيراد البيانات وتحويل HTML إلى قيم خلية مهيئة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

## **كيفية استيراد البيانات إلى Excel من JSON**

توفر Aspose.Cells فئة [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) لمعالجة JSON. تحتوي فئة [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) على أسلوب [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) لاستيراد بيانات JSON. كما توفر Aspose.Cells أيضًا فئة [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) تمثل خيارات تخطيط JSON. يقبل الأسلوب [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) كمعلمة. توفر الفئة [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) الخصائص التالية.

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): يشير ما إذا كان يجب معالجة الصف في مصفوفة كجدول أم لا.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): يحصل أو يعين قيمة تشير ما إذا كان يجب تحويل السلسلة في JSON إلى رقم أو تاريخ.
- [**DateFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): يحصل ويضبط تنسيق قيمة التاريخ.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): يشير ما إذا كان يجب تجاهل العنوان إذا كانت خاصية الكائن مصفوفة
- [**IgnoreNull**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): يشير ما إذا كان يجب تجاهل قيمة الـ Null أم لا.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): يشير ما إذا كان يجب تجاهل العنوان إذا كانت خاصية الكائن هي كائن.
- [**NumberFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): يحصل ويضبط تنسيق القيمة الرقمية.
- [**TitleStyle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): يحصل ويضبط نمط العنوان.

الكود النموذجي الذي يوضح الاستخدام الأسفل للفئتين [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) و [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) لاستيراد بيانات JSON.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

## **مواضيع متقدمة**
- [تحديد حقول الصيغة أثناء استيراد البيانات إلى الورقة العمل](/cells/ar/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [نقل الصف الأول إلى الأسفل عند إدراج صفوف بيانات الخلايا](/cells/ar/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
