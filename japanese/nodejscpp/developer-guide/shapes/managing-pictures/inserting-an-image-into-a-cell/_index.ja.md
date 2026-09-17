---
title: セルに画像を挿入する
linktitle: セルに画像を挿入する
description: Aspose.Cells は、Node.js via C++ のライブラリで、スプレッドシートファイルを扱うために使用されます。この記事では、フローティング画像をセル上に配置するか、画像をセルに直接埋め込むかして、画像を 1 つのセルにぴったり合わせる方法を説明します。
keywords: Aspose.Cells, Node.js via C++ ライブラリ, スプレッドシート, 画像挿入, 画像埋め込み, セル内の画像, セルに画像を合わせる, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /ja/nodejs-cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells では、画像を 1 つのセルに関連付ける 2 つの異なる方法が用意されています。フローティング画像はワークシートの描画レイヤーの図形であり、セル範囲を視覚的に覆います。一方、埋め込み画像はセル自体に保存され、セルの表示領域に合わせて自動的に拡大縮小されます。レイアウトの要件に最適な方法を選択してください。
{{% /alert %}}

## **Introduction**
1 つのセルにぴったり画像を合わせることは、ビジュアルレポート、商品カタログ、従業員ディレクトリ、ダッシュボード、在庫リストとして機能するスプレッドシートをデザインする際の一般的な要件です。多くのセルにまたがるように画像を引き伸ばしたり、ワークシート上に緩く配置したりする代わりに、それを所有するセルと整合性が保たれる、クリーンでセルに束縛された画像が必要になる場合があります。
Aspose.Cells では、このシナリオを 2 つの補完的な方法でサポートしています。
- **方法 1 — フローティング画像をセル上に配置します。** ワークシートに `Picture` を追加し、その `placement` を `MoveAndSize` に設定し、画像が正確に 1 つのセルを覆うようにアンカーセル (`upperLeftRow`、`upperLeftColumn`、`lowerRightRow`、`lowerRightColumn`) を調整します。
- **方法 2 — 画像をセルに直接埋め込みます。** 画像のバイト列をセルの `embeddedImage` プロパティに割り当てます。画像はセルの表示領域に合わせて自動的に拡大縮小され、セルと一緒に移動します。
この記事の残りの部分では、両方の方法を順に説明し、関連する API について説明し、コードでの使用方法を示します。

## **Approach 1: Place a Picture Over a Cell**
フローティング画像は、ワークシートの描画レイヤーに存在する `Picture` オブジェクトです。単一のセルの一部ではありませんが、セル範囲にアンカーされています。画像のアンカーセル (左上と右下の角) は、ワークシート上の視覚的な範囲を決定します。デフォルトでは、新しく追加された画像は複数のセルにまたがります。
フローティング画像が**正確に 1 つのセル**を覆うようにするには、次の手順を実行する必要があります。
1. `worksheet.pictures.add(row, column, stream)` を使用して画像を追加し、新しい画像を指定されたセルにアンカーします。
2. 画像の境界矩形が対象セルと一致するように、4 つのアンカープロパティを設定します。
3. ユーザーが列幅や行の高さを変更したときに画像が基になるセルとともに移動およびサイズ変更されるように、`picture.placement` を `PlacementType.MoveAndSize` に設定します。

### **Anchoring the Picture to a Single Cell**
画像のアンカーは、4 つのゼロベースのインデックスプロパティによって定義されます。
- `picture.upperLeftRow` — 画像の上端の行インデックス。
- `picture.upperLeftColumn` — 画像の左端の列インデックス。
- `picture.lowerRightRow` — 画像の下端の行インデックス。画像の下端を行 `r` の下に配置するには、これを `r + 1` に設定します。
- `picture.lowerRightColumn` — 画像の右端の列インデックス。画像の右端を列 `c` の右に配置するには、これを `c + 1` に設定します。

{{% alert color="primary" %}}
Aspose.Cells の行と列のインデックスは**ゼロベース**です。セル C6 の行インデックスは 5、列インデックスは 2 です。右下アンカーのオフバイワンエラー (1 単位のずれ) は、画像が隣接するセルに重なって見える最も一般的な原因です。

### **Controlling Placement Behavior**
`picture.placement` は `PlacementType` 型の列挙型で、ユーザーが下にある行または列のサイズを変更したときの画像の動作を制御します。単一セル画像に推奨される値は `PlacementType.MoveAndSize` で、これにより画像が基になるセルと一緒に移動およびサイズ変更され、正確なフィッティングが維持されます。

