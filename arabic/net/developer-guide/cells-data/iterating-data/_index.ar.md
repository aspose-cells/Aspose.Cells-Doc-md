---
title: كيف وأين يتم استخدام معدلات الإحصاء
linktitle: تكرار البيانات
type: docs
weight: 55
url: /ar/net/how-and-where-to-use-enumerators/
description: تعلم كيف وأين يتم استخدام المعدلات الإحصائية من خلال واجهة البرمجة التطبيقية Aspose.Cells for .NET.
keywords: كيفية استخدام المعدلات الإحصائية، معدل الخلايا، معدل الصفوف، معدل الأعمدة
---

{{% alert color="primary" %}}

المعدل هو كائن يوفر القدرة على عبور حاوية أو مجموعة. يمكن استخدام المعدلات الإحصائية لقراءة البيانات في المجموعة، ولكن لا يمكن استخدامها لتعديل المجموعة الأساسية. بينما IEnumerable هو واجهة تحدد أحد الأساليب GetEnumerator التي تعيد واجهة IEnumerator، وهذا، بدوره، يسمح بالوصول القراءة فقط إلى مجموعة.

توفر واجهات برمجة تطبيقات Aspose.Cells مجموعة من المعدلات الإحصائية، ومع ذلك، يناقش هذا المقال بشكل رئيسي الثلاثة أنواع المذكورة أدناه.

1. معدل الخلايا
1. معدل الصفوف
1. معدل الأعمدة

{{% /alert %}}

## **كيفية استخدام المعدلات الإحصائية**

### **معدل الخلايا**

هناك طرق مختلفة للوصول إلى معدل الخلايا، ويمكن للشخص استخدام أيًا من هذه الطرق استنادًا إلى متطلبات التطبيق. هنا الطرق التي تُرجع معدل الخلايا.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

تعود الطرق المذكورة أعلاه جميعًا بمُحدِّد العناصر الذي يسمح بجَولة جمعية الخلايا التي تم تهيئتها.

{{% alert color="primary" %}}

أثناء جولة الخلايا، يجب ألا يتم تعديل المجموعة (العمليات التي ستؤدي إلى إنشاء خلية جديدة أو حذف خلية موجودة). وإلا فإن المُحدِّد قد لا يكون قادرًا على جولة جميع الخلايا بشكل صحيح (قد يكون بعض العناصر قد تجولت بشكل متكرر أو تم تخطيها).

{{% /alert %}}

يُظهر المثال البرمجي التالي تنفيذ واجهة IEnumerator لمجموعة الخلايا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

### **مُحدِّد الصفوف**

يمكن الوصول إلى مُحدِّد الصفوف أثناء استخدام الطريقة [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator). يُظهر المثال البرمجي التالي تنفيذ واجهة IEnumerator لـ [**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

### **مُحدِّد الأعمدة**

يمكن الوصول إلى مُحدِّد الأعمدة أثناء استخدام الطريقة [**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection). يُظهر المثال البرمجي التالي تنفيذ واجهة IEnumerator لـ [**ColumnCollection**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

## **أين يجب استخدام المُحدِّدات**

لنناقش فوائد استخدام المُحدِّدات، دعونا نأخذ مثالًا واقعيًا.

**سيناريو**

متطلبات التطبيق تتطلب جولة جميع الخلايا في [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) معينة لقراءة قيمها. يمكن تنفيذ هذا الهدف بعدة طرق. يُظهر بعضها أدناه.

### **استخدام نطاق العرض**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

### **استخدام MaxDataRow و MaxDataColumn**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

كما يمكنك أن تلاحظ أن كلتا الطريقتين المذكورتين تستخدمان تقريبًا نفس المنطق، وهو: الدوران حول جميع الخلايا في المجموعة لقراءة قيم الخلايا. قد يكون هذا مشكلة لعدة أسباب كما سيتم مناقشتها أدناه.

1. تتطلب واجهات برمجة التطبيقات مثل [**MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow)، [**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)، [**MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn)، [**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) و [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) وقت إضافي لجمع الإحصاءات المقابلة. في حالة كانت المصفوفة البيانات (صفوف × أعمدة) كبيرة، فإن استخدام هذه الواجهات قد يفرض عقوبة أداء.
1. في معظم الحالات، لا تتم إنشاء جميع الخلايا في النطاق المعطى. في مثل هذه الحالات، فحص كل خلية في البيانات ليس فعَّالًا كمقارنة بفحص الخلايا المهيئة فقط.
1. الوصول إلى خلية في حلقة مثل Cells row، column سيؤدي إلى إنشاء جميع كائنات الخلايا في النطاق، مما قد يؤدي في النهاية إلى حدوث استثناء نفاد الذاكرة.

## **الاستنتاج**

بناءً على الحقائق المذكورة أعلاه، فإن السيناريوهات الممكنة التالية هي التي يجب استخدام المُحدِّدات فيها.

1. الوصول القراءة فقط لمجموعة الخلايا مطلوب، أي؛ المتطلب هو تفقّد الخلايا فقط.
1. يتعين عبور عدد كبير من الخلايا.
1. يجب عبور الخلايا/الصفوف/الأعمدة المهيأة فقط.
{{< app/cells/assistant language="csharp" >}}
