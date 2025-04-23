---
title: إدراج صورة ربط من عنوان الويب
type: docs
weight: 50
url: /ar/java/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

في بعض الأحيان قد تحتاج إلى إدراج صورة من الويب (http://) في ورقة عمل. للقيام بذلك، حدد عنوان URL للصورة وستتم تنزيل الصورة في كل مرة يتم فيها فتح جدول البيانات في Microsoft Excel. لا تُضاف الصورة بشكل مادي إلى مستند Excel، وإنما تشير إلى مورد ويب.

{{% /alert %}}

## **إدراج صورة مُربّطة من عنوان الويب**

### **استخدام Microsoft Excel**

في Microsoft Excel (على سبيل المثال 2007):

1. انقر فوق قائمة **إدراج** وحدد **صورة**.

![todo:image_alt_text](insert-a-linked-picture-from-web-address_1.png)

1. حدد عنوان الويب للصورة في مربع حوار إدراج صورة. 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_2.png)

سيتم إدراج الصورة.

![todo:image_alt_text](insert-a-linked-picture-from-web-address_3.png)

### **باستخدام Aspose.Cells for Java**

Aspose.Cells for Java يدعم إضافة صورة مرتبطة باستخدام الطريقة [**ShapeCollection.addLinkedPicture(int upperLeftRow, int upperLeftColumn, int height, int width, java.lang.String sourceFullName)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLinkedPicture-int-int-int-int-java.lang.String-).

تُعيد الطريقة كائن [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture).

المثال التالي يوضح كيفية إضافة صورة مرتبطة من عنوان الويب إلى ورقة عمل.

بعد تشغيل الكود، يحتوي ملف Excel الذي تم إنشاؤه على صورة مرتبطة في ورقة العمل الأولى.

ملف الإخراج 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertLinkedPicturefromWebAddress-InsertLinkedPicturefromWebAddress.java" >}}
{{< app/cells/assistant language="java" >}}
