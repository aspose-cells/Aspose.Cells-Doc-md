---
title: 检测超链接类型
type: docs
weight: 160
url: /zh/net/detect-hyperlink-type/
description: 通过 Aspose.Cells for .NET API 了解如何检测超链接类型。
keywords: Detect hyperlink type, Detect the type of hyperlink, Get the type of hyperlink
---
##  **检测超链接类型**

Excel 文件可以有不同类型的超链接，如外部、单元格引用、文件路径等。Aspose.Cells 支持检测超链接类型的功能。超链接的类型由[**目标模式类型**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)枚举。这[**目标模式类型**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)枚举具有以下成员。

- 外部：外部链接
- FilePath：文件\文件夹的本地完整路径。
- 电子邮件： 电子邮件
- CellReference：链接到单元格或命名范围。

要检查超链接的类型，[**超级链接**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink)类提供了一个[**链接类型**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype)返回类型为的属性[**目标模式类型**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)。下面的代码片段演示了使用[**链接类型**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype)通过使用这个属性[源 Excel 文件](94896195.xlsx).

### 源代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

以下是上面给出的代码片段生成的输出。

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
