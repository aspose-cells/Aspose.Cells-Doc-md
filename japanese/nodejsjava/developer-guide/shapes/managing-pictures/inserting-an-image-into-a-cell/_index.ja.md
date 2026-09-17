---
title: セルへの画像の挿入
linktitle: セルへの画像の挿入
description: Aspose.Cells はスプレッドシートファイルを扱うための Node.js via Java ライブラリです。この記事では、フローティング画像をセル上に配置する方法、または画像をセルに直接埋め込む方法のいずれかによって、画像を単一のセルにぴったり合わせる方法を説明します。
keywords: Aspose.Cells, Node.js via Java ライブラリ, スプレッドシート, 画像の挿入, 画像の埋め込み, セル内の画像, セルへの画像合わせ, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /ja/nodejs-java/inserting-an-image-into-a-cell/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、画像を単一のセルに関連付ける 2 つの異なる方法を提供します。フローティング画像はワークシートの描画レイヤーに配置される図形であり、セル範囲を視覚的に覆うのに対し、埋め込み画像はセル自体の中に保存され、セルの表示領域に合わせて自動的に拡大縮小されます。レイアウト要件に最も合った方法を選択してください。
{{% /alert %}}

## **はじめに**
ビジュアルレポート、製品カタログ、社員ディレクトリ、ダッシュボード、在庫リストとして機能するスプレッドシートを設計する際、画像を単一のセルにぴったり合わせることは一般的な要件です。多くのセルにわたって画像を伸ばしたり、ワークシート上に緩く配置したりする代わりに、所有するセルと整列するクリーンなセル紐づきの画像が必要になる場合があります。
Aspose.Cells はこのシナリオを 2 つの補完的な方法でサポートします。
- **方法 1 — フローティング画像をセル上に配置する。** `Picture` をワークシートに追加し、その `Placement` を `MoveAndSize` に設定し、アンカーセル (`UpperLeftRow`、`UpperLeftColumn`、`LowerRightRow`、`LowerRightColumn`) を調整して、画像がちょうど 1 つのセルを覆うようにします。
- **方法 2 — 画像をセルに直接埋め込む。** 画像のバイト列をセルの `EmbeddedImage` プロパティに割り当てます。画像はセルの表示領域に合わせて自動的に拡大縮小され、セルと一緒に移動します。
この記事の残りでは両方の方法を順に説明し、関連する API を解説し、コードでの使用方法を示します。

## **方法 1: セル上に画像を配置する**
フローティング画像はワークシートの描画レイヤーに存在する `Picture` オブジェクトです。単一セルの一部ではありませんが、セル範囲にアンカーされます。画像のアンカーセル (左上隅と右下隅) がワークシート上でのその視覚的な範囲を決定します。デフォルトでは、新しく追加された画像は複数のセルにまたがります。
フローティング画像を **ちょうど 1 つのセル** を覆うようにするには、次の手順が必要です。
1. `worksheet.getPictures().add(int row, int column, InputStream stream)` を使用して画像を追加します。これにより、新しい画像が指定されたセルにアンカーされます。
2. 4 つのアンカープロパティを設定し、画像の境界矩形が対象のセルと一致するようにします。
3. `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` を設定し、ユーザーが列幅または行の高さを変更したときに、画像が下のセルと一緒に移動およびサイズ変更されるようにします。

### **単一セルへの画像のアンカー**
画像のアンカーは、4 つのゼロベースのインデックスプロパティによって定義されます。
- `picture.setUpperLeftRow(int)` — 画像の上端の行インデックス。
- `picture.setUpperLeftColumn(int)` — 画像の左端の列インデックス。
- `picture.setLowerRightRow(int)` — 画像の下端の行インデックス。画像の下端を行 `r` の下端に配置するには、これを `r + 1` に設定します。
- `picture.setLowerRightColumn(int)` — 画像の右端の列インデックス。画像の右端を列 `c` の右端に配置するには、これを `c + 1` に設定します。

{{% alert color="primary" %}}
Aspose.Cells における行と列のインデックスは **ゼロベース** です。セル C6 の行インデックスは 5、列インデックスは 2 です。右下アンカーにおけるオフバイワンエラーは、隣接するセルにはみ出して見える画像の最も一般的な原因です。

### **配置動作の制御**
`Picture.Placement` は `PlacementType` 型の列挙型であり、ユーザーが下の行または列のサイズを変更したときの画像の動作を制御します。単一セル画像に対して推奨される値は `PlacementType.MoveAndSize` です。これにより、画像が下のセルと一緒に移動およびサイズ変更され、正確な適合が維持されます。

