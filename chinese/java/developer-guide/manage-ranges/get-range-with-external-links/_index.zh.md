---
title: 获取带有外部链接的范围
type: docs
weight: 140
url: /zh/java/get-range-with-external-links/
---

## **获取带有外部链接的范围**

许多情况下Excel文件会使用外部链接访问其他Excel文件中的数据。Aspose.Cells提供使用[**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)方法检索这些外部链接的选项。[**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)方法返回[**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)类型的数组。[**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)类提供一个[**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName)属性，返回外部文件的名称。[**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)类公开以下成员。

- [**EndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn)：该区域的结束列
- [**EndRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow)：该区域的结束行
- [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName)：如果这是一个外部引用，则获取外部文件名
- [**IsArea**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea)：指示这是否是一个区域
- [**IsExternalLink**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink)：指示这是否是一个外部链接
- [**SheetName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName)：指示此引用所在的工作表
- [**StartColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn)：该区域的起始列
- [**StartRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow)：该区域的起始行

以下示例代码演示如何使用[**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)方法获取具有外部链接的范围。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
