---
title: إضافة أو إدراج عمود في ورقة العمل
type: docs
weight: 10
url: /ar/net/adding-or-inserting-a-column-into-worksheet/
---
{{% alert color="primary" %}} 

في هذا الموضوع ، سنصف الميزة الأساسية لإضافة وإدراج الأعمدة في أوراق العمل في وقت التشغيل باستخدام API من Aspose.Cells.GridDesktop. يتمثل الاختلاف الأساسي بين الإضافة والإدراج في أنه بالإضافة إلى ذلك ، تتم إضافة العمود في نهاية مجموعة الأعمدة في ورقة العمل حيث يمكن إضافة العمود إلى أي موضع محدد في ورقة العمل ، كما هو الحال في الإدراج.

{{% /alert %}} 
## **إضافة عمود إلى ورقة العمل**
لإضافة عمود جديد إلى ورقة العمل ، يرجى اتباع الخطوات التالية:

-  أضف Aspose.Cells.GridDesktop control إلى ملف**استمارة**
-  الوصول إلى أي ملفات**ورقة عمل**
-  يضيف**عمود** الى**ورقة عمل**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **إدراج عمود في ورقة العمل**
لإدراج عمود جديد في ورقة العمل في موضع محدد ، يرجى اتباع الخطوات التالية:

-  أضف Aspose.Cells.GridDesktop control إلى ملف**استمارة**
-  الوصول إلى أي ملفات**ورقة عمل**
-  إدراج**عمود** داخل**ورقة عمل** (في موضع معين عن طريق تحديد فهرس العمود حيث يتم إدراجه)

{{< highlight "java" >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet to the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
