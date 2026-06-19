---
title: セルに画像を挿入する
description: Aspose.Cells はスプレッドシートファイルを扱うための .NET ライブラリです。この記事では、セル上にフローティング画像を配置する方法と、画像をセルに直接埋め込む方法という 2 つの異なるアプローチを使用して、画像を 1 つのセルサイズにぴったり合わせる方法について説明します。
keywords: Aspose.Cells, NET library, spreadsheet, insert image, embed image, picture in cell, fit image to cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /ja/net/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells は、画像を 1 つのセルに関連付ける 2 つの異なる方法を提供します。フローティング画像はワークシートの描画レイヤー上の図形であり、セル範囲を視覚的に覆うものです。一方、埋め込み画像はセル自体の中に格納され、セルの表示領域に合わせて自動的に拡大縮小されます。レイアウトの要件に最も合ったアプローチを選択してください。

{{% /alert %}}

## **はじめに**

1 つのセルに画像をぴったり合わせることは、ビジュアルレポート、商品カタログ、社員ディレクトリ、ダッシュボード、在庫リストとして機能するスプレッドシートをデザインする際に一般的な要件です。多くのセルにわたって画像を伸ばしたり、ワークシート上に緩く配置したりする代わりに、そのセルに整列されたままになる、クリーンなセル境界付きの画像が必要になる場合があります。

Aspose.Cells はこのシナリオを 2 つの補完的な方法でサポートします。

- **アプローチ 1 — セル上にフローティング画像を配置する。** `Picture` をワークシートに追加し、その `Placement` を `MoveAndSize` に設定し、アンカーセル (`UpperLeftRow`、`UpperLeftColumn`、`LowerRightRow`、`LowerRightColumn`) を調整して、画像がちょうど 1 つのセルを覆うようにします。
- **アプローチ 2 — 画像をセルに直接埋め込む。** 画像のバイト列をセルの `EmbeddedImage` プロパティに割り当てます。画像はセルの表示領域に合わせて自動的に拡大縮小され、セルと一緒に移動します。

この記事の残りの部分では、両方のアプローチを順に説明し、関連する API を解説し、コードでの使用方法を示します。

## **アプローチ 1: セル上に画像を配置する**

フローティング画像は、ワークシートの描画レイヤーに存在する `Picture` オブジェクトです。単一のセルの一部ではありませんが、セル範囲にアンカーされています。画像のアンカーセル (左上隅と右下隅) が、ワークシート上での画像の視覚的な範囲を決定します。デフォルトでは、追加したばかりの画像は複数のセルにまたがります。

フローティング画像を**ちょうど 1 つのセル**に収めるには、次の手順が必要です。

1. `Worksheet.Pictures.Add(int row, int column, Stream stream)` を使用して画像を追加します。これにより、新しい画像が指定されたセルにアンカーされます。
2. 4 つのアンカープロパティを設定して、画像の境界矩形が対象のセルと一致するようにします。
3. `Picture.Placement` を `PlacementType.MoveAndSize` に設定します。これにより、ユーザーが列幅や行の高さを変更したときに、画像が基になるセルと一緒に移動およびリサイズされます。

### **画像を 1 つのセルにアンカーする**

画像のアンカーは、4 つのゼロベースのインデックスプロパティによって定義されます。

- `Picture.UpperLeftRow` — 画像の上端の行インデックス。
- `Picture.UpperLeftColumn` — 画像の左端の列インデックス。
- `Picture.LowerRightRow` — 画像の下端の行インデックス。画像の下端を行 `r` の下部に配置するには、これを `r + 1` に設定します。
- `Picture.LowerRightColumn` — 画像の右端の列インデックス。画像の右端を列 `c` の右側に配置するには、これを `c + 1` に設定します。

たとえば、画像を**C6** セル (行インデックス `5`、列インデックス `2`) にぴったり合わせるには、`UpperLeftRow = 5`、`UpperLeftColumn = 2`、`LowerRightRow = 6`、`LowerRightColumn = 3` を設定します。

{{% alert color="primary" %}}

Aspose.Cells の行および列のインデックスは**ゼロベース**です。C6 セルの行インデックスは 5、列インデックスは 2 です。右下アンカーのオフバイワンエラーは、画像が隣接セルに重なって表示される最も一般的な原因です。

{{% /alert %}}

### **配置動作の制御**

`Picture.Placement` は `PlacementType` 型の列挙型であり、ユーザーが基になる行や列をリサイズしたときに画像がどのように動作するかを制御します。単一セルの画像に推奨される値は `PlacementType.MoveAndSize` です。これにより、画像が基になるセルと一緒に移動およびリサイズされ、ぴったり収まる状態が維持されます。

### **ステップバイステップの手順**

