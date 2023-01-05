---
title: نسخ صفوف وأعمدة GridWeb
type: docs
weight: 80
url: /ar/net/copy-gridweb-rows-and-columns/
---
{{% alert color="primary" %}} 

 Aspose.Cells. يوفر مكون GridWeb وسيلة لنسخ الصف والعمود أثناء استخدام فئة GridCells. توضح هذه المقالة استخدام واجهات برمجة التطبيقات المكشوفة بواسطة Aspose.Cells.GridWeb لنسخ الصفوف والأعمدة على واجهة GridWeb.

ستقوم أساليب GridCells.CopyRow و GridCells.CopyColumn و GridCells.CopyRows & GridCells.CopyColumns بنسخ المحتويات والتصميم والصيغ من صف المصدر والعمود إلى الوجهة.

{{% /alert %}} 
## **نسخ الصفوف والأعمدة**
 إذا لم تكن على دراية بمكون Aspose.Cells.GridWeb ، فنحن نقترح عليك بشدة التحقق من[مقدمة إلى Aspose.Cells.GridWeb](https://docs.aspose.com/cells/net/browsers-capabilities/) ومقال مفصل عن[كيفية إضافة مكون Aspose.Cells.GridWeb في تطبيق WebForms](https://docs.aspose.com/cells/net/add-gridweb-to-web-form/).
### **نسخ صف واحد**
من أجل الحفاظ على المثال بسيطًا ، تستخدم المقالة جدول بيانات موجودًا بصف واحد وصيغة بسيطة تلخص كل القيم في الصف. إليك كيفية عرض جدول البيانات في واجهة Aspose.Cells.GridWeb قبل نسخ الصف.

![ما يجب القيام به: image_بديل_نص](copy-gridweb-rows-and-columns_1.png)

مقتطف الشفرة بسيط كما هو موضح أدناه. يصل إلى كائن GridCells بترتيب ورقة العمل النشط لعمل نسخة من الصف الأول إلى الصف التالي.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


إليك كيفية تعامل Aspose.Cells.GridWeb مع عملية نسخ صف.

![ما يجب القيام به: image_بديل_نص](copy-gridweb-rows-and-columns_2.png)
### **نسخ عمود واحد**
يستخدم المثال التالي جدول بيانات موجود بعمود واحد وصيغة بسيطة تجمع كل القيم الموجودة في العمود. إليك كيفية عرض جدول البيانات في واجهة Aspose.Cells.GridWeb قبل نسخ العمود.

![ما يجب القيام به: image_بديل_نص](copy-gridweb-rows-and-columns_3.png)

على غرار المثال أعلاه ، يصل مقتطف الشفرة التالي إلى كائن GridCells لترتيب ورقة العمل النشطة لعمل نسخة من العمود الأول إلى العمود التالي.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



إليك كيفية تعامل Aspose.Cells.GridWeb مع عملية نسخ العمود.

![ما يجب القيام به: image_بديل_نص](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

يمكنك استخدام أساليب GridCells.CopyRow & GridCells.CopyColumn في حلقة لنسخ صف وعمود المصدر إلى صفوف وأعمدة متعددة على التوالي.

{{% /alert %}} 
### **نسخ صفوف متعددة**
من الممكن أيضًا نسخ صفوف متعددة إلى وجهة جديدة أثناء استخدام طريقة GridCells.CopyRows ، والتي تتطلب معلمة إضافية من النوع الصحيح لتحديد عدد صفوف المصدر المراد نسخها.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



هنا كيف تبدو Aspose.Cells.GridWeb قبل وبعد عملية نسخ الصفوف.

![ما يجب القيام به: image_بديل_نص](copy-gridweb-rows-and-columns_5.png)

![ما يجب القيام به: image_بديل_نص](copy-gridweb-rows-and-columns_6.png)
### **نسخ أعمدة متعددة**
توفر فئة GridCells أيضًا طريقة CopyColumns ، والتي تأخذ معلمة إضافية من النوع الصحيح لتحديد عدد أعمدة المصدر المراد نسخها.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



هنا كيف تبدو Aspose.Cells.GridWeb قبل وبعد عملية نسخ الصفوف.

![ما يجب القيام به: image_بديل_نص](copy-gridweb-rows-and-columns_7.png)

![ما يجب القيام به: image_بديل_نص](copy-gridweb-rows-and-columns_8.png)
