---
title: كيفية وأين تستخدم العدادات مع Golang عبر C++
linktitle: تكرار البيانات
type: docs
weight: 55
url: /ar/go-cpp/how-and-where-to-use-enumerators/
description: تعلم كيفية ومكان استخدام العدادات من خلال واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: كيفية استخدام المعدلات الإحصائية، معدل الخلايا، معدل الصفوف، معدل الأعمدة
---

{{% alert color="primary" %}}

المُععد هو كائن يوفر القدرة على التجول في حاوية أو مجموعة. يمكن استخدام العدادات لقراءة البيانات في المجموعة، لكنها لا يمكن استخدامها لتعديل المجموعة الأساسية، في حين أن IEnumerable هو واجهة تعرف طريقة واحدة GetEnumerator التي تُرجع واجهة IEnumerator، مما يسمح بالوصول للقراءة فقط إلى مجموعة.

توفر واجهات برمجة تطبيقات Aspose.Cells مجموعة من المعدلات الإحصائية، ومع ذلك، يناقش هذا المقال بشكل رئيسي الثلاثة أنواع المذكورة أدناه.

1. معدل الخلايا
1. معدل الصفوف
1. معدل الأعمدة

{{% /alert %}}

## **كيفية استخدام المعدلات الإحصائية**

### **معدل الخلايا**

هناك طرق مختلفة للوصول إلى معدل الخلايا، ويمكن للشخص استخدام أيًا من هذه الطرق استنادًا إلى متطلبات التطبيق. هنا الطرق التي تُرجع معدل الخلايا.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/cells/getenumerator/)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/row/getenumerator/)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/range/getenumerator/)

تعود الطرق المذكورة أعلاه جميعًا بمُحدِّد العناصر الذي يسمح بجَولة جمعية الخلايا التي تم تهيئتها.

{{% alert color="primary" %}}

أثناء جولة الخلايا، يجب ألا يتم تعديل المجموعة (العمليات التي ستؤدي إلى إنشاء خلية جديدة أو حذف خلية موجودة). وإلا فإن المُحدِّد قد لا يكون قادرًا على جولة جميع الخلايا بشكل صحيح (قد يكون بعض العناصر قد تجولت بشكل متكرر أو تم تخطيها).

{{% /alert %}}

يُظهر المثال البرمجي التالي تنفيذ واجهة IEnumerator لمجموعة الخلايا.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData.go" >}}
### **مُحدِّد الصفوف**

يمكن الوصول إلى عداد الصفوف أثناء استخدام طريقة [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/rowcollection/getenumerator/). يُظهر المثال التالي تنفيذ واجهة IEnumerator لـ [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-1.go" >}}
### **الحصول على الأعمدة**

يمكن الوصول إلى الأعمدة أثناء استخدام طريقة [**ColumnCollection.Get**](https://reference.aspose.com/cells/go-cpp/columncollection/get/). يُظهر المثال التالي تنفيذ طريقة Get لـ [**ColumnCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-2.go" >}}
## **أين يجب استخدام المُحدِّدات**

لنناقش فوائد استخدام المُحدِّدات، دعونا نأخذ مثالًا واقعيًا.

**سيناريو**

متطلب التطبيق هو التجول عبر جميع الخلايا في [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) معين لقراءة قيمها. قد توجد عدة طرق لتحقيق هذا الهدف. تم توضيح بعض منها أدناه.

### **استخدام نطاق العرض**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-3.go" >}}
### **استخدام MaxDataRow و MaxDataColumn**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-4.go" >}}
كما يمكنك أن تلاحظ أن كلتا الطريقتين المذكورتين تستخدمان تقريبًا نفس المنطق، وهو: الدوران حول جميع الخلايا في المجموعة لقراءة قيم الخلايا. قد يكون هذا مشكلة لعدة أسباب كما سيتم مناقشتها أدناه.

1. تتطلب واجهات برمجة التطبيقات مثل [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/cells/getmaxrow/)، [**GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/)، [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/)، [**GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) و [**GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) وقتًا إضافيًا لجمع الإحصائيات المقابلة. إذا كانت مصفوفة البيانات (صفوف × أعمدة) كبيرة، فإن استخدام هذه الواجهات يمكن أن يفرض عقبة على الأداء.
1. في معظم الحالات، لا تتم إنشاء جميع الخلايا في النطاق المعطى. في مثل هذه الحالات، فحص كل خلية في البيانات ليس فعَّالًا كمقارنة بفحص الخلايا المهيئة فقط.
1. الوصول إلى خلية في حلقة مثل Cells row، column سيؤدي إلى إنشاء جميع كائنات الخلايا في النطاق، مما قد يؤدي في النهاية إلى حدوث استثناء نفاد الذاكرة.

## **الاستنتاج**

بناءً على الحقائق المذكورة أعلاه، فإن السيناريوهات الممكنة التالية هي التي يجب استخدام المُحدِّدات فيها.

1. الوصول القراءة فقط لمجموعة الخلايا مطلوب، أي؛ المتطلب هو تفقّد الخلايا فقط.
1. يتعين عبور عدد كبير من الخلايا.
1. يجب عبور الخلايا/الصفوف/الأعمدة المهيأة فقط.
