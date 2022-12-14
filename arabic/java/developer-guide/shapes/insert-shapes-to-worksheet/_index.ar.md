---
title: أدخل الأشكال في ورقة العمل في Aspose.Cells
type: docs
weight: 5
url: /ar/java/insert-shapes-to-worksheet-in-aspose-cells/
---
{{% alert color="primary" %}}

تحتاج أحيانًا إلى إدراج بعض الأشكال الضرورية في ورقة العمل ، وقد تحتاج إلى إدراج نفس الشكل في مواضع مختلفة من ورقة العمل ، أو قد تحتاج إلى إدخال أشكال مجمعة في ورقة العمل.

 لا تقلق![Aspose.Cells](https://products.aspose.com/cells/) يدعم كل هذه العمليات.

{{% /alert %}}

تنقسم الأشكال في برنامج Excel بشكل أساسي إلى الأنواع التالية:
- **خطوط**
- **المستطيلات**
- **الأشكال الأساسية**
- **أسهم بلوك**
- **أشكال المعادلة**
- **مخططات انسيابية**
- **النجوم واللافتات**
- **وسائل الشرح**

ستحدد وثيقة الدليل هذه شكلاً أو شكلين من كل نوع لعمل عينات ، ومن خلال هذه الأمثلة سوف تتعلم كيفية الاستخدام[Aspose.Cells](https://products.aspose.com/cells/) لإدراج الشكل المحدد في ورقة العمل.



## **إدراج سطر في ورقة العمل**

 شكل الخط ينتمي إلى**خطوط** الفئة.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية حيث تريد إدراج الخط
- انقر فوق قائمة "إدراج" وانقر فوق الأشكال.
- ثم حدد السطر من "الأشكال المستخدمة مؤخرًا" أو "الخطوط"

![](line.png)

***باستخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج سطر في ورقة العمل.

{{% alert color="primary" %}}

[الشكل العام addShape (نوع int ، int upperLeftRow ، int top ، int upperLeftColumn ، int left ، int height ، int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 تقوم الطريقة بإرجاع ملف[شكل](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) هدف.

{{% /alert %}}

يوضح المثال التالي كيفية إدراج سطر في ورقة العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Line.java" >}}

قم بتنفيذ الكود أعلاه ، ستحصل على النتائج التالية:

![](line2.png)



## **إدراج سهم خط في ورقة العمل**

 شكل سهم الخط ينتمي إلى**خطوط**فئة وهي حالة خاصة من الخط.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية حيث تريد إدراج سهم الخط
- انقر فوق قائمة "إدراج" وانقر فوق الأشكال.
- ثم حدد سهم الخط من "الأشكال المستخدمة مؤخرًا" أو "الخطوط"

![](line_arrow1.png)

***باستخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج سهم خط في ورقة العمل.

{{% alert color="primary" %}}

[الشكل العام addShape (نوع int ، int upperLeftRow ، int top ، int upperLeftColumn ، int left ، int height ، int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 تقوم الطريقة بإرجاع ملف[شكل](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) هدف.

{{% /alert %}}

يوضح المثال التالي كيفية إدراج سهم الخط في ورقة العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-LineArrow.java" >}}

قم بتنفيذ الكود أعلاه ، ستحصل على النتائج التالية:

![](line_arrow2.png)



## **ادراج مستطيل في ورقه العمل**

 شكل المستطيل ينتمي إلى**المستطيلات** الفئة.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية حيث تريد إدراج المستطيل
- انقر فوق قائمة "إدراج" وانقر فوق الأشكال.
- ثم حدد المستطيل من "الأشكال المستخدمة حديثًا" أو "المستطيلات"

![](rectangle.png)

***باستخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج مستطيل في ورقة العمل.

{{% alert color="primary" %}}

[الشكل العام addShape (نوع int ، int upperLeftRow ، int top ، int upperLeftColumn ، int left ، int height ، int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 تقوم الطريقة بإرجاع ملف[شكل](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) هدف.

{{% /alert %}}

يوضح المثال التالي كيفية إدراج مستطيل في ورقة عمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Rectangle.java" >}}

قم بتنفيذ الكود أعلاه ، ستحصل على النتائج التالية:

![](rectangle2.png)



## **إدراج مكعب في ورقة العمل**

 شكل المكعب ينتمي إلى**الأشكال الأساسية** الفئة.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية حيث تريد إدراج المكعب
- انقر فوق قائمة "إدراج" وانقر فوق الأشكال.
-  ثم حدد المكعب من**الأشكال الأساسية**

![](cube.png)

***باستخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج مكعب في ورقة العمل.

{{% alert color="primary" %}}

[الشكل العام addAutoShape (نوع int ، int upperLeftRow ، int top ، int upperLeftColumn ، int left ، int height ، int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 تقوم الطريقة بإرجاع ملف[شكل](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) هدف.

{{% /alert %}}

يوضح المثال التالي كيفية إدراج مكعب في ورقة عمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Cube.java" >}}

قم بتنفيذ الكود أعلاه ، ستحصل على النتائج التالية:

![](cube2.png)



## **إدراج سهم وسيلة شرح رباعي في ورقة العمل**

 شكل سهم وسيلة الشرح الرباعي ينتمي إلى**أسهم بلوك** الفئة.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية حيث تريد إدراج سهم وسيلة الشرح الرباعية
- انقر فوق قائمة "إدراج" وانقر فوق الأشكال.
-  ثم حدد سهم وسيلة الشرح الرباعي من**أسهم بلوك**

![](callout_quad_arrow.png)

***باستخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج سهم رباعي وسيلة الشرح في ورقة العمل.

{{% alert color="primary" %}}

[الشكل العام addAutoShape (نوع int ، int upperLeftRow ، int top ، int upperLeftColumn ، int left ، int height ، int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 تقوم الطريقة بإرجاع ملف[شكل](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) هدف.

{{% /alert %}}

يوضح المثال التالي كيفية إدراج سهم وسيلة الشرح الرباعي في ورقة عمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.java" >}}

قم بتنفيذ الكود أعلاه ، ستحصل على النتائج التالية:

![](callout_quad_arrow2.png)



## **إدراج علامة الضرب في ورقة العمل**

 شكل علامة الضرب ينتمي إلى**أشكال المعادلة** الفئة.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية حيث تريد إدراج علامة الضرب
- انقر فوق قائمة "إدراج" وانقر فوق الأشكال.
-  ثم حدد علامة الضرب من**أشكال المعادلة**

![](multiplication_sign.png)

***باستخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج علامة الضرب في ورقة العمل.

{{% alert color="primary" %}}

[الشكل العام addAutoShape (نوع int ، int upperLeftRow ، int top ، int upperLeftColumn ، int left ، int height ، int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 تقوم الطريقة بإرجاع ملف[شكل](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) هدف.

{{% /alert %}}

يوضح المثال التالي كيفية إدراج علامة الضرب في ورقة العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.java" >}}

قم بتنفيذ الكود أعلاه ، ستحصل على النتائج التالية:

![](multiplication_sign2.png)



## **إدراج مستند متعدد في ورقة العمل**

شكل المستندات المتعددة ينتمي إلى**مخططات انسيابية** الفئة.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية حيث تريد إدراج المستند المتعدد
- انقر فوق قائمة "إدراج" وانقر فوق الأشكال.
-  ثم حدد مستند متعدد من**مخططات انسيابية**

![](multidocument.png)

***باستخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج مستند متعدد في ورقة العمل.

{{% alert color="primary" %}}

[الشكل العام addAutoShape (نوع int ، int upperLeftRow ، int top ، int upperLeftColumn ، int left ، int height ، int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 تقوم الطريقة بإرجاع ملف[شكل](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) هدف.

{{% /alert %}}

يوضح المثال التالي كيفية إدراج مستند متعدد في ورقة عمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Multidocument.java" >}}

قم بتنفيذ الكود أعلاه ، ستحصل على النتائج التالية:

![](multidocument2.png)



## **إدراج نجمة خماسية في ورقة العمل**

 شكل النجمة الخماسية ينتمي إلى**النجوم واللافتات** الفئة.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية حيث تريد إدراج النجمة الخماسية
- انقر فوق قائمة "إدراج" وانقر فوق الأشكال.
-  ثم حدد النجمة الخماسية من**النجوم واللافتات**

![](star_5_points.png)

***باستخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج نجمة خماسية في ورقة العمل.

{{% alert color="primary" %}}

[الشكل العام addAutoShape (نوع int ، int upperLeftRow ، int top ، int upperLeftColumn ، int left ، int height ، int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 تقوم الطريقة بإرجاع ملف[شكل](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) هدف.

{{% /alert %}}

يوضح المثال التالي كيفية إدراج نجمة خماسية في ورقة العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-FivePointedStar.java" >}}

قم بتنفيذ الكود أعلاه ، ستحصل على النتائج التالية:

![](star_5_points2.png)



## **إدراج سحابة فقاعية في ورقة العمل**

 شكل سحابة فقاعة الفكر ينتمي إلى**وسائل الشرح** الفئة.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية حيث تريد إدراج سحابة الفقاعة الفكرية
- انقر فوق قائمة "إدراج" وانقر فوق الأشكال.
-  ثم حدد سحابة الفقاعة الفكرية من**وسائل الشرح**

![](thought_bubble_cloud.png)

***باستخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج سحابة فقاعية في ورقة العمل.

{{% alert color="primary" %}}

[الشكل العام addAutoShape (نوع int ، int upperLeftRow ، int top ، int upperLeftColumn ، int left ، int height ، int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 تقوم الطريقة بإرجاع ملف[شكل](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) هدف.

{{% /alert %}}

يوضح المثال التالي كيفية إدراج سحابة فقاعية فكرية في ورقة عمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.java" >}}

قم بتنفيذ الكود أعلاه ، ستحصل على النتائج التالية:

![](thought_bubble_cloud2.png)
