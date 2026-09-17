---
title: セルへの画像の挿入
linktitle: セルへの画像の挿入
description: Aspose.Cells は、スプレッドシートファイルを扱うための Java ライブラリです。この記事では、セル上にフローティング画像を配置する方法や、画像をセルに直接埋め込むことによって、画像を1つのセルにぴったり合わせる方法について説明します。
keywords: Aspose.Cells, Java ライブラリ, スプレッドシート, 画像の挿入, 画像の埋め込み, セル内の画像, セルへの画像合わせ, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /ja/java/inserting-an-image-into-a-cell/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells では、画像を1つのセルに関連付ける方法が2通りあります。フローティング画像はワークシートの描画レイヤーに配置される図形で、セル範囲を視覚的に覆うのに対し、埋め込み画像はセル自体の中に格納され、セル表示領域に合わせて自動的に拡大縮小されます。レイアウトの要件に最も合った方法を選択してください。
{{% /alert %}}

## **Introduction**
1つのセルにぴったりと画像を合わせることは、ビジュアルレポート、商品カタログ、社員ディレクトリ、ダッシュボード、在庫リストなどとして機能するスプレッドシートをデザインする際によく必要となります。多くのセルにまたがって画像を引き伸ばしたり、ワークシート上に緩く配置したりするのではなく、所有するセルと整合性が保たれる、クリーンでセルに紐付けられた画像が必要になることがあります。
Aspose.Cells では、このシナリオを以下の2つの補完的な方法でサポートしています。
- **方法1 — セル上にフローティング画像を配置する。** `Picture` をワークシートに追加し、その `Placement` を `MOVE_AND_SIZE` に設定し、セル範囲を覆うようにアンカーセル（`getUpperLeftRow`、`getUpperLeftColumn`、`getLowerRightRow`、`getLowerRightColumn`）を調整します。
- **方法2 — 画像をセルに直接埋め込む。** 画像のバイト列をセルの `getEmbeddedImage()` セッターに代入します。画像は表示領域に合わせて自動的に拡大縮小され、セルと一緒に移動します。
この記事の残りの部分では、両方の方法について解説し、関連する API を説明し、コードでの使用方法を示します。

## **Approach 1: Place a Picture Over a Cell**
フローティング画像は、ワークシートの描画レイヤーに存在する `Picture` オブジェクトです。単一のセルの一部ではありませんが、セル範囲にアンカーされています。画像のアンカーセル（左上と右下の角）は、ワークシート上での視覚的な範囲を決定します。既定では、追加されたばかりの画像は複数のセルにまたがります。
フローティング画像を**ちょうど1つのセル**に収めるには、以下を行う必要があります。
1. `Worksheet.getPictures().add(int row, int column, InputStream stream)` を使用して画像を追加し、新しい画像を指定されたセルにアンカーします。
2. 4つのアンカー プロパティを設定し、画像の境界矩形が対象のセルと一致するようにします。
3. `Picture.setPlacement()` を `PlacementType.MOVE_AND_SIZE` に設定し、ユーザーが列幅や行の高さを変更したときに、基になるセルと共に画像が移動およびサイズ変更されるようにします。

### **Anchoring the Picture to a Single Cell**
画像のアンカーは、4つのゼロベースのインデックス プロパティによって定義されます。
- `Picture.getUpperLeftRow()` — 画像の上端の行インデックス。
- `Picture.getUpperLeftColumn()` — 画像の左端の列インデックス。
- `Picture.getLowerRightRow()` — 画像の下端の行インデックス。画像の下端を行 `r` の下部に配置する場合、`r + 1` に設定します。
- `Picture.getLowerRightColumn()` — 画像の右端の列インデックス。画像の右端を列 `c` の右側に配置する場合、`c + 1` に設定します。

{{% alert color="primary" %}}
Aspose.Cells における行と列のインデックスは**ゼロベース**です。セル C6 の行インデックスは 5、列インデックスは 2 です。右下アンカーのオフバイワン エラーが、隣接セルにはみ出して見える画像の最も一般的な原因です。

### **Controlling Placement Behavior**
`Picture.getPlacement()` は `PlacementType` 型の列挙を返し、ユーザーが下の行または列のサイズを変更したときの画像の動作を制御します。単一セル画像に推奨される値は `PlacementType.MOVE_AND_SIZE` で、基になるセルと共に画像が移動およびサイズ変更され、正確な適合が維持されます。

### **Step-by-Step Instructions**
1. 新しい `Workbook` を作成します（または既存のものを開きます）。
2. `workbook.getWorksheets().get(0)` から対象の `Worksheet` にアクセスします。
3. try-with-resources ブロックを使用して、画像ファイルをディスクから `InputStream`（`FileInputStream` など）に開きます。これによりストリームが適切に閉じられます。
4. `worksheet.getPictures().add(5, 2, stream)` を呼び出して、セル C6 にアンカーされた画像を追加します。返された `Picture` 参照を取得します。
5. 4つのアンカー座標を設定し、画像が C6 のみを覆うようにします：`setUpperLeftRow(5)`、`setUpperLeftColumn(2)`、`setLowerRightRow(6)`、`setLowerRightColumn(3)`。
6. `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` を設定し、列または行のサイズが変更されたときに画像が C6 に整合した状態に保たれるようにします。
7. 必要に応じて周囲のセルにサンプルテキストを追加し、セル C6 のみに画像が含まれていることを示します。
8. ワークブックをディスクに `.xlsx` ファイルとして保存します。
次のコードは完全な方法を示しています。

