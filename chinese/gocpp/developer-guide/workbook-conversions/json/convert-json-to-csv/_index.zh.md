---
title: 使用 Golang 通过 C++ 将 JSON 转换为 CSV
linktitle: 将JSON转换为CSV
type: docs
weight: 210
url: /zh/go-cpp/convert-json-to-csv/
description: 学习如何使用 Aspose.Cells for C++ 结合简单和嵌套的 JSON 示例将 JSON 转换为 CSV。
---

## **将JSON转换为CSV**

 Aspose.Cells 支持将简单和嵌套的 JSON 转换为 CSV。为此，API 提供了 [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) 和 [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) 类。[**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) 类提供 JSON 排版的选项，例如 [**SetIgnoreTitle**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/setignoretitle/)（如果数组是对象的属性，则忽略标题）或 [**GetArrayAsTable()**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/getarrayastable/)（将数组作为表处理）。[**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) 类使用 [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) 类设置的排版选项处理 JSON。

 以下代码示例演示了如何使用 [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) 和 [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) 类加载 [源 JSON 文件](104398869.json)，并生成 [输出 CSV 文件](104398870.csv)。

### **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertJsonToCsv.go" >}}
