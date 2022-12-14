---
title: إدارة الصور
type: docs
weight: 10
url: /ar/net/managing-pictures/
---
Aspose.Cells يسمح للمطورين بإضافة الصور إلى جداول البيانات في وقت التشغيل. علاوة على ذلك ، يمكن التحكم في موضع هذه الصور في وقت التشغيل ، وهو ما سيتم مناقشته بمزيد من التفصيل في الأقسام القادمة.

تشرح هذه المقالة كيفية إضافة الصور وكيفية إدراج صورة تعرض محتوى خلايا معينة.

## **مضيفا الصور**

من السهل جدًا إضافة الصور إلى جدول البيانات. لا يتطلب الأمر سوى بضعة أسطر من التعليمات البرمجية:
 ما عليك سوى الاتصال بـ[**يضيف**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) طريقة[**الصور**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) مجموعة (مغلفة في ملف[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) هدف). ال[**يضيف**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)تأخذ الطريقة المعلمات التالية:

- **فهرس الصف العلوي الأيسر**، فهرس الصف العلوي الأيسر.
- **فهرس العمود الأيسر العلوي**، فهرس العمود الأيسر العلوي.
- **اسم ملف الصورة**، اسم ملف الصورة ، كامل مع المسار.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}

## **تحديد المواقع الصور**

توجد طريقتان محتملتان للتحكم في وضع الصور باستخدام Aspose.Cells:

- تحديد الموضع النسبي: تحديد موضع يتناسب مع ارتفاع الصف وعرضه.
- تحديد الموضع المطلق: حدد الموضع الدقيق على الصفحة حيث سيتم إدراج الصورة ، على سبيل المثال ، 40 بكسل إلى اليسار و 20 بكسل أسفل حافة الخلية.

### **التموضع النسبي**

 يمكن للمطورين وضع الصور بما يتناسب مع ارتفاع الصف وعرض العمود باستخدام امتداد[**UpperDeltaX**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltax) و[**UpperDeltaY**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltay) خصائص[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) هدف. أ[**صورة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) يمكن الحصول على الكائن من[**الصور**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)المجموعة عن طريق تمرير فهرس صورتها. يضع هذا المثال صورة في الخلية F6.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.cs" >}}

### **تحديد المواقع المطلقة**

 يمكن للمطورين أيضًا وضع الصور تمامًا باستخدام ملف[**اليسار**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/left) و[**قمة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/top) خصائص[**صورة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)هدف. يضع هذا المثال صورة في الخلية F6 ، 60 بكسل من اليسار و 10 بكسل من أعلى الخلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.cs" >}}

## **إدراج صورة بناءً على مرجع Cell**

Aspose.Cells يتيح لك عرض محتويات خلية ورقة عمل في شكل صورة. يمكنك ربط الصورة بالخلية التي تحتوي على البيانات التي تريد عرضها. نظرًا لأن الخلية أو نطاق الخلية مرتبط بكائن رسومي ، فإن التغييرات التي تجريها على البيانات الموجودة في تلك الخلية أو نطاق الخلايا تظهر تلقائيًا في الكائن الرسومي.

 أضف صورة إلى ورقة العمل عن طريق استدعاء[**إضافة الصورة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) طريقة[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) مجموعة (مغلفة في ملف[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) هدف). حدد نطاق الخلايا باستخدام[**معادلة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) سمة من سمات[**صورة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)هدف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PictureCellReference-1.cs" >}}

## **موضوعات مسبقة**
- [قم بإضافة مجموعة أيقونات شرطية مع نص Cell](/cells/ar/net/add-conditional-icons-set-with-the-cell-text/)
- [أدخل صورة مرتبطة من عنوان الويب](/cells/ar/net/insert-a-linked-picture-from-web-address/)
- [قم بإدراج صورة بناءً على مرجع Cell](/cells/ar/net/insert-a-picture-based-on-cell-reference/)
- [قم بتحميل صورة ويب من عنوان URL إلى ورقة عمل Excel](/cells/ar/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

