---
title: セルへの画像の挿入
description: Aspose.Cells は、Node.js via Java ライブラリで、スプレッドシートファイルの操作に使用されます。この記事では、画像を単一セルサイズに正確に合わせる2つの異なる方法を説明します、セル上にフローティング画像を配置する方法と、画像をセルに直接埋め込む方法です。
keywords: Aspose.Cells, Node.js via Java ライブラリ, スプレッドシート, 画像挿入, 画像埋め込み, セル内画像, セルに画像を合わせる, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /ja/nodejs-java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells は、画像を単一のセルに関連付ける2つの異なる方法を提供します。フローティング画像は、ワークシートの描画レイヤーに配置される図形であり、セル範囲を視覚的に覆います。一方、埋め込み画像はセル自体の中に保存され、セルの表示領域に合わせて自動的にスケーリングされます。レイアウト要件に最も合った方法を選択してください。

{{% /alert %}}

## **はじめに**

1つのセルに画像を正確に合わせることは、ビジュアルレポート、商品カタログ、社員ディレクトリ、ダッシュボード、在庫リストとして機能するスプレッドシートをデザインする際によくある要件です。多くのセルにわたって画像を引き伸ばしたり、ワークシート上に緩く配置したりする代わりに、所有するセルと位置が揃った、すっきりとしたセルに紐付けられた画像が必要になる場合があります。

Aspose.Cells は、このシナリオを2つの補完的な方法でサポートしています:

- **アプローチ 1 — セル上にフローティング画像を配置する。** `Picture` をワークシートに追加し、その `Placement` を `MoveAndSize` に設定し、アンカーセル(`UpperLeftRow`、`UpperLeftColumn`、`LowerRightRow`、`LowerRightColumn`)を調整して、画像がちょうど1つのセルを覆うようにします。
- **アプローチ 2 — 画像をセルに直接埋め込む。** 画像のバイト列をセルの `EmbeddedImage` プロパティに割り当てます。画像はセルの表示領域に合わせて自動的にスケーリングされ、セルと一緒に移動します。

この記事の残りの部分では、両方のアプローチを順を追って説明し、関連する API について説明し、コードでの使用方法を示します。

## **アプローチ 1: セル上に画像を配置する**

フローティング画像は、ワークシートの描画レイヤーに存在する `Picture` オブジェクトです。単一セルの一部ではありませんが、セル範囲にアンカー(固定)されています。画像のアンカーセル(左上と右下のコーナー)によって、ワークシート上の視覚的な範囲が決まります。デフォルトでは、新規追加された画像は複数のセルにまたがります。

フローティング画像を**ちょうど1つのセル**に収めるには、以下の手順が必要です:

1. `worksheet.getPictures().add(int row, int column, InputStream stream)` を使用して画像を追加します。これにより、新しい画像が指定されたセルにアンカーされます。
2. 4つのアンカープロパティを設定して、画像の境界矩形が目的のセルと一致するようにします。
3. `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` を設定して、ユーザーが列幅や行の高さを変更したときに、画像が基になるセルと一緒に移動およびリサイズされるようにします。

### **画像を単一セルにアンカーする**

画像のアンカーは、4つのゼロベースのインデックスプロパティで定義されます:

- `picture.setUpperLeftRow(int)` — 画像の上端の行インデックス。
- `picture.setUpperLeftColumn(int)` — 画像の左端の列インデックス。
- `picture.setLowerRightRow(int)` — 画像の下端の行インデックス。下端を行 `r` の下部に配置するには、これを `r + 1` に設定します。
- `picture.setLowerRightColumn(int)` — 画像の右端の列インデックス。右端を列 `c` の右側に配置するには、これを `c + 1` に設定します。

たとえば、画像をセル **C6**(行インデックス `5`、列インデックス `2`)に正確に適合させるには、`UpperLeftRow = 5`、`UpperLeftColumn = 2`、`LowerRightRow = 6`、`LowerRightColumn = 3` を設定します。

{{% alert color="primary" %}}

Aspose.Cells の行および列インデックスは**ゼロベース**です。セル C6 の行インデックスは 5、列インデックスは 2 です。右下アンカーのオフバイワンエラーは、隣接するセルに重なるように見える画像の最も一般的な原因です。

{{% /alert %}}

### **配置動作の制御**

`Picture.Placement` は `PlacementType` 型の列挙型で、ユーザーが下の行や列をリサイズしたときの画像の動作を制御します。単一セル画像に推奨される値は `PlacementType.MoveAndSize` です。これにより、画像が基になるセルと一緒に移動およびリサイズされ、正確なフィット感が維持されます。

### **手順**

