---
title: أدخل صورة مرتبطة من عنوان الويب
type: docs
weight: 50
url: /ar/java/insert-a-linked-picture-from-web-address/
---
{{% alert color="primary" %}}

تحتاج أحيانًا إلى إدراج صورة من الويب (http: //) في ورقة عمل. للقيام بذلك ، حدد عنوان URL للصورة وسيتم تنزيل الصورة في كل مرة يتم فيها فتح جدول البيانات في Microsoft Excel. لم يتم تضمين الصورة فعليًا في مستند Excel ، ولكنها تشير إلى مورد ويب.

{{% /alert %}}

## **إدراج صورة مرتبطة من عنوان الويب**

### **باستخدام Microsoft إكسل**

في Microsoft Excel (على سبيل المثال 2007):

1.  انقر على**إدراج** القائمة وحدد**صورة**.

![ما يجب القيام به: image_بديل_نص](insert-a-linked-picture-from-web-address_1.png)

1.  حدد عنوان الويب للصورة في مربع الحوار "إدراج صورة".

![ما يجب القيام به: image_بديل_نص](insert-a-linked-picture-from-web-address_2.png)

تم إدراج الصورة.

![ما يجب القيام به: image_بديل_نص](insert-a-linked-picture-from-web-address_3.png)

### **باستخدام Aspose.Cells for Java**

 Aspose.Cells for Java يدعم اضافة صورة مرتبطة باستخدام الطريقة[**ShapeCollection.addLinkedPicture (int upperLeftRow ، int upperLeftColumn ، int height ، int width ، java.lang.String sourceFullName)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLinkedPicture(int,%20int,%20int,%20int,%20java.lang.String)).

 تقوم الطريقة بإرجاع ملف[**صورة**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)هدف.

يوضح المثال التالي كيفية إضافة صورة مرتبطة من عنوان ويب إلى ورقة عمل.

بعد تشغيل الكود ، يحتوي ملف Excel الذي تم إنشاؤه على صورة مرتبطة في ورقة العمل الأولى.

**ملف الإخراج** 

![ما يجب القيام به: image_بديل_نص](insert-a-linked-picture-from-web-address_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertLinkedPicturefromWebAddress-InsertLinkedPicturefromWebAddress.java" >}}
