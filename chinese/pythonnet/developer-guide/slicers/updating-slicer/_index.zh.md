---
title: 更新切片器
linktitle: 更新切片器
type: docs
weight: 50
url: /zh/python-net/updating-slicer/
description: 了解如何使用 Aspose.Cells for Python via .NET 更新切片器，以筛选所关联的数据透视表或表格的数据。
keywords: Aspose.Cells for Python Excel，Excel Python 库，Python 无需 Excel 更新切片器，在 Python 中通过切片器筛选数据透视表，Slicer select_items，Slicer clear_filter。
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
更新切片器是指对切片器所连接的数据透视表或表格的数据进行筛选。在 Microsoft Excel 中选择或取消选择切片器项目时，所关联的数据透视表或表格会相应地重新计算。使用 Aspose.Cells for Python via .NET，您无需手动遍历切片器缓存项并刷新切片器 —— [**Slicer.select_items(labels, append)**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/selectitems/) 方法会更新切片器，并直接根据筛选项重新计算所关联的数据透视表或表格：
- `Slicer.select_items(labels, append)` —— 选择指定的标签并重新计算所关联的数据透视表或表格。当 `append` 为 `True` 时，将保留原先选定的标签，并把指定的标签添加到选定内容中；当 `append` 为 `False` 时，将清除所有原选定内容，仅保留指定的标签处于选定状态。
- `Slicer.unselect_items(labels)` —— 取消选择当前选定项中的一部分。
- `Slicer.clear_filter()` —— 移除筛选并选择所有项目。

{{% alert color="primary" %}}
从 Aspose.Cells for Python via .NET 26.10 开始，`SlicerCacheItem.selected` 属性变为只读，不再支持其 setter。请使用 `Slicer.select_items`、`Slicer.unselect_items` 和 `Slicer.clear_filter` 方法，而不是逐项设置 `SlicerCacheItem.selected`。
{{% /alert %}}

## **如何使用 Aspose.Cells for Python Excel 库更新切片器**
以下示例代码加载包含连接到数据透视表的现有切片器的[示例 Excel 文件](67338475.xlsx)。它使用 `Slicer.select_items(labels, False)` 仅选择切片器的 "Blue" 和 "Pink" 项目 —— 数据透视表直接根据筛选项重新计算，无需手动调用 `Slicer.refresh()`。然后，它将工作簿保存为[输出 Excel 文件](67338476.xlsx)。以下屏幕截图显示了示例代码对示例 Excel 文件的效果。正如您在屏幕截图中看到的，数据透视表仅显示筛选后的项目。
![todo:image_alt_text](updating-slicer_1.png)

## **示例代码**
替换当前选定内容（仅保留指定的标签处于选定状态）并重新计算所关联的数据透视表或表格：

```python
import aspose.cells as ac
# Load sample Excel file containing slicer.
workbook = ac.Workbook("sampleUpdatingSlicer.xlsx")
# Access first worksheet.
worksheet = workbook.worksheets[0]
# Access the first slicer inside the slicer collection.
slicer = worksheet.slicers[0]
# Select only "Blue" and "Pink"; the linked pivot table or table
# is recalculated directly from the filter items.
slicer.select_items(["Blue", "Pink"], False)
# Save the modified workbook.
workbook.save("out.xlsx")
```

保留当前选定的标签并额外选择更多项目：

```python
# Keep the current selection and add "Red" to it.
slicer.select_items(["Red"], True)
```

取消选择部分已选定的项目：

```python
# Remove "Pink" from the current selection.
slicer.unselect_items(["Pink"])
```

移除筛选（选择所有项目）：

```python
# Clear the filter; all slicer items become selected again.
slicer.clear_filter()
```

{{< app/cells/assistant language="python-net" >}}