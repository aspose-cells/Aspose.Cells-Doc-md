---
title: حماية الصفوف والأعمدة
type: docs
weight: 60
url: /ar/net/aspose-cells-gridweb/protect-rows-and-columns/
keywords: GridWeb,protect
description: يقدم هذا المقال كيفية حماية الصفوف والأعمدة في GridWeb.
---

{{% alert color="primary" %}} 

يناقش هذا الموضوع بعض التقنيات لحماية الخلايا في الصفوف والأعمدة من أي نوع من الإجراءات التي يقوم بها المستخدمون النهائيون. يمكن للمطورين تنفيذ هذه الحماية باستخدام تقنيتين: عن طريق جعل الخلايا في الصفوف والأعمدة للقراءة فقط، أو عن طريق تقييد خيارات قائمة السياق في Aspose.Cells.GridWeb. يتم مناقشة كلتا هاتين التقنيتين أدناه بمساعدة الأمثلة.

{{% /alert %}} 
## **حماية الخلايا في الصفوف والأعمدة**
### **جعل الصفوف والأعمدة قراءة فقط**
طريقة لحماية الصفوف والأعمدة في ورقة عمل هي جعل الخلايا للقراءة فقط. ثم لا يمكن حذفها من قبل المستخدمين النهائيين.

لجعل الصفوف والأعمدة للقراءة فقط:

1. أضف تحكم Aspose.Cells.GridWeb إلى استمارة الويب.
1. الوصول إلى GridWorksheet في المجموعة.
1. قم بتحديد الخلايا المراد جعلها قراءة فقط في الصفوف أو الأعمدة.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-MakeRowsColumnsReadOnly.aspx-MakeCellReadOnly.cs" >}}
### **تقييد خيارات القائمة السياقية**
يوفر Aspose.Cells.GridWeb قائمة سياقية يمكن للمستخدمين النهائيين استخدامها لأداء العمليات على الراقبة. تقدم القائمة العديد من الخيارات للتلاعب بالخلايا والصفوف والأعمدة.

**خيارات سياقية كاملة** 

![todo:image_alt_text](protect-rows-and-columns_1.png)

من الممكن تقييد أي نوع من العمليات على الجانب العميل في الصفوف والأعمدة عن طريق تقييد الخيارات المتاحة في القائمة السياقية. يمكن القيام بذلك عن طريق ضبط خصائص EnableClientColumnOperations و EnableClientRowOperations للراقبة إلى false. كما يمكن تقييد المستخدمين من تجميد الصفوف والأعمدة عن طريق ضبط EnableClientFreeze للراقبة إلى false.

**قائمة سياقية بعد تقييد خيارات الصف والعمود** 

![todo:image_alt_text](protect-rows-and-columns_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-RestrictContextMenu.aspx-RestrictContextMenu.cs" >}}
