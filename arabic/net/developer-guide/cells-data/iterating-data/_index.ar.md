---
title: كيف وأين يتم استخدام العدادين
linktitle: تكرار البيانات
type: docs
weight: 55
url: /ar/net/how-and-where-to-use-enumerators/
description: تعرف على كيفية ومكان استخدام العدادين من خلال Aspose.Cells for .NET API.
keywords: How to use Enumerators, Cells Enumerator, Rows Enumerator, Columns Enumerator
---
{{% alert color="primary" %}}

العداد هو كائن يوفر القدرة على اجتياز حاوية أو مجموعة. يمكن استخدام العدادات لقراءة البيانات الموجودة في المجموعة، ولكن لا يمكن استخدامها لتعديل المجموعة الأساسية، في حين أن IEnumerable عبارة عن واجهة تحدد طريقة واحدة GetEnumerator والتي ترجع واجهة IEnumerator، وهذا بدوره يسمح بالوصول للقراءة فقط إلى مجموعة.

توفر واجهات برمجة التطبيقات Aspose.Cells مجموعة من العدادين، ومع ذلك، تناقش هذه المقالة بشكل أساسي الأنواع الثلاثة كما هو موضح أدناه.

1. Cells عداد
1. عداد الصفوف
1. عداد الأعمدة

{{% /alert %}}

##  **كيفية استخدام التعداد**

###  **Cells عداد**

هناك طرق مختلفة للوصول إلى عداد Cells، ويمكن استخدام أي من هذه الطرق بناءً على متطلبات التطبيق. فيما يلي الطرق التي تقوم بإرجاع عداد الخلايا.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

تقوم جميع الطرق المذكورة أعلاه بإرجاع العداد الذي يسمح باجتياز مجموعة الخلايا التي تمت تهيئتها.

{{% alert color="primary" %}}

أثناء اجتياز الخلايا، لا ينبغي تعديل المجموعة (العمليات التي ستتسبب في إنشاء مثيل Cell الجديد أو حذف Cell الموجود). بخلاف ذلك، قد لا يتمكن العداد من اجتياز جميع الخلايا بشكل صحيح (قد يتم اجتياز بعض العناصر بشكل متكرر أو تخطيها).

{{% /alert %}}

يوضح مثال التعليمات البرمجية التالي تنفيذ واجهة IEnumerator لمجموعة Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

###  **عداد الصفوف**

 يمكن الوصول إلى عداد الصفوف أثناء استخدام[**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator) طريقة. يوضح مثال التعليمات البرمجية التالي تطبيق واجهة IEnumerator لـ[**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

###  **عداد الأعمدة**

 يمكن الوصول إلى عداد الأعمدة أثناء استخدام[**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection) طريقة. يوضح مثال التعليمات البرمجية التالي تطبيق واجهة IEnumerator لـ[**ColumnCollection**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

##  **أين يمكن استخدام العدادات**

من أجل مناقشة مزايا استخدام العدادين، دعونا نأخذ مثالا في الوقت الحقيقي.

**سيناريو**

 شرط التطبيق هو اجتياز جميع الخلايا في معين[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)لقراءة قيمهم. يمكن أن يكون هناك عدة طرق لتنفيذ هذا الهدف. يتم عرض عدد قليل أدناه.

###  **استخدام نطاق العرض**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

###  **باستخدام MaxDataRow وMaxDataColumn**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

كما يمكنك ملاحظة أن كلا النهجين المذكورين أعلاه يستخدمان منطقًا مشابهًا إلى حد ما، أي؛ قم بالتكرار فوق جميع الخلايا في المجموعة لقراءة قيم الخلية. قد يكون هذا مشكلة لعدد من الأسباب كما هو موضح أدناه.

1.  واجهات برمجة التطبيقات مثل[**ماكس رو**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)تتطلب وقتًا إضافيًا لجمع الإحصائيات المقابلة. في حالة كون مصفوفة البيانات (صفوف × أعمدة) كبيرة، فإن استخدام واجهات برمجة التطبيقات هذه قد يفرض عقوبة على الأداء.
1. في معظم الحالات، لا يتم إنشاء مثيل لجميع الخلايا في نطاق معين. في مثل هذه المواقف، لا يكون فحص كل خلية في المصفوفة فعالاً مقارنةً بفحص الخلايا التي تمت تهيئتها فقط.
1. سيؤدي الوصول إلى خلية في حلقة كصف Cells وعمود إلى إنشاء مثيل لجميع كائنات الخلية في النطاق، مما قد يؤدي في النهاية إلى OutOfMemoryException.

##  **خاتمة**

بناءً على الحقائق المذكورة أعلاه، فيما يلي السيناريوهات المحتملة التي ينبغي فيها استخدام القائمين بالتعداد.

1. مطلوب الوصول للقراءة فقط لمجموعة الخلايا، وهذا هو؛ الشرط هو فحص الخلايا فقط.
1. يجب اجتياز عدد كبير من الخلايا.
1. فقط الخلايا/الصفوف/الأعمدة التي تم تهيئتها سيتم اجتيازها.
