---
title: احصل على مؤشر Cells
type: docs
weight: 600
url: /ar/net/get-cells-index/
description: تعرف على كيفية إدخال الصف أو العمود باسم الصف أو العمود أو الخلايا. تحويل اسم الخلية إلى فهرس الصف والعمود على أساس صفري.
keywords: Get Row index and Column index by the name of the cell, Get Column index by the name of the column, Get Row index by the name of the row, Get the index by the name of cell. 
---
{{% alert color="primary" %}}
العرض الافتراضي لبرنامج Excel هو مرجع نمط A1، ويتم تعريف كل عمود على أنه A وB وC.... ويتم تسمية الخلايا باسم A1 وB2 وC3... وما إلى ذلك.
قد ترغب في معرفة الصف والعمود الذي توجد به هذه الخلية.

{{% /alert %}}


##  **سيناريوهات الاستخدام المحتملة**
 عندما تحتاج فقط إلى معالجة بيانات محددة في ورقة العمل حسب فهرس الصفوف والأعمدة، فإنك تحتاج إلى معرفة فهارس الأعمدة والأعمدة لتلك الخلية المحددة.
 Aspose.Cells يوفر هذه الميزة للحصول على فهرس الصفوف والأعمدة حسب اسم الصف والعمود والخلية.
Aspose.Cells يوفر الخصائص والأساليب التالية لمساعدتك في تحقيق أهدافك.
- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)

ملحوظة: الفهرسة تعتمد على الصفر في Aspose.Cells لـ .Net، لكن معرف الصف يعتمد على واحد في MS Excel.

##  **احصل على فهارس Cells باستخدام Aspose.Cells**
يوضح هذا المثال كيفية:

1. إنشاء مصنف وإضافة بعض البيانات.
1. ابحث عن الخلية المحددة في ورقة العمل الأولى.
1. احصل على فهرس الصف وفهرس العمود حسب اسم الخلية.
1. احصل على فهرس العمود حسب اسم العمود.
1. احصل على فهرس الصف حسب اسم الصف.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-get-index.cs" >}}