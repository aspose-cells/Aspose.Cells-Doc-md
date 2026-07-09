---
title: セルに画像を挿入する
description: Aspose.Cells for Python via Java はスプレッドシートファイルを操作するためのライブラリです。この記事では、ピクチャを単一セルのサイズにぴったり合わせる方法を 2 つの異なるアプローチで説明します。セル上にフローティングピクチャを配置する方法と、画像をセルに直接埋め込む方法です。
keywords: Aspose.Cells, Python via Java ライブラリ, スプレッドシート, 画像挿入, 画像埋め込み, セル内ピクチャ, セルに画像を合わせる, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /ja/python-java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells では、画像を 1 つのセルに関連付ける方法が 2 通りあります。フローティングピクチャはワークシートの描画レイヤーに配置されるシェイプで、セル範囲の上に視覚的に重なって表示されます。一方、埋め込み画像はセル自体の中に格納され、セルの表示領域に合わせて自動的に拡大縮小されます。レイアウト要件に最も合った方法を選択してください。

{{% /alert %}}

## **はじめに**

ピクチャを 1 つのセルにぴったり合わせることは、ビジュアルレポート、製品カタログ、社員ディレクトリ、ダッシュボード、在庫リストなどとして機能するスプレッドシートを設計する際に頻繁に求められます。多くのセルにまたがって画像を引き伸ばしたり、ワークシート上に緩く配置したりする代わりに、所有するセルと位置がそろったセルに紐付けられたクリーンな画像が望ましい場合があります。

Aspose.Cells では、このシナリオを 2 つの補完的な方法でサポートしています。

- **方法 1 — セル上にフローティングピクチャを配置する。** ワークシートに `Picture` を追加し、その `setPlacement` を `MOVE_AND_SIZE` に設定し、アンカーセル(`setUpperLeftRow`、`setUpperLeftColumn`、`setLowerRightRow`、`setLowerRightColumn`)を調整して、ピクチャがちょうど 1 つのセルを覆うようにします。
- **方法 2 — 画像をセルに直接埋め込む。** 画像バイト列をセルの `setEmbeddedImage` プロパティに割り当てます。画像は自動的にセルの表示領域に合わせて拡大縮小され、セルと一緒に移動します。

この記事の残りでは、両方の方法を順に説明し、関連する API を解説し、コードでの使用例を示します。

## **方法 1: セル上にピクチャを配置する**

フローティングピクチャは、ワークシートの描画レイヤーに存在する `Picture` オブジェクトです。単一セルの一部ではありませんが、セル範囲にアンカーされています。ピクチャのアンカーセル (左上隅と右下隅) は、ワークシート上での表示範囲を決定します。デフォルトでは、追加したばかりのピクチャは複数のセルにまたがります。

フローティングピクチャを**ちょうど 1 つのセル**に収めるには、次の手順が必要です。

1. `Worksheet.getPictures().add(int row, int column, InputStream stream)` を使用してピクチャを追加します。これにより新しいピクチャが指定されたセルにアンカーされます。
2. 4 つのアンカープロパティを設定し、ピクチャの外接する長方形が対象のセルと一致するようにします。
3. ユーザーが列幅や行の高さを変更したときにピクチャがセルと一緒に移動およびサイズ変更されるように、`Picture.setPlacement` を `PlacementType.MOVE_AND_SIZE` に設定します。

### **ピクチャを 1 つのセルにアンカーする**

ピクチャのアンカーは、4 つのゼロベースのインデックスプロパティで定義されます。

- `setUpperLeftRow` — ピクチャの上端の行インデックス。
- `setUpperLeftColumn` — ピクチャの左端の列インデックス。
- `setLowerRightRow` — ピクチャの下端の行インデックス。ピクチャの下端を行 `r` の下部に配置するには、これを `r + 1` に設定します。
- `setLowerRightColumn` — ピクチャの右端の列インデックス。ピクチャの右端を列 `c` の右端に配置するには、これを `c + 1` に設定します。

たとえば、**C6** セル (行インデックス `5`、列インデックス `2`) にピクチャを正確に合わせるには、`setUpperLeftRow(5)`、`setUpperLeftColumn(2)`、`setLowerRightRow(6)`、`setLowerRightColumn(3)` を設定します。

{{% alert color="primary" %}}

Aspose.Cells の行および列のインデックスは**ゼロベース**です。C6 セルの行インデックスは 5、列インデックスは 2 です。右下アンカーのオフバイワンエラーは、ピクチャが隣接セルにはみ出して表示される最も一般的な原因です。

{{% /alert %}}

### **配置動作の制御**

`getPlacement` は `PlacementType` 型の列挙型で、ユーザーが下にある行や列のサイズを変更したときのピクチャの動作を制御します。単一セル用のピクチャに推奨される値は `PlacementType.MOVE_AND_SIZE` です。これを指定すると、ピクチャは下にあるセルと一緒に移動およびサイズ変更され、正確なフィット感が維持されます。

