---
title: إدراج صورة بناءً على مرجع الخلية
type: docs
weight: 150
url: /ar/net/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

أحيانًا يكون لديك صورة فارغة وتحتاج إلى عرض البيانات أو المحتويات في الصورة عن طريق تحديد إشارة للخلية في شريط الصيغة. تدعم Aspose.Cells هذه الميزة (Microsoft Excel 2010).

{{% /alert %}}

## إدراج صورة بناءً على إشارة الخلية

تدعم Aspose.Cells عرض محتوى خلية ورقة العمل في شكل صورة. يمكنك ربط الصورة بالخلية التي تحتوي على البيانات التي ترغب في عرضها. نظرًا لأن الخلية أو نطاق الخلية مرتبط بالكائن الرسومي، فإن التغييرات التي تقوم بها على البيانات في تلك الخلية أو نطاق الخلية تظهر تلقائيًا في الكائن الرسومي. أضف صورة إلى ورقة العمل عن طريق استدعاء الطريقة [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) لمجموعة [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) (المغلفة في كائن [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). حدد نطاق الخلية باستخدام السمة [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) لكائن [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture).

### مثال على الكود

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertPictureCellReference-1.cs" >}}
