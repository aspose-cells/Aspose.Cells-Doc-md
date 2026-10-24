---
title: スライサーの更新
linktitle: スライサーの更新
type: docs
weight: 50
url: /ja/net/updating-slicer/
description: この記事では、Aspose.Cells for .NET APIを使用してスライサーを更新し、リンクされたピボットテーブルまたはテーブルのデータをフィルター処理する方法を示します。
keywords: Aspose.Cells C# スライサーの更新、C# スライサーの変更方法、C#でスライサーによるピボットテーブルのフィルター方法、C# Slicer SelectItems、C# Slicer ClearFilter、C# Slicer UnselectItems。
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能な使用シナリオ**
スライサーの更新とは、スライサーが接続されているピボットテーブルまたはテーブルのデータをフィルター処理することを意味します。Microsoft Excelでスライサーのアイテムを選択または選択解除すると、リンクされたピボットテーブルまたはテーブルがそれに応じて再計算されます。Aspose.Cells for .NETでは、スライサーキャッシュアイテムを反復処理してスライサーを手動でリフレッシュする必要はありません。[**Slicer.SelectItems(string[], bool)**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/selectitems/)メソッドがスライサーを更新し、フィルターアイテムから直接、リンクされたピボットテーブルまたはテーブルを再計算します：
- `Slicer.SelectItems(labels, append)` — 指定されたラベルを選択し、リンクされたピボットテーブルまたはテーブルを再計算します。`append`が`true`の場合は元々選択されていたラベルが保持され、指定されたラベルが選択に追加されます。`append`が`false`の場合は元の選択がすべてクリアされ、指定されたラベルのみが選択された状態になります。
- `Slicer.UnselectItems(labels)` — 現在選択されているアイテムの一部を選択解除します。
- `Slicer.ClearFilter()` — フィルターを解除してすべてのアイテムを選択します。

{{% alert color="primary" %}}
Aspose.Cells for .NET 26.10以降、`SlicerCacheItem.Selected`プロパティは読み取り専用になり、そのセッターはサポートされなくなります。`SlicerCacheItem.Selected`をアイテムごとに設定する代わりに、`Slicer.SelectItems`、`Slicer.UnselectItems`、`Slicer.ClearFilter`メソッドを使用してください。
{{% /alert %}}

## **スライサーの更新方法**
次のサンプルコードは、ピボットテーブルに接続された既存のスライサーを含む[サンプルExcelファイル](67338475.xlsx)を読み込みます。`Slicer.SelectItems(labels, false)`を使用してスライサーの"Blue"と"Pink"のアイテムのみを選択すると、ピボットテーブルはフィルターアイテムから直接再計算され、手動での`Slicer.Refresh()`の呼び出しは不要です。その後、ワークブックを[出力Excelファイル](67338476.xlsx)として保存します。次のスクリーンショットは、サンプルコードがサンプルExcelファイルに与える影響を示しています。スクリーンショットでわかるように、ピボットテーブルにはフィルターされたアイテムのみが表示されます。
![todo:image_alt_text](updating-slicer_1.png)

## **サンプルコード**
現在の選択を置き換え（指定されたラベルのみが選択された状態になります）、リンクされたピボットテーブルまたはテーブルを再計算します：

```csharp
using Aspose.Cells;
using Aspose.Cells.Slicers;
// Load sample Excel file containing slicer.
Workbook workbook = new Workbook("sampleUpdatingSlicer.xlsx");
// Access first worksheet.
Worksheet worksheet = workbook.Worksheets[0];
// Access the first slicer inside the slicer collection.
Slicer slicer = worksheet.Slicers[0];
// Select only "Blue" and "Pink"; the linked pivot table or table
// is recalculated directly from the filter items.
slicer.SelectItems(new string[] { "Blue", "Pink" }, false);
// Save the modified workbook.
workbook.Save("out.xlsx");
```

現在選択されているラベルを保持したまま、さらにアイテムを選択します：

```csharp
// Keep the current selection and add "Red" to it.
slicer.SelectItems(new string[] { "Red" }, true);
```

選択されたアイテムの一部を選択解除します：

```csharp
// Remove "Pink" from the current selection.
slicer.UnselectItems(new string[] { "Pink" });
```

フィルターを解除します（すべてのアイテムを選択します）：

```csharp
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter();
```

{{< app/cells/assistant language="csharp" >}}