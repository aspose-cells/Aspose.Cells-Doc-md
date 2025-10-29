---
title: 在使用 C++ 通过 Golang 将文件保存为 PDF 时打印批注
linktitle: 保存为PDF时打印注释
type: docs
weight: 10
url: /zh/go-cpp/print-comments-while-saving-to-pdf/
description: 了解如何在使用Aspose.Cells for C++将Excel文件保存为PDF时打印批注。
---

{{% alert color="primary" %}}

Microsoft Excel允许您通过以下选项在打印或保存为PDF格式时打印批注：

- 无
- 工作表末尾
- 如在工作表上显示的那样

Aspose.Cells提供了[**PrintCommentsType**](https://reference.aspose.com/cells/go-cpp/printcommentstype/)枚举以支持相同的功能。[**PrintCommentsType**](https://reference.aspose.com/cells/go-cpp/printcommentstype/)枚举具有以下成员：

- PrintNoComments
- PrintInPlace
- PrintSheetEnd

{{% /alert %}}

## **保存为PDF时打印注释**

以下示例代码说明了如何使用[**PrintCommentsType**](https://reference.aspose.com/cells/go-cpp/printcommentstype/)在保存为PDF时打印批注。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PrintCommentsWhileSavingToPdf.go" >}}
