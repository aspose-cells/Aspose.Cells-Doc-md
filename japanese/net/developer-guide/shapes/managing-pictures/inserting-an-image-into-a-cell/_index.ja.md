---
title: セルへの画像の挿入
linktitle: セルへの画像の挿入
description: Aspose.Cells はスプレッドシートファイルを扱うための .NET ライブラリです。この記事では、フローティング画像をセル上に配置する方法、または画像をセルに直接埋め込むことによって、画像を単一セルにぴったり合わせる方法を説明します。
keywords: Aspose.Cells, .NET ライブラリ, スプレッドシート, 画像挿入, 画像埋め込み, セル内の画像, 画像サイズをセルに合わせる, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /ja/net/inserting-an-image-into-a-cell/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、画像と単一セルを関連付ける 2 つの異なる方法を提供します。フローティング画像はワークシートの描画レイヤーに存在する図形で、セル範囲の上に視覚的に重なります。一方、埋め込み画像はセル自体の中に格納され、セルの表示領域に合わせて自動的に拡大縮小されます。レイアウト要件に最適な方法を選択してください。
{{% /alert %}}

## **Introduction**
画像を単一セルにぴったり合わせることは、ビジュアルレポート、商品カタログ、社員ディレクトリ、ダッシュボード、在庫リストのように動作するスプレッドシートをデザインする際によくある要件です。多くのセルにまたがって画像を引き伸ばしたり、ワークシート上に緩く配置したりする代わりに、所有セルと位置が整合するクリーンなセル境界の画像が必要になることがあります。
Aspose.Cells はこのシナリオを 2 つの補完的な方法でサポートします。
- **方法 1 — セル上にフローティング画像を配置する。** `Picture` をワークシートに追加し、その `Placement` を `MoveAndSize` に設定し、画像を 1 セルだけを覆うようにアンカーセル (`UpperLeftRow`、`UpperLeftColumn`、`LowerRightRow`、`LowerRightColumn`) を調整します。
- **方法 2 — 画像をセルに直接埋め込む。** 画像のバイト列をセルの `EmbeddedImage` プロパティに割り当てます。画像は自動的にセルの表示領域に合わせて拡大縮小され、セルと一緒に移動します。
この記事の残りの部分では、両方の方法を順に説明し、関連する API を取り上げ、それらをコードで使用する方法を示します。

## **Approach 1: Place a Picture Over a Cell**
フローティング画像は、ワークシートの描画レイヤーに存在する `Picture` オブジェクトです。単一セルの一部ではありませんが、セル範囲にアンカーされます。画像のアンカーセル (左上と右下の角) が、ワークシート上での視覚的な範囲を決定します。デフォルトでは、追加したばかりの画像は複数のセルにまたがります。
フローティング画像を **ちょうど 1 セル** だけにカバーさせるには、次のことを行う必要があります。
1. `Worksheet.Pictures.Add(int row, int column, Stream stream)` を使用して画像を追加します。これは新しい画像を指定されたセルにアンカーします。
2. 4 つのアンカープロパティを設定して、画像の境界矩形が対象セルと一致するようにします。
3. `Picture.Placement` を `PlacementType.MoveAndSize` に設定し、ユーザーが列幅や行の高さを変更したときに、画像が基になるセルと一緒に移動およびサイズ変更されるようにします。

### **Anchoring the Picture to a Single Cell**
画像のアンカーは、4 つの 0 始まりのインデックスプロパティで定義されます。
- `Picture.UpperLeftRow` — 画像の上端の行インデックス。
- `Picture.UpperLeftColumn` — 画像の左端の列インデックス。
- `Picture.LowerRightRow` — 画像の下端の行インデックス。画像の下端を行 `r` の下に配置するには、これを `r + 1` に設定します。
- `Picture.LowerRightColumn` — 画像の右端の列インデックス。画像の右端を列 `c` の右に配置するには、これを `c + 1` に設定します。

{{% alert color="primary" %}}
Aspose.Cells の行と列のインデックスは **0 始まり** です。セル C6 の行インデックスは 5、列インデックスは 2 です。右下アンカーでのオフバイワンエラーは、画像が隣接セルに重なって表示される最も一般的な原因です。

### **Controlling Placement Behavior**
`Picture.Placement` は `PlacementType` 型の列挙体で、ユーザーが下の行または列をサイズ変更したときの画像の動作を制御します。単一セル画像に推奨される値は `PlacementType.MoveAndSize` です。これにより、画像が基になるセルと一緒に移動およびサイズ変更され、正確なフィット感が維持されます。

