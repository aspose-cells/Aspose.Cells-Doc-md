---
title: 检测超链接类型
type: docs
weight: 180
url: /zh/java/detect-hyperlink-type/
---

## **检测超链接类型**

Excel文件可以具有不同类型的超链接，如外部链接、单元引用、文件路径等。Aspose.Cells支持检测超链接的类型功能。超链接的类型由[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)枚举表示。[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)枚举具有以下成员。

- [**EXTERNAL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EXTERNAL)：外部链接
- [**FILE_PATH**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#FILE_PATH)：本地和完整的文件/文件夹路径。
- [**EMAIL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EMAIL)：电子邮件
- [**CELL_REFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#CELL_REFERENCE)：链接到单元格或命名范围。

要检查超链接的类型，[**Hyperlink**](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink)类提供一个[**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType)属性，返回类型为[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)。以下代码片段演示了如何使用这个[**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType)属性[使用此源Excel文件](LinkTypes.xlsx)。

## 源代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-DetectLinkTypes-1.java" >}}

以下是上述代码片段生成的输出。

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
