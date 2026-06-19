---
title: セルに画像を挿入する
description: Aspose.Cells はスプレッドシートファイルを扱うための Java ライブラリです。この記事では、画像を単一セルのサイズに正確に合わせる 2 つの方法を説明します。1 つはセル上にフローティング画像を配置する方法、もう 1 つは画像をセルに直接埋め込む方法です。
keywords: Aspose.Cells, Java ライブラリ, スプレッドシート, 画像挿入, 画像埋め込み, セル内画像, 画像をセルに合わせる, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /ja/java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells は、画像を単一のセルに関連付ける 2 つの異なる方法を提供します。フローティング画像はワークシートの描画レイヤー上の図形であり、セル範囲の上に視覚的に重ねて表示されます。一方、埋め込み画像はセル自体の中に格納され、セルの表示領域に合わせて自動的に拡大縮小されます。レイアウト要件に最も合った方法を選択してください。

{{% /alert %}}

## **はじめに**

スプレッドシートをビジュアルレポート、製品カタログ、従業員ディレクトリ、ダッシュボード、在庫リストなどとしてデザインする場合、画像を 1 つのセルに正確に合わせることは一般的な要件です。複数のセルにわたって画像を引き伸ばしたり、ワークシート上に緩く配置したりする代わりに、所有するセルに揃った状態で維持される、セルにバインドされたクリーンな画像が必要になる場合があります。

Aspose.Cells は、このシナリオを 2 つの補完的な方法でサポートしています。

- **方法 1 — セル上にフローティング画像を配置する。** ワークシートに `Picture` を追加し、その `Placement` を `MOVE_AND_SIZE` に設定し、アンカーセル (`getUpperLeftRow`、`getUpperLeftColumn`、`getLowerRightRow`、`getLowerRightColumn`) を調整して、画像がちょうど 1 つのセルを覆うようにします。
- **方法 2 — 画像をセルに直接埋め込む。** 画像のバイト列をセルの `getEmbeddedImage()` セッターに割り当てます。画像は自動的にセルの表示領域に合わせて拡大縮小され、セルと一緒に移動します。

この記事の残り部分では、両方の方法を順に説明し、関連する API を解説し、コードでの使用方法を示します。

## **方法 1: セル上に画像を配置する**

フローティング画像は、ワークシートの描画レイヤーに存在する `Picture` オブジェクトです。単一セルの一部ではありませんが、セル範囲にアンカーされています。画像が視覚的に占める範囲を決定するのは、画像のアンカーセル (左上隅と右下隅) です。既定では、新しく追加された画像は複数のセルにまたがります。

フローティング画像を **ちょうど 1 つのセル** に収めるには、次の手順が必要です。

1. `Worksheet.getPictures().add(int row, int column, InputStream stream)` を使用して画像を追加します。これにより、新しい画像が指定されたセルにアンカーされます。
2. 4 つのアンカー プロパティを設定して、画像の境界矩形が対象のセルと一致するようにします。
3. `Picture.setPlacement()` を `PlacementType.MOVE_AND_SIZE` に設定し、ユーザーが列幅や行の高さを変更したときに、画像が基になるセルと一緒に移動およびサイズ変更されるようにします。

### **画像を単一セルにアンカーする**

画像のアンカーは、4 つの 0 始まりのインデックス プロパティによって定義されます。

- `Picture.getUpperLeftRow()` — 画像の上端の行インデックス。
- `Picture.getUpperLeftColumn()` — 画像の左端の列インデックス。
- `Picture.getLowerRightRow()` — 画像の下端の行インデックス。画像の下端を行 `r` の下部に配置するには、これを `r + 1` に設定します。
- `Picture.getLowerRightColumn()` — 画像の右端の列インデックス。画像の右端を列 `c` の右側に配置するには、これを `c + 1` に設定します。

たとえば、画像をセル **C6** (行インデックス `5`、列インデックス `2`) に正確に合わせて配置するには、`setUpperLeftRow(5)`、`setUpperLeftColumn(2)`、`setLowerRightRow(6)`、`setLowerRightColumn(3)` を設定します。

{{% alert color="primary" %}}

Aspose.Cells における行と列のインデックスは **0 始まり** です。セル C6 の行インデックスは 5、列インデックスは 2 です。右下アンカーにおけるオフバイワン エラーは、画像が隣接セルにはみ出して見える最も一般的な原因です。

{{% /alert %}}

### **配置動作の制御**

`Picture.getPlacement()` は、`PlacementType` 型の列挙を返し、基になる行や列をユーザーがサイズ変更したときに画像がどのように動作するかを制御します。単一セル画像に推奨される値は `PlacementType.MOVE_AND_SIZE` です。これにより、画像が基になるセルと一緒に移動およびサイズ変更され、正確なフィット感が維持されます。