1. 新しい `Workbook` を作成します(または既存のものを開きます)。
2. `workbook.getWorksheets().get(0)` から対象の `Worksheet` にアクセスします。
3. 画像ファイルをディスクから `InputStream` に開きます(たとえば、`FileInputStream` を使用)。これにより、ストリームが適切に閉じられます。
4. `worksheet.getPictures().add(5, 2, stream)` を呼び出して、セル C6 にアンカーされた画像を追加します。返された `Picture` 参照を取得します。
5. 4つのアンカー座標を設定して、画像がセル C6 のみを覆うようにします: `UpperLeftRow = 5`、`UpperLeftColumn = 2`、`LowerRightRow = 6`、`LowerRightColumn = 3`。
6. `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` を設定して、列または行がリサイズされたときに画像が C6 に揃ったままになるようにします。
7. オプションで、セル C6 のみが画像を含むことを示すために、周囲のセルにサンプルテキストを追加します。
8. ワークブックをディスクに `.xlsx` ファイルとして保存します。

次のコードは、完全なアプローチを示しています。

```javascript
const AsposeCells = require("aspose.cells-node");

var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

var picIndex = worksheet.getPictures().add(5, 2, "logo.png");
var picture = worksheet.getPictures().get(picIndex);
picture.setUpperLeftRow(5);
picture.setUpperLeftColumn(2);
picture.setLowerRightRow(6);
picture.setLowerRightColumn(3);
picture.setPlacement(AsposeCells.PlacementType.MoveAndSize);

workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **アプローチ 2: 画像をセルに直接埋め込む**

Aspose.Cells は、セルに紐付けられた画像に対するよりシンプルなメカニズムも提供しています: `Cell.EmbeddedImage` プロパティです。このプロパティに画像のバイト列を割り当てることで、あたかもインラインコンテンツのように、画像がセル自体にアタッチされます。

### **埋め込み画像の仕組み**

- 画像は、描画レイヤー上の図形としてではなく、セルコンテンツの一部として保存されます。
- 画像は、セルのレンダリング境界内に収まるように自動的にスケーリングされます。アンカー座標や配置設定は不要です。
- セルは実際のセルのままで、数式で参照できる実際のアドレスを持ち、行の一部としてソートされたり、他のセルレベルの操作で使用されたりできます。

これにより、`Cell.EmbeddedImage` は「セル内にある画像」という単純な目標がある場合に最も簡潔な選択肢となります。

### **手順**

1. 新しい `Workbook` を作成します(または既存のものを開きます)。
2. `workbook.getWorksheets().get(0)` から対象の `Worksheet` にアクセスします。
3. 画像ファイルをディスクからバイト配列に読み込みます(たとえば、`java.nio.file.Files` の `Files.readAllBytes` を使用)。
4. 対象のセルへの参照を取得します — `worksheet.getCells().get("C6")` または `worksheet.getCells().get(5, 2)` のいずれかを使用します。
5. バイト配列を `cell.setEmbeddedImage(bytes)` を通じてセルの `EmbeddedImage` プロパティに割り当てます。
6. オプションで、対象の行と列の行の高さと列の幅を調整し、埋め込み画像をより目立つようにします。
7. ワークブックをディスクに `.xlsx` ファイルとして保存します。

次のコードは、完全なアプローチを示しています。

```javascript
const AsposeCells = require("aspose.cells-node");
const fs = require("fs");

var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// ターゲットセル C6 を取得
var cell = worksheet.getCells().get("C6");

// 画像ファイルをバイト配列に読み込む
var imageData = fs.readFileSync("logo.png");

// 画像をセルに直接埋め込む
cell.setEmbeddedImage(imageData);

// 埋め込まれた画像をより見やすくするため、行の高さと列の幅を調整する（任意）
worksheet.getCells().setColumnWidth(2, 30);   // 列 C（インデックス 2）
worksheet.getCells().setRowHeight(5, 100);     // 行 6（インデックス 5）

// 結果のワークブックを .xlsx ファイルとして保存する
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **適切なアプローチの選択**

両方のアプローチは単一セル内に収まる画像を生成しますが、画像の保存方法と動作が異なります:

- **次のような場合は、フローティング画像(アプローチ 1)を使用します:**
  - 配置、レイヤリング、他の描画オブジェクトとの位置揃えをより細かく制御する必要がある場合。
  - 画像を他の図形と選択したり、並べ替えたり、グループ化したりできる図形として動作させたい場合。
  - すでに `PictureCollection` で動作するコードとのレガシー互換性が必要な場合。
  - ワークシートのレイアウトに基づいてアンカー座標を動的に計算する必要がある場合。

- **次のような場合は、埋め込み画像(アプローチ 2)を使用します:**
  - セルへの画像の挿入を可能な限りシンプルにしたい場合。
  - 画像が他のセルコンテンツと同様にセルと一緒に移動するようにする場合。
  - 画像を図形として操作する必要がない場合。

{{% alert color="primary" %}}

両方のアプローチは、同じワークブック内で共存できます。2つのメカニズムはファイル内の異なるストレージレイヤーを使用するため、あるセル群にフローティング画像を配置し、他のセルに画像を直接埋め込むことができます。

{{% /alert %}}



{{< app/cells/assistant language="javascript" >}}