1. 新しい `Workbook` を作成します (または既存のブックを開きます)。
2. `workbook.Worksheets[0]` から対象の `Worksheet` にアクセスします。
3. `using` ブロックを使用して、画像ファイルをディスクから `FileStream` に開きます。これにより、ストリームが適切に破棄されます。
4. `worksheet.Pictures.Add(5, 2, stream)` を呼び出して、C6 セルにアンカーされた画像を追加します。返された `Picture` 参照を取得します。
5. 4 つのアンカー座標を設定して、画像が C6 セルだけを覆うようにします: `UpperLeftRow = 5`、`UpperLeftColumn = 2`、`LowerRightRow = 6`、`LowerRightColumn = 3`。
6. `picture.Placement = PlacementType.MoveAndSize` を設定して、列または行がリサイズされたときに画像が C6 に整列されたままになるようにします。
7. 必要に応じて、周囲のセルにサンプルテキストを追加して、C6 セルにのみ画像が含まれていることを示します。
8. ワークブックを `.xlsx` ファイルとしてディスクに保存します。

次のコードは、完全なアプローチを示しています。

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

## **アプローチ 2: 画像をセルに直接埋め込む**

Aspose.Cells は、セルにバインドされた画像のためのよりシンプルなメカニズムも公開しています: `Cell.EmbeddedImage` プロパティです。このプロパティに画像のバイト列を割り当てると、画像がインラインコンテンツのようにセル自体に添付されます。

### **埋め込み画像の仕組み**

- 画像は、描画レイヤー上の図形としてではなく、セルコンテンツの一部として格納されます。
- 画像は、セルのレンダリング境界内に収まるように自動的に拡大縮小されます。アンカー座標や配置設定は必要ありません。
- セルは実際のセルとしてのアドレスを保持し、数式で参照したり、行の一部としてソートしたり、他のセルレベルの操作で使用したりできます。

これにより、`Cell.EmbeddedImage` は単に「このセル内に存在する画像」が目的の場合に最も簡潔なオプションとなります。

### **ステップバイステップの手順**

1. 新しい `Workbook` を作成します (または既存のブックを開きます)。
2. `workbook.Worksheets[0]` から対象の `Worksheet` にアクセスします。
3. 画像ファイルをディスクから `byte[]` 配列に読み込みます (たとえば、`File.ReadAllBytes` を使用します)。
4. 対象のセルへの参照を取得します — `worksheet.Cells["C6"]` または `worksheet.Cells[5, 2]` のいずれかを使用します。
5. バイト配列をセルの `EmbeddedImage` プロパティに割り当てます。
6. 必要に応じて、対象行と対象列の行の高さと列幅を調整し、埋め込み画像をより目立つように表示します。
7. ワークブックを `.xlsx` ファイルとしてディスクに保存します。

次のコードは、完全なアプローチを示しています。

```csharp
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];

// 対象セル C6 を取得
var cell = worksheet.Cells["C6"];

// 画像ファイルをバイト配列に読み込む
byte[] imageData = File.ReadAllBytes("logo.png");

// 画像をセルに直接埋め込む
cell.EmbeddedImage = imageData;

// 埋め込まれた画像をより見やすくするために、行の高さと列の幅をオプションで調整する
worksheet.Cells.SetColumnWidth(2, 30);   // 列 C (インデックス 2)
worksheet.Cells.SetRowHeight(5, 100);     // 行 6 (インデックス 5)

// 結果として得られたワークブックを .xlsx ファイルとして保存
workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **適切なアプローチの選択**

両方のアプローチは単一セル内に収まる画像を生成しますが、画像の格納方法と動作が異なります。

- **次のような場合は、フローティング画像 (アプローチ 1) を使用します:**
  - 配置、レイヤリング、または他の描画オブジェクトとの整列をより細かく制御する必要がある場合。
  - 画像を、他の図形と選択、並べ替え、グループ化が可能な図形として動作させたい場合。
  - 既に `PictureCollection` で動作するコードとのレガシー互換性が必要な場合。
  - ワークシートのレイアウトに基づいてアンカー座標を動的に計算する必要がある場合。

- **次のような場合は、埋め込み画像 (アプローチ 2) を使用します:**
  - セルへの画像の挿入を可能な限りシンプルにしたい場合。
  - 画像が他のセルコンテンツと同様にセルと一緒に移動するようにする場合。
  - 画像を図形として操作する必要がない場合。

{{% alert color="primary" %}}

両方のアプローチは同じワークブック内で共存できます。2 つのメカニズムはファイル内の異なるストレージレイヤーを使用するため、あるセル群にはフローティング画像を配置し、他のセルには画像を直接埋め込むことができます。

{{% /alert %}}

## **関連記事**

- [How to Insert Picture in Cell](/cells/ja/net/how-to-place-image-to-cell/)
- [How to Fit Image to Cell Width and Height](/cells/ja/net/how-to-fit-image-to-cell-width-height/)
- [Add Image Hyperlinks](/cells/ja/net/add-image-hyperlinks/)
- [Load a Web Image from a URL into an Excel Worksheet](/cells/ja/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Manipulate Position Size and Designer Chart](/cells/ja/net/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="csharp" >}}