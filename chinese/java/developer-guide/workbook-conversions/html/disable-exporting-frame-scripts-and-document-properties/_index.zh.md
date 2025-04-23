---
title: 在保存为HTML时禁用导出框架脚本和文档属性
type: docs
weight: 410
url: /zh/java/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}} 

Aspose.Cells将工作簿转换为HTML时导出框架脚本和文档属性。 Aspose.Cells for Java 的 8.6.0 版本引入了一个选项，允许您选择性地禁用导出框架脚本和文档属性。 请使用 [HtmlSaveOptions.setExportFrameScriptsAndProperties()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportFrameScriptsAndProperties) 属性来禁用导出。

{{% /alert %}} 
## **禁用导出框架脚本和文档属性**
以下示例代码允许您禁用导出框架脚本和文档属性。一旦您将工作簿转换为HTML，输出文件将不包含任何框架脚本和文档属性。

以下是示例代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableExporting-DisableExporting.java" >}}
{{< app/cells/assistant language="java" >}}
