---
title: C++経由のGolangによるスライサーの更新
linktitle: スライサーの更新
type: docs
weight: 50
url: /ja/go-cpp/updating-slicer/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: この記事では、Aspose.Cells for Go via C++ APIを使用してスライサーを更新し、リンクされたピボットテーブルまたはテーブルのデータをフィルター処理する方法を示します。
keywords: Aspose.Cells Go via C++ スライサーの更新、Go スライサーの変更方法、Goでスライサーによるピボットテーブルのフィルター方法、Slicer SelectItems、Slicer ClearFilter、Slicer UnselectItems。
---

## **可能な使用シナリオ**
スライサーの更新とは、スライサーが接続されているピボットテーブルまたはテーブルのデータをフィルター処理することを意味します。Microsoft Excelでスライサーのアイテムを選択または選択解除すると、リンクされたピボットテーブルまたはテーブルがそれに応じて再計算されます。Aspose.Cells for Go via C++では、スライサーキャッシュアイテムを反復処理してスライサーを手動でリフレッシュする必要はありません。[**Slicer.SelectItems(labels, append)**](https://reference.aspose.com/cells/go-cpp/slicer/)メソッドがスライサーを更新し、フィルターアイテムから直接、リンクされたピボットテーブルまたはテーブルを再計算します：
- `Slicer.SelectItems(labels, append)` — 指定されたラベルを選択し、リンクされたピボットテーブルまたはテーブルを再計算します。`append`が`true`の場合は元々選択されていたラベルが保持され、指定されたラベルが選択に追加されます。`append`が`false`の場合は元の選択がすべてクリアされ、指定されたラベルのみが選択された状態になります。
- `Slicer.UnselectItems(labels)` — 現在選択されているアイテムの一部を選択解除します。
- `Slicer.ClearFilter()` — フィルターを解除してすべてのアイテムを選択します。

{{% alert color="primary" %}}
Aspose.Cells for Go via C++ 26.10以降、`SlicerCacheItem.Selected`プロパティは読み取り専用になり、そのセッターはサポートされなくなります。`SlicerCacheItem.Selected`をアイテムごとに設定する代わりに、`Slicer.SelectItems`、`Slicer.UnselectItems`、`Slicer.ClearFilter`メソッドを使用してください。
{{% /alert %}}

## **スライサーの更新方法**
次のサンプルコードは、ピボットテーブルに接続された既存のスライサーを含む[サンプルExcelファイル](67338475.xlsx)を読み込みます。`Slicer.SelectItems(labels, false)`を使用してスライサーの"Blue"と"Pink"のアイテムのみを選択すると、ピボットテーブルはフィルターアイテムから直接再計算され、手動での`Slicer.Refresh()`の呼び出しは不要です。その後、ワークブックを[出力Excelファイル](67338476.xlsx)として保存します。次のスクリーンショットは、サンプルコードがサンプルExcelファイルに与える影響を示しています。スクリーンショットでわかるように、ピボットテーブルにはフィルターされたアイテムのみが表示されます。

## **サンプルコード**
現在の選択を置き換え（指定されたラベルのみが選択された状態になります）、リンクされたピボットテーブルまたはテーブルを再計算します：

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

現在選択されているラベルを保持したまま、さらにアイテムを選択します：

```go
// Keep the current selection and add "Red" to it.
slicer.SelectItems([]string{ "Red" }, true)
```

選択されたアイテムの一部を選択解除します：

```go
// Remove "Pink" from the current selection.
slicer.UnselectItems([]string{ "Pink" })
```

フィルターを解除します（すべてのアイテムを選択します）：

```go
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter()
```

{{< app/cells/assistant language="go" >}}