### **手順ごとの説明**

1. 新しい `Workbook` を作成します (または既存のブックを開きます)。
2. `workbook.getWorksheets().get(0)` から対象の `Worksheet` を取得します。
3. ディスク上の画像ファイルを `InputStream` (通常は `FileInputStream`) に開いて、ストリームが適切にクローズされるようにします。
4. `worksheet.getPictures().add(5, 2, stream)` を呼び出して、C6 セルにアンカーされたピクチャを追加します。返される `Picture` 参照を取得します。
5. 4 つのアンカー座標を設定し、ピクチャが C6 セルのみを覆うようにします: `setUpperLeftRow(5)`、`setUpperLeftColumn(2)`、`setLowerRightRow(6)`、`setLowerRightColumn(3)`。
6. 列または行のサイズが変更されたときにピクチャが C6 に揃ったままになるように、`picture.setPlacement(PlacementType.MOVE_AND_SIZE)` を設定します。
7. 必要に応じて、周囲のセルにサンプルテキストを追加して C6 セルにのみピクチャが含まれていることを示します。
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

## **方法 2: 画像をセルに直接埋め込む**

Aspose.Cells では、セルに紐付けられた画像用のよりシンプルな仕組みも提供されています。それが `Cell.setEmbeddedImage` プロパティです。このプロパティに画像バイト列を割り当てると、画像はインラインコンテンツであるかのようにセル自体に添付されます。

### **埋め込み画像の仕組み**

- 画像は、描画レイヤー上のシェイプとしてではなく、セルコンテンツの一部として格納されます。
- 画像は、セルのレンダリング境界内に収まるように自動的に拡大縮小されます。アンカー座標や配置設定は不要です。
- セルは実際のセルとしてそのまま存在し、実際のアドレスを持つため、数式で参照したり、行のソート対象にしたり、その他のセルレベルの操作に使用したりできます。

このため `Cell.setEmbeddedImage` は、「このセル内に存在する画像」を単純に実現したい場合の最も簡潔なオプションです。

### **手順ごとの説明**

1. 新しい `Workbook` を作成します (または既存のブックを開きます)。
2. `workbook.getWorksheets().get(0)` から対象の `Worksheet` を取得します。
3. ディスク上の画像ファイルを `byte[]` 配列に読み込みます (たとえば `java.nio.file.Files` の `Files.readAllBytes` 呼び出しを使用します)。
4. 対象のセルへの参照を取得します (`worksheet.getCells().get("C6")` または `worksheet.getCells().get(5, 2)` のいずれか)。
5. バイト配列をセルの `setEmbeddedImage` プロパティに割り当てます。
6. 必要に応じて、対象の行と列の行の高さと列幅を調整し、埋め込み画像をより目立つようにします。
7. ワークブックをディスクに `.xlsx` ファイルとして保存します。

次のコードは完全な方法を示しています。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat

# 移植されたコード
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# 対象セルC6を取得
cell = worksheet.getCells().get("C6")

# 画像ファイルをバイト配列に読み込む
imageData = open("logo.png", "rb").read()

# 画像をセルに直接埋め込む
cell.setEmbeddedImage(imageData)

# 埋め込まれた画像をより見やすくするため、必要に応じて行の高さと列の幅を調整する
worksheet.getCells().setColumnWidth(2, 30)   # 列C（インデックス2）
worksheet.getCells().setRowHeight(5, 100)    # 行6（インデックス5）

# 結果のワークブックを.xlsxファイルとして保存する
workbook.save("output.xlsx", SaveFormat.Xlsx)

jpype.shutdownJVM()
```

## **適切な方法の選択**

どちらの方法も単一セル内に収まるピクチャを生成しますが、ピクチャの格納方法と動作が異なります。

- **次のような場合はフローティングピクチャ (方法 1) を使用します。**
  - 配置、レイヤー順、または他の描画オブジェクトとの位置合わせをより細かく制御する必要がある場合。
  - ピクチャを他のシェイプと選択したり、並び替えたり、グループ化したりできるシェイプとして扱いたい場合。
  - すでに `PictureCollection` を使用しているコードとのレガシー互換性が必要な場合。
  - ワークシートのレイアウトに基づいてアンカー座標を動的に計算する必要がある場合。

- **次のような場合は埋め込み画像 (方法 2) を使用します。**
  - セルへの画像の挿入を可能な限りシンプルに行いたい場合。
  - 画像が他のセルコンテンツと同様にセルと一緒に移動するようにしたい場合。
  - 画像をシェイプとして操作する必要がない場合。

{{% alert color="primary" %}}

両方の方法は同じワークブック内に共存できます。2 つの仕組みはファイル内で異なるストレージレイヤーを使用しているため、一方のセル群にはフローティングピクチャを配置し、別のセルには画像を直接埋め込むことができます。

{{% /alert %}}



{{< app/cells/assistant language="python" >}}