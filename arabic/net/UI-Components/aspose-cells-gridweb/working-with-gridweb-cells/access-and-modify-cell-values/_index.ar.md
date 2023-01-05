---
title: الوصول إلى وتعديل Cell القيم
type: docs
weight: 20
url: /ar/net/access-and-modify-cell-values/
---
{{% alert color="primary" %}} 

[ورقة عمل الوصول Cells](/cells/ar/net/access-worksheet-cells/) ناقش الوصول إلى الخلايا. يوسع هذا الموضوع المناقشة لإظهار كيفية الوصول إلى قيم الخلايا وتعديلها باستخدام Aspose.Cells.GridWeb API.

{{% /alert %}} 
## **الوصول إلى قيمة Cell وتعديلها**
### **قيم السلسلة**
 قبل الوصول إلى قيمة الخلية وتعديلها ، تحتاج إلى معرفة كيفية الوصول إلى الخلايا. للحصول على تفاصيل حول الأساليب المختلفة للوصول إلى الخلايا ، يرجى الرجوع إلى[ورقة عمل الوصول Cells](/cells/ar/net/access-worksheet-cells/).

كل خلية لها خاصية تسمى StringValue. بمجرد الوصول إلى الخلية ، يمكن للمطورين استخدام خاصية StringValue للوصول إلى قيمة سلسلة الخلايا. لتعديل قيم الخلية ، يتم توفير طريقة خاصة PutValue ، والتي يمكن استخدامها لتحديث قيمة سلسلة الخلية.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellStringValue.cs" >}}
### **جميع أنواع القيم**
تحتوي طريقة PutValue لكائن الخلية على 8 حمولات زائدة متاحة والتي يمكن استخدامها لتعديل أي نوع من القيم (Boolean و int و double و DateTime و string) في الخلية.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellIntValue.cs" >}}



هناك أيضًا نسخة محملة بشكل زائد من طريقة PutValue يمكن أن تأخذ أي نوع من القيمة في تنسيق سلسلة وتحويلها إلى نوع بيانات مناسب تلقائيًا. لتحقيق ذلك ، قم بتمرير القيمة المنطقية true إلى معلمة أخرى لطريقة PutValue كما هو موضح أدناه في المثال.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellDoubleValue.cs" >}}
