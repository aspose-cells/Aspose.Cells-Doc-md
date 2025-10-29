---
title: 检测超链接类型
type: docs
weight: 160
url: /zh/python-net/detect-hyperlink-type/
description: 学习如何通过Aspose.Cells for Python via .NET API检测超链接类型。
keywords: Python Excel库，Python检测超链接类型，Python检测超链接的类型，Python获取超链接的类型。
---

## **检测超链接类型**

Excel文件可以具有不同类型的超链接，例如外部链接，单元格引用，文件路径等。Aspose.Cells for Python via .NET支持检测超链接的功能。超链接的类型由[**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype)枚举表示。[**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype)枚举具有以下成员。

- EXTERNAL: 外部链接
- FILE_PATH: 本地和完整的文件\文件夹路径。
- EMAIL: 电子邮件
- CELL_REFERENCE：链接到单元格或已命名范围。

要检查超链接的类型，[**Hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink) 类提供了一个返回类型为 [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype) 的 [**link_type**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink/link_type/) 属性。以下代码片段演示了如何使用 [**link_type**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink/link_type/) 属性，通过使用此[source excel file](94896195.xlsx)。

### 源代码

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DetectLinkTypes-1.py" >}}

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
{{< app/cells/assistant language="python-net" >}}
