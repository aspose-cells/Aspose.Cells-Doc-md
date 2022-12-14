---
title: 检测超链接类型
type: docs
weight: 180
url: /zh/java/detect-hyperlink-type/
---
## **检测超链接类型**

Excel 文件可以有不同类型的超链接，如外部、单元格引用、文件路径等。Aspose.Cells 支持检测超链接类型的功能。超链接的类型由[**目标模式类型**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)枚举。这[**目标模式类型**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)枚举具有以下成员。

- [**外部的**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EXTERNAL)： 外部链接
- [**文件路径**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#FILE_PATH)：文件\文件夹的本地和完整路径。
- [**电子邮件**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EMAIL)： 电子邮件
- [**CELL_REFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#CELL_REFERENCE)：链接到单元格或命名区域。

要检查超链接的类型，[**超级链接**](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink)类提供了[**链接类型**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType)返回类型为[**目标模式类型**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType).下面的代码片段演示了使用[**链接类型**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType)通过使用这个属性[源文件](LinkTypes.xlsx).

## 源代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-DetectLinkTypes-1.java" >}}

以下是上面给出的代码片段生成的输出。

## 控制台输出
```
LinkTypes.xlsx: FILE_PATH </br>
C:\Windows\System32\cmd.exe: FILE_PATH </br>
C:\Program Files\Common Files: FILE_PATH </br>
'Test Sheet'!B2: CELL_REFERENCE </br>
FullPathExample: CELL_REFERENCE </br>
https://products.aspose.com/cells/ : EXTERNAL </br>
mailto:test@test.com?subject=TestLink: EMAIL
```
