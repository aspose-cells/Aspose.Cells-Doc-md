---
title: إدراج صورة بناءً على إشارة الخلية
type: docs
weight: 90
url: /ar/java/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

أحيانًا يكون لديك صورة فارغة وتحتاج إلى عرض البيانات أو المحتويات في الصورة عن طريق تحديد إشارة للخلية في شريط الصيغة. تدعم Aspose.Cells هذه الميزة (Microsoft Excel 2010).

{{% /alert %}}

## إدراج صورة بناءً على إشارة الخلية

تدعم Aspose.Cells عرض محتويات خلية ورقة العمل في شكل صورة. يمكنك ربط الصورة بالخلية التي تحتوي على البيانات التي تريد عرضها. نظرًا لأن الخلية أو نطاق الخلايا مرتبط بالكائن الرسومي، فإن التغييرات في البيانات ستظهر تلقائيًا في الكائن الرسومي. أضف صورة إلى ورقة العمل من خلال استدعاء الطريقة [**addPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPicture-int-int-int-int-java.io.InputStream-) من مجموعة الكائنات [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) (محاطة بكائن [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)). حدد نطاق الخلية باستخدام الطريقة [**setFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#Formula) من كائن [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture).

أدناه يوجد لقطة شاشة للملف الذي يقوم الكود أدناه بإنشائه.

إدراج صورة بناءً على إشارة الخلية

![todo:image_alt_text](insert-a-picture-based-on-cell-reference_1.png)

## كود عينة

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
{{< app/cells/assistant language="java" >}}
