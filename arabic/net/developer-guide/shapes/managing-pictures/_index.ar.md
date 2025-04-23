---
title: إدارة الصور
type: docs
weight: 10
url: /ar/net/managing-pictures/
---

يسمح Aspose.Cells للمطورين بإضافة الصور إلى جداول البيانات في وقت التشغيل. علاوة على ذلك، يمكن التحكم في تحديد موضع هذه الصور في وقت التشغيل، والأمر الذي يتم مناقشته بتفصيل أكثر في الأقسام القادمة.

يشرح هذا المقال كيفية إضافة الصور، وكيفية إدراج صورة تعرض محتوى خلايا معينة.

## **إضافة الصور**

إضافة الصور إلى جدول بيانات سهل للغاية. يستغرق الأمر سوى بضعة أسطر من الكود:
اتصل ببساطة بالطريقة [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) لمجموعة [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)، المغلفة في كائن [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). تأخذ الطريقة [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) المعاملات التالية:

- **فهرس الصف الأعلى الأيسر**، فهرس الصف الأعلى.
- **فهرس العمود الأعلى الأيسر**، فهرس العمود الأعلى.
- **اسم ملف الصورة**، اسم ملف الصورة، مع المسار الكامل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}

## **تحديد مواقع الصور**

هناك طريقتان ممكنتان للتحكم في تحديد موقع الصور باستخدام Aspose.Cells:

- تحديد موقع نسبي: تعريف موقع نسبي لارتفاع الصف والعرض.
- تحديد موقع مطلق: تعريف الموقع الدقيق على الصفحة حيث سيتم إدراج الصورة، على سبيل المثال، 40 بكسل إلى اليسار و 20 بكسل أسفل حافة الخلية.

### **التحديد النسبي**

يمكن للمطورين تحديد مواقع الصور بنسبة لارتفاع الصف وعرض العمود باستخدام الخصائص [**UpperDeltaX**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltax) و [**UpperDeltaY**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltay) لكائن [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture). يمكن الحصول على كائن [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) من مجموعة [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) عن طريق تمرير فهرس الصورة الخاصة به. يضع هذا المثال صورة في الخلية F6.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.cs" >}}

### **التحديد المطلق**

يمكن للمطورين أيضًا تحديد مواقع الصور بشكل مطلق باستخدام الخصائص [**Left**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/left) و [**Top**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/top) لكائن [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture). يضع هذا المثال صورة في الخلية F6، على بعد 60 بكسل من اليسار و10 بكسل من أعلى الخلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.cs" >}}

## **إدراج صورة بناءً على مرجع الخلية**

يتيح Aspose.Cells عرض محتويات خلية ورق العمل في شكل صورة. يمكنك ربط الصورة بالخلية التي تحتوي على البيانات التي ترغب في عرضها. نظرًا لأن الخلية، أو نطاق الخلية، مرتبط بالكائن الرسومي، فإن التغييرات التي تقوم بها في البيانات في تلك الخلية أو نطاق الخلية ستظهر تلقائيًا في الكائن الرسومي.

إضافة صورة إلى ورقة العمل عن طريق استدعاء الطريقة [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) من مجموعة [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) (التي تم تغليفها في كائن [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). حدد نطاق الخلية باستخدام السمة [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) لكائن [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PictureCellReference-1.cs" >}}

## **مواضيع متقدمة**
- [إضافة مجموعة رموز مشروطة مع نص الخلية](/cells/ar/net/add-conditional-icons-set-with-the-cell-text/)
- [إدراج صورة مرتبطة من عنوان ويب](/cells/ar/net/insert-a-linked-picture-from-web-address/)
- [إدراج صورة بناءً على مرجع الخلية](/cells/ar/net/insert-a-picture-based-on-cell-reference/)
- [تحميل صورة ويب من عنوان URL إلى ورقة عمل Excel](/cells/ar/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

{{< app/cells/assistant language="csharp" >}}
