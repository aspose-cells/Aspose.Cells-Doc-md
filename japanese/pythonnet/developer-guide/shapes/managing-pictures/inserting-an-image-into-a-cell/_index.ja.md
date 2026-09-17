---
title: セルに画像を挿入する
linktitle: セルに画像を挿入する
description: Aspose.Cellsは、スプレッドシートファイルを扱うためのライブラリです。この記事では、セル上にフローティング画像を配置する方法や、画像をセルに直接埋め込むことによって、画像を単一のセルにぴったり合わせる方法を説明します。
keywords: Aspose.Cells, Python, ライブラリ, スプレッドシート, 画像挿入, 画像埋め込み, セル内画像, 画像サイズ調整, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /ja/python-net/inserting-an-image-into-a-cell/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cellsは、単一のセルに画像を関連付ける2つの異なる方法を提供します。フローティング画像はワークシートの描画レイヤーに配置される図形で、セル範囲を視覚的に覆うのに対し、埋め込み画像はセル自体の中に格納され、セルの表示領域に自動的にスケールします。レイアウトの要件に最適な方法を選択してください。
{{% /alert %}}

## **はじめに**
単一のセルに画像をぴったり合わせることは、視覚的なレポート、製品カタログ、社員ディレクトリ、ダッシュボード、在庫リストなどとして機能するスプレッドシートを設計する際の一般的な要件です。多くのセルにわたって画像を伸ばしたり、ワークシート上に緩く配置したりする代わりに、所有するセルに揃った清潔なセル境界の画像が必要となる場合があります。
Aspose.Cellsは、このシナリオを2つの補完的な方法でサポートしています。
- **アプローチ1 — セル上にフローティング画像を配置する。** `Picture`をワークシートに追加し、その`placement`を`MOVE_AND_SIZE`に設定し、アンカーセル(`upper_left_row`、`upper_left_column`、`lower_right_row`、`lower_right_column`)を調整して、画像が正確に1つのセルを覆うようにします。
- **アプローチ2 — 画像をセルに直接埋め込む。** 画像のバイトをセルの`embedded_image`プロパティに割り当てます。画像はセルの表示領域に合わせて自動的にスケールされ、セルと一緒に移動します。
この記事の残りの部分では、両方のアプローチについて説明し、関連するAPIを紹介し、コードでの使用方法を示します。

## **アプローチ1: セル上に画像を配置する**
フローティング画像は、ワークシートの描画レイヤーに存在する`Picture`オブジェクトです。単一セルの一部ではありませんが、セル範囲にアンカーされています。画像のアンカーセル(左上と右下の角)は、ワークシート上の視覚的な範囲を決定します。デフォルトでは、新しく追加された画像は複数のセルにまたがります。
フローティング画像を**正確に1つのセル**に覆わせるには、次の手順が必要です。
1. `Worksheet.pictures.add(row, column, stream)`を使用して画像を追加します。これにより、新しい画像が指定されたセルにアンカーされます。
2. 4つのアンカープロパティを設定して、画像の境界矩形がターゲットセルと一致するようにします。
3. `Picture.placement`を`PlacementType.MOVE_AND_SIZE`に設定し、ユーザーが列幅または行の高さを変更したときに画像が基になるセルと一緒に移動およびサイズ変更されるようにします。

### **画像を単一のセルにアンカーする**
画像のアンカーは、4つのゼロベースのインデックスプロパティによって定義されます。
- `Picture.upper_left_row` — 画像の上端の行インデックス。
- `Picture.upper_left_column` — 画像の左端の列インデックス。
- `Picture.lower_right_row` — 画像の下端の行インデックス。画像の下端を行`r`の下部に配置するには、これを`r + 1`に設定します。
- `Picture.lower_right_column` — 画像の右端の列インデックス。画像の右端を列`c`の右側に配置するには、これを`c + 1`に設定します。

{{% alert color="primary" %}}
Aspose.Cellsの行と列のインデックスは**ゼロベース**です。セルC6の行インデックスは5、列インデックスは2です。右下アンカーでの1つ違いのエラーは、画像が隣接セルに重なって表示される最も一般的な原因です。

### **配置動作の制御**
`Picture.placement`は`PlacementType`型の列挙型で、ユーザーが下の行または列をサイズ変更したときの画像の動作を制御します。単一セル画像に対する推奨値は`PlacementType.MOVE_AND_SIZE`で、これにより画像が基になるセルと一緒に移動およびサイズ変更され、正確なフィット感が維持されます。

