---
title: حماية الخلايا
type: docs
weight: 50
url: /ar/net/aspose-cells-gridweb/protect-cells/
keywords: تُقدم GridWeb طرقًا مختلفة لحماية الخلايا وضبط مستوى الحماية عندما يكون التحكم في [وضع التحرير](/cells/ar/net/aspose cells gridweb/enable different gridweb modes/#edit mode) (الوضع الافتراضي). يحمي هذا الخلايا من التعديل من قبل المستخدمين النهائيين.
description: يعرض هذا المقال كيفية حماية الخلايا في GridWeb.
---

{{% alert color="primary" %}} 

يصف هذا الموضوع بعض التقنيات لحماية الخلايا. باستخدام هذه التقنيات، يُمكن للمطورين تقييد مستخدمي القيام بتحرير كل الخلايا أو نطاق محدد من الخلايا في ورق العمل.

{{% /alert %}} 
## **حماية الخلايا**
يوفر Aspose.Cells.GridWeb تقنيات مختلفة للتحكم في مستوى الحماية على الخلايا عندما يكون التحكم في [وضع التحرير](/cells/ar/net/aspose-cells-gridweb/enable-different-gridweb-modes/#edit-mode) (الوضع الافتراضي). يحمي هذا الخلايا من التعديل من قبل المستخدمين النهائيين.
### **جعل جميع الخلايا للقراءة فقط**
لتعيين جميع الخلايا في ورقة عمل للقراءة فقط، اتصل بطريقة SetAllCellsReadonly للورقة العمل.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **جعل جميع الخلايا قابلة للتحرير**
لإزالة الحماية من جميع الخلايا، اتصل بطريقة SetAllCellsEditable للورقة العمل. تُعد هذه الطريقة لها التأثير المعاكس لطريقة SetAllCellsReadonly.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **جعل الخلايا المحددة للقراءة فقط**
لحماية نطاق محدد من الخلايا:

1. اجعل جميع الخلايا قابلة للتحرير أولاً باستدعاء طريقة SetAllCellsEditable.
1. حدد نطاق الخلايا المراد حمايته باستدعاء طريقة SetReadonlyRange للورقة العمل. تأخذ هذه الطريقة عدد الصفوف والأعمدة لتحديد نطاق الخلايا.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **جعل الخلايا المحددة قابلة للتحرير**
لإلغاء الحماية عن نطاق محدد من الخلايا:

1. قم بجعل جميع الخلايا للقراءة فقط من خلال استدعاء أسلوب SetAllCellsReadonly.
1. حدد نطاق الخلايا التي يمكن تحريرها من خلال استدعاء أسلوب SetEditableRange للورقة العمل. يأخذ هذا الأسلوب عدد الصفوف والأعمدة لتحديد نطاق الخلايا.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}
