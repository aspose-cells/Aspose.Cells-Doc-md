---
title: 读取由Apple Inc.开发的Numbers电子表格
type: docs
weight: 140
url: /zh/go-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
---

## **可能的使用场景**

Numbers是由苹果公司开发的电子表格应用程序，Aspose.Cells可以读取Numbers电子表格，但不支持写入。它可以读取Numbers电子表格的数据、样式和公式。

## **使用 Aspose.Cells 读取由 Apple Inc. 开发的 Numbers 电子表格**

以下示例代码加载[示例数字表](sampleNumbersByAppleInc.numbers)，并将其转换为[输出PDF格式](outputNumbersByAppleInc.pdf)。你需要使用**[LoadOptions](https://reference.aspose.com/cells/go-cpp/loadoptions/)**类，并在其构造函数中指定**[LoadFormat::Numbers](https://reference.aspose.com/cells/go-cpp/loadformat/)**作为参数以成功加载。请从给定链接下载两个文件。你可以用任何数字表试试这段代码，也请阅读代码中的注释以获得更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReadNumbersSpreadsheet.go" >}}
