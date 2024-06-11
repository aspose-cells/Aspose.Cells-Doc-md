---
title: 在保存为HTML时禁用导出框架脚本和文档属性
type: docs
weight: 310
url: /zh/net/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}}

在将工作簿转换为HTML时，Aspose.Cells会导出框架脚本和文档属性。Aspose.Cells for .NET的8.6.0版本引入了一个选项，允许您选择是否禁用导出框架脚本和文档属性。请使用HtmlSaveOptions.ExportFrameScriptsAndProperties属性来禁用导出。

{{% /alert %}}

## **禁用导出框架脚本和文档属性**

以下示例代码允许您禁用导出框架脚本和文档属性。一旦您将工作簿转换为HTML，输出文件将不包含任何框架脚本和文档属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-HtmlExportFrameScripts-1.cs" >}}
