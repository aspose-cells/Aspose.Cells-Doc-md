---
title: 用Golang通过C++从Gear类型SmartArt形状提取文本
linktitle: 从齿轮型智能图形中提取文本
type: docs
weight: 500
url: /zh/go-cpp/extract-text-from-the-gear-type-smartart-shape/
description: 学习如何使用Aspose.Cells for C++逐步指导和代码示例，从Excel中的Gear类型SmartArt形状中提取文本。
---

## **可能的使用场景**

Aspose.Cells for C++可以提取Gear类型SmartArt形状中的文本。请按以下步骤操作：
1. 使用[**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/go-cpp/)方法将SmartArt形状转换为组形状。
2. 使用[**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/go-cpp/)方法获取组成组形状的所有单个形状。
3. 遍历每个单个形状并使用[**GetText()**](https://reference.aspose.com/cells/go-cpp/)方法提取文本。

## **从齿轮型智能图形中提取文本**

以下示例代码加载包含Gear类型SmartArt形状的【示例Excel文件】(67338483.xlsx)，并从其单个形状中提取文本。结果请参见下面的控制台输出。

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractTextFromTheGearTypeSmartartShape.go" >}}
## **控制台输出**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}
