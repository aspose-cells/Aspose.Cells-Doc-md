---
title: الأسماء والمؤشرات
type: docs
weight: 10
url: /ar/cpp/names-and-indices/
---
## **احصل على Cell الاسم من فهارس الصفوف والأعمدة**
من الممكن العثور على اسم الخلية في ضوء فهرس الصف والعمود. يشرح هذا المقال كيف.
يوفر Aspose.Cells طريقة ICellsHelper.CellIndexToName_i التي تسمح للمطورين بالحصول على اسم الخلية إذا قاموا بتوفير فهرس الصف والعمود.

{{% alert color="primary" %}} 

بخلاف Microsoft Excel ، حيث تبدأ فهارس الصفوف والأعمدة من 1 ، يبدأ Aspose.Cells عد فهارس الصفوف والأعمدة من 0.

{{% /alert %}} 

يوضح نموذج التعليمات البرمجية التالي كيفية استخدام ICellsHelper.CellIndexToName_i للوصول إلى اسم الخلية المعطى فهرس صف وعمود معروف. يولد الكود الناتج التالي.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn.cpp" >}}
## **احصل على فهارس الصفوف والأعمدة من Cell الاسم**
من الممكن العثور على فهرس صف وعمود للخلية من اسمها. يشرح هذا المقال كيف.
يوفر Aspose.Cells طريقة ICellsHelper.CellNameToIndex_i التي تسمح للمطورين بالحصول على فهرس صف وعمود من اسم الخلية.

{{% alert color="primary" %}} 

بخلاف Microsoft Excel ، حيث تبدأ فهارس الصفوف والأعمدة من 1 ، يبدأ Aspose.Cells عد فهارس الصفوف والأعمدة من 0.

{{% /alert %}} 

يوضح نموذج التعليمات البرمجية التالي كيفية استخدام CellsHelper.CellNameToIndex للحصول على فهرس الصف والعمود من اسم الخلية. يولد الكود الناتج التالي.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName.cpp" >}}
