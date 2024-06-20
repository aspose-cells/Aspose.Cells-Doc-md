---
title: إدراج صورة ربط من عنوان الويب
type: docs
weight: 450
url: /ar/net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

في بعض الأحيان قد تحتاج إلى إدراج صورة من الويب (http://) في ورقة عمل. للقيام بذلك، حدد عنوان URL للصورة وستتم تنزيل الصورة في كل مرة يتم فيها فتح جدول البيانات في Microsoft Excel. لا تُضاف الصورة بشكل مادي إلى مستند Excel، وإنما تشير إلى مورد ويب.

{{% /alert %}}

## **استخدام Microsoft Excel**

في Microsoft Excel (على سبيل المثال 2007):

1. انقر فوق قائمة **إدراج** وحدد **صورة**.
1. حدد عنوان الويب للصورة في مربع حوار إدراج صورة.

## **استخدام Aspose.Cells for .NET**

يدعم Aspose.Cells for .NET إضافة صورة مرتبطة باستخدام [**ShapeCollection.AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, string sourceFullName)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlinkedpicture). تُرجع الطريقة كائن [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture).

المثال التالي يوضح كيفية إضافة صورة مرتبطة من عنوان الويب إلى ورقة عمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertLinkedPicture-1.cs" >}}
