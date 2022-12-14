---
title: احتواء تلقائي للصفوف والأعمدة
type: docs
weight: 20
url: /ar/net/autofit-rows-and-columns/
---
{{% alert color="primary" %}}

Microsoft يسمح Excel للمستخدمين تلقائيًا بتغيير حجم عرض الخلايا وارتفاعها وفقًا لمحتواها. تتوفر هذه الميزة أيضًا من خلال Aspose.Cells بحيث يمكن للمطورين تغيير حجم أبعاد الخلية تلقائيًا في وقت التشغيل.

{{% /alert %}}

## **تركيب تلقائي**

يوفر Aspose.Cells أ[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)فئة تمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) توفر class مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. تبحث هذه المقالة في استخدام[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)فئة للاحتواء التلقائي للصفوف أو الأعمدة.

### **صف الاحتواء التلقائي - بسيط**

 تتمثل الطريقة الأكثر مباشرة في تغيير حجم عرض الصف وارتفاعه تلقائيًا في استدعاء[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) طريقة. ال[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)تأخذ الطريقة فهرس الصف (للصف الذي سيتم تغيير حجمه) كمعامل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **صف الاحتواء التلقائي في نطاق Cells**

 يتكون الصف من عدة أعمدة. يسمح Aspose.Cells للمطورين بملاءمة صف تلقائيًا استنادًا إلى المحتوى في نطاق من الخلايا داخل الصف عن طريق استدعاء نسخة محملة بشكل زائد من[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)طريقة. يأخذ المعلمات التالية:

- **فهرس الصف**، فهرس الصف الذي سيتم تركيبه تلقائيًا.
- **فهرس العمود الأول**، فهرس العمود الأول للصف.
- **فهرس العمود الأخير**، فهرس العمود الأخير للصف.

 ال[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)يتحقق الأسلوب من محتويات جميع الأعمدة في الصف ثم يقوم تلقائيًا بملاءمة الصف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **عمود الاحتواء التلقائي في نطاق Cells**

 يتكون العمود من عدة صفوف. من الممكن أن يتم احتواء عمود تلقائيًا استنادًا إلى المحتوى الموجود في نطاق من الخلايا في العمود عن طريق استدعاء نسخة محملة بشكل زائد من[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)الطريقة التي تأخذ المعلمات التالية:

- **فهرس العمود**، فهرس العمود الذي على وشك أن يتم تركيبه تلقائيًا.
- **فهرس الصف الأول**، فهرس الصف الأول للعمود.
- **فهرس الصف الأخير**، فهرس الصف الأخير للعمود.

 ال[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)يتحقق الأسلوب من محتويات جميع الصفوف في العمود ثم يقوم تلقائيًا بملاءمة العمود.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **صفوف AutoFit للدمج Cells**

 مع Aspose.Cells ، من الممكن احتواء الصفوف تلقائيًا حتى للخلايا التي تم دمجها باستخدام[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API. [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)فئة تقدم[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) الخاصية التي يمكن استخدامها للاحتواء التلقائي للصفوف للخلايا المدمجة.[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)يقبل[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) معدود يضم الأعضاء التالية أسماؤهم.

- بلا: تجاهل الخلايا المدمجة.
- FirstLine: يوسع ارتفاع الصف الأول فقط.
- LastLine: يوسع ارتفاع الصف الأخير فقط.
- EveryLine: يوسع فقط ارتفاع كل صف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

 يمكنك أيضًا محاولة استخدام الإصدارات المحملة بشكل زائد من[**AutoFitRows**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) & [**الأعمدة التلقائية**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) الطرق التي تقبل نطاقًا من الصفوف / الأعمدة ومثيلًا لـ[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) لملاءمة الصفوف / الأعمدة المحددة تلقائيًا مع ما تريده[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)وفقاً لذلك.

تواقيع الطرق المذكورة هي كما يلي:

1.  AutoFitRows (int startRow، int endRow،[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)والخيارات)
1. AutoFitColumns (int firstColumn ، int lastColumn ،[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)والخيارات)

{{% /alert %}}

## **من المهم أن تعرف**

{{% alert color="primary" %}}

 إذا تم دمج خلية ، فلن يتم تطبيق أساليب الاحتواء التلقائي ، وهو نفس السلوك كما في Microsoft Excel. يمكنك التغلب على هذا باستخدام المرشح التلقائي API. علاوة على ذلك ، إذا تم التفاف النص في الخلية ،[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) لن يتم تطبيق الطريقة أيضًا. شيء آخر تحتاج إلى معرفته هو أن ملف*احتواء تلقائي*الأساليب تستغرق وقتًا طويلاً. لذلك ، يجب أن تسمي هذه الطرق نادرًا ما يكون ذلك ممكنًا لضمان كفاءة تطبيقك.

{{% /alert %}}

## **موضوعات مسبقة**
- [صفوف AutoFit للدمج Cells](/cells/ar/net/autofit-rows-for-merged-cells/)
