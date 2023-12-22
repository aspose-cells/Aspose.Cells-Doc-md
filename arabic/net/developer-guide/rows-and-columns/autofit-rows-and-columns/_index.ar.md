---
title: الاحتواء التلقائي للصفوف والأعمدة
type: docs
weight: 20
url: /ar/net/autofit-rows-and-columns/
description: توضح هذه المقالة كيفية الاحتواء التلقائي للصفوف والأعمدة وصفوف الخلايا المدمجة والصف في نطاق من الخلايا بواسطة Aspose.Cells for .NET API.
keywords: Autofit rows, autofit columns, autofit row in a range of cells, autofit rows of merged cells
---
{{% alert color="primary" %}}

Microsoft يتيح Excel للمستخدمين ضبط حجم عرض وارتفاع الخلايا تلقائيًا وفقًا لمحتواها. تتوفر هذه الميزة أيضًا من خلال Aspose.Cells حتى يتمكن المطورون من تغيير حجم أبعاد الخلية تلقائيًا في وقت التشغيل.

{{% /alert %}}

##  **تركيب السيارات**

Aspose.Cells يوفر أ[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)فئة تمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)يحتوي الفصل على أ[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فصل. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) يوفر class نطاقًا واسعًا من الخصائص والأساليب لإدارة ورقة العمل. تتناول هذه المقالة استخدام[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)فئة لضبط الصفوف أو الأعمدة تلقائيًا.

###  **صف الاحتواء التلقائي - بسيط**

 الطريقة الأكثر مباشرة لتحديد الحجم التلقائي لعرض الصف وارتفاعه هي استدعاء[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فصل[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) طريقة. ال[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)تأخذ الطريقة فهرس الصف (الصف المراد تغيير حجمه) كمعلمة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

###  **كيفية الاحتواء التلقائي للصف في نطاق Cells**

 يتكون الصف من عدة أعمدة. Aspose.Cells يسمح للمطورين باحتواء الصف تلقائيًا استنادًا إلى المحتوى الموجود في نطاق من الخلايا داخل الصف عن طريق استدعاء إصدار محمّل بشكل زائد من[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)طريقة. يستغرق المعلمات التالية:

- *فهرس الصف**، فهرس الصف الذي سيتم تركيبه تلقائيًا.
- *فهرس العمود الأول**، فهرس العمود الأول من الصف.
- *فهرس العمود الأخير**، فهرس العمود الأخير في الصف.

 ال[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)تتحقق الطريقة من محتويات كافة الأعمدة الموجودة في الصف ثم تقوم باحتواء الصف تلقائيًا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

###  **كيفية الاحتواء التلقائي للعمود في نطاق Cells**

 يتكون العمود من عدة صفوف من الممكن احتواء عمود تلقائيًا استنادًا إلى المحتوى الموجود في نطاق من الخلايا في العمود عن طريق استدعاء إصدار محمّل بشكل زائد من[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)الطريقة التي تأخذ المعلمات التالية:

- *فهرس العمود**، فهرس العمود الذي سيتم تركيبه تلقائيًا.
- *فهرس الصف الأول**، فهرس الصف الأول من العمود.
- *فهرس الصف الأخير**، فهرس الصف الأخير من العمود.

 ال[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)تتحقق الطريقة من محتويات جميع الصفوف في العمود ثم تقوم باحتواء العمود تلقائيًا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

###  **كيفية الاحتواء التلقائي للصفوف المدمجة Cells**

 باستخدام Aspose.Cells، من الممكن ضبط الصفوف تلقائيًا حتى بالنسبة للخلايا التي تم دمجها باستخدام[**خيارات AutoFitter**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API. [**خيارات AutoFitter**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)يوفر الفصل[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) الخاصية التي يمكن استخدامها لضبط الصفوف تلقائيًا للخلايا المدمجة.[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)يقبل[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) enumerable الذي يحتوي على الأعضاء التاليين.

- لا شيء: تجاهل الخلايا المدمجة.
- FirstLine: يقوم بتوسيع ارتفاع الصف الأول فقط.
- LastLine: يقوم بتوسيع ارتفاع الصف الأخير فقط.
- EachLine: يقوم فقط بتوسيع ارتفاع كل صف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

 يمكنك أيضًا محاولة استخدام الإصدارات المحملة بشكل زائد من[**AutoFitRows**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) & [**AutoFitColumns**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) الأساليب التي تقبل نطاقًا من الصفوف/الأعمدة ومثيلًا لها[**خيارات AutoFitter**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) لملاءمة الصفوف/الأعمدة المحددة تلقائيًا مع ما تريد[**خيارات AutoFitter**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)وفقاً لذلك.

التوقيعات على الطرق المذكورة هي كما يلي:

1.  AutoFitRows(int startRow، int endRow،[**خيارات AutoFitter**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)خيارات)
1.  AutoFitColumns (int firstColumn، int lastColumn،[**خيارات AutoFitter**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)خيارات)

{{% /alert %}}

##  **من المهم أن تعرف**

{{% alert color="primary" %}}

إذا تم دمج خلية، فلن يتم تطبيق أساليب الاحتواء التلقائي، وهو نفس السلوك كما في Microsoft Excel. يمكنك التغلب على ذلك باستخدام الفلتر التلقائي API. علاوة على ذلك، إذا كان النص الموجود في الخلية ملتفًا، فإن[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) ولن يتم تطبيق الطريقة أيضًا. شيء آخر تحتاج إلى معرفته هو أن*احتواء تلقائي*الأساليب تستغرق وقتًا طويلاً. لذا، يجب عليك استدعاء هذه الأساليب نادرًا قدر الإمكان لضمان كفاءة تطبيقك.

{{% /alert %}}

##  **مواضيع متقدمة**
- [صفوف الاحتواء التلقائي للدمج Cells](/cells/ar/net/autofit-rows-for-merged-cells/)
