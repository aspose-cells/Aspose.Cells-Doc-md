---
title: 将JSON转换为CSV
type: docs
weight: 210
url: /zh/python-net/convert-json-to-csv/
description: 学习如何使用Aspose.Cells for Python via .NET API将json转换为csv文件。
keywords: Python将json转换为csv，将json转换为csv Pyton via NET，导出json为csv，将json转换为csv
---

## **将JSON转换为CSV**

Aspose.Cells for Python via .NET 可以将简单和嵌套的 JSON 转换为 CSV。为此，API 提供了 [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) 和 [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) 类。[**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) 类提供了 JSON 布局的选项，如 [**ignore_array_title**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/ignore_array_title/)（如果数组是对象的属性，则忽略标题）或 [**array_as_table**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/array_as_table/)（将数组处理为表）。[**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) 类使用使用与 [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) 类设置的布局选项处理 JSON。

以下代码示例演示了使用 [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) 和 [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) 类加载 [源 JSON 文件](104398869.json) 并生成 [输出 CSV 文件](104398870.csv)。

### **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.py" >}}
