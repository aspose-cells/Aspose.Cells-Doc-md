---
title: セルに画像を挿入する
description: Aspose.Cells は、Node.js via C++ でスプレッドシートファイルを操作するためのライブラリです。この記事では、セル上にフローティング画像を配置する方法と、セルに直接画像を埋め込む方法という 2 つのアプローチを使用して、画像を 1 つのセルサイズにぴったり合わせる方法を説明します。
keywords: Aspose.Cells, Node.js via C++ library, spreadsheet, insert image, embed image, picture in cell, fit image to cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /ja/nodejs-cpp/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells は、画像を単一セルに関連付けるための 2 つの異なる方法を提供します。フローティング画像はワークシートの描画レイヤーに配置される図形であり、セル範囲の上に視覚的に重なります。一方、埋め込み画像はセル自体の中に格納され、セルの表示領域に合わせて自動的に拡大縮小されます。レイアウト要件に最適なアプローチを選択してください。

{{% /alert %}}

## **はじめに**

画像を単一セルにぴったり合わせることは、ビジュアルレポート、製品カタログ、社員ディレクトリ、ダッシュボード、在庫リストとして機能するスプレッドシートをデザインする際の一般的な要件です。複数のセルに画像を伸ばしたり、ワークシート上に緩く配置したりする代わりに、所有するセルと整列したきれいなセル境界の画像が必要になる場合があります。

Aspose.Cells は、このシナリオを 2 つの補完的な方法でサポートします。

- **アプローチ 1 — セル上にフローティング画像を配置する。** ワークシートに `Picture` を追加し、その `placement` を `MoveAndSize` に設定し、セルを完全にカバーするようにアンカーセル (`upperLeftRow`、`upperLeftColumn`、`lowerRightRow`、`lowerRightColumn`) を調整します。
- **アプローチ 2 — セル内に画像を直接埋め込む。** セルの `embeddedImage` プロパティに画像バイトを割り当てます。画像はセルの表示領域に合わせて自動的に拡大縮小され、セルと共に移動します。

この記事の残りの部分では、両方のアプローチを順に説明し、関連する API について説明し、コードでの使用方法を示します。

## **アプローチ 1: セル上に画像を配置する**

フローティング画像は、ワークシート描画レイヤーに存在する `Picture` オブジェクトです。単一セルの一部ではありませんが、セル範囲にアンカーされています。画像のアンカーセル（左上隅と右下隅）によって、ワークシート上の表示範囲が決まります。デフォルトでは、新しく追加された画像は複数のセルにまたがります。

フローティング画像を **正確に 1 つのセル** だけカバーするようにするには、以下を行う必要があります。

1. `worksheet.pictures.add(row, column, stream)` を使用して画像を追加し、新しい画像を特定のセルにアンカーします。
2. 4 つのアンカープロパティを設定して、画像の境界矩形がターゲットセルと一致するようにします。
3. `picture.placement` を `PlacementType.MoveAndSize` に設定して、ユーザーが列幅や行の高さを変更したときに、基になるセルと共に画像が移動およびサイズ変更されるようにします。

### **単一セルへの画像のアンカー**

画像のアンカーは、4 つのゼロベースのインデックスプロパティによって定義されます。

- `picture.upperLeftRow` — 画像の上端の行インデックス。
- `picture.upperLeftColumn` — 画像の左端の列インデックス。
- `picture.lowerRightRow` — 画像の下端の行インデックス。画像の下端を行 `r` の下に配置するには、これを `r + 1` に設定します。
- `picture.lowerRightColumn` — 画像の右端の列インデックス。画像の右端を列 `c` の右に配置するには、これを `c + 1` に設定します。

たとえば、画像を **C6** セル（行インデックス `5`、列インデックス `2`）にぴったり合わせるには、`upperLeftRow = 5`、`upperLeftColumn = 2`、`lowerRightRow = 6`、`lowerRightColumn = 3` を設定します。

{{% alert color="primary" %}}

Aspose.Cells の行と列のインデックスは **ゼロベース** です。C6 セルの行インデックスは 5、列インデックスは 2 です。右下アンカーのオフバイワンエラーは、隣接セルに重なるように見える画像のもっとも一般的な原因です。

{{% /alert %}}

### **配置動作の制御**

`picture.placement` は `PlacementType` 型の列挙型で、画像が基になる行または列のサイズを変更したときに画像がどのように動作するかを制御します。単一セル画像に推奨される値は `PlacementType.MoveAndSize` です。これにより、画像が基になるセルと一緒に移動およびサイズ変更され、正確なフィット感が維持されます。

### **ステップバイステップの手順**

