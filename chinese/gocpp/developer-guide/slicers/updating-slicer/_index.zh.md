---
title: 使用Golang通过C++更新切片器
linktitle: 更新切片器
type: docs
weight: 50
url: /zh/go-cpp/updating-slicer/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: 本文展示如何使用 Aspose.Cells for Go via C++ API 更新切片器，以筛选所关联的数据透视表或表格的数据。
keywords: Aspose.Cells Go via C++ 更新切片器，Go 如何更改切片器，如何在 Go 中通过切片器筛选数据透视表，Slicer SelectItems，Slicer ClearFilter，Slicer UnselectItems。
---

## **可能的使用场景**
更新切片器是指对切片器所连接的数据透视表或表格的数据进行筛选。在 Microsoft Excel 中选择或取消选择切片器项目时，所关联的数据透视表或表格会相应地重新计算。使用 Aspose.Cells for Go via C++，您无需手动遍历切片器缓存项并刷新切片器 —— [**Slicer.SelectItems(labels, append)**](https://reference.aspose.com/cells/go-cpp/slicer/) 方法会更新切片器，并直接根据筛选项重新计算所关联的数据透视表或表格：
- `Slicer.SelectItems(labels, append)` —— 选择指定的标签并重新计算所关联的数据透视表或表格。当 `append` 为 `true` 时，将保留原先选定的标签，并把指定的标签添加到选定内容中；当 `append` 为 `false` 时，将清除所有原选定内容，仅保留指定的标签处于选定状态。
- `Slicer.UnselectItems(labels)` —— 取消选择当前选定项中的一部分。
- `Slicer.ClearFilter()` —— 移除筛选并选择所有项目。

{{% alert color="primary" %}}
从 Aspose.Cells for Go via C++ 26.10 开始，`SlicerCacheItem.Selected` 属性变为只读，不再支持其 setter。请使用 `Slicer.SelectItems`、`Slicer.UnselectItems` 和 `Slicer.ClearFilter` 方法，而不是逐项设置 `SlicerCacheItem.Selected`。
{{% /alert %}}

## **如何更新切片器**
以下示例代码加载包含连接到数据透视表的现有切片器的[示例 Excel 文件](67338475.xlsx)。它使用 `Slicer.SelectItems(labels, false)` 仅选择切片器的 "Blue" 和 "Pink" 项目 —— 数据透视表直接根据筛选项重新计算，无需手动调用 `Slicer.Refresh()`。然后，它将工作簿保存为[输出 Excel 文件](67338476.xlsx)。以下屏幕截图显示了示例代码对示例 Excel 文件的效果。正如您在屏幕截图中看到的，数据透视表仅显示筛选后的项目。

## **示例代码**
替换当前选定内容（仅保留指定的标签处于选定状态）并重新计算所关联的数据透视表或表格：

```go
package main

import (
    "fmt"

    . "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)

func main() {
    // Load sample Excel file containing slicer.
    wb, _ := NewWorkbook_String("sampleUpdatingSlicer.xlsx")

    // Access first worksheet.
    wss, _ := wb.GetWorksheets()
    ws, _ := wss.Get_Int(0)

    // Access the first slicer inside the slicer collection.
    slicers, _ := ws.GetSlicers()
    slicer, _ := slicers.Get_Int(0)

    // Select only "Blue" and "Pink"; the linked pivot table or table
    // is recalculated directly from the filter items.
    slicer.SelectItems([]string{ "Blue", "Pink" }, false)

    // Save the modified workbook.
    wb.Save_String("out.xlsx")

    fmt.Println("Slicer updated and workbook saved successfully!")
}
```

保留当前选定的标签并额外选择更多项目：

```go
// Keep the current selection and add "Red" to it.
slicer.SelectItems([]string{ "Red" }, true)
```

取消选择部分已选定的项目：

```go
// Remove "Pink" from the current selection.
slicer.UnselectItems([]string{ "Pink" })
```

移除筛选（选择所有项目）：

```go
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter()
```

{{< app/cells/assistant language="go" >}}