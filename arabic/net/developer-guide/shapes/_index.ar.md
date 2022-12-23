---
title: إدراج صور وأشكال لملفات Excel.
linktitle: الأشكال
type: docs
weight: 140
url: /ar/net/insert-shapes/
description: إدارة الصور والكائنات والأشكال في ملفات Excel.
---
{{% alert color="primary" %}}

تحتاج أحيانًا إلى إدراج بعض الأشكال الضرورية في ورقة العمل ، وقد تحتاج إلى إدراج نفس الشكل في مواضع مختلفة من ورقة العمل ، أو قد تحتاج إلى إدخال أشكال مجمعة في ورقة العمل.

 لا تقلق![Aspose.Cells](https://products.aspose.com/cells/)يدعم كل هذه العمليات.

{{% /alert %}}

تنقسم الأشكال في برنامج Excel بشكل أساسي إلى الأنواع التالية:
- **الصور**
- **OleObjects**
- **خطوط**
- **المستطيلات**
- **الأشكال الأساسية**
- **أسهم بلوك**
- **أشكال المعادلة**
- **مخططات انسيابية**
- **النجوم واللافتات**
- **وسائل الشرح**

 ستحدد وثيقة الدليل هذه شكلاً أو شكلين من كل نوع لعمل عينات ، ومن خلال هذه الأمثلة سوف تتعلم كيفية الاستخدام[Aspose.Cells](https://products.aspose.com/cells/) لإدراج الشكل المحدد في ورقة العمل.

## **إضافة الصور في ورقة عمل Excel في C#**

من السهل جدًا إضافة الصور إلى جدول البيانات. لا يتطلب الأمر سوى بضعة أسطر من التعليمات البرمجية:
 ما عليك سوى الاتصال بـ[**يضيف**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) طريقة[**الصور**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) مجموعة (مغلفة في ملف[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) موضوع). ال[**يضيف**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)تأخذ الطريقة المعلمات التالية:

- **فهرس الصف العلوي الأيسر**، فهرس الصف العلوي الأيسر.
- **فهرس العمود الأيسر العلوي**، فهرس العمود الأيسر العلوي.
- **اسم ملف الصورة**، اسم ملف الصورة ، كامل مع المسار.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}


## **إدراج كائنات OLE في ورقة عمل Excel في C#**

يدعم Aspose.Cells إضافة واستخراج ومعالجة كائنات OLE في أوراق العمل. لهذا السبب ، يمتلك Aspose.Cells الامتداد[**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection) فئة ، تستخدم لإضافة كائن OLE جديد إلى قائمة المجموعة. فئة أخرى ،[**كائن أوله**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject)، يمثل كائن OLE. لها بعض الأعضاء المهمين:

-  ال[**بيانات الصورة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)تحدد الخاصية بيانات الصورة (الرمز) لنوع مصفوفة البايت. سيتم عرض الصورة لإظهار كائن OLE في ورقة العمل.
-  ال[**بيانات الكائن**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)تحدد الخاصية بيانات الكائن في شكل مصفوفة بايت. سيتم عرض هذه البيانات في البرنامج ذي الصلة عند النقر نقرًا مزدوجًا فوق رمز كائن OLE.

يوضح المثال التالي كيفية إضافة كائن (كائنات) OLE إلى ورقة عمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

## **إدراج سطر في ورقة عمل Excel في C#**

 شكل الخط ينتمي إلى**خطوط** الفئة.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية حيث تريد إدراج الخط
- انقر فوق قائمة "إدراج" وانقر فوق الأشكال.
- ثم حدد السطر من "الأشكال المستخدمة مؤخرًا" أو "الخطوط"

![](line.png)

***باستخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج سطر في ورقة العمل.

{{% alert color="primary" %}}

[الخط العام لشكل الخط الإضافي (
 int upperLeftRow ،
 قمة int ،
 int upperLeftColumn ،
 اليسار int ،
 ارتفاع كثافة العمليات ،
 عرض كثافة العمليات
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

 تقوم الطريقة بإرجاع ملف[شكل خط](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) موضوع.

{{% /alert %}}

يوضح المثال التالي كيفية إدراج سطر في ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Line.cs" >}}

قم بتنفيذ الكود أعلاه ، ستحصل على النتائج التالية:

![](line2.png)



## **إدراج سهم خط في ورقة عمل Excel في C#**

 شكل سهم الخط ينتمي إلى**خطوط** فئة وهي حالة خاصة من الخط.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية حيث تريد إدراج سهم الخط
- انقر فوق قائمة "إدراج" وانقر فوق الأشكال.
- ثم حدد سهم الخط من "الأشكال المستخدمة مؤخرًا" أو "الخطوط"

![](line_arrow1.png)

***باستخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج سهم خط في ورقة العمل.

{{% alert color="primary" %}}

[الخط العام لشكل الخط الإضافي (
 int upperLeftRow ،
 قمة int ،
 int upperLeftColumn ،
 اليسار int ،
 ارتفاع كثافة العمليات ،
 عرض كثافة العمليات
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

 تقوم الطريقة بإرجاع ملف[شكل خط](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) موضوع.

{{% /alert %}}

يوضح المثال التالي كيفية إدراج سهم الخط في ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-LineArrow.cs" >}}

قم بتنفيذ الكود أعلاه ، ستحصل على النتائج التالية:

![](line_arrow2.png)



## **إدخال مستطيل في ورقة عمل Excel في C#**

 شكل المستطيل ينتمي إلى**المستطيلات** الفئة.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية حيث تريد إدراج المستطيل
- انقر فوق قائمة "إدراج" وانقر فوق الأشكال.
- ثم حدد المستطيل من "الأشكال المستخدمة حديثًا" أو "المستطيلات"

![](rectangle.png)

***باستخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج مستطيل في ورقة العمل.

{{% alert color="primary" %}}

[مستطيل عام شكل إضافة مستطيل (
 int upperLeftRow ،
 قمة int ،
 int upperLeftColumn ،
 اليسار int ،
 ارتفاع كثافة العمليات ،
 عرض كثافة العمليات
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)

 تقوم الطريقة بإرجاع ملف[شكل مستطيل](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) موضوع.

{{% /alert %}}

يوضح المثال التالي كيفية إدراج مستطيل في ورقة عمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Rectangle.cs" >}}

قم بتنفيذ الكود أعلاه ، ستحصل على النتائج التالية:

![](rectangle2.png)



## **إدراج مكعب في ورقة عمل Excel في C#**

شكل المكعب ينتمي إلى**الأشكال الأساسية** الفئة.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية حيث تريد إدراج المكعب
- انقر فوق قائمة "إدراج" وانقر فوق الأشكال.
-  ثم حدد المكعب من**الأشكال الأساسية**

![](cube.png)

***باستخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج مكعب في ورقة العمل.

{{% alert color="primary" %}}

[الشكل العام AddAutoShape (
 نوع AutoShapeType ،
 int upperLeftRow ،
 قمة int ،
 int upperLeftColumn ،
 اليسار int ،
 ارتفاع كثافة العمليات ،
 عرض كثافة العمليات
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 تقوم الطريقة بإرجاع ملف[شكل](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) موضوع.

{{% /alert %}}

يوضح المثال التالي كيفية إدراج مكعب في ورقة عمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Cube.cs" >}}

قم بتنفيذ الكود أعلاه ، ستحصل على النتائج التالية:

![](cube2.png)



## **إدراج سهم وسيلة شرح رباعي في ورقة عمل Excel في C#**

 شكل سهم وسيلة الشرح الرباعي ينتمي إلى**أسهم بلوك** الفئة.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية حيث تريد إدراج سهم وسيلة الشرح الرباعية
- انقر فوق قائمة "إدراج" وانقر فوق الأشكال.
-  ثم حدد سهم وسيلة الشرح الرباعي من**أسهم بلوك**

![](callout_quad_arrow.png)

***باستخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج سهم رباعي وسيلة الشرح في ورقة العمل.

{{% alert color="primary" %}}

[الشكل العام AddAutoShape (
 نوع AutoShapeType ،
 int upperLeftRow ،
 قمة int ،
 int upperLeftColumn ،
 اليسار int ،
 ارتفاع كثافة العمليات ،
 عرض كثافة العمليات
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 تقوم الطريقة بإرجاع ملف[شكل](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) موضوع.

{{% /alert %}}

يوضح المثال التالي كيفية إدراج سهم وسيلة الشرح الرباعي في ورقة عمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.cs" >}}

قم بتنفيذ الكود أعلاه ، ستحصل على النتائج التالية:

![](callout_quad_arrow2.png)



## **إدخال علامة الضرب في ورقة عمل Excel في C#**

 شكل علامة الضرب ينتمي إلى**أشكال المعادلة** الفئة.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية حيث تريد إدراج علامة الضرب
- انقر فوق قائمة "إدراج" وانقر فوق الأشكال.
-  ثم حدد علامة الضرب من**أشكال المعادلة**

![](multiplication_sign.png)

***باستخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج علامة الضرب في ورقة العمل.

{{% alert color="primary" %}}

[الشكل العام AddAutoShape (
 نوع AutoShapeType ،
 int upperLeftRow ،
 قمة int ،
 int upperLeftColumn ،
 اليسار int ،
 ارتفاع كثافة العمليات ،
 عرض كثافة العمليات
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 تقوم الطريقة بإرجاع ملف[شكل](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) موضوع.

{{% /alert %}}

يوضح المثال التالي كيفية إدراج علامة الضرب في ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.cs" >}}

قم بتنفيذ الكود أعلاه ، ستحصل على النتائج التالية:

![](multiplication_sign2.png)



## **إدخال مستند متعدد في ورقة عمل Excel في C#**

 شكل المستندات المتعددة ينتمي إلى**مخططات انسيابية** الفئة.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية حيث تريد إدراج المستند المتعدد
- انقر فوق قائمة "إدراج" وانقر فوق الأشكال.
-  ثم حدد مستند متعدد من**مخططات انسيابية**

![](multidocument.png)

***باستخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج مستند متعدد في ورقة العمل.

{{% alert color="primary" %}}

[الشكل العام AddAutoShape (
 نوع AutoShapeType ،
 int upperLeftRow ،
 قمة int ،
 int upperLeftColumn ،
 اليسار int ،
 ارتفاع كثافة العمليات ،
 عرض كثافة العمليات
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 تقوم الطريقة بإرجاع ملف[شكل](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) موضوع.

{{% /alert %}}

يوضح المثال التالي كيفية إدراج مستند متعدد في ورقة عمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Multidocument.cs" >}}

قم بتنفيذ الكود أعلاه ، ستحصل على النتائج التالية:

![](multidocument2.png)



## **إدخال نجمة خماسية في ورقة عمل Excel في C#**

 شكل النجمة الخماسية ينتمي إلى**النجوم واللافتات** الفئة.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية حيث تريد إدراج النجمة الخماسية
- انقر فوق قائمة "إدراج" وانقر فوق الأشكال.
-  ثم حدد النجمة الخماسية من**النجوم واللافتات**

![](star_5_points.png)

***باستخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج نجمة خماسية في ورقة العمل.

{{% alert color="primary" %}}

[الشكل العام AddAutoShape (
 نوع AutoShapeType ،
 int upperLeftRow ،
 قمة int ،
 int upperLeftColumn ،
 اليسار int ،
 ارتفاع كثافة العمليات ،
 عرض كثافة العمليات
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 تقوم الطريقة بإرجاع ملف[شكل](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) موضوع.

{{% /alert %}}

يوضح المثال التالي كيفية إدراج نجمة خماسية في ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-FivePointedStar.cs" >}}

قم بتنفيذ الكود أعلاه ، ستحصل على النتائج التالية:

![](star_5_points2.png)



## **إدراج سحابة فقاعية فكرية في ورقة عمل Excel في C#**

 شكل سحابة فقاعة الفكر ينتمي إلى**وسائل الشرح** الفئة.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية حيث تريد إدراج سحابة الفقاعة الفكرية
- انقر فوق قائمة "إدراج" وانقر فوق الأشكال.
-  ثم حدد سحابة الفقاعة الفكرية من**وسائل الشرح**

![](thought_bubble_cloud.png)

***باستخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج سحابة فقاعية في ورقة العمل.

{{% alert color="primary" %}}

[الشكل العام AddAutoShape (
 نوع AutoShapeType ،
 int upperLeftRow ،
 قمة int ،
 int upperLeftColumn ،
 اليسار int ،
 ارتفاع كثافة العمليات ،
 عرض كثافة العمليات
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 تقوم الطريقة بإرجاع ملف[شكل](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) موضوع.

{{% /alert %}}

يوضح المثال التالي كيفية إدراج سحابة فقاعية فكرية في ورقة عمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.cs" >}}

قم بتنفيذ الكود أعلاه ، ستحصل على النتائج التالية:

![](thought_bubble_cloud2.png)

## **موضوعات مسبقة**
- [تغيير قيم الضبط للشكل](/cells/ar/net/change-adjustment-values-of-the-shape/)
- [نسخ الأشكال بين أوراق العمل](/cells/ar/net/copy-shapes-between-worksheets/)
- [البيانات في شكل غير بدائي](/cells/ar/net/data-in-non-primitive-shape/)
- [البحث عن الموضع المطلق للشكل داخل ورقة العمل](/cells/ar/net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [احصل على نقاط الاتصال من الشكل](/cells/ar/net/get-connection-points-from-shape/)
- [إدارة الضوابط](/cells/ar/net/managing-controls/)
- [أضف أيقونات إلى ورقة العمل](/cells/ar/net/insert-svg-to-excel/)
- [إدارة كائنات OLE](/cells/ar/net/managing-ole-objects/)
- [إدارة الصور](/cells/ar/net/managing-pictures/)
- [إدارة الفن الذكي](/cells/ar/net/managing-smartart/)
- [إدارة TextBox](/cells/ar/net/managing-textbox-of-excel/)
- [أضف علامة WordArt المائية إلى ورقة العمل](/cells/ar/net/add-wordart-watermark-to-worksheet/)
- [قم بتحديث قيم الأشكال المرتبطة](/cells/ar/net/refresh-values-of-linked-shapes/)
- [أرسل Shape Front أو Back داخل ورقة العمل](/cells/ar/net/send-shape-front-or-back-inside-the-worksheet/)
- [إدارة خيارات الشكل](/cells/ar/net/managing-shape-options/)
- [إدارة خيارات نص الشكل](/cells/ar/net/managing-shape-text-options/)
- [ملحقات الويب - الوظائف الإضافية للمكتب](/cells/ar/net/web-extensions-office-add-ins/)

