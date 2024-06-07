---
title: 更新切片器
type: docs
weight: 50
url: /zh/net/updating-slicer/
description: 本文介绍了如何通过Aspose.Cells for .NET API更新连接的数据透视表，以更新切片器。
keywords: Aspose.Cells C# 更新切片器，C# 如何更改切片器，如何在C#中调整切片器，如何选择或取消选择切片器项目。
---

## **可能的使用场景**

如果要在Microsoft Excel中更新切片器，并选择或取消选择其项目，然后它将相应地更新切片器表或数据透视表。请使用[**Slicer.SlicerCache.SlicerCacheItems**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercache/properties/slicercacheitems)在Aspose.Cells中选择或取消选择切片器项目，然后调用[**Slicer.Refresh()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/methods/refresh)方法来更新切片器表或数据透视表。

## **如何更新切片器**

以下示例代码加载包含现有切片器的[示例Excel文件](67338475.xlsx)。它取消选择切片器的第2和第3个项目，并刷新切片器。然后将工作簿另存为[输出Excel文件](67338476.xlsx)。以下屏幕截图显示了示例代码对示例Excel文件的影响。如截图所示，刷新具有选定项目的切片器还刷新了数据透视表。

![todo:image_alt_text](updating-slicer_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-UpdatingSlicer.cs" >}}
