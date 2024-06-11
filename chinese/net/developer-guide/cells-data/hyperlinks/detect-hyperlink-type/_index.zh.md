---
title: 检测超链接类型
type: docs
weight: 160
url: /zh/net/detect-hyperlink-type/
description: 使用Aspose.Cells for .NET API学习如何通过检测超链接类型。
keywords: 检测超链接类型，检测超链接的类型，获取超链接的类型
---

## **检测超链接类型**

Excel文件可以有不同类型的超链接，例如外部链接、单元格引用、文件路径等。Aspose.Cells支持检测超链接类型的功能。超链接的类型由[**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)枚举表示。[**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)枚举具有以下成员。

- 外部：外部链接
- 文件路径：文件/文件夹的本地和完整路径。
- 电子邮件：邮件
- 单元格引用：链接到单元格或命名范围。

要检查超链接的类型，[**Hyperlink**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) 类提供了一个返回类型为 [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype) 的 [**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) 属性。以下代码片段演示了如何使用 [**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) 属性，通过使用此[source excel file](94896195.xlsx)。

### 源代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

以下是上述代码片段生成的输出。

### 控制台输出
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