### **ステップバイステップの手順**
1. 新しい`Workbook`を作成します(または既存のものを開きます)。
2. `workbook.worksheets[0]`からターゲットの`Worksheet`にアクセスします。
3. `with`ブロックを使用して、画像ファイルをディスクからファイルストリーム(または`BytesIO`オブジェクト)に開きます。これにより、ストリームが適切に破棄されます。
4. `worksheet.pictures.add(5, 2, stream)`を呼び出して、セルC6にアンカーされた画像を追加します。返された`Picture`参照を取得します。
5. 4つのアンカー座標を設定して、画像がセルC6のみを覆うようにします。`upper_left_row = 5`、`upper_left_column = 2`、`lower_right_row = 6`、`lower_right_column = 3`。
6. `picture.placement = PlacementType.MOVE_AND_SIZE`を設定し、列または行がサイズ変更されたときに画像をC6に揃えたままにします。
7. オプションで周囲のセルにサンプルテキストを追加して、セルC6のみに画像が含まれていることを示します。
8. ワークブックを`.xlsx`ファイルとしてディスクに保存します。
次のコードは、完全なアプローチを示しています。

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

## **アプローチ2: 画像をセルに直接埋め込む**
Aspose.Cellsは、セルにバインドされた画像のためのよりシンプルなメカニズムも提供しています。`Cell.embedded_image`プロパティです。このプロパティに画像のバイトを割り当てると、画像がセル自体に、インラインコンテンツのように添付されます。

### **埋め込み画像の仕組み**
- 画像は描画レイヤー上の図形としてではなく、セルコンテンツの一部として格納されます。
- 画像は、セルのレンダリング境界に合わせて自動的にスケールされます。アンカー座標や配置設定は必要ありません。
- セルは実際のアドレスを持つ実際のセルのままで、数式で参照したり、行の一部として並べ替えたり、他のセルレベルの操作に使用したりできます。
これにより、`Cell.embedded_image`は目標が単に「このセル内に存在する画像」である場合の最も簡潔なオプションになります。

### **ステップバイステップの手順**
1. 新しい`Workbook`を作成します(または既存のものを開きます)。
2. `workbook.worksheets[0]`からターゲットの`Worksheet`にアクセスします。
3. 画像ファイルをディスクから`bytes`オブジェクトに読み込みます(たとえば、バイナリモードでファイルを開き、`.read()`を呼び出します)。
4. ターゲットセルへの参照を取得します — `worksheet.cells["C6"]`または`worksheet.cells[5, 2]`のいずれかを使用します。
5. bytesオブジェクトをセルの`embedded_image`プロパティに割り当てます。
6. オプションで、ターゲット行と列の行の高さと列の幅を調整して、埋め込み画像をより目立たせます。
7. ワークブックを`.xlsx`ファイルとしてディスクに保存します。
次のコードは、完全なアプローチを示しています。

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Get the target cell C6
cell = worksheet.cells["C6"]
# Read the image file into a byte array
with open("logo.png", "rb") as f:
    imageData = f.read()
# Embed the image directly into the cell
cell.embedded_image = imageData
# Optionally adjust row height and column width so the embedded image is more visible
worksheet.cells.set_column_width(2, 30)   # Column C (index 2)
worksheet.cells.set_row_height(5, 100)     # Row 6 (index 5)
# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **適切なアプローチの選択**
両方のアプローチは単一のセル内に収まる画像を生成しますが、画像の格納方法と動作が異なります。
- **次のような場合は、フローティング画像(アプローチ1)を使用します。**
  - 他の描画オブジェクトとの配置、レイヤリング、位置合わせをより細かく制御する必要がある場合。
  - 画像を他の図形と一緒に選択したり、並べ替えたり、グループ化したりできる図形として動作させたい場合。
  - すでに`pictures`コレクションで動作するコードとのレガシー互換性が必要な場合。
  - ワークシートのレイアウトに基づいてアンカー座標を動的に計算する必要がある場合。
- **次のような場合は、埋め込み画像(アプローチ2)を使用します。**
  - セルへの画像の挿入を可能な限りシンプルにしたい場合。
  - 画像が他のセルコンテンツと同様にセルと一緒に移動する必要がある場合。
{{% /alert %}}

## 関連記事
- [Aspose.Cells for Python via .NETのExcelカメラ](/cells/ja/python-net/excel-camera/)
- [Aspose.Cells for Python via .NETでピボットテーブルにフィルターフィールドを追加する](/cells/ja/python-net/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via .NETでピボットテーブルにスタイルを適用する](/cells/ja/python-net/apply-style-to-pivot-table/)
- [ピボットテーブルのページフィールドのレイアウトを変更する](/cells/ja/python-net/change-page-field-layout/)
- [Aspose.Cells for Python via .NETでスパークラインを画像とHTMLに変換する](/cells/ja/python-net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="python" >}}