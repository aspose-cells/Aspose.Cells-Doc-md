---
title: 更新切片器
type: docs
weight: 50
url: /zh/java/updating-slicer/
---

## **可能的使用场景**
如果想在 Microsoft Excel 中更新切片器，可以选择或取消选择其项目，它会相应更新切片器表或数据透视表。请使用 [Slicer.SlicerCache.SlicerCacheItems](https://reference.aspose.com/cells/java/com.aspose.cells/slicercache#SlicerCacheItems) 选择或取消选择切片器项目，然后调用 [Slicer.refresh()](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#refresh--) 方法以更新切片器表或数据透视表。 
## **更新分析器**
以下示例代码加载包含现有分析器的 [示例 Excel 文件](67338506.xlsx)。取消选择分析器的第 2 和第 3 项目并刷新分析器。然后将工作簿另存为 [输出 Excel 文件](67338505.xlsx)。下面的截图显示示例代码对示例 Excel 文件的影响。如您在截图中所见，刷新具有选定项目的分析器也相应地刷新了数据透视表。

![todo:image_alt_text](updating-slicer_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-UpdatingSlicer.java" >}}
{{< app/cells/assistant language="java" >}}
