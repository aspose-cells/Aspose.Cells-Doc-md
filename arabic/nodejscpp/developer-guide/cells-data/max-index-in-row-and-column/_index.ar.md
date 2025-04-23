---
title: الحصول على الحد الأقصى لمؤشر العمود في الصف والحد الأقصى لمؤشر الصف في العمود
type: docs
weight: 600
url: /ar/nodejs-cpp/get-max-index-in-row-and-column/
description: تعرف على كيفية الحصول على أقصى فهرس عمود في الصف وأقصى فهرس صف في العمود من خلال API Aspose.Cells for Node.js via C++.
keywords: الحصول على أقصى فهرس عمود في الصف عبر Node.js باستخدام C++، الحصول على أقصى فهرس صف في العمود عبر Node.js باستخدام C++, الحصول على أقصى فهرس عمود للبيانات في الصف عبر Node.js باستخدام C++, الحصول على أقصى فهرس صف للبيانات في العمود عبر Node.js باستخدام C++.
---

## **سيناريوهات الاستخدام المحتملة**
عندما تحتاج فقط إلى تعديل بعض البيانات في الصفوف أو الأعمدة، من الضروري معرفة مدى البيانات للصفوف والأعمدة. تقدم Aspose.Cells for Node.js via C++ هذه الميزة. للحصول على الحد الأقصى لفهرس العمود في الصف، يمكنك استخدام طريقتي [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--) و [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--)، ثم استخدام طريقة [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--) للحصول على الحد الأقصى لفهرس العمود وفهرس البيانات للعمود. لكن من أجل الحصول على أقصى فهرس صف وفهرس بيانات الصف في العمود، تحتاج إلى إنشاء نطاق على العمود، ثم استعراض النطاق للعثور على آخر خلية، وأخيرًا استدعاء طريقة [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--) على الخلية.

تقدم Aspose.Cells for Node.js via C++ الخصائص والطرق التالية لمساعدتك على تحقيق أهدافك.
- [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--)
- [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--)
- [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--)
- [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--)

## **الحصول على أقصى فهرس عمود في الصف وأقصى فهرس صف في العمود**
يوضح هذا المثال كيف:

1. قم بتحميل [ملف العينة](sample.xlsx).
2. الحصول على الصف الذي يحتاج إلى الحصول على الحد الأقصى لمؤشر العمود والحد الأقصى لمؤشر البيانات في العمود.
1. استدعاء طريقة [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--) على الخلية.
1. أنشئ نطاقًا استنادًا إلى العمود.
1. احصل على المحدد وانتقل عبر النطاق.
1. استدعاء طريقة [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--) على الخلية.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-max-index-in-row-and-column.js" >}}

