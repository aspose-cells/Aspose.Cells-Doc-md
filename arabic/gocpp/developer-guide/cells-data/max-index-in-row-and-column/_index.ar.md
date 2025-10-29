---
title: الحصول على مؤشر العمود الأقصى في الصف ومؤشر الصف الأقصى في العمود باستخدام Golang عبر C++
linktitle: الحصول على الحد الأقصى لمؤشر العمود في الصف والحد الأقصى لمؤشر الصف في العمود
type: docs
weight: 600
url: /ar/go-cpp/get-max-index-in-row-and-column/
description: تعرف على كيفية الحصول على أقصى فهرس عمود في الصف وأقصى فهرس صف في العمود من خلال API Aspose.Cells for C++.
keywords: الحصول على مؤشر العمود الأقصى في الصف، الحصول على مؤشر الصف الأقصى في العمود، الحصول على مؤشر البيانات العمود الأقصى في الصف، الحصول على مؤشر بيانات الصف الأقصى في العمود.
---

## **سيناريوهات الاستخدام المحتملة**
عندما تحتاج فقط إلى التلاعب ببيانات في الصفوف أو الأعمدة، تحتاج إلى معرفة نطاق البيانات الخاص بالصفوف والأعمدة. تقدم Aspose.Cells هذه الميزة. للحصول على مؤشر العمود الأقصى في صف، يمكنك الحصول على خصائص [Row.GetLastCell()](https://reference.aspose.com/cells/go-cpp/row/getlastcell/) و [Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/)، ثم استخدام خاصية [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) للحصول على مؤشر العمود الأقصى ومؤشر عمود البيانات الأقصى. ولكن من أجل الحصول على مؤشر الصف الأقصى ومؤشر بيانات الصف الأقصى على عمود، تحتاج إلى إنشاء نطاق على العمود، ثم التمرن عبر النطاق للعثور على الخلية الأخيرة، وأخيرًا الحصول على السمة [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) على الخلية.

Aspose.Cells توفر الخصائص والأساليب التالية للمساعدة في تحقيق أهدافك.
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/go-cpp/cell/getrow/)

## **الحصول على مؤشر العمود الأقصى في الصف ومؤشر الصف الأقصى في العمود باستخدام Aspose.Cells**
يوضح هذا المثال كيف:

1. قم بتحميل [ملف العينة](sample.xlsx).
2. الحصول على الصف الذي يحتاج إلى الحصول على الحد الأقصى لمؤشر العمود والحد الأقصى لمؤشر البيانات في العمود.
1. الحصول على سمة [Cell.GetColumn()](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/) على الخلية.
1. أنشئ نطاقًا استنادًا إلى العمود.
1. احصل على المحدد وانتقل عبر النطاق.
1. الحصول على سمة [Cell.GetRow()](https://reference.aspose.com/cells/go-cpp/cell/getrow/) على الخلية.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MaxIndexInRowAndColumn.go" >}}