### **Step-by-Step Instructions**
1. 新しい `Workbook` を作成します (または既存のものを開きます)。
2. `workbook.Worksheets[0]` から対象の `Worksheet` にアクセスします。
3. `using` ブロックを使用して、ディスクから画像ファイルを `FileStream` に開き、ストリームが適切に破棄されるようにします。
4. `worksheet.Pictures.Add(5, 2, stream)` を呼び出して、セル C6 にアンカーされた画像を追加します。返された `Picture` 参照を取得します。
5. 4 つのアンカー座標を設定して、画像がセル C6 のみをカバーするようにします: `UpperLeftRow = 5`、`UpperLeftColumn = 2`、`LowerRightRow = 6`、`LowerRightColumn = 3`。
6. `picture.Placement = PlacementType.MoveAndSize` を設定し、列または行のサイズが変更されたときに画像を C6 に揃えたままにします。
7. 必要に応じて、周辺のセルにサンプルテキストを追加して、セル C6 のみに画像が含まれることを示します。
8. ワークブックを `.xlsx` ファイルとしてディスクに保存します。
次のコードは完全な方法を示しています。

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Drawing;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
using (FileStream fs = new FileStream("logo.png", FileMode.Open, FileAccess.Read))
{
    int picIndex = worksheet.Pictures.Add(5, 2, fs);
    Picture picture = worksheet.Pictures[picIndex];
    picture.UpperLeftRow = 5;
    picture.UpperLeftColumn = 2;
    picture.LowerRightRow = 6;
    picture.LowerRightColumn = 3;
    picture.Placement = PlacementType.MoveAndSize;
}
workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **Approach 2: Embed an Image Directly in a Cell**
Aspose.Cells は、セル境界の画像に対してよりシンプルな仕組みも公開しています。それが `Cell.EmbeddedImage` プロパティです。このプロパティに画像のバイト列を割り当てると、画像はインラインコンテンツであるかのようにセル自体に添付されます。

### **How Embedded Images Work**
- 画像は、描画レイヤー上の図形としてではなく、セルコンテンツの一部として格納されます。
- 画像は、セルのレンダリング境界内に自動的に収まるように拡大縮小されます。アンカー座標や配置設定は不要です。
- セルは実際のアドレスを持つ実際のセルのままであり、数式で参照したり、行の一部として並べ替えたり、他のセルレベルの操作に使用したりできます。
このため、`Cell.EmbeddedImage` は「セル内にある画像」という単純な目標がある場合に最も簡潔な選択肢となります。

### **Step-by-Step Instructions**
1. 新しい `Workbook` を作成します (または既存のものを開きます)。
2. `workbook.Worksheets[0]` から対象の `Worksheet` にアクセスします。
3. ディスクから画像ファイルを `byte[]` 配列に読み込みます (たとえば、`File.ReadAllBytes` を使用します)。
4. `worksheet.Cells["C6"]` または `worksheet.Cells[5, 2]` のいずれかを使用して、対象セルへの参照を取得します。
5. バイト配列をセルの `EmbeddedImage` プロパティに割り当てます。
6. 必要に応じて、対象の行と列の行の高さと列の幅を調整し、埋め込まれた画像をより目立つように表示します。
7. ワークブックを `.xlsx` ファイルとしてディスクに保存します。
次のコードは完全な方法を示しています。

```csharp
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
// 対象セル C6 を取得
var cell = worksheet.Cells["C6"];
// 画像ファイルをバイト配列に読み込む
byte[] imageData = File.ReadAllBytes("logo.png");
// 画像をセルに直接埋め込む
cell.EmbeddedImage = imageData;
// 埋め込まれた画像がより見やすくなるように、必要に応じて行の高さと列の幅を調整する
worksheet.Cells.SetColumnWidth(2, 30);   // 列 C (インデックス 2)
worksheet.Cells.SetRowHeight(5, 100);     // 行 6 (インデックス 5)
// 結果のワークブックを .xlsx ファイルとして保存
workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **Choosing the Right Approach**
両方の方法は単一セル内に収まる画像を生成しますが、画像の格納方法と動作が異なります。
- **次のような場合はフローティング画像 (方法 1) を使用します。**
  - 他の描画オブジェクトとの配置、レイヤー、整列をより細かく制御する必要がある場合。
  - 画像を他の図形と一緒に選択、並べ替え、グループ化できる図形として動作させたい場合。
  - 既に `PictureCollection` で動作するコードとのレガシー互換性が必要な場合。
  - ワークシートのレイアウトに基づいてアンカー座標を動的に計算する必要がある場合。
- **次のような場合は埋め込み画像 (方法 2) を使用します。**
  - セルへの画像の挿入をできるだけシンプルにしたい場合。
  - 画像が他のセルコンテンツと同じようにセルと一緒に移動する必要がある場合。
{{% /alert %}}

## Related Articles
- [Aspose.Cells for .NET の Excel カメラ](/cells/ja/net/excel-camera/)
- [Aspose.Cells for .NET でピボットテーブルにページフィールドを追加する](/cells/ja/net/add-page-field-in-pivot-table/)
- [Aspose.Cells for .NET でピボットテーブルにスタイルを適用する](/cells/ja/net/apply-style-to-pivot-table/)
- [ピボットテーブルのページフィールドのレイアウトを変更する](/cells/ja/net/change-page-field-layout/)
- [Aspose.Cells for .NET でスパークラインを画像と HTML に変換する](/cells/ja/net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="csharp" >}}