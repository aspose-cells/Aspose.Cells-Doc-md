---
title: تغيير حجم الصفوف والأعمدة
type: docs
weight: 30
url: /ar/net/resize-rows-and-columns/
---
{{% alert color="primary" %}} 

في بعض الأحيان تكون قيم الخلية أوسع من الخلية الموجودة فيها أو موجودة في عدة أسطر. هذه القيم ليست مرئية بالكامل للمستخدمين ما لم يغيروا ارتفاع وعرض الصفوف والأعمدة. Aspose.Cells.GridWeb يدعم بشكل كامل تحديد ارتفاع الصف وعرض العمود. يناقش هذا الموضوع هذه الميزات بالتفصيل بمساعدة الأمثلة.

{{% /alert %}} 
## **العمل مع ارتفاع الصفوف وعرض العمود**
### **ضبط ارتفاع الصف**
لتعيين ارتفاع الصف:

1. قم بإضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج ويب الخاص بك.
1. قم بالوصول إلى مجموعة Cells الخاصة بورقة العمل.
1. عيّن ارتفاع جميع الخلايا في أي صف محدد.

{{% alert color="primary" %}} 

يحتوي أسلوب SetRowHeight و SetColumnWidth لمجموعة Cells أيضًا على متغيرات متاحة لتعيين قياسات ارتفاع الصف وعرض العمود بالبوصة والبكسل.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetRowHeight.cs" >}}
### **ضبط عرض العمود**
لتعيين عرض العمود:

1. قم بإضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج ويب الخاص بك.
1. قم بالوصول إلى مجموعة Cells الخاصة بورقة العمل.
1. قم بتعيين عرض جميع الخلايا في أي عمود محدد.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetColumnWidth.cs" >}}
