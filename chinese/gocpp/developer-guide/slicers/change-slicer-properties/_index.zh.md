---
title: 用Golang通过C++更改切片器属性
linktitle: 更改切片器属性
type: docs
weight: 70
url: /zh/go-cpp/change-slicer-properties/
description: 用Golang通过C++更改Excel文件中切片器的属性。
---

## **可能的使用场景**

也许会出现您希望更改切片器的属性的情况，比如位置或行高等。Aspose.Cells为您提供了更新这些属性的选项。

## **更改切片器属性**

请查看以下示例代码。它加载包含表的[sample Excel file](sampleCreateSlicerToExcelTable.xlsx)，然后基于第一列创建切片器，并更改其属性，如行高、宽度、是否可打印、标题等。将工作簿另存为[outputChangeSlicerProperties.xlsx](outputChangeSlicerProperties.xlsx)。

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeSlicerProperties.go" >}}
