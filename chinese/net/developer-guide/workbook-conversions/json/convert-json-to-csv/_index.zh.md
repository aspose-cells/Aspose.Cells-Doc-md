---
title: 将 JSON 转换为 CSV
type: docs
weight: 210
url: /zh/net/convert-json-to-csv/
---
## **将 JSON 转换为 CSV**

Aspose.Cells 支持将简单和嵌套的 JSON 转换为 CSV。为此，API 提供**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**和**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**类。这**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**类提供 JSON 布局的选项，例如**[IgnoreArrayTitle](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle)**（如果数组是对象的属性，则忽略标题）或**[ArrayAsTable](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable)**（将数组作为表格处理）。这**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**类使用设置的布局选项处理 JSON**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**班级。

下面的代码示例演示了使用**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**和**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**加载的类[源 JSON 文件](104398869.json)并生成[输出 CSV 文件](104398870.csv).

### **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.cs" >}}
