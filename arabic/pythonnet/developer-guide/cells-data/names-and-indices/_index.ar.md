---
title: التحويل بين اسم الخلية ومؤشر الصف / العمود
linktitle: تحويل اسم الخلية ومؤشرها
type: docs
weight: 10
url: /ar/python-net/names-and-indices/
description: تعلم كيفية الحصول على التحويل بين اسم الخلية ومؤشر الصف / العمود من خلال Aspose.Cells for Python via .NET API.
keywords: مكتبة Python Excel ، Python الحصول على اسم الخلية من مؤشرات الصف والعمود ، Python الحصول على مؤشرات الصف والعمود من اسم الخلية ، Python إنشاء أسماء ورق العمل الآمنة ، Python إضافة أسماء ورق العمل الآمنة
---

## **الحصول على اسم الخلية من مؤشرات الصف والعمود**
من الممكن العثور على اسم الخلية مع الاعتماد على مؤشرات الصف والعمود. يشرح هذا المقال كيفية ذلك.
Aspose.Cells for Python via .NET توفر الطريقة [**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int) التي تسمح للمطورين بالحصول على اسم الخلية إذا قدموا مؤشرات الصف والعمود.

{{% alert color="primary" %}} 

على عكس Microsoft Excel، حيث تبدأ فهارس الصفوف والأعمدة من 1، تبدأ Aspose.Cells for Python via .NET في عد الفهارس للصفوف والأعمدة من 0.

{{% /alert %}} 

الكود العيني التالي يوضح كيفية استخدام [**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int) للوصول إلى اسم الخلية بناءً على فهرس الصف والعمود المعروف. يولد الكود الناتج التالي.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-IndexToName-1.py" >}}

## **الحصول على فهارس الصفوف والأعمدة من اسم الخلية**
من الممكن العثور على فهرس الصف والعمود للخلية من اسمها. يشرح هذا المقال كيفية ذلك.
يوفر Aspose.Cells for Python via .NET الطريقة [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any) التي تسمح للمطورين بالحصول على فهرس الصف والعمود من اسم الخلية.

{{% alert color="primary" %}} 

على عكس Microsoft Excel، حيث تبدأ فهارس الصفوف والأعمدة من 1، تبدأ Aspose.Cells for Python via .NET في عد الفهارس للصفوف والأعمدة من 0.

{{% /alert %}} 

الكود العيني التالي يوضح كيفية استخدام [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any) للحصول على فهرس الصف والعمود من اسم الخلية. يولد الكود الناتج التالي.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-NameToIndex-1.py" >}}

## **إنشاء أسماء صفحات آمنة**
أحيانًا هناك حاجة لتعيين اسم الصفحة أثناء التشغيل. في هذ scenfile النيو ، قد تحتوي أسماء الصفحات على بعض الأحرف الإضافية مثل <>+(?”. هناك حاجة لاستبدال أي حرف من هذا القبيل، والذي لا يُسمح باسم الصفحة بحرف محدد مسبقًا مقدم من المستخدم. بالمثل قد يزيد الطول إلى أكثر من 31 حرفًا يجب مقارعته. توفر Apache POI بعض الميزات لإنشاء الأسماء الآمنة، وبالتالي يوفر Aspose.Cells for Python via .NET ميزة مماثلة للتعامل مع كل هذه المشاكل. يوضح الكود العيني التالي هذه الميزة:



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-CreateSafeSheetNames.py" >}}

الإخراج:

هذا هو الاسم الأول الذي تم إنشاؤه

` `<> + (adj.Private _ " خاص"
{{< app/cells/assistant language="python-net" >}}
