---
title: إدراج صورة مرتبطة من عنوان ويب باستخدام Golang عبر C++
linktitle: إدراج صورة ربط من عنوان الويب
type: docs
weight: 450
url: /ar/go-cpp/insert-a-linked-picture-from-web-address/
description: تعلم كيفية إدراج صورة مربوطة من عنوان ويب في ورقة عمل باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

في بعض الأحيان قد تحتاج إلى إدراج صورة من الويب (http://) في ورقة عمل. للقيام بذلك، حدد عنوان URL للصورة وستتم تنزيل الصورة في كل مرة يتم فيها فتح جدول البيانات في Microsoft Excel. لا تُضاف الصورة بشكل مادي إلى مستند Excel، وإنما تشير إلى مورد ويب.

{{% /alert %}}

## **استخدام Microsoft Excel**

في Microsoft Excel (على سبيل المثال 2007):

1. انقر فوق قائمة **إدراج** وحدد **صورة**.
1. حدد عنوان الويب للصورة في مربع حوار إدراج صورة.

## **باستخدام Aspose.Cells for C++**

يدعم Aspose.Cells for C++ إضافة صورة مربوطة باستخدام طريقة [**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/go-cpp/shapecollection/addlinkedpicture/). تعيد الطريقة كائن [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

يظهر المثال التالي كيفية إضافة صورة مرتبطة من عنوان ويب إلى ورقة عمل.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertALinkedPictureFromWebAddress.go" >}}
