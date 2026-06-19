---
title: セルへの画像の挿入
description: Aspose.Cells はスプレッドシートファイルを操作するための C++ ライブラリです。この記事では、フローティングピクチャをセル上に配置する方法と、画像をセルに直接埋め込む方法という 2 つの異なるアプローチを使用して、画像を単一セルサイズにぴったり合わせる方法について説明します。
keywords: Aspose.Cells, C++ ライブラリ, スプレッドシート, 画像挿入, 画像埋め込み, セル内のピクチャ, セルに画像を合わせる, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /ja/cpp/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells は、単一セルに画像を関連付ける 2 つの異なる方法を提供します。フローティングピクチャはワークシートの描画レイヤ上の図形であり、セルの範囲を視覚的に覆うものです。一方、埋め込み画像はセル自体の中に保存され、セルの表示領域に合わせて自動的に拡大縮小されます。レイアウト要件に最も合った方法を選択してください。

{{% /alert %}}

## **はじめに**

ピクチャを単一セルにぴったり合わせることは、ビジュアルレポート、商品カタログ、社員ディレクトリ、ダッシュボード、在庫リストとして機能するスプレッドシートを設計する際によく求められる要件です。複数のセルにわたって画像を引き伸ばしたり、ワークシート上に緩く配置したりする代わりに、所有するセルに整列されたクリーンなセルバウンド画像を必要とする場合があります。

Aspose.Cells は、このシナリオを 2 つの補完的な方法でサポートします。

- **アプローチ 1 — フローティングピクチャをセル上に配置する。** ワークシートに `Picture` を追加し、その `Placement` を `MoveAndSize` に設定し、アンカーセル (`UpperLeftRow`、`UpperLeftColumn`、`LowerRightRow`、`LowerRightColumn`) を調整して、ピクチャがちょうど 1 セルを覆うようにします。
- **アプローチ 2 — セル内に画像を直接埋め込む。** 画像のバイト列をセルの `EmbeddedImage` プロパティに割り当てます。画像はセルの表示領域に合わせて自動的に拡大縮小され、セルと一緒に移動します。

この記事の残りの部分では、両方のアプローチについて順を追って説明し、関連する API を解説し、コードでの使用方法を示します。

## **アプローチ 1: ピクチャをセル上に配置する**

フローティングピクチャは、ワークシートの描画レイヤ上に存在する `Picture` オブジェクトです。単一セルの一部ではありませんが、セルの範囲にアンカーされます。ピクチャのアンカーセル (左上隅と右下隅) が、ワークシート上での視覚的な範囲を決定します。デフォルトでは、新しく追加されたピクチャは複数のセルにまたがります。

フローティングピクチャが **ちょうど 1 セル** を覆うようにするには、次の手順が必要です。

1. `Worksheet.Pictures.Add(int row, int column, Vector<uint8_t> stream)` を使用してピクチャを追加します。これにより、新しいピクチャが指定されたセルにアンカーされます。
2. 4 つのアンカープロパティを設定して、ピクチャの境界矩形がターゲットセルと一致するようにします。
3. ユーザーが列幅または行の高さを変更したときにピクチャが基になるセルと一緒に移動およびサイズ変更されるように、`Picture.Placement` を `PlacementType.MoveAndSize` に設定します。

### **ピクチャを単一セルにアンカーする**

ピクチャのアンカーは、4 つのゼロベースのインデックスプロパティによって定義されます。

- `Picture.UpperLeftRow` — ピクチャの上端の行インデックス。
- `Picture.UpperLeftColumn` — ピクチャの左端の列インデックス。
- `Picture.LowerRightRow` — ピクチャの下端の行インデックス。ピクチャの下端を行 `r` の下部に配置するには、これを `r + 1` に設定します。
- `Picture.LowerRightColumn` — ピクチャの右端の列インデックス。ピクチャの右端を列 `c` の右側に配置するには、これを `c + 1` に設定します。

たとえば、ピクチャを **C6** セル (行インデックス `5`、列インデックス `2`) に正確にはめ込むには、`UpperLeftRow = 5`、`UpperLeftColumn = 2`、`LowerRightRow = 6`、`LowerRightColumn = 3` を設定します。

{{% alert color="primary" %}}

Aspose.Cells の行および列のインデックスは **ゼロベース** です。C6 セルの行インデックスは 5、列インデックスは 2 です。右下アンカーの off-by-one エラーは、ピクチャが隣接セルにはみ出して表示される最も一般的な原因です。

{{% /alert %}}

### **配置動作の制御**

`Picture.Placement` は `PlacementType` 型の列挙型であり、ユーザーが基になる行または列のサイズを変更したときのピクチャの動作を制御します。単一セルピクチャに推奨される値は `PlacementType.MoveAndSize` であり、これによりピクチャが基になるセルと一緒に移動およびサイズ変更され、正確なフィット感が維持されます。

### **ステップバイステップの手順**

1. 新しい `Workbook` を作成します (または既存のものを開きます)。
2. `workbook.Worksheets[0]` からターゲットの `Worksheet` にアクセスします。
3. 画像ファイルをディスクから `Vector<uint8_t>` バイトバッファに読み込み、画像のバイト列を API で利用できるようにします。
4. `worksheet.Pictures.Add(5, 2, imageData)` を呼び出して、C6 セルにアンカーされたピクチャを追加します。返された `Picture` 参照をキャプチャします。
5. 4 つのアンカー座標を設定して、ピクチャが C6 セルのみを覆うようにします: `UpperLeftRow = 5`、`UpperLeftColumn = 2`、`LowerRightRow = 6`、`LowerRightColumn = 3`。
6. 列または行のサイズが変更されたときにピクチャが C6 に整列された状態を維持するように、`picture.Placement = PlacementType.MoveAndSize` を設定します。
7. オプションとして、C6 セルにのみピクチャが含まれていることを示すために、周囲のセルにサンプルテキストを追加します。
8. ワークブックをディスクに `.xlsx` ファイルとして保存します。

