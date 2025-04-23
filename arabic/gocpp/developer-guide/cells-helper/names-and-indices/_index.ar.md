---
title: الأسماء والفهارس
type: docs
weight: 10
url: /ar/go-cpp/names-and-indices/
---

## **الحصول على اسم الخلية من مؤشرات الصف والعمود**

من الممكن العثور على اسم الخلية مع الاعتماد على مؤشرات الصف والعمود. يشرح هذا المقال كيفية ذلك.
توفر Aspose.Cells طريقة [CellsHelper_CellIndexToName](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellindextoname/)، التي تتيح للمطورين الحصول على اسم الخلية إذا قدموا فهرس الصف والعمود.

{{% alert color="primary" %}}

على عكس Microsoft Excel، حيث تبدأ فهارس الصف والعمود من 1، تبدأ Aspose.Cells في عد فهارس الصف والعمود من 0.

{{% /alert %}}

يُوضح الكود النموذجي التالي كيفية استخدام [CellsHelper_CellIndexToName](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellindextoname/) للوصول إلى اسم خلية معين من خلال معرف الصف والعمود. يُنتج الكود المخرجات التالية.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetCellNameFromRowAndColumn.go" >}}

## **الحصول على فهارس الصفوف والأعمدة من اسم الخلية**

من الممكن العثور على فهرس الصف والعمود للخلية من اسمها. يشرح هذا المقال كيفية ذلك.
توفر Aspose.Cells طريقة [CellsHelper_CellNameToIndex](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellnametoindex/)، التي تتيح للمطورين الحصول على فهرس الصف والعمود من اسم الخلية.

{{% alert color="primary" %}}

على عكس Microsoft Excel، حيث تبدأ فهارس الصف والعمود من 1، تبدأ Aspose.Cells في عد فهارس الصف والعمود من 0.

{{% /alert %}}

يُوضح الكود النموذجي التالي كيفية استخدام [CellsHelper_CellNameToIndex](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellnametoindex/) للحصول على فهـرس الصف والعمود من اسم الخلية. يُنتج الكود المخرجات التالية.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetRowAndColumnFromCellName.go" >}}
