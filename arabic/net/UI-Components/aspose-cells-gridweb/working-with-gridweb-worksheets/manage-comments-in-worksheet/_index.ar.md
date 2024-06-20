---
title: إدارة التعليقات في ورقة العمل
type: docs
weight: 110
url: /ar/net/aspose-cells-gridweb/manage-comment-in-worksheet/
keywords: GridWeb,comment
description: يقدم هذا المقال كيفية العمل مع التعليق في GridWeb.
---

{{% alert color="primary" %}} 

يناقش هذا الموضوع إضافة التعليقات، والوصول إليها، وإزالتها من الأوراق العمل. التعليقات مفيدة لإضافة ملاحظات أو معلومات مفيدة للمستخدمين الذين سيعملون مع الورقة. لدى المطورين مرونة في إضافة التعليقات إلى أي خلية من ورقة العمل.

{{% /alert %}} 
## **العمل مع التعليقات**
### **إضافة التعليقات**
لإضافة تعليق إلى ورقة العمل، يرجى اتباع الخطوات التالية:

1. أضف عنصر تحكم Aspose.Cells.GridWeb إلى نموذج الويب.
1. الوصول إلى ورقة العمل التي ترغب في إضافة تعليقات إليها.
1. أضف تعليقًا لخلية.
1. تحديد ملاحظة للتعليق الجديد.

**تمت إضافة تعليق إلى ورقة العمل** 

![todo:image_alt_text](manage-comments-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AddComments.cs" >}}
### **الوصول إلى التعليقات**
للوصول إلى تعليق:

1. الوصول إلى الخلية التي تحتوي على التعليق.
1. الحصول على إشارة الخلية.
1. تمرير الإشارة إلى مجموعة التعليقات للوصول إلى التعليق.
1. الآن يمكن تعديل خصائص التعليق.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AccessComments.cs" >}}
### **إزالة التعليقات**
لإزالة تعليق:

1. الوصول إلى الخلية كما هو موضح أعلاه.
1. استخدم أسلوب إزالة RemoveAt في مجموعة التعليقات لإزالة التعليق.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-RemoveComments.cs" >}}
