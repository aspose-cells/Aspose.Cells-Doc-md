---
title: إضافة أو إدراج صف في ورقة العمل
type: docs
weight: 30
url: /ar/net/adding-or-inserting-a-row-into-worksheet/
---
{{% alert color="primary" %}} 

على غرار أحد موضوعاتنا السابقة ، يصف هذا الموضوع ميزة إضافة وإدراج الصفوف في أوراق العمل في وقت التشغيل باستخدام API من Aspose.Cells.GridDesktop. يتمثل الاختلاف الأساسي بين الإضافة والإدراج في أنه بالإضافة إلى ذلك ، يتم إضافة صف في نهاية مجموعة صفوف ورقة العمل حيث يمكن إضافة صف إلى أي موضع محدد في ورقة العمل كما في الإدراج.

{{% /alert %}} 
## **إضافة صف إلى ورقة العمل**
لإضافة صف جديد إلى ورقة العمل ، يرجى اتباع الخطوات التالية:

-  أضف Aspose.Cells.GridDesktop control إلى ملف**استمارة**
-  الوصول إلى أي ملفات**ورقة عمل**
-  يضيف**صف** الى**ورقة عمل**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **إدراج صف في ورقة العمل**
لإدراج صف جديد في ورقة العمل في موضع محدد ، يرجى اتباع الخطوات التالية:

-  أضف Aspose.Cells.GridDesktop control إلى ملف**استمارة**
-  الوصول إلى أي ملفات**ورقة عمل**
-  إدراج**صف** داخل**ورقة عمل**(في موضع معين عن طريق تحديد فهرس الصف الذي يتم إدخاله فيه)

{{< highlight "java" >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