次のコードは、完全なアプローチを示しています。

```cpp
#include "Aspose.Cells.h"
#include <fstream>
#include <vector>
#include <iterator>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    std::ifstream fs("logo.png", std::ios::binary);
    std::vector<uint8_t> stdData((std::istreambuf_iterator<char>(fs)),
                                  std::istreambuf_iterator<char>());
    fs.close();

    Vector<uint8_t> imageData(reinterpret_cast<const uint8_t*>(stdData.data()),
                              static_cast<int32_t>(stdData.size()));

    int picIndex = worksheet.GetPictures().Add(5, 2, imageData);
    Picture picture = worksheet.GetPictures().Get(picIndex);
    picture.SetUpperLeftRow(5);
    picture.SetUpperLeftColumn(2);
    picture.SetLowerRightRow(6);
    picture.SetLowerRightColumn(3);
    picture.SetPlacement(PlacementType::MoveAndSize);

    workbook.Save(u"output.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **アプローチ 2: セル内に画像を直接埋め込む**

Aspose.Cells は、セルバウンド画像に対してより簡単なメカニズムも公開しています: `Cell.EmbeddedImage` プロパティです。このプロパティに画像のバイト列を割り当てると、画像はインラインコンテンツであるかのようにセル自体に添付されます。

### **埋め込み画像の仕組み**

- 画像は描画レイヤ上の図形としてではなく、セルコンテンツの一部として保存されます。
- 画像はセルのレンダリング境界に合わせて自動的に拡大縮小されます。アンカー座標や配置設定は不要です。
- セルは実際のセルとしてのアドレスを保持し、数式で参照したり、行の一部として並べ替えたり、他のセルレベルの操作で使用したりできます。

これにより、`Cell.EmbeddedImage` は、「このセルの中に存在する画像」という単純な目的の場合に最も簡潔なオプションとなります。

### **ステップバイステップの手順**

1. 新しい `Workbook` を作成します (または既存のものを開きます)。
2. `workbook.Worksheets[0]` からターゲットの `Worksheet` にアクセスします。
3. 画像ファイルをディスクから `Vector<uint8_t>` バイト配列に読み込みます。
4. ターゲットセルへの参照を取得します — `worksheet.Cells["C6"]` または `worksheet.Cells[5, 2]` のいずれかを使用します。
5. バイト配列をセルの `EmbeddedImage` プロパティに割り当てます。
6. オプションとして、埋め込み画像をより目立たせるために、ターゲット行および列の行の高さと列の幅を調整します。
7. ワークブックをディスクに `.xlsx` ファイルとして保存します。

次のコードは、完全なアプローチを示しています。

```cpp
#include "Aspose.Cells.h"
#include <vector>
#include <fstream>
#include <iterator>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    Cell cell = worksheet.GetCells().Get(u"C6");

    // 画像ファイルをバイト配列に読み込む
    std::ifstream file("logo.png", std::ios::binary);
    std::vector<uint8_t> stdImageData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();

    // ポインタ+サイズコンストラクタを使用して std::vector を Aspose::Cells::Vector に変換する
    Vector<uint8_t> imageData(stdImageData.data(), (int32_t)stdImageData.size());

    // 画像をセルに直接埋め込む
    cell.SetEmbeddedImage(imageData);

    // 埋め込まれた画像をより見やすくするために、オプションで行の高さと列の幅を調整する
    worksheet.GetCells().SetColumnWidth(2, 30);   // 列 C (インデックス 2)
    worksheet.GetCells().SetRowHeight(5, 100);    // 行 6 (インデックス 5)

    // 結果のワークブックを .xlsx ファイルとして保存する
    wb.Save(u"output.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **適切なアプローチの選択**

両方のアプローチは単一セル内に収まるピクチャを生成しますが、ピクチャの保存方法と動作が異なります。

- **次のような場合は、フローティングピクチャ (アプローチ 1) を使用します。**
  - 他の描画オブジェクトとの配置、レイヤリング、または整列をより細かく制御する必要がある場合。
  - ピクチャを他の図形と一緒に選択したり、並べ替えたり、グループ化したりできる図形として扱いたい場合。
  - すでに `PictureCollection` で動作するコードとのレガシー互換性が必要な場合。
  - ワークシートのレイアウトに基づいてアンカー座標を動的に計算する必要がある場合。

- **次のような場合は、埋め込み画像 (アプローチ 2) を使用します。**
  - セルへの画像の挿入をできる限りシンプルにしたい場合。
  - 画像が他のセルコンテンツと同様にセルと一緒に移動するようにする場合。
  - 画像を図形として操作する必要がない場合。

{{% alert color="primary" %}}

両方のアプローチは同じワークブック内で共存できます。2 つのメカニズムはファイル内の異なるストレージレイヤを使用するため、あるセルにはフローティングピクチャを配置し、他のセルには画像を直接埋め込むことができます。

{{% /alert %}}

## **関連記事**

- [セルにピクチャを挿入する方法](/cells/ja/cpp/how-to-place-image-to-cell/)
- [画像ハイパーリンクを追加](/cells/ja/cpp/add-image-hyperlinks/)
- [URL から Web 画像を Excel ワークシートに読み込む](/cells/ja/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [位置、サイズ、およびデザイナーグラフを操作する](/cells/ja/cpp/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="cpp" >}}