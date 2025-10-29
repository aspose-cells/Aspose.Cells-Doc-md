---
title: الحصول على فهرس الخلايا
type: docs
weight: 600
url: /ar/python-net/get-cells-index/
description: تعلم كيفية الحصول على صف أو عمود بواسطة اسم الصف من خلال Aspose.Cells for Python via .NET API، العمود أو الخلايا. تحويل اسم الخلية إلى فهرس الصف والعمود بناءً على Aspose.Cells for Python via .NET API.
keywords: Python Excel, الحصول على فهرس الصف والعمود باسم الخلية باستخدام Python, الحصول على فهرس العمود بواسطة اسم العمود باستخدام Python, الحصول على فهرس الصف بواسطة اسم الصف باستخدام Python, الحصول على الفهرس بواسطة اسم الخلية باستخدام Python. 
---

{{% alert color="primary" %}}
العرض الافتراضي لإكسل هو إعادة النظر في نمط A1 المرجعي، حيث يتم تعريف كل عمود بأحرف A وB وC...، وتسمى الخلايا A1 وB2 وC3... وهكذا.
قد ترغب في معرفة الصف والعمود الذي يحتوي هذه الخلية فيه.

{{% /alert %}}


## **سيناريوهات الاستخدام المحتملة**
عندما تحتاج إلى تعديل بيانات معينة على ورقة العمل بواسطة مؤشر الصف والعمود فقط، تحتاج إلى معرفة مؤشر الصف والعمود لتلك الخلية المحددة. 
تقدم Aspose.Cells لـ Python via .NET هذه الميزة للحصول على مؤشر الصف والعمود بواسطة اسم الصف والعمود والخلية. 
توفر Aspose.Cells لـ Python via .NET الخصائص والطرق التالية لمساعدتك في تحقيق أهدافك.
- [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any)
- [**CellsHelper.column_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_index_to_name/#int)
- [**CellsHelper.column_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_name_to_index/#str)
- [**CellsHelper.row_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_index_to_name/#int)
- [**CellsHelper.row_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_name_to_index/#str)

ملاحظة: تكون الترقيمات بناءً على الصفر في Aspose.Cells لـ Python via .NET، ولكن معرف الصف يكون بناءاً على الواحد في MS Excel.

## **الحصول على مؤشرات الخلايا باستخدام مكتبة Aspose.Cells لـ Python Excel**
يوضح هذا المثال كيف:

1. إنشاء دفتر عمل وإضافة بعض البيانات.
1. العثور على الخلية المحددة في الورقة العمل الأولى.
1. الحصول على مؤشر الصف والعمود بواسطة اسم الخلية.
1. الحصول على مؤشر العمود بواسطة اسم العمود.
1. الحصول على مؤشر الصف بواسطة اسم الصف.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-get-index.py" >}}
{{< app/cells/assistant language="python-net" >}}
