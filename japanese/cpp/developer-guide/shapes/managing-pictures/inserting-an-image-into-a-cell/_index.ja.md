---
title: セルへの画像の挿入
linktitle: セルへの画像の挿入
description: Aspose.Cellsは、スプレッドシートファイルを扱うためのC++ライブラリです。この記事では、セル上にフローティング画像を配置する方法と、画像をセルに直接埋め込む方法のいずれかによって、画像を1つのセルに正確に合わせる方法について説明します。
keywords: Aspose.Cells, C++ライブラリ, スプレッドシート, 画像挿入, 画像埋め込み, セル内の画像, セルに画像を合わせる, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /ja/cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cellsは、画像を1つのセルに関連付ける2つの異なる方法を提供します。フローティング画像はワークシートの描画レイヤーに配置される図形であり、セルの範囲を視覚的に覆うのに対し、埋め込み画像はセル自体の中に格納され、セルの表示領域に合わせて自動的に拡大縮小されます。レイアウト要件に最も適したアプローチを選択してください。
{{% /alert %}}

## **Introduction**
1つのセルに正確に画像を合わせることは、視覚的なレポート、製品カタログ、社員ディレクトリ、ダッシュボード、在庫リストとして機能するスプレッドシートをデザインする際に一般的な要件です。多くのセルにわたって画像を引き伸ばしたり、ワークシート上に緩く配置したりする代わりに、所有するセルと整合性を保つクリーンなセル境界の画像が必要になる場合があります。
Aspose.Cellsは、このシナリオを2つの補完的な方法でサポートします。
- **方法1 — セル上にフローティング画像を配置する。** ワークシートに`Picture`を追加し、その`Placement`を`MoveAndSize`に設定し、配置セル（`UpperLeftRow`、`UpperLeftColumn`、`LowerRightRow`、`LowerRightColumn`）を調整して、画像がちょうど1つのセルを覆うようにします。
- **方法2 — 画像をセルに直接埋め込む。** 画像のバイトをセルの`EmbeddedImage`プロパティに割り当てます。画像はセルの表示領域に合わせて自動的に拡大縮小され、セルと一緒に移動します。
この記事の残りの部分では、両方のアプローチを順に説明し、関連するAPIを説明し、コードでの使用法を示します。

## **Approach 1: Place a Picture Over a Cell**
フローティング画像は、ワークシートの描画レイヤーに存在する`Picture`オブジェクトです。単一のセルの一部ではありませんが、セルの範囲に固定されます。画像の固定セル — 左上と右下の角 — は、ワークシート上の視覚的な範囲を決定します。デフォルトでは、新しく追加された画像は複数のセルにまたがります。
フローティング画像を**ちょうど1つのセル**を覆うようにするには、次の手順が必要です。
1. `Worksheet.Pictures.Add(int row, int column, Vector<uint8_t> stream)`を使用して画像を追加します。これにより、新しい画像が指定されたセルに固定されます。
2. 4つの固定プロパティを設定して、画像の境界矩形が目的のセルと一致するようにします。
3. ユーザーが列幅または行の高さを変更したときに、画像が基になるセルと共に移動およびサイズ変更されるように、`Picture.Placement`を`PlacementType.MoveAndSize`に設定します。

### **Anchoring the Picture to a Single Cell**
画像の固定は、4つの0から始まるインデックスプロパティによって定義されます。
- `Picture.UpperLeftRow` — 画像の上端の行インデックス。
- `Picture.UpperLeftColumn` — 画像の左端の列インデックス。
- `Picture.LowerRightRow` — 画像の下端の行インデックス。画像の下端を行`r`の下部に配置するには、これを`r + 1`に設定します。
- `Picture.LowerRightColumn` — 画像の右端の列インデックス。画像の右端を列`c`の右側に配置するには、これを`c + 1`に設定します。

{{% alert color="primary" %}}
Aspose.Cellsの行と列のインデックスは**0から始まる**ものです。セルC6の行インデックスは5、列インデックスは2です。右下アンカーのオフバイワンエラーは、画像が隣接セルに重なって表示される最も一般的な原因です。

### **Controlling Placement Behavior**
`Picture.Placement`は`PlacementType`型の列挙型であり、ユーザーが下の行または列のサイズを変更したときの画像の動作を制御します。単一セル画像に推奨される値は`PlacementType.MoveAndSize`であり、これにより画像が基になるセルと一緒に移動およびサイズ変更され、正確なフィット感が維持されます。

