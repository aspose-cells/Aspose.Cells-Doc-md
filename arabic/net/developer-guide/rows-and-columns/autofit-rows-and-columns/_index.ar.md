---
title: ضبط تلقائي للصفوف والأعمدة
type: docs
weight: 20
url: /ar/net/autofit-rows-and-columns/
description: توضح هذه المقالة كيفية ضبط حجم الصفوف، الأعمدة، الصفوف في الخلايا المدمجة والصف في مجموعة من الخلايا باستخدام واجهة برمجة التطبيقات Aspose.Cells for .NET.
keywords: ضبط تلقائي للصفوف، ضبط تلقائي للأعمدة، ضبط تلقائي للصف في مجموعة من الخلايا، ضبط تلقائي للصفوف في الخلايا المدمجة
---

{{% alert color="primary" %}}

يتيح Microsoft Excel للمستخدمين تحديد التلقائي لعرض وارتفاع الخلايا وفقًا لمحتواها. هذه الميزة متاحة أيضًا من خلال Aspose.Cells مما يتيح للمطورين ضبط أبعاد الخلية تلقائيًا أثناء التشغيل.

{{% /alert %}}

## **ضبط تلقائي**

يوفر Aspose.Cells [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يمثل ملف Microsoft Excel. كما تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة ورقة عمل. تتناول هذه المقالة استخدام فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) لضبط تلقائي للصفوف أو الأعمدة.

### **ضبط تلقائي للصف - بسيط**

أبسط الطرق لضبط عرض وارتفاع الصف هي استدعاء [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) الفئة [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index). يستغرق الأمر المنهج [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) فهو خطوة بسيطة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **كيفية ضبط صف تلقائيًا في مجموعة من الخلايا**

يتكون الصف من العديد من الأعمدة. تُسمح Aspose.Cells للمطورين بضبط الصف تلقائيًا بناءً على المحتوى في مجموعة من الخلايا داخل الصف عن طريق استدعاء نسخة محملة لـ [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1). يأخذ الأسلوب الزائد الإصدار ما يلي:

- **فهرس الصف**, فهرس الصف المراد ضبطه تلقائياً.
- **فهرس العمود الأول**, فهرس العمود الأول للصف.
- **فهرس العمود الأخير**, فهرس العمود الأخير للصف.

يقوم الأسلوب [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1) بفحص محتوى كل الأعمدة في الصف ثم يضبط الصف تلقائيًا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **كيفية ضبط العمود تلقائيًا في مجموعة من الخلايا**

يتكون العمود من العديد من الصفوف. يمكن ضبط عرض العمود تلقائيًا بناءً على المحتوى في مجموعة من الخلايا في العمود عن طريق استدعاء نسخة محملة من [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) الذي يأخذ المعلمات التالية:

- **فهرس العمود**: فهرس العمود الذي سيتم تلائم حجمه تلقائياً.
- **فهرس الصف الأول**: فهرس أول صف في العمود.
- **فهرس الصف الأخير**: فهرس آخر صف في العمود.

يقوم الطريقة [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) بفحص محتويات جميع الصفوف في العمود ثم يقوم بضبط حجم العمود تلقائياً.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **كيفية تلائم حجم الصفوف للخلايا المدمجة**

مع Aspose.Cells من الممكن تلائم حجم الصفوف تلقائياً حتى للخلايا التي تم دمجها باستخدام واجهة برمجة التطبيقات [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions). تقدم فئة [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) خاصية [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) التي يمكن استخدامها لتلائم حجم الصفوف للخلايا المدمجة. [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) تقبل عنصرًا قابلاً للتعداد [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) الذي يحتوي على الأعضاء التالية.

- None: تجاهل الخلايا المدمجة.
- FirstLine: توسيع ارتفاع الصف الأول فقط.
- LastLine: توسيع ارتفاع الصف الأخير فقط.
- EachLine: توسيع ارتفاع كل صف على حدة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

يمكنك أيضًا محاولة استخدام الإصدارات الزائدة من الأساليب [**AutoFitRows**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) و [**AutoFitColumns**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) التي تقبل مجموعة من الصفوف/الأعمدة ومثيلًا من [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) لتلائم حجم الصفوف/الأعمدة المحددة بالطريقة التي ترغب فيها [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions).

توقيعات الأساليب المذكورة أعلاه هي كالتالي:

1. AutoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) خيارات)
1. AutoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) خيارات)

{{% /alert %}}

## **مهم معرفته**

{{% alert color="primary" %}}

إذا كانت الخلية مدمجة، فلن تُطبق الأساليب تلقائي التلائم، وهو نفس السلوك الذي تظهره Microsoft Excel. يمكنك حل هذا عن طريق استخدام API تصفية تلقائية. علاوة على ذلك، إذا كان النص في الخلية ملتفًّا، فلن يتم تطبيق أسلوب [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) أيضًا. شيء آخر تحتاج إلى معرفته هو أن أساليب التلائم التلقائي تستهلك الوقت. لذا، يجب عليك استدعاء هذه الأساليب بأقل عدد ممكن من المرات لضمان كفاءة تطبيقك.

{{% /alert %}}

## **مواضيع متقدمة**
- [تلائم حجم الصفوف للخلايا المدمجة](/cells/ar/net/autofit-rows-for-merged-cells/)
