---
title: إدراج الصور والأشكال في ملفات إكسيل.
linktitle: الأشكال
type: docs
weight: 140
url: /ar/net/insert-shapes/
description: إدارة الصور، الكائنات ole والأشكال في ملفات إكسيل.
---

{{% alert color="primary" %}}

في بعض الأحيان قد تحتاج إلى إدراج بعض الأشكال الضرورية في ورقة العمل. قد تحتاج إلى إدراج نفس الشكل في مواقع مختلفة في ورقة العمل. أو قد تحتاج إلى إدراج أشكال بشكل دُفعي في ورقة العمل.

لا تقلق! [Aspose.Cells](https://products.aspose.com/cells/) تدعم جميع هذه العمليات.

{{% /alert %}}

الأشكال في إكسل تنقسم أساسًا إلى الأنواع التالية:
- **الصور**
- **الكائنات OLE**
- **الخطوط**
- **المستطيلات**
- **الأشكال الأساسية**
- **السهام البلوكية**
- **أشكال المعادلة**
- **رسوم بيانية لسير العمل**
- **النجوم والرايات**
- **التلويحات**

سيتم في هذا الدليل اختيار شكل أو اثنين من كل نوع لإنشاء أمثلة. من خلال هذه الأمثلة، ستتعلم كيفية استخدام [Aspose.Cells](https://products.aspose.com/cells/) لإدراج الشكل المحدد في ورقة العمل.

## **إضافة الصور في ورقة عمل إكسل في س#**

إضافة الصور إلى جدول بيانات سهل للغاية. يستغرق الأمر سوى بضعة أسطر من الكود:
اتصل ببساطة بالطريقة [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) لمجموعة [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)، المغلفة في كائن [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). تأخذ الطريقة [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) المعاملات التالية:

- **فهرس الصف الأعلى الأيسر**، فهرس الصف الأعلى.
- **فهرس العمود الأعلى الأيسر**، فهرس العمود الأعلى.
- **اسم ملف الصورة**، اسم ملف الصورة، مع المسار الكامل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}


## **إدراج كائنات OLE في ورقة العمل إكسل في س#**

تدعم Aspose.Cells إضافة واستخراج وتلاعب بكائنات OLE في الأوراق العمل. لهذا السبب، لديها Aspose.Cells [**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection) الفئة التي تُستخدم لإضافة كائن OLE جديد إلى قائمة المجموعة. فئة أُخرى، [**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject)، تمثل كائن OLE. لها بعض الأعضاء المهمة:

- تحدد الخاصية [**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata) بيانات الصورة (الرمز) من نوع مصفوفة بايت. سيتم عرض الصورة لعرض كائن OLE في ورقة العمل.
- تحدد الخاصية [**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata) بيانات الكائن بشكل مصفوفة بايت. سيتم عرض هذه البيانات في البرنامج المرتبط بها عند النقر المزدوج على أيقونة كائن OLE.

المثال التالي يوضح كيفية إضافة كائنات OLE إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

## **إدراج خط في ورقة Excel في C#**

شكل الخط ينتمي إلى فئة ال**خطوط**.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية التي تريد إدراج الخط فيها
- انقر فوق القائمة إدراج وانقر فوق الأشكال.
- ثم، حدد الخط من 'الأشكال المستخدمة مؤخرًا' أو 'الخطوط'.

![](line.png)

***استخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج خط في ورقة العمل.

{{% alert color="primary" %}}

[**public LineShape AddLine(int upperLeftRow, int top, int upperLeftColumn, int left,	int height,	int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

تُرجع الطريقة كائن [LineShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape).

{{% /alert %}}

يظهر المثال التالي كيفية إدراج خط في ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Line.cs" >}}

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:

![](line2.png)



## **إدراج سهم خط في ورقة Excel في C#**

شكل سهم الخط ينتمي إلى فئة **الخطوط**. إنه حالة خاصة من الخط.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية التي تريد إدراج سهم الخط فيها
- انقر فوق القائمة إدراج وانقر فوق الأشكال.
- ثم، حدد سهم الخط من 'الأشكال المستخدمة مؤخرًا' أو 'الخطوط'.

![](line_arrow1.png)

***استخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج سهم خط في ورقة العمل.

{{% alert color="primary" %}}

[**public LineShape AddLine(int upperLeftRow, int top, int upperLeftColumn,	int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

تُرجع الطريقة كائن [LineShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape).

{{% /alert %}}

المثال التالي يوضح كيفية إدراج سهم خط في ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-LineArrow.cs" >}}

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:

![](line_arrow2.png)



## **إدراج مستطيل في ورقة العمل Excel باستخدام C#**

شكل المستطيل ينتمي إلى فئة **المستطيلات**.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية التي تريد إدراج المستطيل فيها
- انقر فوق القائمة إدراج وانقر فوق الأشكال.
- ثم اختر المستطيل من 'الأشكال المستخدمة مؤخرًا' أو 'المستطيلات'

![](rectangle.png)

***استخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج مستطيل في ورقة العمل.

{{% alert color="primary" %}}

[**public RectangleShape AddRectangle(int upperLeftRow,	int top, int upperLeftColumn, int left,	int height,	int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)

تعيد الطريقة كائن [RectangleShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape).

{{% /alert %}}

المثال التالي يوضح كيفية إدراج مستطيل في ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Rectangle.cs" >}}

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:

![](rectangle2.png)



## **إدراج مكعب في ورقة العمل في Excel باستخدام C#**

شكل المكعب ينتمي إلى فئة **الأشكال الأساسية**.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية التي تريد إدراج المكعب فيها
- انقر فوق القائمة إدراج وانقر فوق الأشكال.
- ثم، حدد المكعب من **الأشكال الأساسية**

![](cube.png)

***استخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج مكعب في الورقة العمل.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

تعيد الطريقة كائن [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape).

{{% /alert %}}

المثال التالي يوضح كيفية إدراج مكعب في ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Cube.cs" >}}

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:

![](cube2.png)



## **إدراج سهم رباعي القطب إلى ورقة العمل في Excel باستخدام C#**

شكل سهم مربعي الدعوة ينتمي إلى فئة **السهام الكتلية**.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية التي تريد إدراج سهم المربعي الدعوة فيها
- انقر فوق القائمة إدراج وانقر فوق الأشكال.
- ثم، حدد سهم المربعي الدعوة من **السهام الكتلية**

![](callout_quad_arrow.png)

***استخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج سهم رباعي الاتصال في ورقة العمل.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

تعيد الطريقة كائن [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape).

{{% /alert %}}

المثال التالي يُظهر كيفية إدراج سهم رباعي الاتصال في ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.cs" >}}

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:

![](callout_quad_arrow2.png)



## **إدراج علامة الضرب في ورقة عمل Excel في C#**

شكل علامة الضرب ينتمي إلى فئة **أشكال المعادلة**.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية التي ترغب في إدراج علامة الضرب فيها
- انقر فوق القائمة إدراج وانقر فوق الأشكال.
- ثم، حدد علامة الضرب من **أشكال المعادلة**

![](multiplication_sign.png)

***استخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج علامة الضرب في ورقة العمل.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

تعيد الطريقة كائن [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape).

{{% /alert %}}

المثال التالي يُظهر كيفية إدراج علامة الضرب في ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.cs" >}}

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:

![](multiplication_sign2.png)



## **إدراج وثيقة متعددة في ورقة Excel بلغة C#**

شكل مستند متعدد الوثائق ينتمي إلى فئة **الرسوم البيانية للتدفقات**.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية التي ترغب في إدراج مستند متعدد الوثائق فيها
- انقر فوق القائمة إدراج وانقر فوق الأشكال.
- ثم اختر مستند متعدد الوثائق من **الرسوم البيانية للتدفقات**

![](multidocument.png)

***استخدام Aspose.Cells***

يمكنك استخدام الطريقة التالية لإدراج مستند متعدد الوثائق في ورقة العمل.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

تعيد الطريقة كائن [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape).

{{% /alert %}}

المثال التالي يوضح كيفية إدراج مستند متعدد الوثائق في ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Multidocument.cs" >}}

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:

![](multidocument2.png)



## **إدراج نجمة خماسية إلى ورقة العمل في Excel باستخدام C#**

شكل النجمة المؤلفة من خمس نقاط ينتمي إلى فئة **النجوم والرايات**.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية التي ترغب في إدراج النجمة المؤلفة من خمس نقاط فيها
- انقر فوق القائمة إدراج وانقر فوق الأشكال.
- ثم اختر النجمة المؤلفة من خمس نقاط من **النجوم والرايات**

![](star_5_points.png)

***استخدام Aspose.Cells***

يمكنك استخدام الأسلوب التالي لإدراج نجمة ذات خمس نقاط في ورقة العمل.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

تعيد الطريقة كائن [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape).

{{% /alert %}}

توضح النموذج التالي كيفية إدراج نجمة ذات خمس نقاط في ورق عمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-FivePointedStar.cs" >}}

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:

![](star_5_points2.png)



## **إدراج سحابة فكرية إلى ورقة العمل في Excel باستخدام C#**

شكل سحابة الفكر ينتمي إلى فئة **المكالمات**.

***في Microsoft Excel (على سبيل المثال 2007):***

- حدد الخلية التي تريد إدراج سحابة الفكر فيها
- انقر فوق القائمة إدراج وانقر فوق الأشكال.
- ثم، حدد سحابة الفكر من **المكالمات**

![](thought_bubble_cloud.png)

***استخدام Aspose.Cells***

يمكنك استخدام الأسلوب التالي لإدراج سحابة فكرية في ورقة العمل.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

تعيد الطريقة كائن [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape).

{{% /alert %}}

المثال التالي يوضح كيفية إدراج سحابة فكرية في ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.cs" >}}

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:

![](thought_bubble_cloud2.png)

## **مواضيع متقدمة**
- [تغيير قيم التعديل للشكل](/cells/ar/net/change-adjustment-values-of-the-shape/)
- [نسخ الأشكال بين أوراق العمل](/cells/ar/net/copy-shapes-between-worksheets/)
- [البيانات في شكل غير مبدل](/cells/ar/net/data-in-non-primitive-shape/)
- [العثور على الموضع المطلق للشكل داخل الورقة العمل](/cells/ar/net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [الحصول على نقاط الاتصال من الشكل](/cells/ar/net/get-connection-points-from-shape/)
- [إدارة الضوابط](/cells/ar/net/managing-controls/)
- [إضافة رموز إلى ورقة العمل](/cells/ar/net/insert-svg-to-excel/)
- [إدارة كائنات OLE](/cells/ar/net/managing-ole-objects/)
- [إدارة الصور](/cells/ar/net/managing-pictures/)
- [إدارة الذكاء الفني](/cells/ar/net/managing-smartart/)
- [إدارة مربع النص](/cells/ar/net/managing-textbox-of-excel/)
- [إضافة كلمة WaterArt كعلامة مائية إلى ورقة العمل](/cells/ar/net/add-wordart-watermark-to-worksheet/)
- [تحديث القيم للأشكال المرتبطة](/cells/ar/net/refresh-values-of-linked-shapes/)
- [إرسال الشكل إلى الأمام أو الوراء داخل ورقة العمل](/cells/ar/net/send-shape-front-or-back-inside-the-worksheet/)
- [إدارة خيارات الشكل](/cells/ar/net/managing-shape-options/)
- [إدارة خيارات نص الشكل](/cells/ar/net/managing-shape-text-options/)
- [ملحقات الويب - إضافات الأوفيس](/cells/ar/net/web-extensions-office-add-ins/)

{{< app/cells/assistant language="csharp" >}}
