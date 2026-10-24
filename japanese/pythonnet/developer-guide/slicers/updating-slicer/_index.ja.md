---
title: スライサーの更新
linktitle: スライサーの更新
type: docs
weight: 50
url: /ja/python-net/updating-slicer/
description: Aspose.Cells for Python via .NETでスライサーを更新し、リンクされたピボットテーブルまたはテーブルのデータをフィルター処理する方法を学びます。
keywords: Aspose.Cells for Python Excel、Excel Pythonライブラリ、ExcelなしでPythonスライサーを更新、Pythonでスライサーによるピボットテーブルのフィルター、Slicer select_items、Slicer clear_filter。
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能な使用シナリオ**
スライサーの更新とは、スライサーが接続されているピボットテーブルまたはテーブルのデータをフィルター処理することを意味します。Microsoft Excelでスライサーのアイテムを選択または選択解除すると、リンクされたピボットテーブルまたはテーブルがそれに応じて再計算されます。Aspose.Cells for Python via .NETでは、スライサーキャッシュアイテムを反復処理してスライサーを手動でリフレッシュする必要はありません。[**Slicer.select_items(labels, append)**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/selectitems/)メソッドがスライサーを更新し、フィルターアイテムから直接、リンクされたピボットテーブルまたはテーブルを再計算します：
- `Slicer.select_items(labels, append)` — 指定されたラベルを選択し、リンクされたピボットテーブルまたはテーブルを再計算します。`append`が`True`の場合は元々選択されていたラベルが保持され、指定されたラベルが選択に追加されます。`append`が`False`の場合は元の選択がすべてクリアされ、指定されたラベルのみが選択された状態になります。
- `Slicer.unselect_items(labels)` — 現在選択されているアイテムの一部を選択解除します。
- `Slicer.clear_filter()` — フィルターを解除してすべてのアイテムを選択します。

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET 26.10以降、`SlicerCacheItem.selected`プロパティは読み取り専用になり、そのセッターはサポートされなくなります。`SlicerCacheItem.selected`をアイテムごとに設定する代わりに、`Slicer.select_items`、`Slicer.unselect_items`、`Slicer.clear_filter`メソッドを使用してください。
{{% /alert %}}

## **Aspose.Cells for Python Excel Libraryを使用したスライサーの更新方法**
次のサンプルコードは、ピボットテーブルに接続された既存のスライサーを含む[サンプルExcelファイル](67338475.xlsx)を読み込みます。`Slicer.select_items(labels, False)`を使用してスライサーの"Blue"と"Pink"のアイテムのみを選択すると、ピボットテーブルはフィルターアイテムから直接再計算され、手動での`Slicer.refresh()`の呼び出しは不要です。その後、ワークブックを[出力Excelファイル](67338476.xlsx)として保存します。次のスクリーンショットは、サンプルコードがサンプルExcelファイルに与える影響を示しています。スクリーンショットでわかるように、ピボットテーブルにはフィルターされたアイテムのみが表示されます。
![todo:image_alt_text](updating-slicer_1.png)

## **サンプルコード**
現在の選択を置き換え（指定されたラベルのみが選択された状態になります）、リンクされたピボットテーブルまたはテーブルを再計算します：

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

現在選択されているラベルを保持したまま、さらにアイテムを選択します：

```python
# Keep the current selection and add "Red" to it.
slicer.select_items(["Red"], True)
```

選択されたアイテムの一部を選択解除します：

```python
# Remove "Pink" from the current selection.
slicer.unselect_items(["Pink"])
```

フィルターを解除します（すべてのアイテムを選択します）：

```python
# Clear the filter; all slicer items become selected again.
slicer.clear_filter()
```

{{< app/cells/assistant language="python-net" >}}