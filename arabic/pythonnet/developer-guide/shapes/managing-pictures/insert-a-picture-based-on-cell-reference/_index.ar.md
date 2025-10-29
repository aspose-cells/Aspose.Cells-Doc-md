---
title: إدراج صورة بناءً على مرجع الخلية
type: docs
weight: 150
url: /ar/python-net/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

 في بعض الأحيان لديك صورة فارغة وتحتاج إلى عرض البيانات أو المحتويات في الصورة عن طريق تعيين مرجع خلية في شريط الصيغة. تدعم Aspose.Cells لـ Python via .NET هذه الميزة (مايكروسوفت إكسل 2010).

{{% /alert %}}

## إدراج صورة بناءً على إشارة الخلية

 تدعم Aspose.Cells لـ Python via .NET عرض محتوى خلية ورقة عمل في شكل صورة. يمكنك ربط الصورة بالخلية التي تحتوي على البيانات التي تريد عرضها. بما أن الخلية أو نطاق الخلايا مرتبط بالكائن الرسومي، فإن التغييرات التي تجريها على البيانات في تلك الخلية أو النطاق تظهر تلقائيًا في الكائن الرسومي. أضف صورة إلى ورقة العمل عن طريق استدعاء أسلوب [**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture) من مجموعة [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) (المحاطة في الكائن [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)). حدد نطاق الخلايا باستخدام الخاصية [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula) من كائن [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture). 

### مثال على الكود

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertPictureCellReference-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
