---
title: 使用Golang通过C++更新切片
linktitle: 更新切片器
type: docs
weight: 50
url: /zh/go-cpp/updating-slicer/
description: 本文介绍如何通过更新切片器来更新关联的透视表，使用Aspose.Cells for C++ API。
keywords: Aspose.Cells C++更新切片器，如何在C++中更改切片器、调整切片器、选择或取消选择切片器项。
---

## **可能的使用场景**

如果你想在Microsoft Excel中更新切片器，选择或取消选择其项目，它将相应地更新切片器表或透视表。请使用[**Slicer.GetSlicerCacheItems()**](https://reference.aspose.com/cells/go-cpp/slicercache/getslicercacheitems/)选择或取消选择切片器项，然后调用[**Slicer.Refresh()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/refresh/)方法更新切片器表或透视表。

## **如何更新数据透视切片器**

以下示例代码加载包含现有数据透视切片器的[示例 Excel 文件](67338475.xlsx)，取消选择数据透视切片器的第 2 和第 3 个项目，并刷新数据透视切片器，然后将工作簿保存为[输出 Excel 文件](67338476.xlsx)。以下屏幕截图显示了示例代码对示例 Excel 文件的效果。如屏幕截图所示，使用选定项目刷新数据透视切片器也已相应地刷新了数据透视表。

![todo:image_alt_text](updating-slicer_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UpdatingSlicer.go" >}}
