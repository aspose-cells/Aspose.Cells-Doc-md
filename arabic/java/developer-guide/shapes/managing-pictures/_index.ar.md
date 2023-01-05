---
title: إدارة الصور
type: docs
weight: 10
url: /ar/java/managing-pictures/
---
{{% alert color="primary" %}}

Aspose.Cells يسمح للمطورين بإضافة الصور إلى جداول البيانات في وقت التشغيل. علاوة على ذلك ، يمكن التحكم في موضع هذه الصور في وقت التشغيل ، وهو ما سيتم مناقشته بمزيد من التفصيل في الأقسام القادمة.

Aspose.Cells for Java يدعم فقط تنسيقات الصور: BMP ، JPEG ، PNG ، GIF.

الفهارس المستخدمة في الأمثلة تبدأ من 0.

{{% /alert %}}

## **مضيفا الصور**

من السهل جدًا إضافة الصور إلى جدول البيانات. لا يتطلب الأمر سوى بضعة أسطر من التعليمات البرمجية.

 ما عليك سوى الاتصال بـ[**يضيف**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String) ) طريقة ال[**الصور**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection) مجموعة (مغلفة في ملف[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) موضوع). ال[**يضيف**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)) تأخذ الطريقة المعلمات التالية:

- **فهرس الصف العلوي الأيسر**، فهرس الصف العلوي الأيسر.
- **فهرس العمود الأيسر العلوي**، فهرس العمود الأيسر العلوي.
- **اسم ملف الصورة**، اسم ملف الصورة ، كامل مع المسار.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **وضع الصور**

يمكن وضع الصور باستخدام Aspose.Cells على النحو التالي:

- [تحديد المواقع المطلقة](/cells/ar/java/managing-pictures/#absolute-positioning).

### **تحديد المواقع المطلقة**

 يمكن للمطورين وضع الصور تمامًا باستخدام ملف[**setUpperDeltaX**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX) و[**setUpperDeltaY**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY) طرق[**صورة**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)موضوع.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **موضوعات مسبقة**
- [أدخل صورة مرتبطة من عنوان الويب](/cells/ar/java/insert-a-linked-picture-from-web-address/)
- [قم بإدراج صورة بناءً على مرجع Cell](/cells/ar/java/insert-a-picture-based-on-cell-reference/)
- [أدخل صورة ويب من عنوان URL في ورقة عمل Excel](/cells/ar/java/insert-web-image-from-a-url-into-an-excel-worksheet/)
