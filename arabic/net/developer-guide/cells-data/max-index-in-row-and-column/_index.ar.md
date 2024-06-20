---
title: الحصول على الحد الأقصى لمؤشر العمود في الصف والحد الأقصى لمؤشر الصف في العمود
type: docs
weight: 600
url: /ar/net/get-max-index-in-row-and-column/
description: تعلم كيفية الحصول على مؤشر العمود الأقصى في الصف ومؤشر الصف الأقصى في العمود من خلال واجهة Aspose.Cells for .NET API.
keywords: الحصول على مؤشر العمود الأقصى في الصف، الحصول على مؤشر الصف الأقصى في العمود، الحصول على مؤشر البيانات العمود الأقصى في الصف، الحصول على مؤشر بيانات الصف الأقصى في العمود. 
---

## **سيناريوهات الاستخدام المحتملة**
عندما تحتاج فقط إلى التلاعب ببعض البيانات على الصفوف أو الأعمدة، تحتاج إلى معرفة نطاق البيانات للصفوف والأعمدة. Aspose.Cells توفر هذه الميزة. للحصول على مؤشر العمود الأقصى في صف، يمكنك الحصول على خصائص [Row.LastCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/) و[Row.LastDataCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)، ثم استخدام خاصية [Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) للحصول على مؤشر العمود الأقصى ومؤشر البيانات العمودية الأقصى. ولكن للحصول على مؤشر الصف الأقصى ومؤشر بيانات الصف الأقصى في العمود، تحتاج إلى إنشاء نطاق على العمود، ثم عبور النطاق للعثور على آخر خلية، وأخيرًا الحصول على السمة [Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) على الخلية.

Aspose.Cells توفر الخصائص والأساليب التالية للمساعدة في تحقيق أهدافك.
- [**Row.LastCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**Row.LastDataCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

## **الحصول على مؤشر العمود الأقصى في الصف ومؤشر الصف الأقصى في العمود باستخدام Aspose.Cells**
يوضح هذا المثال كيف:

1. قم بتحميل [ملف العينة](sample.xlsx).
2. الحصول على الصف الذي يحتاج إلى الحصول على الحد الأقصى لمؤشر العمود والحد الأقصى لمؤشر البيانات في العمود.
1. الحصول على سمة الخلية [Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/).
1. أنشئ نطاقًا استنادًا إلى العمود.
1. احصل على المحدد وانتقل عبر النطاق.
1. الحصول على سمة الخلية [Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}
