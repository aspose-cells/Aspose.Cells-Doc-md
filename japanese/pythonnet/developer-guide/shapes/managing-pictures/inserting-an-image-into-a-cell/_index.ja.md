---
title: セルへの画像の挿入
description: Aspose.Cells はスプレッドシートファイルを扱うための Python ライブラリです。この記事では、フローティング画像をセル上に配置する方法と、画像をセルに直接埋め込む方法という 2 つの異なるアプローチを使用して、画像を 1 つのセルサイズに正確に合わせる方法を説明します。
keywords: Aspose.Cells, Python ライブラリ, スプレッドシート, 画像挿入, 画像埋め込み, セル内画像, セルへの画像の合わせ方, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /ja/python-net/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells は、画像を 1 つのセルに関連付ける 2 つの異なる方法を提供します。フローティング画像はワークシートの描画レイヤー上の図形であり、セル範囲を視覚的に重ね合わせますが、埋め込み画像はセル自体の中に格納され、セルの表示領域に合わせて自動的に拡大縮小されます。レイアウト要件に最も合う方法を選択してください。

{{% /alert %}}

## **はじめに**

ビジュアルレポート、商品カタログ、社員ディレクトリ、ダッシュボード、在庫リストなどとして機能するスプレッドシートを設計する際、画像を 1 つのセルに正確に合わせることは一般的な要件です。多くのセルに画像をまたがって配置したり、ワークシート上に緩く配置したりする代わりに、それを所有するセルに整列された、クリーンでセルに紐づいた画像が必要になる場合があります。

Aspose.Cells は、このシナリオを 2 つの補完的な方法でサポートしています。

- **方法 1 — セル上にフローティング画像を配置する。** ワークシートに `Picture` を追加し、その `placement` を `MOVE_AND_SIZE` に設定し、画像がちょうど 1 つのセルをカバーするようにアンカーセル (`upper_left_row`、`upper_left_column`、`lower_right_row`、`lower_right_column`) を調整します。
- **方法 2 — 画像をセルに直接埋め込む。** 画像のバイト列をセルの `embedded_image` プロパティに割り当てます。画像はセルの表示領域に合わせて自動的に拡大縮小され、セルと一緒に移動します。

この記事の残りでは、両方の方法を順を追って説明し、関連する API について説明し、コードでの使用方法を示します。

## **方法 1: セル上に画像を配置する**

フローティング画像は、ワークシートの描画レイヤーに存在する `Picture` オブジェクトです。単一セルの一部ではありませんが、セル範囲にアンカーされています。画像のアンカーセル (左上隅と右下隅) は、ワークシート上の画像の視覚的な範囲を決定します。デフォルトでは、新しく追加された画像は複数のセルにまたがります。

フローティング画像を **ちょうど 1 つのセル** をカバーするようにするには、次の手順が必要です。

1. `Worksheet.pictures.add(row, column, stream)` を使用して画像を追加します。これにより、新しい画像が指定されたセルにアンカーされます。
2. 4 つのアンカープロパティを設定して、画像の境界矩形がターゲットセルと一致するようにします。
3. `Picture.placement` を `PlacementType.MOVE_AND_SIZE` に設定します。これにより、ユーザーが列幅または行の高さを変更したときに、画像が下のセルと一緒に移動およびサイズ変更されます。

### **単一セルへの画像のアンカー設定**

画像のアンカーは、4 つのゼロベースインデックスプロパティで定義されています。

- `Picture.upper_left_row` — 画像の上端の行インデックス。
- `Picture.upper_left_column` — 画像の左端の列インデックス。
- `Picture.lower_right_row` — 画像の下端の行インデックス。画像の下端を行 `r` の底部に配置するには、これを `r + 1` に設定します。
- `Picture.lower_right_column` — 画像の右端の列インデックス。画像の右端を列 `c` の右側に配置するには、これを `c + 1` に設定します。

たとえば、画像をセル **C6** (行インデックス `5`、列インデックス `2`) に正確に合わせるには、`upper_left_row = 5`、`upper_left_column = 2`、`lower_right_row = 6`、`lower_right_column = 3` を設定します。

{{% alert color="primary" %}}

Aspose.Cells の行と列のインデックスは **ゼロベース** です。セル C6 は行インデックス 5、列インデックス 2 を持ちます。右下アンカーでの 1 つずつのエラーは、隣接するセルに重なって見える画像の最も一般的な原因です。

{{% /alert %}}

### **配置動作の制御**

`Picture.placement` は `PlacementType` 型の列挙型で、ユーザーが下にある行または列のサイズを変更したときに画像がどのように動作するかを制御します。単一セル画像の推奨値は `PlacementType.MOVE_AND_SIZE` であり、これにより画像はその下のセルと一緒に移動およびサイズ変更され、正確なフィット感が維持されます。

### **ステップバイステップの手順**

