---
title: 用 Golang 通过 C++ 导出带网格线的 Excel 转 HTML
linktitle: 将Excel导出为带有网格线的HTML
type: docs
weight: 40
url: /zh/go-cpp/export-excel-to-html-with-gridlines/
description: 学习如何使用编号Aspose.Cells for C++导出带网格线的Excel文件到HTML。
---

{{% alert color="primary" %}} 

如果你想带网格线将Excel文件导出为HTML，请使用【HtmlSaveOptions.GetExportGridLines()】属性并设置为**true**。

{{% /alert %}} 

## **将Excel导出为带有网格线的HTML**
以下示例代码创建一个工作簿，填写其工作表一些值，然后在设置【HtmlSaveOptions.GetExportGridLines()】为**true**后将其保存为 HTML。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportExcelToHtmlWithGridlines.go" >}}
