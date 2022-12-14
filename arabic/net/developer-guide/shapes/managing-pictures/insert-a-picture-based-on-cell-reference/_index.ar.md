---
title: قم بإدراج صورة بناءً على مرجع Cell
type: docs
weight: 150
url: /ar/net/insert-a-picture-based-on-cell-reference/
---
{{% alert color="primary" %}}

في بعض الأحيان يكون لديك صورة فارغة وتحتاج إلى إظهار البيانات أو المحتويات في الصورة عن طريق تعيين مرجع خلية في شريط الصيغة. يدعم Aspose.Cells هذه الميزة (Microsoft Excel 2010).

{{% /alert %}}

## إدراج صورة بناءً على مرجع Cell

يدعم Aspose.Cells عرض محتويات خلية ورقة العمل في شكل صورة. يمكنك ربط الصورة بالخلية التي تحتوي على البيانات التي تريد عرضها. نظرًا لأن الخلية أو نطاق الخلية مرتبط بكائن رسومي ، فإن التغييرات التي تجريها على البيانات الموجودة في تلك الخلية أو نطاق الخلايا تظهر تلقائيًا في الكائن الرسومي. أضف صورة إلى ورقة العمل عن طريق استدعاء[**إضافة الصورة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) طريقة[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) مجموعة (مغلفة في ملف[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) هدف). حدد نطاق الخلايا باستخدام[**معادلة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) سمة من سمات[**صورة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)هدف.

### مثال رمز

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertPictureCellReference-1.cs" >}}
