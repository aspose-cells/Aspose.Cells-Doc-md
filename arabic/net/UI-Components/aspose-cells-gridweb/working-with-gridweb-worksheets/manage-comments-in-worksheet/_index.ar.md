---
title: إدارة التعليقات في ورقة العمل
type: docs
weight: 110
url: /ar/net/manage-comments-in-worksheet/
---
{{% alert color="primary" %}} 

يناقش هذا الموضوع إضافة التعليقات والوصول إليها وإزالتها من أوراق العمل. التعليقات مفيدة لإضافة ملاحظات أو معلومات مفيدة للمستخدمين الذين سيعملون مع الورقة. يتمتع المطورون بالمرونة لإضافة تعليقات إلى أي خلية في ورقة العمل.

{{% /alert %}} 
## **التعامل مع التعليقات**
### **إضافة التعليقات**
لإضافة تعليق إلى ورقة العمل ، يرجى اتباع الخطوات التالية:

1. قم بإضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج ويب.
1. قم بالوصول إلى ورقة العمل التي تضيف تعليقات إليها.
1. أضف تعليقًا إلى خلية.
1. ضع ملاحظة للتعليق الجديد.

**تمت إضافة تعليق إلى ورقة العمل** 

![ما يجب القيام به: image_بديل_نص](manage-comments-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AddComments.cs" >}}
### **الوصول إلى التعليقات**
للوصول إلى تعليق:

1. قم بالوصول إلى الخلية التي تحتوي على التعليق.
1. احصل على مرجع الخلية.
1. قم بتمرير المرجع إلى مجموعة التعليقات للوصول إلى التعليق.
1. من الممكن الآن تعديل خصائص التعليق.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AccessComments.cs" >}}
### **إزالة التعليقات**
لإزالة تعليق:

1. قم بالوصول إلى الخلية كما هو موضح أعلاه.
1. استخدم طريقة RemoveAt الخاصة بمجموعة التعليقات لإزالة التعليق.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-RemoveComments.cs" >}}
