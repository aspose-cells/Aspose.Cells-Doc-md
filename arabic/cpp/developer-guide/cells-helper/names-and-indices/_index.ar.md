---
title: الأسماء والفهارس
type: docs
weight: 10
url: /ar/cpp/names-and-indices/
---

## **الحصول على اسم الخلية من مؤشرات الصف والعمود**
من الممكن العثور على اسم الخلية مع الاعتماد على مؤشرات الصف والعمود. يشرح هذا المقال كيفية ذلك.
توفر Aspose.Cells [CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/) الأسلوب الذي يسمح للمطورين بالحصول على اسم الخلية إذا قدموا فهرس الصف والعمود.

{{% alert color="primary" %}} 

على عكس Microsoft Excel، حيث تبدأ فهارس الصف والعمود من 1، تبدأ Aspose.Cells في عد فهارس الصف والعمود من 0.

{{% /alert %}} 

يوضح الشيفرة النموذجية التالية كيفية استخدام [CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/) للوصول إلى اسم الخلية مع مؤشر الصف والعمود المعروف. تولد الشيفرة النموذجية الناتج التالي.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn-new.cpp" >}}
## **الحصول على فهارس الصفوف والأعمدة من اسم الخلية**
من الممكن العثور على فهرس الصف والعمود للخلية من اسمها. يشرح هذا المقال كيفية ذلك.
يوفر Aspose.Cells [CellsHelper.CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/) الأسلوب الذي يسمح للمطورين بالحصول على فهرس الصف والعمود من اسم الخلية.

{{% alert color="primary" %}} 

على عكس Microsoft Excel، حيث تبدأ فهارس الصف والعمود من 1، تبدأ Aspose.Cells في عد فهارس الصف والعمود من 0.

{{% /alert %}} 

الشيفرة النموذجية التالية توضح كيفية استخدام [CellsHelper::CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/) للحصول على فهرس الصف والعمود من اسم الخلية. تولد الشيفرة النموذجية الناتج التالي.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
