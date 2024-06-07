---
title: 将JSON转换为CSV
type: docs
weight: 210
url: /zh/net/convert-json-to-csv/
---

## **将JSON转换为CSV**

Aspose.Cells支持将简单json以及嵌套json转换为CSV。为此，API提供了**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**和**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**类。**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**类提供了JSON布局选项，如**[IgnoreArrayTitle](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle)**(如果数组是对象的属性，则忽略标题)或**[ArrayAsTable](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable)**(将数组处理为表格)。**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**类使用与**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**类设置的布局选项处理JSON。

以下代码示例演示了如何使用**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**和**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**类加载**[源JSON文件](104398869.json)**并生成**[输出CSV文件](104398870.csv)**。

### **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.cs" >}}
