---
title: 用 Golang 通过 C++ 在导出 Excel 文件为 HTML 时从右向左扩展文本
linktitle: 将Excel文件导出为HTML时从右向左扩展文本
type: docs
weight: 60
url: /zh/go-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/
description: 学习在用Aspose.Cells for C++将Excel文件导出为HTML时，从右到左扩展文本的方法。
---

{{% alert color="primary" %}} 

从现在起，Aspose.Cells for C++支持在导出Excel为HTML时从右向左扩展文本。此功能自v8.9.0.0版本起实现。如果你的Excel源文件中包含任何从右到左扩展的文本，Aspose.Cells会正确导出。

{{% /alert %}} 

## **在将Excel文件导出为HTML时，将文本从右向左扩展**

以下示例代码将[样本Excel文件](5115502.xlsx)转换为HTML。此屏幕截图显示了在Microsoft Excel 2013中样本文件的样子。

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

此截图显示了[由较旧版本生成的输出HTML](5115509)。

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

此截图显示了[由较新版本生成的输出HTML](5115508)。

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

如截图所示，较新版本能正确展开右对齐的文本到左侧，就像Microsoft Excel一样。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExpandingTextFromRightToLeftWhileExportingExcelFileToHtml.go" >}}
