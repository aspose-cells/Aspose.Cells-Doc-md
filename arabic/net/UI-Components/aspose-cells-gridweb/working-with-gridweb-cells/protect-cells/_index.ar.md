---
title: حماية Cells
type: docs
weight: 50
url: /ar/net/protect-cells/
---
{{% alert color="primary" %}} 

يصف هذا الموضوع بعض الأساليب لحماية الخلايا. يسمح استخدام هذه الأساليب للمطورين بتقييد المستخدمين من تحرير كل أو نطاق محدد من الخلايا في ورقة العمل.

{{% /alert %}} 
## **حماية Cells**
 Aspose.Cells.GridWeb يوفر بعض التقنيات المختلفة للتحكم في مستوى الحماية على الخلايا عندما يكون عنصر التحكم في[وضع التحرير](/cells/ar/net/enable-different-gridweb-modes/#edit-mode) (الوضع الافتراضي). هذا يحمي الخلايا من التعديل من قبل المستخدمين النهائيين.
### **جعل الكل Cells للقراءة فقط**
لتعيين جميع الخلايا في ورقة العمل للقراءة فقط ، قم باستدعاء أسلوب SetAllCellsReadonly الخاص بورقة العمل.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **جعل كل Cells قابل للتحرير**
لإزالة الحماية من جميع الخلايا ، قم باستدعاء أسلوب SetAllCellsEditable الخاص بورقة العمل. هذه الطريقة لها تأثير معاكس لأسلوب SetAllCellsReadonly.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **جعل Cells المحدد للقراءة فقط**
لحماية نطاق من الخلايا فقط:

1. أولاً ، اجعل جميع الخلايا قابلة للتحرير عن طريق استدعاء طريقة SetAllCellsEditable.
1. حدد نطاق الخلايا المطلوب حمايتها عن طريق استدعاء أسلوب SetReadonlyRange الخاص بورقة العمل. تأخذ هذه الطريقة عدد الصفوف والأعمدة لتحديد نطاق الخلايا.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **جعل مختارة Cells قابلة للتحرير**
لإلغاء حماية نطاق من الخلايا:

1. اجعل كل الخلايا مقروءة فقط عن طريق استدعاء الأسلوب SetAllCellsReadonly.
1. حدد نطاق الخلايا التي يمكن تحريرها عن طريق استدعاء أسلوب SetEditableRange الخاص بورقة العمل. تأخذ هذه الطريقة عدد الصفوف والأعمدة لتحديد نطاق الخلايا.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}
