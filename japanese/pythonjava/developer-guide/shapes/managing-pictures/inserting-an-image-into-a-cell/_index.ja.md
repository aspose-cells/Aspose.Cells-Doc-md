---
title: セルへの画像の挿入
linktitle: セルへの画像の挿入
description: Aspose.Cells for Python via Java はスプレッドシートファイルを操作するためのライブラリです。この記事では、フローティング画像をセル上に配置する方法、または画像をセルに直接埋め込むことによって、画像を正確に 1 つのセルに合わせる方法について説明します。
keywords: Aspose.Cells, Python via Java ライブラリ, スプレッドシート, 画像挿入, 画像埋め込み, セル内画像, 画像をセルに合わせる, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /ja/python-java/inserting-an-image-into-a-cell/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は画像を単一セルに関連付ける 2 つの異なる方法を提供します。フローティング画像はワークシートの描画レイヤーに配置される図形であり、セル範囲の上に視覚的に重なります。一方、埋め込み画像はセル自体の中に保存され、セルの表示領域に合わせて自動的にスケーリングされます。レイアウト要件に最も合った方法を選択してください。

## **はじめに**
ビジュアルレポート、製品カタログ、社員ディレクトリ、ダッシュボード、在庫リストのように機能するスプレッドシートを設計する際、画像を正確に 1 つのセルに合わせることは一般的な要件です。画像を複数のセルにまたがって引き伸ばしたり、ワークシート上に緩く配置したりする代わりに、それを所有するセルと整合性が保たれるクリーンなセル境界の画像が必要になる場合があります。
Aspose.Cells はこのシナリオを 2 つの補完的な方法でサポートします。
- **方法 1 — フローティング画像をセル上に配置する。** `Picture` をワークシートに追加し、その `setPlacement` を `MOVE_AND_SIZE` に設定し、アンカーセル (`setUpperLeftRow`、`setUpperLeftColumn`、`setLowerRightRow`、`setLowerRightColumn`) を調整して、画像を正確に 1 つのセルに合わせます。
- **方法 2 — 画像をセルに直接埋め込む。** 画像のバイト配列をセルの `setEmbeddedImage` プロパティに割り当てます。画像はセルの表示領域に合わせて自動的にスケーリングされ、セルと一緒に移動します。
この記事の残りの部分では、両方の方法を順に説明し、関連する API を解説し、それらをコードで使用する方法を示します。

## **方法 1：画像をセル上に配置する**
フローティング画像は、ワークシートの描画レイヤーに存在する `Picture` オブジェクトです。単一セルの一部ではありませんが、セル範囲にアンカーされています。画像の位置と範囲を決定するのは、画像アンカーセル（画像の左上隅と右下隅）です。デフォルトでは、追加直後の画像は複数のセルにまたがります。
フローティング画像を**正確に 1 つのセル**に合わせるには、以下の手順が必要です。
1. `Worksheet.getPictures().add(int row, int column, InputStream stream)` を使用して画像を追加し、新しい画像を指定されたセルにアンカーします。
2. 4 つのアンカープロパティを設定し、画像の境界矩形が対象のセルと一致するようにします。
3. `Picture.setPlacement` を `PlacementType.MOVE_AND_SIZE` に設定し、ユーザーが列幅や行高を変更したときに、画像が基になるセルと一緒に移動およびサイズ変更されるようにします。

### **画像を単一セルにアンカーする**
画像アンカーは、4 つのゼロベースインデックスプロパティで定義されます。
- `setUpperLeftRow` — 画像の上端の行インデックス。
- `setUpperLeftColumn` — 画像の左端の列インデックス。
- `setLowerRightRow` — 画像の下端の行インデックス。画像の下端を行 `r` の下部に配置するには、これを `r + 1` に設定します。
- `setLowerRightColumn` — 画像の右端の列インデックス。画像の右端を列 `c` の右側に配置するには、これを `c + 1` に設定します。

{{% alert color="primary" %}}
Aspose.Cells の行と列のインデックスは **ゼロベース** です。セル C6 の行インデックスは 5、列インデックスは 2 です。右下アンカーにおけるオフバイワンエラーが、隣接セルにはみ出して表示される画像の最も一般的な原因です。

### **配置動作の制御**
`getPlacement` は `PlacementType` の列挙型で、ユーザーが基になる行または列のサイズを変更したときの画像の動作を制御します。単一セル画像に推奨される値は `PlacementType.MOVE_AND_SIZE` であり、これにより画像が基になるセルと一緒に移動およびサイズ変更され、正確な適合が維持されます。

