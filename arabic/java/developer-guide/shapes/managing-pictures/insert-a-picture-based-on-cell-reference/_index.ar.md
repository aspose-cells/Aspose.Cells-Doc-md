---
title: قم بإدراج صورة بناءً على مرجع Cell
type: docs
weight: 90
url: /ar/java/insert-a-picture-based-on-cell-reference/
---
{{% alert color="primary" %}}

في بعض الأحيان يكون لديك صورة فارغة وتحتاج إلى إظهار البيانات أو المحتويات في الصورة عن طريق تعيين مرجع خلية في شريط الصيغة. يدعم Aspose.Cells هذه الميزة (Microsoft Excel 2010).

{{% /alert %}}

## إدراج صورة بناءً على مرجع Cell

يدعم Aspose.Cells عرض محتويات خلية ورقة العمل في شكل صورة. يمكنك ربط الصورة بالخلية التي تحتوي على البيانات التي تريد عرضها. نظرًا لأن الخلية أو نطاق الخلية مرتبط بكائن رسومي ، تظهر التغييرات التي يتم إجراؤها على البيانات تلقائيًا في الكائن الرسومي. أضف صورة إلى ورقة العمل عن طريق استدعاء[**إضافة الصورة**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPicture(int,%20int,%20int,%20int,%20java.io.InputStream) ) طريقة ال[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) مجموعة (مغلفة في ملف[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) هدف). حدد نطاق الخلايا باستخدام[**مجموعة الصيغة**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#Formula) طريقة[**صورة**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)هدف.

يوجد أدناه لقطة شاشة للملف الذي ينشئه الكود أدناه.

**إدراج صورة بناءً على مرجع الخلية**

![ما يجب القيام به: image_بديل_نص](insert-a-picture-based-on-cell-reference_1.png)

## عينة من الرموز

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
