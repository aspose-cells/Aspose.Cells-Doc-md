---
title: إضافة أو إدراج عمود في ورقة العمل
type: docs
weight: 10
url: /ar/net/aspose-cells-griddesktop/add-or-insert-a-column-into-worksheet/
keywords: GridDesktop,insert,add,column,insert column,insert row
description: يقدم هذا المقال كيفية إدراج أو إضافة عمود في GridDesktop.
---

{{% alert color="primary" %}} 

في هذا الموضوع ، سنصف الميزة الأساسية لإضافة وإدراج الأعمدة إلى ورقات العمل في وقت التشغيل باستخدام واجهة برمجة تطبيقات Aspose.Cells.GridDesktop. الفرق الأساسي بين الإضافة والإدراج هو أنه في الإضافة ، يتم إضافة العمود في نهاية مجموعة الأعمدة لورقة العمل أما في الإدراج ، يمكن إضافة العمود إلى أي موقع محدد في ورقة العمل.

{{% /alert %}} 
## **إضافة عمود إلى ورقة العمل**
لإضافة عمود جديد إلى ورقة العمل ، يرجى اتباع الخطوات التالية:

- أضف عنصر تحكم Aspose.Cells.GridDesktop إلى نموذجك **(Form)**
- الوصول إلى أي **ورقة عمل** مرغوبة
- إضافة **Column** إلى **Worksheet**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **إدراج عمود في ورقة العمل**
لإدراج عمود جديد في ورقة العمل في موقع محدد ، يرجى اتباع الخطوات التالية:

- أضف عنصر تحكم Aspose.Cells.GridDesktop إلى نموذجك **(Form)**
- الوصول إلى أي **ورقة عمل** مرغوبة
- إدراج **Column** في **Worksheet** (في موضع محدد عن طريق تحديد فهرس العمود الذي تريد إدراجه فيه)

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet to the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
