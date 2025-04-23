---
title: 在保存为HTML时禁用导出框架脚本和文档属性
type: docs
weight: 310
url: /zh/python-net/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET 在将工作簿转换为HTML时，导出框架脚本和文档属性。8.6.0 版本引入了一个选项，可以选择性禁用框架脚本和文档属性的导出。请使用 HtmlSaveOptions.ExportFrameScriptsAndProperties 属性禁用此导出。

{{% /alert %}}

## **禁用导出框架脚本和文档属性**

以下示例代码允许您禁用导出框架脚本和文档属性。一旦您将工作簿转换为HTML，输出文件将不包含任何框架脚本和文档属性。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-HtmlExportFrameScripts-1.py" >}}
