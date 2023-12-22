---
title: 将 JSON 转换为 CSV
type: docs
weight: 210
url: /zh/python-net/convert-json-to-csv/
description: 了解如何使用 Aspose.Cells for Python via .NET API 将 json 转换为 csv 文件。
keywords: Python Convert json to csv, Convert json to csv Pyton via NET, Export json to csv, Convert json to csv
---
##  **将 JSON 转换为 CSV**

Aspose.Cells for Python via .NET 支持将简单以及嵌套的 JSON 转换为 CSV。为此，API 提供**[JsonLayoutOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions)**和**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**类。这**[JsonLayoutOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions)**类提供了 JSON 布局的选项，例如**[ignore_array_title](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/ignore_array_title/)**（如果数组是对象的属性，则忽略标题）或** [array_as_table](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/array_as_table/)**（将数组处理为表）。 **[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**类使用布局选项设置处理 JSON**[JsonLayoutOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions)**班级。

下面的代码示例演示了使用**[JsonLayoutOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions)**和**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**类来加载[源JSON文件](104398869.json)并生成[输出CSV文件](104398870.csv).

###  **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.py" >}}
