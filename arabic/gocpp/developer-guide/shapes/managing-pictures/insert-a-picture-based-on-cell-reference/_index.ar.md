---
title: إدراج صورة استنادًا إلى مرجع الخلية باستخدام Golang عبر C++
linktitle: إدراج صورة بناءً على مرجع الخلية
type: docs
weight: 150
url: /ar/go-cpp/insert-a-picture-based-on-cell-reference/
description: تعلم كيفية إدراج صورة استنادًا إلى مرجع الخلية باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

أحيانًا يكون لديك صورة فارغة وتحتاج إلى عرض البيانات أو المحتويات في الصورة عن طريق تحديد إشارة للخلية في شريط الصيغة. تدعم Aspose.Cells هذه الميزة (Microsoft Excel 2010).

{{% /alert %}}

## إدراج صورة بناءً على إشارة الخلية

تدعم Aspose.Cells عرض محتوى خلية ورقة العمل في شكل صورة. يمكنك ربط الصورة بالخلية التي تحتوي على البيانات التي ترغب في عرضها. نظرًا لأن الخلية أو نطاق الخلية مرتبط بالكائن الرسومي، فإن التغييرات التي تقوم بها على البيانات في تلك الخلية أو نطاق الخلية تظهر تلقائيًا في الكائن الرسومي. أضف صورة إلى ورقة العمل عن طريق استدعاء الطريقة [**AddPicture**](https://reference.aspose.com/cells/go-cpp/shapecollection/addpicture_int_int_int_int_stream/) لمجموعة [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) (المغلفة في كائن [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). حدد نطاق الخلية باستخدام السمة [**Formula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) لكائن [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

### مثال على الكود

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertAPictureBasedOnCellReference.go" >}}
