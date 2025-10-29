---
title: 用 Golang 通过 C++ 禁用导出框架脚本和文档属性
type: docs
weight: 310
url: /zh/go-cpp/disable-exporting-frame-scripts-and-document-properties/
description: 使用 Golang 通过 C++ 结合 Aspose.Cells 禁用导出框架脚本和文档属性
---

{{% alert color="primary" %}}

Aspose.Cells在将工作簿转换为HTML时，会导出框架脚本和文档属性。Aspose.Cells for C++的8.6.0版本引入了一个选项，可以选择性禁用框架脚本和文档属性的导出。请使用HtmlSaveOptions.ExportFrameScriptsAndProperties属性禁用导出。

{{% /alert %}}

## **禁用导出框架脚本和文档属性**

以下示例代码允许您禁用导出框架脚本和文档属性。一旦您将工作簿转换为HTML，输出文件将不包含任何框架脚本和文档属性。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableExportingFrameScriptsAndDocumentProperties.go" >}}
