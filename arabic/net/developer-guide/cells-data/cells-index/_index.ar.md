---
title: الحصول على فهرس الخلايا
type: docs
weight: 600
url: /ar/net/get-cells-index/
description: تعلم كيفية الحصول على صف أو عمود بواسطة اسم الصف، العمود أو الخلايا. تحويل اسم الخلية إلى فهرس صف وعمود بنظام العد القائم على الصفر.
keywords: الحصول على فهرس الصف والعمود بواسطة اسم الخلية، الحصول على فهرس العمود بواسطة اسم العمود، الحصول على فهرس الصف بواسطة اسم الصف، الحصول على الفهرس بواسطة اسم الخلية. 
---

{{% alert color="primary" %}}
العرض الافتراضي لإكسل هو إعادة النظر في نمط A1 المرجعي، حيث يتم تعريف كل عمود بأحرف A وB وC...، وتسمى الخلايا A1 وB2 وC3... وهكذا.
قد ترغب في معرفة الصف والعمود الذي يحتوي هذه الخلية فيه.

{{% /alert %}}


## **سيناريوهات الاستخدام المحتملة**
عندما تحتاج إلى تعديل بيانات معينة على ورقة العمل بواسطة مؤشر الصف والعمود فقط، تحتاج إلى معرفة مؤشر الصف والعمود لتلك الخلية المحددة. 
تقدم Aspose.Cells هذه الميزة للحصول على فهرس الصف والعمود بواسطة اسم الصف، العمود والخلية. 
Aspose.Cells توفر الخصائص والأساليب التالية للمساعدة في تحقيق أهدافك.
- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)

ملحوظة: الفهرسة في أسبوز.خلايا ل .نت تبدأ من الصفر، لكن معرف الصف يبدأ من الواحد في برنامج إم إس إكسل.

## **الحصول على فهارس الخلايا باستخدام Aspose.Cells**
يوضح هذا المثال كيف:

1. إنشاء دفتر عمل وإضافة بعض البيانات.
1. العثور على الخلية المحددة في الورقة العمل الأولى.
1. الحصول على مؤشر الصف والعمود بواسطة اسم الخلية.
1. الحصول على مؤشر العمود بواسطة اسم العمود.
1. الحصول على مؤشر الصف بواسطة اسم الصف.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-get-index.cs" >}}