### **ステップごとの手順**
1. 新しい `Workbook` を作成するか、既存のものを開きます。
2. `workbook.getWorksheets().get(0)` から対象の `Worksheet` にアクセスします。
3. ディスクから画像ファイルを `InputStream` に開きます (たとえば、`FileInputStream` を使用します)。これにより、ストリームが適切に閉じられます。
4. `worksheet.getPictures().add(5, 2, stream)` を呼び出して、セル C6 にアンカーされた画像を追加します。返された `Picture` 参照を取得します。
5. 4 つのアンカー座標を設定して、画像がセル C6 のみを覆うようにします: `UpperLeftRow = 5`、`UpperLeftColumn = 2`、`LowerRightRow = 6`、`LowerRightColumn = 3`。
6. `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` を設定して、列または行のサイズが変更されたときに画像が C6 と位置を揃えたままになるようにします。
7. オプションで周囲のセルにサンプルテキストを追加し、セル C6 のみが画像を含むことを示します。
8. ワークブックを `.xlsx` ファイルとしてディスクに保存します。
次のコードは完全な方法を示しています。

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

## **方法 2: セル内に画像を直接埋め込む**
Aspose.Cells は、セルに束縛された画像のためのよりシンプルなメカニズムも公開しています。それが `Cell.EmbeddedImage` プロパティです。このプロパティに画像のバイト列を割り当てることで、画像はインラインコンテンツのようにセル自体に付加されます。

### **埋め込み画像の仕組み**
- 画像は描画レイヤー上の図形としてではなく、セルコンテンツの一部として保存されます。
- 画像はセルのレンダリング境界内に収まるよう自動的に拡大縮小されます。アンカー座標や配置設定は不要です。
- セルは、数式で参照でき、行の一部としてソートでき、他のセルレベルの操作で使用できる、実際のアドレスを持つ実際のセルのままです。
これにより、`Cell.EmbeddedImage` は「セル内に存在する画像」という単純な目的の場合に最も簡潔な選択肢となります。

### **ステップごとの手順**
1. 新しい `Workbook` を作成するか、既存のものを開きます。
2. `workbook.getWorksheets().get(0)` から対象の `Worksheet` にアクセスします。
3. ディスクから画像ファイルをバイト配列に読み込みます (たとえば、`java.nio.file.Files` の `Files.readAllBytes` を使用します)。
4. 対象のセルへの参照を取得します。`worksheet.getCells().get("C6")` または `worksheet.getCells().get(5, 2)` のいずれかを使用します。
5. `cell.setEmbeddedImage(bytes)` を通じてバイト配列をセルの `EmbeddedImage` プロパティに割り当てます。
6. オプションで対象の行と列の行の高さと列幅を調整し、埋め込まれた画像をより目立つようにします。
7. ワークブックを `.xlsx` ファイルとしてディスクに保存します。
次のコードは完全な方法を示しています。

```javascript
const AsposeCells = require("aspose.cells-node");
const fs = require("fs");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// 対象セル C6 を取得
var cell = worksheet.getCells().get("C6");
// 画像ファイルをバイト配列に読み込む
var imageData = fs.readFileSync("logo.png");
// 画像をセルに直接埋め込む
cell.setEmbeddedImage(imageData);
// 埋め込まれた画像をより見やすくするため、必要に応じて行の高さと列の幅を調整する
worksheet.getCells().setColumnWidth(2, 30);   // 列 C (インデックス 2)
worksheet.getCells().setRowHeight(5, 100);     // 行 6 (インデックス 5)
// 結果のワークブックを .xlsx ファイルとして保存する
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **適切な方法の選択**
両方の方法は単一セル内に収まる画像を生成しますが、画像の保存方法と動作が異なります。
- **次のような場合はフローティング画像 (方法 1) を使用します:**
  - 他の描画オブジェクトとの配置、レイヤリング、または整列をより細かく制御する必要がある場合。
  - 画像を他の図形と選択、並べ替え、グループ化できる図形として動作させたい場合。
  - すでに `PictureCollection` を扱うコードとのレガシー互換性が必要な場合。
  - ワークシートのレイアウトに基づいてアンカー座標を動的に計算する必要がある場合。
- **次のような場合は埋め込み画像 (方法 2) を使用します:**
  - セルへの画像の挿入をできるだけシンプルにしたい場合。
  - 画像が他のセルコンテンツと同様にセルと一緒に移動する必要がある場合。
{{% /alert %}}

{{< app/cells/assistant language="javascript" >}}