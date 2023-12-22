---
title: احصل على مؤشر الحد الأقصى للعمود في الصف ومؤشر الصف الأقصى في العمود
type: docs
weight: 600
url: /ar/net/get-max-index-in-row-and-column/
description: تعرف على كيفية الحصول على مؤشر الحد الأقصى للعمود في الصف ومؤشر الصف الأقصى في العمود من خلال Aspose.Cells for .NET API.
keywords: Get Max Column Index in Row, Get Max Row Index in Column, Get Max Data Column Index in Row, Get Max Data Row Index in Column. 
---
##  **سيناريوهات الاستخدام المحتملة**
عندما تحتاج فقط إلى معالجة بعض البيانات الموجودة في الصفوف أو الأعمدة، فأنت بحاجة إلى معرفة نطاق بيانات الصفوف والأعمدة. Aspose.Cells يقدم هذه الميزة. للحصول على الحد الأقصى لفهرس الأعمدة على التوالي، يمكنك الحصول على[Row.LastCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/) و[Row.LastDataCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/) الخصائص، ثم استخدم[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) الخاصية للحصول على الحد الأقصى لفهرس العمود والحد الأقصى لفهرس عمود البيانات. ولكن للحصول على الحد الأقصى لفهرس الصف والحد الأقصى لفهرس بيانات الصف في عمود، فأنت بحاجة إلى إنشاء نطاق في العمود، ثم اجتياز النطاق للعثور على الخلية الأخيرة، وأخيرًا الحصول على[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) السمة على الخلية.

Aspose.Cells يوفر الخصائص والأساليب التالية لمساعدتك في تحقيق أهدافك.
- [**Row.LastCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**Row.LastDataCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

##  **احصل على مؤشر الحد الأقصى للعمود في الصف ومؤشر الصف الأقصى في العمود باستخدام Aspose.Cells**
يوضح هذا المثال كيفية:

1.  حمل ال[ملف عينة](sample.xlsx).
1. احصل على الصف الذي يحتاج إلى الحصول على الحد الأقصى لفهرس العمود والحد الأقصى لفهرس عمود البيانات.
1.  يحصل[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) السمة على الخلية.
1. إنشاء نطاق على أساس العمود.
1. احصل على المكرر ونطاق الاجتياز.
1.  يحصل[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) السمة على الخلية.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}