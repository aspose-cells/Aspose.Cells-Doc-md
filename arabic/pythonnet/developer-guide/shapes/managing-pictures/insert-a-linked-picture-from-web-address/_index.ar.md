---
title: إدراج صورة ربط من عنوان الويب
type: docs
weight: 450
url: /ar/python-net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

في بعض الأحيان قد تحتاج إلى إدراج صورة من الويب (http://) في ورقة عمل. للقيام بذلك، حدد عنوان URL للصورة وستتم تنزيل الصورة في كل مرة يتم فيها فتح جدول البيانات في Microsoft Excel. لا تُضاف الصورة بشكل مادي إلى مستند Excel، وإنما تشير إلى مورد ويب.

{{% /alert %}}

## **استخدام Microsoft Excel**

في Microsoft Excel (على سبيل المثال 2007):

1. انقر فوق قائمة **إدراج** وحدد **صورة**.
1. حدد عنوان الويب للصورة في مربع حوار إدراج صورة.

## **باستخدام Aspose.Cells لبايثون via .NET**

 تدعم Aspose.Cells لـ Python via .NET إضافة صورة مرتبطة باستخدام [**ShapeCollection.add_linked_picture(int upper_left_row, int upper_left_column, int height_pixels, int width_pixels, str source_full_name)**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_linked_picture). تُرجع الطريقة كائن [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture).

المثال التالي يوضح كيفية إضافة صورة مرتبطة من عنوان الويب إلى ورقة عمل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertLinkedPicture-1.py" >}}
