---
title: كشف الأوراق العمل الفارغة
type: docs
weight: 710
url: /ar/java/detecting-empty-worksheets/
---

## **فحص الخلايا المعبأة**
قد تحتوي ورقة العمل على خلية واحدة أو أكثر مملوءة بقيم حيث يمكن أن تكون القيمة بسيطة (نص، رقم، تاريخ/وقت) أو صيغة أو قيمة معتمدة على الصيغة. في مثل هذه الحالة، من السهل اكتشاف ما إذا كانت ورقة العمل المعطاة فارغة أم لا. كل ما علينا فحصه هو [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) أو [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) properties. إذا كانت الخصائص المذكورة تعيد قيمًا صفرية أو إيجابية، فإن ذلك يعني أنه تم ملأ واحد أو أكثر من الخلايا، ومع ذلك، إذا عادت أيًا من هذه الخصائص -1، فإن ذلك يدل على أنه لم يتم ملأ أي من الخلايا في ورقة العمل المعطاة.

{{% alert color="primary" %}} 

مجموعات الصفوف والأعمدة لها فهرس يبدأ من الصفر، لذلك الخلية في الصف 0 والعمود 0 تعني أول خلية في ورقة العمل، وهي A1.

{{% /alert %}} 
## **فحص الخلايا المهيأة الفارغة**
تتم مهيأة جميع الخلايا التي تحتوي على قيم تلقائيًا، ومع ذلك، هناك احتمال أن تحتوي ورقة العمل على خلايا تم تطبيق التنسيق فقط عليها. في مثل هذا السيناريو، ستعود الخصائص [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) أو [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) بالقيمة -1 مشيرة إلى عدم وجود أي قيم معبأة ولكن لا يمكن اكتشاف الخلايا المهيأة الفارغة باستخدام هذا النهج. من أجل التحقق مما إذا كانت ورقة العمل تحتوي على خلايا مهيأة فارغة، يُنصح باستخدام *Iterator.hasNext* الطريقة على المُنظر الذي تم الحصول عليه من مجموعة الخلايا. إذا عادت طريقة *iterator.hasNext* بقيمة صحيحة، فإن ذلك يعني وجود مزيد من الخلايا المهيأة في ورقة العمل المعطاة.

{{% alert color="primary" %}} 

هناك عدة طرق للحصول على مُنظر الخلايا كما هو مفصل في [كيف وأين يتم استخدام المُنظرات](/cells/ar/java/how-and-where-to-use-iterators/).

{{% /alert %}} 
## **فحص الأشكال**
من الممكن أن تكون ورقة العمل المعطاة لا تحتوي على أي خلايا معبأة، ومع ذلك، يمكن أن تحتوي على أشكال وكائنات مثل عناصر التحكم، الرسوم البيانية، الصور وما إلى ذلك. إذا كنا بحاجة للتحقق مما إذا كانت ورقة العمل تحتوي على أي شكل، يمكننا فعل ذلك عن طريق فحص [ShapeCollection.Count](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#Count) property. أي قيمة إيجابية تشير إلى وجود شكل(أشكال) في ورقة العمل.
## **نموذج برمجة**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CheckForShapes-1.java" >}}
{{< app/cells/assistant language="java" >}}