### **ステップごとの手順**
1. 新しい `Workbook` を作成します（または既存のものを開きます）。
2. `workbook.getWorksheets().get(0)` から対象の `Worksheet` にアクセスします。
3. ディスクから画像ファイルを `InputStream`（通常は `FileInputStream`）に開き、ストリームが適切に閉じられるようにします。
4. `worksheet.getPictures().add(5, 2, stream)` を呼び出して、セル C6 にアンカーされた画像を追加します。返された `Picture` 参照を取得します。
5. 4 つのアンカー座標を設定して、画像がセル C6 のみを覆うようにします：`setUpperLeftRow(5)`、`setUpperLeftColumn(2)`、`setLowerRightRow(6)`、`setLowerRightColumn(3)`。
6. 列または行のサイズが変更されたときに画像を C6 に整合させるために、`picture.setPlacement(PlacementType.MOVE_AND_SIZE)` を設定します。
7. 必要に応じて、周囲のセルにサンプルテキストを追加して、セル C6 のみに画像が含まれていることを示します。
8. ワークブックをディスクに `.xlsx` ファイルとして保存します。
次のコードは完全な方法を示しています。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, SaveFormat, PlacementType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
FileInputStream = jpype.JClass("java.io.FileInputStream")
fs = FileInputStream("logo.png")
try:
    picIndex = worksheet.getPictures().add(5, 2, fs)
    picture = worksheet.getPictures().get(picIndex)
    picture.setUpperLeftRow(5)
    picture.setUpperLeftColumn(2)
    picture.setLowerRightRow(6)
    picture.setLowerRightColumn(3)
    picture.setPlacement(PlacementType.MoveAndSize)
finally:
    fs.close()
workbook.save("output.xlsx", SaveFormat.Xlsx)
jpype.shutdownJVM()
```

## **方法 2：画像をセルに直接埋め込む**
Aspose.Cells は、セルにバインドされた画像のためのよりシンプルなメカニズムも提供しています：`Cell.setEmbeddedImage` プロパティです。このプロパティに画像バイト配列を割り当てると、画像がセル自体にインラインコンテンツのようにアタッチされます。

### **埋め込み画像の仕組み**
- 画像は描画レイヤー上の図形としてではなく、セルコンテンツの一部として保存されます。
- 画像は、セルのレンダリング境界内に収まるように自動的にスケーリングされます。アンカー座標や配置設定は必要ありません。
- セルは実際のセルであり、数式で参照できる実際のアドレスを持ち、行の一部としてソートされたり、他のセルレベルの操作で使用されたりできます。
これにより、`Cell.setEmbeddedImage` は目標が単純に「このセル内に存在する画像」である場合の最も簡潔なオプションになります。

### **ステップごとの手順**
1. 新しい `Workbook` を作成します（または既存のものを開きます）。
2. `workbook.getWorksheets().get(0)` から対象の `Worksheet` にアクセスします。
3. ディスクから画像ファイルを `byte[]` 配列に読み込みます（たとえば、`java.nio.file.Files` の `Files.readAllBytes` 呼び出しを使用します）。
4. 対象のセルへの参照を取得します。`worksheet.getCells().get("C6")` または `worksheet.getCells().get(5, 2)` のいずれかを使用します。
5. バイト配列をセルの `setEmbeddedImage` プロパティに割り当てます。
6. 必要に応じて、対象の行と列の行高と列幅を調整して、埋め込み画像をより目立つようにします。
7. ワークブックをディスクに `.xlsx` ファイルとして保存します。
次のコードは完全な方法を示しています。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Get the target cell C6
cell = worksheet.getCells().get("C6")
# Read the image file into a byte array
imageData = open("logo.png", "rb").read()
# Embed the image directly into the cell
cell.setEmbeddedImage(imageData)
# Optionally adjust row height and column width so the embedded image is more visible
worksheet.getCells().setColumnWidth(2, 30)   # Column C (index 2)
worksheet.getCells().setRowHeight(5, 100)    # Row 6 (index 5)
# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", SaveFormat.Xlsx)
jpype.shutdownJVM()
```

## **適切な方法の選択**
両方の方法は単一セル内に収まる画像を生成しますが、画像の保存方法と動作が異なります。
- **次のような場合は、フローティング画像（方法 1）を使用します：**
  - 他の描画オブジェクトとの配置、レイヤー化、整列をより細かく制御する必要がある場合。
  - 画像を、他の図形と選択、並べ替え、グループ化できる図形として動作させたい場合。
  - `PictureCollection` で既に動作するコードとのレガシー互換性が必要な場合。
  - ワークシートのレイアウトに基づいてアンカー座標を動的に計算する必要がある場合。
- **次のような場合は、埋め込み画像（方法 2）を使用します：**
  - セルへの画像の挿入を可能な限りシンプルにしたい場合。
  - 画像が他のセルコンテンツと同様にセルと一緒に移動するべき場合。
  - 画像を図形として操作する必要がない場合。
{{% /alert %}}

{{% /alert %}}

{{< app/cells/assistant language="python" >}}