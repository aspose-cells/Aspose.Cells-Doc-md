---
title: إدارة الصور
type: docs
weight: 10
url: /ar/java/managing-pictures/
---

يسمح Aspose.Cells للمطورين بإضافة الصور إلى جداول البيانات في وقت التشغيل. علاوة على ذلك، يمكن التحكم في تحديد موضع هذه الصور في وقت التشغيل، والأمر الذي يتم مناقشته بتفصيل أكثر في الأقسام القادمة.

يشرح هذا المقال كيفية إضافة الصور، وكيفية إدراج صورة تعرض محتوى خلايا معينة.

## **إضافة الصور**

إضافة الصور إلى جدول بيانات سهل للغاية. فإنه يستغرق سوى بضعة أسطر من الشيفرة.

قم ببساطة باستدعاء الطريقة [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add-int-int-java.lang.String-) من مجموعة [**Pictures**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection) (مغلفة في كائن [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)). تأخذ الطريقة [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add-int-int-java.lang.String-) المعلمات التالية:

- **فهرس الصف الأعلى الأيسر**، فهرس الصف الأعلى.
- **فهرس العمود الأعلى الأيسر**، فهرس العمود الأعلى.
- **اسم ملف الصورة**، اسم ملف الصورة، مع المسار الكامل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **توضيح مواقع الصور**

يمكن وضع الصور باستخدام Aspose.Cells على النحو التالي:

- [الوضع المطلق](/cells/ar/java/managing-pictures/#absolute-positioning).

### **التحديد المطلق**

يمكن للمطورين تحديد موقع الصور بشكل مطلق باستخدام طرق [**setUpperDeltaX**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX) و [**setUpperDeltaY**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY) من كائن [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **مواضيع متقدمة**
- [إدراج صورة مرتبطة من عنوان ويب](/cells/ar/java/insert-a-linked-picture-from-web-address/)
- [إدراج صورة بناءً على مرجع الخلية](/cells/ar/java/insert-a-picture-based-on-cell-reference/)
- [إدراج صورة ويب من عنوان URL في ورقة عمل Excel](/cells/ar/java/insert-web-image-from-a-url-into-an-excel-worksheet/)
{{< app/cells/assistant language="java" >}}
