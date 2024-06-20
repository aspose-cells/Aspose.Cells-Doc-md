---
title: إضافة أو إدراج صف في ورقة العمل
type: docs
weight: 30
url: /ar/net/aspose-cells-griddesktop/add-or-insert-a-row-into-worksheet/
keywords: GridDesktop,insert,add,row,insert row,add row
description: يقدم هذا المقال كيفية إضافة أو إدراج صف في GridDesktop.
---

{{% alert color="primary" %}} 

مشابهًا لأحد المواضيع السابقة لدينا، يصف هذا الموضوع ميزة إضافة وإدراج الصفوف إلى أوراق العمل أثناء التشغيل باستخدام واجهة برمجة التطبيقات لـ Aspose.Cells.GridDesktop. الفارق الأساسي بين الإضافة والإدراج هو أنه في الإضافة، يتم إضافة صف في نهاية مجموعة الصفوف لورقة العمل، بينما في الإدراج، يمكن إضافة صف إلى أي موقع محدد في ورقة العمل.

{{% /alert %}} 
## **إضافة صف إلى ورقة العمل**
لإضافة صف جديد إلى ورقة العمل، يرجى اتباع الخطوات أدناه:

- أضف عنصر تحكم Aspose.Cells.GridDesktop إلى نموذجك **(Form)**
- الوصول إلى أي **ورقة عمل** مرغوبة
- إضافة **صف** إلى **ورقة العمل**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **إدراج صف في ورقة العمل**
لإدراج صف جديد في ورقة العمل في موقع محدد، يرجى اتباع الخطوات أدناه:

- أضف عنصر تحكم Aspose.Cells.GridDesktop إلى نموذجك **(Form)**
- الوصول إلى أي **ورقة عمل** مرغوبة
- إدراج **صف** في **ورقة العمل** (في موقع محدد عن طريق تحديد فهرس الصف الذي يتم إدراجه)

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
