---
title: إدراج الأشكال في ورقة عمل في Aspose.Cells
type: docs
weight: 5
url: /ar/java/insert-shapes-to-worksheet-in-aspose-cells/
---


{{% alert color="primary" %}}

في بعض الأحيان قد تحتاج إلى إدراج بعض الأشكال الضرورية في ورقة العمل. قد تحتاج إلى إدراج نفس الشكل في مواقع مختلفة في ورقة العمل. أو قد تحتاج إلى إدراج أشكال بشكل دُفعي في ورقة العمل.

لا تقلق! [Aspose.Cells](https://products.aspose.com/cells/) تدعم جميع هذه العمليات.

{{% /alert %}}

الأشكال في إكسل تنقسم أساسًا إلى الأنواع التالية:
- **الخطوط**
- **المستطيلات**
- **الأشكال الأساسية**
- **السهام البلوكية**
- **أشكال المعادلة**
- **رسوم بيانية لسير العمل**
- **النجوم والرايات**
- **التلويحات**

سيتم في هذا الدليل اختيار شكل أو اثنين من كل نوع لإنشاء أمثلة. من خلال هذه الأمثلة، ستتعلم كيفية استخدام [Aspose.Cells](https://products.aspose.com/cells/) لإدراج الشكل المحدد في ورقة العمل.



## **إدراج خط في ورقة العمل**

شكل الخط ينتمي إلى فئة ال**خطوط**.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية التي تريد إدراج الخط فيها
- انقر فوق القائمة إدراج وانقر فوق الأشكال.
- ثم، حدد الخط من 'الأشكال المستخدمة مؤخرًا' أو 'الخطوط'.

![](line.png)

***استخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج خط في ورقة العمل.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

يعيد الأسلوب كائن [شكل](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

يظهر المثال التالي كيفية إدراج خط في ورقة العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Line.java" >}}

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:

![](line2.png)



## **إدراج سهم خط في ورقة العمل**

شكل سهم الخط ينتمي إلى فئة **الخطوط**. إنه حالة خاصة من الخط.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية التي تريد إدراج سهم الخط فيها
- انقر فوق القائمة إدراج وانقر فوق الأشكال.
- ثم، حدد سهم الخط من 'الأشكال المستخدمة مؤخرًا' أو 'الخطوط'.

![](line_arrow1.png)

***استخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج سهم خط في ورقة العمل.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

يعيد الأسلوب كائن [شكل](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

المثال التالي يوضح كيفية إدراج سهم خط في ورقة العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-LineArrow.java" >}}

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:

![](line_arrow2.png)



## **إدراج مستطيل في ورقة العمل**

شكل المستطيل ينتمي إلى فئة **المستطيلات**.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية التي تريد إدراج المستطيل فيها
- انقر فوق القائمة إدراج وانقر فوق الأشكال.
- ثم اختر المستطيل من 'الأشكال المستخدمة مؤخرًا' أو 'المستطيلات'

![](rectangle.png)

***استخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج مستطيل في ورقة العمل.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

يعيد الأسلوب كائن [شكل](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

المثال التالي يوضح كيفية إدراج مستطيل في ورقة العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Rectangle.java" >}}

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:

![](rectangle2.png)



## **إدراج مكعب في ورقة العمل**

شكل المكعب ينتمي إلى فئة **الأشكال الأساسية**.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية التي تريد إدراج المكعب فيها
- انقر فوق القائمة إدراج وانقر فوق الأشكال.
- ثم، حدد المكعب من **الأشكال الأساسية**

![](cube.png)

***استخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج مكعب في الورقة العمل.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

يعيد الأسلوب كائن [شكل](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

المثال التالي يوضح كيفية إدراج مكعب في ورقة العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Cube.java" >}}

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:

![](cube2.png)



## **إدراج سهم مربعي الدعوة إلى ورقة العمل**

شكل سهم مربعي الدعوة ينتمي إلى فئة **السهام الكتلية**.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية التي تريد إدراج سهم المربعي الدعوة فيها
- انقر فوق القائمة إدراج وانقر فوق الأشكال.
- ثم، حدد سهم المربعي الدعوة من **السهام الكتلية**

![](callout_quad_arrow.png)

***استخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج سهم رباعي الاتصال في ورقة العمل.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

يعيد الأسلوب كائن [شكل](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

المثال التالي يُظهر كيفية إدراج سهم رباعي الاتصال في ورقة العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.java" >}}

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:

![](callout_quad_arrow2.png)



## **إدراج علامة الضرب في ورقة العمل**

شكل علامة الضرب ينتمي إلى فئة **أشكال المعادلة**.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية التي ترغب في إدراج علامة الضرب فيها
- انقر فوق القائمة إدراج وانقر فوق الأشكال.
- ثم، حدد علامة الضرب من **أشكال المعادلة**

![](multiplication_sign.png)

***استخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج علامة الضرب في ورقة العمل.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

يعيد الأسلوب كائن [شكل](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

المثال التالي يُظهر كيفية إدراج علامة الضرب في ورقة العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.java" >}}

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:

![](multiplication_sign2.png)



## **إدراج مستند متعدد الوثائق في ورقة العمل**

شكل مستند متعدد الوثائق ينتمي إلى فئة **الرسوم البيانية للتدفقات**.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية التي ترغب في إدراج مستند متعدد الوثائق فيها
- انقر فوق القائمة إدراج وانقر فوق الأشكال.
- ثم اختر مستند متعدد الوثائق من **الرسوم البيانية للتدفقات**

![](multidocument.png)

***استخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج مستند متعدد الوثائق في ورقة العمل.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

يعيد الأسلوب كائن [شكل](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

المثال التالي يوضح كيفية إدراج مستند متعدد الوثائق في ورقة العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Multidocument.java" >}}

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:

![](multidocument2.png)



## **إدراج نجمة مؤلفة من خمس نقاط في ورقة العمل**

شكل النجمة المؤلفة من خمس نقاط ينتمي إلى فئة **النجوم والرايات**.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية التي ترغب في إدراج النجمة المؤلفة من خمس نقاط فيها
- انقر فوق القائمة إدراج وانقر فوق الأشكال.
- ثم اختر النجمة المؤلفة من خمس نقاط من **النجوم والرايات**

![](star_5_points.png)

***استخدام Aspose.Cells***

يمكنك استخدام الأسلوب التالي لإدراج نجمة ذات خمس نقاط في ورقة العمل.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

يعيد الأسلوب كائن [شكل](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

توضح النموذج التالي كيفية إدراج نجمة ذات خمس نقاط في ورق عمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-FivePointedStar.java" >}}

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:

![](star_5_points2.png)



## **إدراج سحابة فكرية في ورقة العمل**

شكل سحابة الفكر ينتمي إلى فئة **المكالمات**.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية التي تريد إدراج سحابة الفكر فيها
- انقر فوق القائمة إدراج وانقر فوق الأشكال.
- ثم، حدد سحابة الفكر من **المكالمات**

![](thought_bubble_cloud.png)

***استخدام Aspose.Cells***

يمكنك استخدام الأسلوب التالي لإدراج سحابة فكرية في ورقة العمل.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

يعيد الأسلوب كائن [شكل](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

المثال التالي يوضح كيفية إدراج سحابة فكرية في ورقة العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.java" >}}

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:

![](thought_bubble_cloud2.png)
