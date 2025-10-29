---
title: 用Golang via C++检测超链接类型
linktitle: 检测超链接类型
type: docs
weight: 160
url: /zh/go-cpp/detect-hyperlink-type/
description: 通过Aspose.Cells for C++ API学习如何检测超链接类型。
keywords: 检测超链接类型，检测超链接的类型，获取超链接的类型
---

## **检测超链接类型**

Excel文件可以有不同类型的超链接，例如外部链接、单元格引用、文件路径等。Aspose.Cells支持检测超链接类型的功能。超链接的类型由[**TargetModeType**](https://reference.aspose.com/cells/go-cpp/targetmodetype/)枚举表示。[**TargetModeType**](https://reference.aspose.com/cells/go-cpp/targetmodetype/)枚举具有以下成员。

- 外部：外部链接
- 文件路径：文件/文件夹的本地和完整路径。
- 电子邮件：邮件
- 单元格引用：链接到单元格或命名范围。

要检查超链接的类型，[**Hyperlink**](https://reference.aspose.com/cells/go-cpp/hyperlink/) 类提供了一个返回类型为 [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/) 的 [**LinkType**](https://reference.aspose.com/cells/go-cpp/hyperlink/getlinktype/) 属性。以下代码片段演示了如何使用 [**LinkType**](https://reference.aspose.com/cells/go-cpp/hyperlink/getlinktype/) 属性，通过使用此[source excel file](94896195.xlsx)。

### 源代码

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectHyperlinkType.go" >}}
以下是上述代码片段生成的输出。

### 控制台输出
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectHyperlinkType-1.go" >}}