### **Step-by-Step Instructions**
1. 新しい `Workbook` を作成します (または既存のものを開きます)。
2. `workbook.worksheets[0]` から対象の `Worksheet` にアクセスします。
3. ディスクから画像ファイルをストリームに開き、使用後にストリームが適切に閉じられることを確認します。
4. `worksheet.pictures.add(5, 2, stream)` を呼び出して、セル C6 にアンカーされた画像を追加します。返された `Picture` 参照を取得します。
5. 4 つのアンカー座標を設定して、セル C6 のみを覆うようにします: `upperLeftRow = 5`、`upperLeftColumn = 2`、`lowerRightRow = 6`、`lowerRightColumn = 3`。
6. 列または行のサイズが変更されたときに画像が C6 に揃えられたままになるように、`picture.placement = PlacementType.MoveAndSize` を設定します。
7. 必要に応じて、周囲のセルにサンプルテキストを追加して、セル C6 のみが画像を含むことを示します。
8. ワークブックを `.xlsx` ファイルとしてディスクに保存します。
次のコードは完全な方法を示しています。

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const fs_stream = fs.createReadStream("logo.png");
const picIndex = worksheet.getPictures().add(5, 2, fs_stream);
const picture = worksheet.getPictures().get(picIndex);
picture.setUpperLeftRow(5);
picture.setUpperLeftColumn(2);
picture.setLowerRightRow(6);
picture.setLowerRightColumn(3);
picture.setPlacement(AsposeCells.PlacementType.MoveAndSize);
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Approach 2: Embed an Image Directly in a Cell**
Aspose.Cells では、セルにバインドされた画像のためによりシンプルなメカニズムも公開されています: `cell.embeddedImage` プロパティです。このプロパティに画像バイト列を割り当てると、画像をインラインコンテンツのようにセル自体に添付します。

### **How Embedded Images Work**
- 画像は、描画レイヤー上の図形としてではなく、セルコンテンツの一部として保存されます。
- 画像は、セルのレンダリング境界内に収まるように自動的に拡大縮小されます。アンカー座標や配置設定は不要です。
- セルは実際のセルのままで、数式で参照できる実際のアドレスを持ち、行の一部として並べ替えられたり、他のセルレベルの操作に使用されたりできます。
これにより、目標が単に「このセル内に存在する画像」となる場合、`cell.embeddedImage` が最も簡潔なオプションになります。

### **Step-by-Step Instructions**
1. 新しい `Workbook` を作成します (または既存のものを開きます)。
2. `workbook.worksheets[0]` から対象の `Worksheet` にアクセスします。
3. Node.js のファイルシステム API (たとえば `fs.readFileSync`) を使用して、ディスクから画像ファイルを Buffer またはバイト配列に読み込みます。
4. 対象セルへの参照を取得します。`worksheet.cells["C6"]` または `worksheet.cells[5, 2]` のいずれかを使用します。
5. バイト配列をセルの `embeddedImage` プロパティに割り当てます。
6. 必要に応じて、対象行と対象列の行の高さと列幅を調整して、埋め込み画像をより目立つようにします。
7. ワークブックを `.xlsx` ファイルとしてディスクに保存します。
次のコードは完全な方法を示しています。

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// ターゲットセル C6 を取得
var cell = worksheet.getCells().get("C6");
// 画像ファイルをバイト配列に読み込む
var imageData = fs.readFileSync("logo.png");
// 画像をセルに直接埋め込む
cell.setEmbeddedImage(imageData);
// 埋め込まれた画像をより見やすくするために、必要に応じて行の高さと列の幅を調整する
worksheet.getCells().setColumnWidth(2, 30);   // 列 C (インデックス 2)
worksheet.getCells().setRowHeight(5, 100);     // 行 6 (インデックス 5)
// 結果のワークブックを .xlsx ファイルとして保存
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Choosing the Right Approach**
両方の方法で 1 つのセル内に収まる画像が生成されますが、画像の保存方法と動作が異なります。
- **次のような場合はフローティング画像 (方法 1) を使用します:**
  - 配置、レイヤー化、または他の描画オブジェクトとの整列をより細かく制御する必要がある場合。
  - 画像を選択、並べ替え、または他の図形とグループ化できる図形として動作させる場合。
  - ピクチャコレクションで既に動作するコードとのレガシー互換性が必要な場合。
  - ワークシートのレイアウトに基づいてアンカー座標を動的に計算する必要がある場合。
- **次のような場合は埋め込み画像 (方法 2) を使用します:**
  - セルへの画像の挿入をできるだけシンプルにしたい場合。
  - 画像が他のセルコンテンツのようにセルと一緒に移動する必要がある場合。
{{% /alert %}}

## Related Articles
- [Aspose.Cells for Node.js via C++ の Excel Camera](/cells/ja/nodejs-cpp/excel-camera/)
- [Aspose.Cells for Node.js via C++ でピボットテーブルにフィルターフィールドを追加する](/cells/ja/nodejs-cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for Node.js via C++ でピボットテーブルにスタイルを適用する](/cells/ja/nodejs-cpp/apply-style-to-pivot-table/)
- [ピボットテーブルのページフィールドのレイアウトを変更する](/cells/ja/nodejs-cpp/change-page-field-layout/)
- [Aspose.Cells for Node.js via C++ でスパークラインを画像と HTML に変換する](/cells/ja/nodejs-cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="javascript" >}}