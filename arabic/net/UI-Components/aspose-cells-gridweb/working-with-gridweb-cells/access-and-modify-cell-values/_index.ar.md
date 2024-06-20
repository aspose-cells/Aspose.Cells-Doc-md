---
title: الوصول وتعديل قيمة الخلية
type: docs
weight: 20
url: /ar/net/aspose-cells-gridweb/access-and-modify-cell-value/
keywords: GridWeb، قيمة الخلية، تعديل، قيمة
description: يقدم هذا المقال كيفية الحصول على قيمة الخلية وتعديلها في GridWeb.
---

{{% alert color="primary" %}} 

[الوصول إلى خلايا ورق العمل](/cells/ar/net/aspose-cells-gridweb/access-worksheet-cells/) تناول الوصول إلى الخلايا. يوسع هذا الموضوع تلك المناقشة ليظهر كيفية الوصول وتعديل قيم الخلية باستخدام واجهة برمجة تطبيقات Aspose.Cells.GridWeb.

{{% /alert %}} 
## **الوصول وتعديل قيمة الخلية**
### **قيم السلاسل**
قبل الوصول وتعديل قيمة الخلية، يجب عليك معرفة كيفية الوصول إلى الخلايا. لمزيد من التفاصيل حول الطرق المختلفة للوصول إلى الخلايا، راجع [الوصول إلى خلايا ورق العمل](/cells/ar/net/aspose-cells-gridweb/access-worksheet-cells/).

كل خلية لها خاصية تسمى StringValue. بمجرد الوصول إلى الخلية، يمكن للمطورين استخدام خاصية StringValue للوصول إلى قيمة السلسلة للخلايا. لتعديل قيم الخلايا، يتوفر طريقة خاصة تسمى PutValue والتي يمكن استخدامها لتحديث قيمة السلسلة للخلية.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellStringValue.cs" >}}
### **جميع أنواع القيم**
طريقة PutValue لكائن الخلية تحتوي على 8 تحديثات متوفرة يمكن استخدامها لتعديل أي نوع من القيم (قيمة منطقية، عدد صحيح، عدد عشري، التاريخ والوقت والسلسلة) في خلية.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellIntValue.cs" >}}



هناك أيضًا نسخة محملة من طريقة PutValue يمكن أن تأخذ أي نوع من القيم في شكل سلسلة وتحويلها إلى نوع بيانات صحيح تلقائيًا. لجعل هذا يحدث، يتم تمرير قيمة المنطقية true إلى معلمة أخرى لطريقة PutValue كما هو موضح أدناه في المثال.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellDoubleValue.cs" >}}
