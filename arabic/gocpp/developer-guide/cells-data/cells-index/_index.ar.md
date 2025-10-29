---
title: الحصول على فهرس الخلايا باستخدام Golang عبر C++
linktitle: الحصول على فهرس الخلايا
type: docs
weight: 600
url: /ar/go-cpp/get-cells-index/
description: تعلم كيفية الحصول على فهرس الصف أو العمود باسم الصف أو العمود أو الخلايا. تحويل اسم الخلية إلى فهرس الصف والعمود من البداية باستخدام Aspose.Cells مع Golang عبر C++.
keywords: الحصول على فهرس الصف والعمود بواسطة اسم الخلية، الحصول على فهرس العمود بواسطة اسم العمود، الحصول على فهرس الصف بواسطة اسم الصف، الحصول على الفهرس بواسطة اسم الخلية.
---

{{% alert color="primary" %}}
العرض الافتراضي لExcel هو مرجع نمط A1، حيث يُعرف كل عمود بالحرف A و B و C ....، وتُسمى الخلايا A1 و B2 و C3 ... وهلم جرا.
قد ترغب في معرفة أي صف وعمود تحتوي عليه هذه الخلية.

{{% /alert %}}

## **سيناريوهات الاستخدام المحتملة**

عندما تحتاج فقط إلى التلاعب ببيانات معينة على ورقة العمل بواسطة فهرس الصف والعمود، تحتاج إلى معرفة فهارس الصف والعمود لتلك الخلية المحددة.
تقدم Aspose.Cells هذه الميزة للحصول على فهرس الصف والعمود بواسطة اسم الصف والعمود والخلية.
توفر Aspose.Cells الخصائص والأساليب التالية لمساعدتك على تحقيق أهدافك:

- [**CellsHelper::CellNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/cellnametoindex/)
- [**CellsHelper::ColumnIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnindextoname/)
- [**CellsHelper::ColumnNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnnametoindex/)
- [**CellsHelper::RowIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/rowindextoname/)
- [**CellsHelper::RowNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/rownametoindex/)

ملاحظة: الفهرسة تبدأ من الصفر في Aspose.Cells for C++، ولكن معرف الصف يبدأ من واحد في MS Excel.

## **الحصول على فهارس الخلايا باستخدام Aspose.Cells**

يوضح هذا المثال كيف:

1. إنشاء دفتر عمل وإضافة بعض البيانات.
1. العثور على الخلية المحددة في الورقة العمل الأولى.
1. الحصول على مؤشر الصف والعمود بواسطة اسم الخلية.
1. الحصول على مؤشر العمود بواسطة اسم العمود.
1. الحصول على مؤشر الصف بواسطة اسم الصف.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsIndex.go" >}}