### **Step-by-Step Instructions**
1. 新しい`Workbook`を作成します（または既存のものを開きます）。
2. `workbook.GetWorksheets().Get(0]`から対象の`Worksheet`にアクセスします。
3. 画像ファイルをディスクから`Vector<uint8_t>`バイトバッファに読み込み、画像バイトをAPIで利用できるようにします。
4. `worksheet.Pictures.Add(5, 2, imageData)`を呼び出して、セルC6に固定された画像を追加します。返された`Picture`参照を取得します。
5. 画像がセルC6のみを覆うように、4つの固定座標を設定します：`UpperLeftRow = 5`、`UpperLeftColumn = 2`、`LowerRightRow = 6`、`LowerRightColumn = 3`。
6. 列または行のサイズが変更されたときに画像をC6に整列させたままにするために、`picture.Placement = PlacementType.MoveAndSize`を設定します。
7. オプションで、セルC6のみが画像を含むことを示すために、周囲のセルにサンプルテキストを追加します。
8. ワークブックを`.xlsx`ファイルとしてディスクに保存します。
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

## **Approach 2: Embed an Image Directly in a Cell**
Aspose.Cellsは、セルにバインドされた画像のよりシンプルなメカニズムも公開しています。それは`Cell.EmbeddedImage`プロパティです。このプロパティに画像バイトを割り当てると、画像がインラインコンテンツのようにセル自体に添付されます。

### **How Embedded Images Work**
- 画像は描画レイヤー上の図形としてではなく、セルコンテンツの一部として保存されます。
- 画像はセルのレンダリング境界内に収まるように自動的に拡大縮小されます。アンカー座標や配置設定は必要ありません。
- セルは実際のアドレスを持つ実際のセルのままであり、数式で参照したり、行の一部として並べ替えたり、他のセルレベルの操作で使用したりできます。
これにより、`Cell.EmbeddedImage`は目標が単に「このセル内に存在する画像」である場合に最も簡潔なオプションになります。

### **Step-by-Step Instructions**
1. 新しい`Workbook`を作成します（または既存のものを開きます）。
2. `workbook.GetWorksheets().Get(0]`から対象の`Worksheet`にアクセスします。
3. 画像ファイルをディスクから`Vector<uint8_t>`バイト配列に読み込みます。
4. 対象のセルへの参照を取得します — `worksheet.GetCells().Get("C6"]`または`worksheet.GetCells().Get(5, 2]`のいずれかで。
5. バイト配列をセルの`EmbeddedImage`プロパティに割り当てます。
6. オプションで、対象行と列の行の高さと列幅を調整して、埋め込み画像をより目立つようにします。
7. ワークブックを`.xlsx`ファイルとしてディスクに保存します。
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
    // Read the image file into a byte array
    std::ifstream file("logo.png", std::ios::binary);
    std::vector<uint8_t> stdImageData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();
    // Convert std::vector to Aspose::Cells::Vector using pointer+size constructor
    Vector<uint8_t> imageData(stdImageData.data(), (int32_t)stdImageData.size());
    // Embed the image directly into the cell
    cell.SetEmbeddedImage(imageData);
    // Optionally adjust row height and column width so the embedded image is more visible
    worksheet.GetCells().SetColumnWidth(2, 30);   // Column C (index 2)
    worksheet.GetCells().SetRowHeight(5, 100);    // Row 6 (index 5)
    // Save the resulting workbook as an .xlsx file
    wb.Save(u"output.xlsx", SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Choosing the Right Approach**
どちらのアプローチも単一セル内に収まる画像を生成しますが、画像の保存方法と動作が異なります。
- **次のような場合は、フローティング画像（方法1）を使用します。**
  - 他の描画オブジェクトとの配置、レイヤー化、整列をより細かく制御する必要がある場合。
  - 画像を、他の図形と一緒に選択、並べ替え、グループ化できる図形として動作させたい場合。
  - すでに`PictureCollection`で動作するコードとのレガシー互換性が必要な場合。
  - ワークシートのレイアウトに基づいてアンカー座標を動的に計算する必要がある場合。
- **次のような場合は、埋め込み画像（方法2）を使用します。**
  - セルへの画像の最も簡単な挿入方法を希望する場合。
  - 画像が他のセルコンテンツのようにセルと一緒に移動する必要がある場合。
{{% /alert %}}

## Related Articles
- [Aspose.Cells for C++のExcelカメラ](/cells/ja/cpp/excel-camera/)
- [Aspose.Cells for C++でピボットテーブルにフィルターフィールドを追加](/cells/ja/cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for C++でピボットテーブルにスタイルを適用](/cells/ja/cpp/apply-style-to-pivot-table/)
- [ピボットテーブルのページフィールドのレイアウトを変更](/cells/ja/cpp/change-page-field-layout/)
- [Aspose.Cells for C++でスパークラインを画像とHTMLに変換](/cells/ja/cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="cpp" >}}