```java
import com.aspose.cells.*;
import java.io.FileInputStream;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
try (FileInputStream fs = new FileInputStream("logo.png"))
{
    int picIndex = worksheet.getPictures().add(5, 2, fs);
    Picture picture = worksheet.getPictures().get(picIndex);
    picture.setUpperLeftRow(5);
    picture.setUpperLeftColumn(2);
    picture.setLowerRightRow(6);
    picture.setLowerRightColumn(3);
    picture.setPlacement(PlacementType.MOVE_AND_SIZE);
}
workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **Approach 2: Embed an Image Directly in a Cell**
Aspose.Cells は、セルに紐付けられた画像のよりシンプルなメカニズムも公開しています。`Cell.setEmbeddedImage(byte[])` メソッドです。このプロパティに画像のバイト列を代入すると、画像がまるでインライン コンテンツのようにセル自体に添付されます。

### **How Embedded Images Work**
- 画像は描画レイヤー上の図形ではなく、セルコンテンツの一部として格納されます。
- 画像は、セルのレンダリング境界内に収まるよう自動的に拡大縮小されます。アンカー座標や配置設定は必要ありません。
- セルは実際のアドレスを持つ実際のセルのままで、数式で参照したり、行の一部として並べ替えたり、その他のセルレベルの操作に使用したりできます。
このため、`setEmbeddedImage()` は「セル内に存在する画像」というシンプルな目標の場合に最も簡潔な選択肢となります。

### **Step-by-Step Instructions**
1. 新しい `Workbook` を作成します（または既存のものを開きます）。
2. `workbook.getWorksheets().get(0)` から対象の `Worksheet` にアクセスします。
3. 画像ファイルをディスクから `byte[]` 配列に読み込みます（たとえば、`java.nio.file` の `Files.readAllBytes()` 経由で読み込みます）。
4. 対象のセルへの参照を取得します（`worksheet.getCells().get("C6")` または `worksheet.getCells().get(5, 2)` のいずれか）。
5. `cell.setEmbeddedImage(bytes)` を使用してバイト配列をセルに代入します。
6. 必要に応じて対象の行と列の行の高さと列幅を調整し、埋め込まれた画像をより目立つようにします。
7. ワークブックをディスクに `.xlsx` ファイルとして保存します。
次のコードは完全な方法を示しています。

```java
import com.aspose.cells.*;
import java.nio.file.Files;
import java.nio.file.Paths;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// 対象のセル C6 を取得
Cell cell = worksheet.getCells().get("C6");
// 画像ファイルをバイト配列に読み込みます
byte[] imageData = Files.readAllBytes(Paths.get("logo.png"));
// 画像をセルに直接埋め込みます
cell.setEmbeddedImage(imageData);
// 画像がより見やすくなるよう、必要に応じて行の高さと列の幅を調整します
worksheet.getCells().setColumnWidth(2, 30);   // 列 C（インデックス 2）
worksheet.getCells().setRowHeight(5, 100);     // 行 6（インデックス 5）
// 結果のワークブックを .xlsx ファイルとして保存します
workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **Choosing the Right Approach**
両方的方法で1つのセル内に収まる画像が生成されますが、画像の保存方法と動作が異なります。
- **次のような場合は、フローティング画像（方法1）を使用します。**
  - 配置、レイヤー化、または他の描画オブジェクトとの整列をより細かく制御する必要がある場合。
  - 画像を他の図形と一緒に選択、並べ替え、またはグループ化できる図形として扱いたい場合。
  - すでに `PictureCollection` で動作するコードとのレガシー互換性が必要な場合。
  - ワークシートのレイアウトに基づいてアンカー座標を動的に計算する必要がある場合。
- **次のような場合は、埋め込み画像（方法2）を使用します。**
  - セルへの画像の挿入を可能な限りシンプルにしたい場合。
  - 画像が他のセル コンテンツと同様にセルと一緒に移動する必要がある場合。
{{% /alert %}}

## Related Articles
- [Aspose.Cells for Java の Excel カメラ](/cells/ja/java/excel-camera/)
- [Aspose.Cells for Java でピボットテーブルにページフィルターを追加](/cells/ja/java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Java でピボットテーブルにスタイルを適用](/cells/ja/java/apply-style-to-pivot-table/)
- [ピボットテーブルのページフィールドのレイアウトを変更](/cells/ja/java/change-page-field-layout/)
- [Aspose.Cells for Java でスパークラインを画像と HTML に変換](/cells/ja/java/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="java" >}}