1. 新しい `Workbook` を作成します (または既存のものを開きます)。
2. `workbook.worksheets[0]` からターゲットの `Worksheet` にアクセスします。
3. `with` ブロックを使用して、画像ファイルをディスクからファイルストリーム (または `BytesIO` オブジェクト) に開きます。これにより、ストリームが適切に破棄されます。
4. `worksheet.pictures.add(5, 2, stream)` を呼び出して、セル C6 にアンカーされた画像を追加します。返された `Picture` 参照をキャプチャします。
5. 4 つのアンカー座標を設定して、画像がセル C6 のみをカバーするようにします: `upper_left_row = 5`、`upper_left_column = 2`、`lower_right_row = 6`、`lower_right_column = 3`。
6. `picture.placement = PlacementType.MOVE_AND_SIZE` を設定して、列または行のサイズが変更されたときに画像を C6 に整列させます。
7. オプションで、周囲のセルにサンプルテキストを追加して、セル C6 のみに画像が含まれていることを示します。
8. ワークブックをディスクに `.xlsx` ファイルとして保存します。

次のコードは、完全な方法を示しています。

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

with open("logo.png", "rb") as fs:
    pic_index = worksheet.pictures.add(5, 2, fs)
    picture = worksheet.pictures[pic_index]
    picture.upper_left_row = 5
    picture.upper_left_column = 2
    picture.lower_right_row = 6
    picture.lower_right_column = 3
    picture.placement = ac.PlacementType.MOVE_AND_SIZE

workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **方法 2: 画像をセルに直接埋め込む**

Aspose.Cells は、セルに紐づいた画像のためのよりシンプルなメカニズムも公開しています。それは `Cell.embedded_image` プロパティです。このプロパティに画像バイトを割り当てると、画像がインラインコンテンツのようにセル自体に添付されます。

### **埋め込み画像の仕組み**

- 画像は、描画レイヤー上の図形としてではなく、セルコンテンツの一部として格納されます。
- 画像は、セルのレンダリングされた境界内に収まるように自動的に拡大縮小されます。アンカー座標や配置設定は必要ありません。
- セルは、数式で参照したり、行の一部として並べ替えたり、他のセルレベルの操作に使用したりできる、実アドレスを持つ実際のセルのままです。

これにより、目標が単に「このセル内に存在する画像」である場合、`Cell.embedded_image` が最も簡潔なオプションになります。

### **ステップバイステップの手順**

1. 新しい `Workbook` を作成します (または既存のものを開きます)。
2. `workbook.worksheets[0]` からターゲットの `Worksheet` にアクセスします。
3. 画像ファイルをディスクから `bytes` オブジェクトに読み込みます (たとえば、バイナリモードでファイルを開き、`.read()` を呼び出します)。
4. ターゲットセルへの参照を取得します — `worksheet.cells["C6"]` または `worksheet.cells[5, 2]` のいずれかを介して。
5. `bytes` オブジェクトをセルの `embedded_image` プロパティに割り当てます。
6. オプションで、ターゲット行と列の行の高さと列の幅を調整して、埋め込み画像をより目立つようにします。
7. ワークブックをディスクに `.xlsx` ファイルとして保存します。

次のコードは、完全な方法を示しています。

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# 対象セル C6 を取得する
cell = worksheet.cells["C6"]

# 画像ファイルをバイト配列に読み込む
with open("logo.png", "rb") as f:
    imageData = f.read()

# 画像をセルに直接埋め込む
cell.embedded_image = imageData

# 埋め込まれた画像をより見やすくするために、必要に応じて行の高さと列の幅を調整する
worksheet.cells.set_column_width(2, 30)   # 列 C (インデックス 2)
worksheet.cells.set_row_height(5, 100)     # 行 6 (インデックス 5)

# 結果のワークブックを .xlsx ファイルとして保存する
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **適切な方法を選択する**

両方の方法とも、単一セル内に収まる画像を生成しますが、画像の保存方法と動作が異なります。

- **次のような場合は、フローティング画像 (方法 1) を使用します。**
  - 他の描画オブジェクトとの配置、レイヤー化、整列をより細かく制御する必要がある場合。
  - 画像を他の図形と選択、並べ替え、グループ化できる図形として動作させたい場合。
  - すでに `pictures` コレクションで動作するコードとのレガシー互換性が必要な場合。
  - ワークシートのレイアウトに基づいてアンカー座標を動的に計算する必要がある場合。

- **次のような場合は、埋め込み画像 (方法 2) を使用します。**
  - セルへの画像の挿入をできるだけシンプルにしたい場合。
  - 画像が他のセルコンテンツと同様にセルと一緒に移動するようにしたい場合。
  - 画像を図形として操作する必要がない場合。

{{% alert color="primary" %}}

両方の方法は同じワークブック内で共存できます。1 セットのセルにフローティング画像を配置し、他のセルに画像を直接埋め込むことができます。これは、2 つのメカニズムがファイル内の異なるストレージレイヤーを使用するためです。

{{% /alert %}}

## **関連記事**

- [セルに画像を挿入する方法](/cells/ja/python-net/how-to-place-image-to-cell/)
- [画像ハイパーリンクの追加](/cells/ja/python-net/add-image-hyperlinks/)
- [URL から Web 画像を Excel ワークシートに読み込む](/cells/ja/python-net/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [位置、サイズ、デザイナーグラフの操作](/cells/ja/python-net/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="python" >}}