1. 新しい `Workbook` を作成します（または既存のものを開きます）。
2. `workbook.worksheets[0]` からターゲットの `Worksheet` にアクセスします。
3. 使用後に適切に閉じられるように、ディスクから画像ファイルをストリームに開きます。
4. `worksheet.pictures.add(5, 2, stream)` を呼び出して、C6 セルにアンカーされた画像を追加します。返された `Picture` 参照を取得します。
5. 4 つのアンカー座標を設定して、画像が C6 セルのみをカバーするようにします: `upperLeftRow = 5`、`upperLeftColumn = 2`、`lowerRightRow = 6`、`lowerRightColumn = 3`。
6. 列または行のサイズが変更されたときに画像を C6 に整列させたままにするために、`picture.placement = PlacementType.MoveAndSize` を設定します。
7. オプションで周囲のセルにサンプルテキストを追加して、C6 セルにのみ画像が含まれていることを示します。
8. ワークブックをディスクに `.xlsx` ファイルとして保存します。

次のコードは、完全なアプローチを示しています。

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

## **アプローチ 2: セル内に画像を直接埋め込む**

Aspose.Cells は、セル境界の画像に対するよりシンプルなメカニズムも公開しています: `cell.embeddedImage` プロパティです。このプロパティに画像バイトを割り当てると、画像はインラインコンテンツのようにセル自体にアタッチされます。

### **埋め込み画像の仕組み**

- 画像は描画レイヤー上の図形としてではなく、セルコンテンツの一部として格納されます。
- 画像はセルのレンダリング境界内に自動的にフィットするように拡大縮小されます。アンカー座標や配置設定は必要ありません。
- セルは、数式で参照したり、行の一部として並べ替えたり、他のセルレベルの操作に使用したりできる、実際のアドレスを持つ実際のセルのままです。

これにより、`cell.embeddedImage` は、「このセル内に存在する画像」というシンプルな目標を達成するための最も簡潔なオプションとなります。

### **ステップバイステップの手順**

1. 新しい `Workbook` を作成します（または既存のものを開きます）。
2. `workbook.worksheets[0]` からターゲットの `Worksheet` にアクセスします。
3. Node.js のファイルシステム API（たとえば、`fs.readFileSync`）を使用して、ディスクから画像ファイルを Buffer またはバイト配列に読み込みます。
4. ターゲットセルへの参照を取得します — `worksheet.cells["C6"]` または `worksheet.cells[5, 2]` のいずれかを使用します。
5. バイト配列をセルの `embeddedImage` プロパティに割り当てます。
6. オプションで、ターゲット行と列の行の高さと列の幅を調整して、埋め込み画像をより目立つように表示します。
7. ワークブックをディスクに `.xlsx` ファイルとして保存します。

次のコードは、完全なアプローチを示しています。

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// ターゲットセル C6 を取得
var cell = worksheet.getCells().get("C6");

// 画像ファイルをバイト配列に読み込む
var imageData = fs.readFileSync("logo.png");

// 画像をセルに直接埋め込む
cell.setEmbeddedImage(imageData);

// 必要に応じて行の高さと列の幅を調整し、埋め込まれた画像をより見やすくする
worksheet.getCells().setColumnWidth(2, 30);   // 列 C (インデックス 2)
worksheet.getCells().setRowHeight(5, 100);     // 行 6 (インデックス 5)

// 結果のワークブックを .xlsx ファイルとして保存
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **適切なアプローチの選択**

両方のアプローチは単一セル内に収まる画像を生成しますが、画像の保存方法と動作が異なります。

- **次のような場合はフローティング画像（アプローチ 1）を使用します:**
  - 他の描画オブジェクトとの配置、レイヤー化、整列をより細かく制御する必要がある場合。
  - 画像を、他の図形と選択、並べ替え、グループ化できる図形として動作させたい場合。
  - すでに画像コレクションを操作するコードとのレガシー互換性が必要な場合。
  - ワークシートのレイアウトに基づいてアンカー座標を動的に計算する必要がある場合。

- **次のような場合は埋め込み画像（アプローチ 2）を使用します:**
  - セルへの画像挿入をできるだけシンプルにしたい場合。
  - 画像が他のセルコンテンツと同様にセルと一緒に移動する必要がある場合。
  - 画像を図形として操作する必要がない場合。

{{% alert color="primary" %}}

両方のアプローチは同じワークブック内で共存できます。2 つのメカニズムはファイル内で異なるストレージレイヤーを使用するため、あるセルにはフローティング画像を配置し、他のセルには画像を直接埋め込むことができます。

{{% /alert %}}

## **関連記事**

- [セルに画像を挿入する方法](/cells/ja/nodejs-cpp/how-to-place-image-to-cell/)
- [画像ハイパーリンクの追加](/cells/ja/nodejs-cpp/add-image-hyperlinks/)
- [URL から Web 画像を Excel ワークシートに読み込む](/cells/ja/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [位置、サイズ、デザイナーグラフの操作](/cells/ja/nodejs-cpp/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="javascript" >}}