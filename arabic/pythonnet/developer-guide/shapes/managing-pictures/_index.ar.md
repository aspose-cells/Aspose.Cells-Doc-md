---
title: إدارة الصور
type: docs
weight: 10
url: /ar/python-net/managing-pictures/
---

يسمح Aspose.Cells for Python via .NET للمطورين بإضافة صور إلى جداول البيانات أثناء التشغيل. علاوة على ذلك، يمكن التحكم في موضع هذه الصور أثناء التشغيل، وهو ما سيتم مناقشته بمزيد من التفصيل في الأقسام القادمة.

يشرح هذا المقال كيفية إضافة الصور، وكيفية إدراج صورة تعرض محتوى خلايا معينة.

## **إضافة الصور**

إضافة الصور إلى جدول بيانات سهل للغاية. يستغرق الأمر سوى بضعة أسطر من الكود:
اتصل ببساطة بالطريقة [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) لمجموعة [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection)، المغلفة في كائن [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). تأخذ الطريقة [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) المعاملات التالية:

- **فهرس الصف الأعلى الأيسر**، فهرس الصف الأعلى.
- **فهرس العمود الأعلى الأيسر**، فهرس العمود الأعلى.
- **اسم ملف الصورة**، اسم ملف الصورة، مع المسار الكامل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-AddingPictures-1.py" >}}

## **تحديد مواقع الصور**

هناك طريقتان محتملتان للتحكم في موضع الصور باستخدام Aspose.Cells for Python via .NET:

- تحديد موقع نسبي: تعريف موقع نسبي لارتفاع الصف والعرض.
- تحديد موقع مطلق: تعريف الموقع الدقيق على الصفحة حيث سيتم إدراج الصورة، على سبيل المثال، 40 بكسل إلى اليسار و 20 بكسل أسفل حافة الخلية.

### **التحديد النسبي**

يمكن للمطورين تحديد مواقع الصور بنسبة لارتفاع الصف وعرض العمود باستخدام الخصائص [**upper_delta_x**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_x) و [**upper_delta_y**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_y) لكائن [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture). يمكن الحصول على كائن [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) من مجموعة [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection) عن طريق تمرير فهرس الصورة الخاصة به. يضع هذا المثال صورة في الخلية F6.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.py" >}}

### **التحديد المطلق**

يمكن للمطورين أيضًا تحديد مواقع الصور بشكل مطلق باستخدام الخصائص [**left**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/left) و [**top**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/top) لكائن [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture). يضع هذا المثال صورة في الخلية F6، على بعد 60 بكسل من اليسار و10 بكسل من أعلى الخلية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.py" >}}

## **إدراج صورة بناءً على مرجع الخلية**

يتيح لك Aspose.Cells for Python via .NET عرض محتوى خلية ورقة العمل كشكل صورة. يمكنك ربط الصورة بالخلية التي تحتوي على البيانات التي تريد عرضها. نظرًا لربط الخلية أو النطاق بالعنصر الرسومي، فإن التغييرات التي تجريها على البيانات في تلك الخلية أو النطاق تظهر تلقائيًا في العنصر الرسومي.

إضافة صورة إلى ورقة العمل عن طريق استدعاء الطريقة [**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture) من مجموعة [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) (التي تم تغليفها في كائن [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)). حدد نطاق الخلية باستخدام السمة [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula) لكائن [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PictureCellReference-1.py" >}}

## **مواضيع متقدمة**
- [إضافة مجموعة رموز مشروطة مع نص الخلية](/cells/ar/python-net/add-conditional-icons-set-with-the-cell-text/)
- [إدراج صورة مرتبطة من عنوان ويب](/cells/ar/python-net/insert-a-linked-picture-from-web-address/)
- [إدراج صورة بناءً على مرجع الخلية](/cells/ar/python-net/insert-a-picture-based-on-cell-reference/)
- [تحميل صورة ويب من عنوان URL إلى ورقة عمل Excel](/cells/ar/python-net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

{{< app/cells/assistant language="python-net" >}}
