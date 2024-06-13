---
title: 将JSON转换为CSV
type: docs
weight: 210
url: /zh/net/convert-json-to-csv/
---

## **将JSON转换为CSV**

Aspose.Cells 支持将简单的 JSON 和嵌套的 JSON 转换为 CSV。为此，API 提供了 [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) 和 [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) 类。[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) 类提供了处理 JSON 布局的选项，例如 [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle)（如果数组是对象的属性，则忽略标题）或 [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable)（将数组处理为表）。[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) 类使用设置了 [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) 类的布局选项处理 JSON。

以下代码示例演示了使用 [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) 和 [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) 类加载 [源 JSON 文件](104398869.json) 并生成 [输出 CSV 文件](104398870.csv)。

### **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.cs" >}}
