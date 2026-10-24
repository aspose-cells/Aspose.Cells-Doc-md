---
title: スライサーの更新
linktitle: スライサーの更新
type: docs
weight: 50
url: /ja/java/updating-slicer/
description: この記事では、Aspose.Cells for Java APIを使用してスライサーを更新し、リンクされたピボットテーブルまたはテーブルのデータをフィルター処理する方法を示します。
keywords: Aspose.Cells Java スライサーの更新、Java スライサーの変更方法、Javaでスライサーによるピボットテーブルのフィルター方法、Java Slicer selectItems、Java Slicer clearFilter、Java Slicer unselectItems。
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能な使用シナリオ**
スライサーの更新とは、スライサーが接続されているピボットテーブルまたはテーブルのデータをフィルター処理することを意味します。Microsoft Excelでスライサーのアイテムを選択または選択解除すると、リンクされたピボットテーブルまたはテーブルがそれに応じて再計算されます。Aspose.Cells for Javaでは、スライサーキャッシュアイテムを反復処理してスライサーを手動でリフレッシュする必要はありません。[Slicer.selectItems(String[], boolean)](https://reference.aspose.com/cells/java/com.aspose.cells/slicer/#selectItems-java.lang.String---boolean-)メソッドがスライサーを更新し、フィルターアイテムから直接、リンクされたピボットテーブルまたはテーブルを再計算します：
- `Slicer.selectItems(labels, append)` — 指定されたラベルを選択し、リンクされたピボットテーブルまたはテーブルを再計算します。`append`が`true`の場合は元々選択されていたラベルが保持され、指定されたラベルが選択に追加されます。`append`が`false`の場合は元の選択がすべてクリアされ、指定されたラベルのみが選択された状態になります。
- `Slicer.unselectItems(labels)` — 現在選択されているアイテムの一部を選択解除します。
- `Slicer.clearFilter()` — フィルターを解除してすべてのアイテムを選択します。

{{% alert color="primary" %}}
Aspose.Cells for Java 26.10以降、`SlicerCacheItem.Selected`プロパティは読み取り専用になり、そのセッターはサポートされなくなります。`SlicerCacheItem.Selected`をアイテムごとに設定する代わりに、`Slicer.selectItems`、`Slicer.unselectItems`、`Slicer.clearFilter`メソッドを使用してください。
{{% /alert %}}

## **スライサーを更新する**
次のサンプルコードは、ピボットテーブルに接続された既存のスライサーを含む[サンプルExcelファイル](67338506.xlsx)を読み込みます。`Slicer.selectItems(labels, false)`を使用してスライサーの"Blue"と"Pink"のアイテムのみを選択すると、ピボットテーブルはフィルターアイテムから直接再計算され、手動での`Slicer.refresh()`の呼び出しは不要です。その後、ワークブックを[出力Excelファイル](67338505.xlsx)として保存します。次のスクリーンショットは、サンプルコードがサンプルExcelファイルに与える影響を示しています。スクリーンショットでわかるように、ピボットテーブルにはフィルターされたアイテムのみが表示されます。
![todo:image_alt_text](updating-slicer_1.png)

## **サンプルコード**
現在の選択を置き換え（指定されたラベルのみが選択された状態になります）、リンクされたピボットテーブルまたはテーブルを再計算します：

```java
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
import com.aspose.cells.Slicer;
// Load sample Excel file containing slicer.
Workbook workbook = new Workbook("sampleUpdatingSlicer.xlsx");
// Access first worksheet.
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
Slicer slicer = worksheet.getSlicers().get(0);
// Select only "Blue" and "Pink"; the linked pivot table or table
// is recalculated directly from the filter items.
slicer.selectItems(new String[] { "Blue", "Pink" }, false);
// Save the modified workbook.
workbook.save("out.xlsx");
```

現在選択されているラベルを保持したまま、さらにアイテムを選択します：

```java
// Keep the current selection and add "Red" to it.
slicer.selectItems(new String[] { "Red" }, true);
```

選択されたアイテムの一部を選択解除します：

```java
// Remove "Pink" from the current selection.
slicer.unselectItems(new String[] { "Pink" });
```

フィルターを解除します（すべてのアイテムを選択します）：

```java
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="java" >}}