---
title: 更新切片器
type: docs
weight: 50
url: /zh/python-net/updating-slicer/
description: 学习如何使用 Aspose.Cells for Python 通过 .NET 更新切片器。
keywords: Aspose.Cells for Python Excel，Excel Python 库，Python 更新不使用 Excel 的切片器，使用 Aspose.Cells for Python 更新切片器。
---

## **可能的使用场景**

如果您想要更新 Microsoft Excel 中的切片器，请选择或取消选择其项目，然后它将相应地更新切片器表或数据透视表。请使用 [**Slicer.slicer_cache.slicer_cache_items**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercache/slicer_cache_items/) 来选择或取消选择切片器项目，然后调用 [**Slicer.refresh()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/refresh/#) 方法来更新切片器表或数据透视表。

## **如何使用 Aspose.Cells for Python Excel 库更新切片器**

以下示例代码加载包含现有切片器的[示例Excel文件](67338475.xlsx)。它取消选择切片器的第2和第3个项目，并刷新切片器。然后将工作簿另存为[输出Excel文件](67338476.xlsx)。以下屏幕截图显示了示例代码对示例Excel文件的影响。如截图所示，刷新具有选定项目的切片器还刷新了数据透视表。

![todo:image_alt_text](updating-slicer_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-UpdatingSlicer.py" >}}
