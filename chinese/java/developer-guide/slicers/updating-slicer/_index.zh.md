---
title: 更新切片器
type: docs
weight: 50
url: /zh/java/updating-slicer/
---

## **可能的使用场景**
如果您想要在Microsoft Excel中更新切片器，请选择或取消选择其项目，然后它将会相应地更新切片器表或数据透视表。请使用 [Slicer.SlicerCache.SlicerCacheItems](https://reference.aspose.com/cells/java/com.aspose.cells/slicercache#SlicerCacheItems) 来在Aspose.Cells中选择或取消选择切片器项目，然后调用 [Slicer.refresh()](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#refresh\(\)) 方法来更新切片器表或数据透视表。 
## **更新分割器**
以下示例代码会加载包含现有切片器的 [示例Excel文件](67338506.xlsx)。它取消选择切片器的第2个和第3个项目，然后刷新切片器。然后将工作簿另存为 [输出Excel文件](67338505.xlsx)。以下截屏显示示例代码对示例Excel文件的影响。如您在截屏中所看到的，刷新带有被选择项目的切片器也已相应地刷新了数据透视表。

![todo:image_alt_text](updating-slicer_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-UpdatingSlicer.java" >}}
