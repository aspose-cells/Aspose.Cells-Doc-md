---
title: スライサーの更新
linktitle: スライサーの更新
type: docs
weight: 60
url: /ja/python-java/updating-slicer/
description: この記事では、Aspose.Cells for Python via Java APIを使用してスライサーを更新し、リンクされたピボットテーブルまたはテーブルのデータをフィルター処理する方法を示します。
keywords: Aspose.Cells for Python via Java スライサーの更新、Python Java スライサーの更新、Pythonでスライサーによるピボットテーブルのフィルター方法、Slicer selectItems、Slicer clearFilter、Slicer unselectItems。
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **スライサーを更新する**
スライサーの更新とは、スライサーが接続されているピボットテーブルまたはテーブルのデータをフィルター処理することを意味します。Aspose.Cells for Python via Javaは、フィルターアイテムから直接スライサーを更新し、リンクされたピボットテーブルまたはテーブルを再計算します：
- `Slicer.selectItems(labels, append)` — 指定されたラベルを選択し、リンクされたピボットテーブルまたはテーブルを再計算します。`append`が`True`の場合は元々選択されていたラベルが保持され、指定されたラベルが選択に追加されます。`append`が`False`の場合は元の選択がすべてクリアされ、指定されたラベルのみが選択された状態になります。
- `Slicer.unselectItems(labels)` — 現在選択されているアイテムの一部を選択解除します。
- `Slicer.clearFilter()` — フィルターを解除してすべてのアイテムを選択します。

{{% alert color="primary" %}}
Aspose.Cells for Python via Java 26.10以降、`SlicerCacheItem.Selected`プロパティは読み取り専用になり、そのセッターはサポートされなくなります。`SlicerCacheItem.Selected`をアイテムごとに設定する代わりに、`Slicer.selectItems`、`Slicer.unselectItems`、`Slicer.clearFilter`メソッドを使用してください。
次のコードスニペットは、ピボットテーブルに接続されたスライサーを含む[サンプルExcelファイル](106365050.xlsx)を読み込みます。`Slicer.selectItems(labels, False)`を使用してスライサーの"Blue"と"Pink"のアイテムのみを選択すると、ピボットテーブルはフィルターアイテムから直接再計算され、手動での`Slicer.refresh()`の呼び出しは不要です。その後、ワークブックを[出力Excelファイル](106365051.xlsx)として保存します。次のスクリーンショットは、サンプルコードがサンプルExcelファイルに与える影響を示しています。スクリーンショットでわかるように、ピボットテーブルにはフィルターされたアイテムのみが表示されます。
![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
{{% /alert %}}

## **サンプルコード**
現在の選択を置き換え（指定されたラベルのみが選択された状態になります）、リンクされたピボットテーブルまたはテーブルを再計算します：

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Load sample Excel file containing slicer.
workbook = Workbook("sampleUpdatingSlicer.xlsx")
# Access first worksheet.
worksheet = workbook.getWorksheets().get(0)
# Access the first slicer inside the slicer collection.
slicer = worksheet.getSlicers().get(0)
# Select only "Blue" and "Pink"; the linked pivot table or table
# is recalculated directly from the filter items.
slicer.selectItems(["Blue", "Pink"], False)
# Save the modified workbook.
workbook.save("out.xlsx")
jpype.shutdownJVM()
```

現在選択されているラベルを保持したまま、さらにアイテムを選択します：

```python
# Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], True)
```

選択されたアイテムの一部を選択解除します：

```python
# Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"])
```

フィルターを解除します（すべてのアイテムを選択します）：

```python
# Clear the filter; all slicer items become selected again.
slicer.clearFilter()
```

{{< app/cells/assistant language="python" >}}