---
title: كيف وأين تستخدم العدادين
linktitle: تكرار البيانات
type: docs
weight: 55
url: /ar/net/how-and-where-to-use-enumerators/
---
{{% alert color="primary" %}}

العداد هو كائن يوفر القدرة على اجتياز حاوية أو مجموعة. يمكن استخدام العدادين لقراءة البيانات الموجودة في المجموعة ، ولكن لا يمكن استخدامها لتعديل المجموعة الأساسية ، في حين أن IEnumerable هي واجهة تحدد طريقة واحدة GetEnumerator والتي تعيد واجهة IEnumerator ، وهذا بدوره يسمح بالوصول للقراءة فقط إلى مجموعة.

توفر واجهات برمجة التطبيقات Aspose.Cells مجموعة من العدادين ، ومع ذلك ، تتناول هذه المقالة بشكل أساسي الأنواع الثلاثة كما هو موضح أدناه.

1. Cells العداد
1. عداد الصفوف
1. عداد الأعمدة

{{% /alert %}}

## **كيفية استخدام العدادين**

### **Cells العداد**

هناك طرق مختلفة للوصول إلى Cells Enumerator ، ويمكن للمرء استخدام أي من هذه الطرق بناءً على متطلبات التطبيق. فيما يلي الطرق التي تُرجع عد الخلايا.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

تقوم جميع الطرق المذكورة أعلاه بإرجاع العداد الذي يسمح بعبور مجموعة الخلايا التي تمت تهيئتها.

{{% alert color="primary" %}}

أثناء عبور الخلايا ، لا ينبغي تعديل المجموعة (العمليات التي ستؤدي إلى إنشاء نسخة جديدة من Cell أو حذف Cell الموجود). خلاف ذلك ، قد لا يتمكن العداد من اجتياز جميع الخلايا بشكل صحيح (قد يتم اجتياز بعض العناصر بشكل متكرر أو تخطيها).

{{% /alert %}}

يوضح المثال التالي من التعليمات البرمجية تطبيق واجهة IEnumerator لمجموعة Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

### **عداد الصفوف**

 يمكن الوصول إلى Rows Enumerator أثناء استخدام ملف[**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator) طريقة. يوضح المثال التالي من التعليمات البرمجية تطبيق واجهة IEnumerator لـ[**مجموعة RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

### **عداد الأعمدة**

 يمكن الوصول إلى عدّاد الأعمدة أثناء استخدام ملف[**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection) طريقة. يوضح المثال التالي من التعليمات البرمجية تطبيق واجهة IEnumerator لـ[**جمع العمود**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

## **أين تستخدم العدادين**

من أجل مناقشة مزايا استخدام العدادين ، لنأخذ مثالاً في الوقت الفعلي.

**سيناريو**

 مطلب التطبيق هو اجتياز جميع الخلايا في معطى[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)لقراءة قيمهم. يمكن أن يكون هناك عدة طرق لتنفيذ هذا الهدف. يتم عرض القليل أدناه.

### **باستخدام نطاق العرض**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

### **استخدام MaxDataRow & MaxDataColumn**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

كما يمكنك ملاحظة أن كلا النهجين المذكورين أعلاه يستخدمان منطقًا متشابهًا إلى حد ما ، أي ؛ حلقة فوق جميع الخلايا في المجموعة لقراءة قيم الخلية. قد يكون هذا مشكلة لعدد من الأسباب كما هو موضح أدناه.

1.  واجهات برمجة التطبيقات مثل[**ماكسرو**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**ماكسداتارو**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)تتطلب وقتًا إضافيًا لجمع الإحصائيات المقابلة. إذا كانت مصفوفة البيانات (الصفوف × الأعمدة) كبيرة ، فقد يؤدي استخدام واجهات برمجة التطبيقات هذه إلى فرض عقوبة على الأداء.
1. في معظم الحالات ، لا يتم إنشاء مثيل لكافة الخلايا الموجودة في النطاق المحدد. في مثل هذه الحالات ، لا يكون التحقق من كل خلية في المصفوفة فعالاً مقارنة بفحص الخلايا التي تمت تهيئتها فقط.
1. الوصول إلى خلية في حلقة مثل صف Cells ، سيؤدي العمود إلى إنشاء مثيل لجميع كائنات الخلية في النطاق ، مما قد يتسبب في النهاية في OutOfMemoryException.

## **استنتاج**

بناءً على الحقائق المذكورة أعلاه ، فيما يلي السيناريوهات المحتملة حيث يجب استخدام العدادين.

1. مطلوب وصول للقراءة فقط لمجموعة الخلايا ، أي ؛ الشرط هو فحص الخلايا فقط.
1. يجب اجتياز عدد كبير من الخلايا.
1. يتم اجتياز الخلايا / الصفوف / الأعمدة المهيأة فقط.
