---
title: 检测超链接类型
type: docs
weight: 160
url: /zh/nodejs-cpp/detect-hyperlink-type/
description: 了解如何通过Aspose.Cells for Node.js via C++ API检测超链接类型。
keywords: 通过C++在Node.js中检测超链接类型，判断超链接类型，利用C++在Node.js中获取超链接类型
---

## **检测超链接类型**

Excel文件可以包含不同类型的超链接，比如外部链接、单元格引用、文件路径等。Aspose.Cells for Node.js via C++支持检测超链接类型的功能。超链接类型由 [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype) 枚举表示。[**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype) 枚举包含以下成员。

- External：外部链接
- FilePath：本地文件/文件夹的完整路径。
- Email：电子邮件
- CellReference：链接到单元格或命名区域。

要检查超链接的类型，[**Hyperlink**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink)类提供了一个 [**getLinkType()**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#getLinkType--) 方法，其返回类型为 [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype)。以下代码片段演示了如何使用 [**getLinkType()**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#getLinkType--) 方法，使用此[源Excel文件](94896195.xlsx)。

### 源代码

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-DetectHyperlinkType.js" >}}


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
