---
title: أدخل صورة مرتبطة من عنوان الويب
type: docs
weight: 450
url: /ar/net/insert-a-linked-picture-from-web-address/
---
{{% alert color="primary" %}}

تحتاج أحيانًا إلى إدراج صورة من الويب (http: //) في ورقة عمل. للقيام بذلك ، حدد عنوان URL للصورة وسيتم تنزيل الصورة في كل مرة يتم فيها فتح جدول البيانات في Microsoft Excel. لم يتم تضمين الصورة فعليًا في مستند Excel ، ولكنها تشير إلى مورد ويب.

{{% /alert %}}

## **باستخدام Microsoft إكسل**

في Microsoft Excel (على سبيل المثال 2007):

1.  انقر على**إدراج** القائمة وحدد**صورة**.
1. حدد عنوان الويب للصورة في مربع الحوار "إدراج صورة".

## **باستخدام Aspose.Cells for .NET**

 Aspose.Cells for .NET يدعم إضافة صورة مرتبطة باستخدام[**ShapeCollection.AddLinkedPicture (int upperLeftRow ، int upperLeftColumn ، int heightPixels ، int widthPixels ، string sourceFullName)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlinkedpicture) . تقوم الطريقة بإرجاع ملف[**صورة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)هدف.

يوضح المثال التالي كيفية إضافة صورة مرتبطة من عنوان ويب إلى ورقة عمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertLinkedPicture-1.cs" >}}
