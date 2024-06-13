---
title: 获取带有外部链接的范围
type: docs
weight: 140
url: /zh/java/get-range-with-external-links/
---

## **获取带有外部链接的范围**

许多时候，Excel文件通过外部链接访问其他Excel文件的数据。 Aspose.Cells 提供了通过使用 [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) 方法来检索这些外部链接的选项。[**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) 方法返回 [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) 类型的数组。[**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) 类提供了 [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName) 属性，返回外部文件的名称。[**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) 类公开了以下成员。

- [**EndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn)：区域的结束列
- [**EndRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow)：区域的结束行
- [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName)：如果这是外部引用，获取外部文件名
- [**IsArea**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea): 表示这是否为一个区域
- [**IsExternalLink**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink): 表示这是否为外部链接
- [**SheetName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName): 表示此引用所在的工作表
- [**StartColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn): 区域的起始列
- [**StartRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow): 区域的起始行

下面给出的示例代码演示了使用 [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) 方法来获取带有外部链接的范围。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