### **ステップバイステップの手順**

1. 新しい `Workbook` を作成します (または既存のものを開きます)。
2. `workbook.getWorksheets().get(0)` から対象の `Worksheet` にアクセスします。
3. ディスク上の画像ファイルを try-with-resources ブロックを使用して `InputStream` (たとえば `FileInputStream`) に開きます。これにより、ストリームが適切に閉じられます。
4. `worksheet.getPictures().add(5, 2, stream)` を呼び出して、セル C6 にアンカーされた画像を追加します。返された `Picture` 参照を取得します。
5. 4 つのアンカー座標を設定して、画像が C6 セルのみを覆うようにします。`setUpperLeftRow(5)`、`setUpperLeftColumn(2)`、`setLowerRightRow(6)`、`setLowerRightColumn(3)`。
6. `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` を設定し、列や行のサイズが変更されたときに画像を C6 に揃えたままにします。
7. 必要に応じて周囲のセルにサンプル テキストを追加し、セル C6 のみに画像が含まれていることを示します。
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

## **方法 2: 画像をセルに直接埋め込む**

Aspose.Cells は、セルにバインドされた画像のためのよりシンプルな仕組みも提供しています。それが `Cell.setEmbeddedImage(byte[])` メソッドです。このプロパティに画像のバイト列を割り当てると、画像はインラインコンテンツのようにセル自体に添付されます。

### **埋め込み画像の仕組み**

- 画像は描画レイヤー上の図形としてではなく、セルコンテンツの一部として格納されます。
- 画像はセルの描画境界内に自動的に収まるように拡大縮小されます。アンカー座標や配置設定は必要ありません。
- セルは実際のセルとして残り、数式で参照したり、行の一部として並べ替えたり、他のセルレベルの操作に使用したりできる実際のアドレスを持ちます。

このため、`setEmbeddedImage()` は、「このセル内に存在する画像」という単純な目的の場合に最も簡潔なオプションです。

### **ステップバイステップの手順**

1. 新しい `Workbook` を作成します (または既存のものを開きます)。
2. `workbook.getWorksheets().get(0)` から対象の `Worksheet` にアクセスします。
3. ディスク上の画像ファイルを `byte[]` 配列に読み込みます (たとえば、`java.nio.file` の `Files.readAllBytes()` を使用します)。
4. 対象セルへの参照を取得します。`worksheet.getCells().get("C6")` または `worksheet.getCells().get(5, 2)` のいずれかを使用します。
5. `cell.setEmbeddedImage(bytes)` を使用して、バイト配列をセルに割り当てます。
6. 必要に応じて、対象の行と列の行の高さと列の幅を調整し、埋め込み画像をより目立つようにします。
7. ワークブックをディスクに `.xlsx` ファイルとして保存します。

次のコードは完全な方法を示しています。

```java
import com.aspose.cells.*;
import java.nio.file.Files;
import java.nio.file.Paths;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// ターゲットセル C6 を取得する
Cell cell = worksheet.getCells().get("C6");

// 画像ファイルをバイト配列に読み込む
byte[] imageData = Files.readAllBytes(Paths.get("logo.png"));

// 画像をセルに直接埋め込む
cell.setEmbeddedImage(imageData);

// 埋め込まれた画像が見やすくなるように、必要に応じて行の高さと列の幅を調整する
worksheet.getCells().setColumnWidth(2, 30);   // 列 C (インデックス 2)
worksheet.getCells().setRowHeight(5, 100);     // 行 6 (インデックス 5)

// 結果のワークブックを .xlsx ファイルとして保存する
workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **適切な方法の選択**

どちらの方法も単一セル内に収まる画像を生成しますが、画像の格納方法と動作が異なります。

- **次のような場合はフローティング画像 (方法 1) を使用します。**
  - 配置、レイヤー順、他の描画オブジェクトとの整列をより細かく制御する必要がある場合。
  - 画像を他の図形と一緒に選択、並べ替え、グループ化できる図形として動作させたい場合。
  - すでに `PictureCollection` を使用しているコードとのレガシー互換性が必要な場合。
  - ワークシートのレイアウトに基づいてアンカー座標を動的に計算する必要がある場合。

- **次のような場合は埋め込み画像 (方法 2) を使用します。**
  - セルへの画像の挿入をできるだけシンプルに行いたい場合。
  - 画像が他のセルコンテンツと同様にセルと一緒に移動するようにする場合。
  - 画像を図形として操作する必要がない場合。

{{% alert color="primary" %}}

両方の方法は同じワークブック内で共存できます。2 つの仕組みはファイル内で異なるストレージ レイヤーを使用しているため、あるセルにはフローティング画像を配置し、他のセルには画像を直接埋め込むことができます。

{{% /alert %}}



{{< app/cells/assistant language="java" >}}