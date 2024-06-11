---
title: 更新切片器
type: docs
weight: 50
url: /zh/net/updating-slicer/
description: 本文章展示了如何通过 Aspose.Cells for .NET API 更新链接的数据透视表并更新切片器。
keywords: Aspose.Cells C# 更新数据透视切片器，C# 如何更改数据透视切片器，在 C# 中如何调整数据透视切片器，如何选择或取消选择数据透视切片器的项目。
---

## **可能的使用场景**

如果您想在 Microsoft Excel 中更新数据透视切片器，选择或取消选择它的项目，它将随后相应地更新数据透视切片器表或数据透视表。请使用 [**Slicer.SlicerCache.SlicerCacheItems**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercache/properties/slicercacheitems) 以选中或取消选择数据透视切片器项目，然后调用 [**Slicer.Refresh()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/methods/refresh) 方法以更新数据透视切片器表或数据透视表。

## **如何更新数据透视切片器**

以下示例代码加载包含现有数据透视切片器的[示例 Excel 文件](67338475.xlsx)，取消选择数据透视切片器的第 2 和第 3 个项目，并刷新数据透视切片器，然后将工作簿保存为[输出 Excel 文件](67338476.xlsx)。以下屏幕截图显示了示例代码对示例 Excel 文件的效果。如屏幕截图所示，使用选定项目刷新数据透视切片器也已相应地刷新了数据透视表。

![todo:image_alt_text](updating-slicer_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-UpdatingSlicer.cs" >}}
