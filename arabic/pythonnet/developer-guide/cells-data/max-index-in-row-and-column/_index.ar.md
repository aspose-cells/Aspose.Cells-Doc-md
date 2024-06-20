---
title: الحصول على الحد الأقصى لمؤشر العمود في الصف والحد الأقصى لمؤشر الصف في العمود
type: docs
weight: 600
url: /ar/python-net/get-max-index-in-row-and-column/
description: تعلم كيفية الحصول على الحد الأقصى لمؤشر العمود في الصف والحد الأقصى لمؤشر الصف في العمود من خلال واجهة برمجة التطبيقات Aspose.Cells لـ Python via .NET.
keywords: مكتبة إكسيل بلغة Python، الحصول على الحد الأقصى لمؤشر العمود في الصف باستخدام Python، الحصول على الحد الأقصى لمؤشر الصف في العمود باستخدام Python، الحصول على الحد الأقصى لمؤشر البيانات في الصف باستخدام Python، الحصول على الحد الأقصى لمؤشر الصف البيانات في العمود باستخدام Python. 
---

## **سيناريوهات الاستخدام المحتملة**
عندما تحتاج فقط إلى التلاعب ببعض البيانات في الصفوف أو الأعمدة، تحتاج إلى معرفة نطاق البيانات للصفوف والأعمدة. تقدم Aspose.Cells لـ Python via .NET هذه الميزة. للحصول على الحد الأقصى لمؤشر العمود في صف، يمكنك الحصول على خاصية [Row.last_cell](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_cell/) و [Row.last_data_cell](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_data_cell/)، ثم استخدام الخاصية [Cell.column](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/) للحصول على الحد الأقصى لمؤشر العمود والحد الأقصى لمؤشر البيانات على العمود. ولكن من أجل الحصول على الحد الأقصى لمؤشر الصف والحد الأقصى لمؤشر بيانات الصف في العمود، تحتاج إلى إنشاء نطاق على العمود، ثم عبر النطاق للعثور على الخلية الأخيرة، وأخيرًا الحصول على [Cell.row](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/) على الخلية.

توفر Aspose.Cells لـ Python via .NET الخصائص والطرق التالية لمساعدتك في تحقيق أهدافك.
- [**Row.last_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_cell/)
- [**Row.last_data_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_data_cell/)
- [**Cell.column**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/)
- [**Cell.row**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/)

## **الحصول على الحد الأقصى لمؤشر العمود في الصف والحد الأقصى لمؤشر الصف في العمود باستخدام واجهة برمجة التطبيقات Aspose.Cells لـ Python**
يوضح هذا المثال كيف:

1. قم بتحميل [ملف العينة](sample.xlsx).
2. الحصول على الصف الذي يحتاج إلى الحصول على الحد الأقصى لمؤشر العمود والحد الأقصى لمؤشر البيانات في العمود.
1. احصل على سمة [Cell.column](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/) على الخلية.
1. أنشئ نطاقًا استنادًا إلى العمود.
1. احصل على المحدد وانتقل عبر النطاق.
1. احصل على سمة [Cell.row](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/) على الخلية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Cells-max-index-of-row-and-column.py" >}}
