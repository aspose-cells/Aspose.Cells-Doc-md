---
title: データ範囲とスパークライングループの位置を指定してスパークラインをコピーする
type: docs
weight: 120
url: /ja/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

MS Excelでデータ範囲とスパークライングループの場所を指定してスパークラインをコピーする

Microsoft Excelでは、データ範囲とスパークライングループの位置を指定してスパークラインをコピーすることができます。次の手順に従って、スパークラインを他のセルにコピーできます。

- Sparklineを含むセルを選択します。
- **デザイン**タブ内の**スパークライン**セクションから**データの編集**を選択します
- **グループの場所とデータの編集...**を選択します
- データ範囲と場所を指定し、OKをクリックします。

## 例

Aspose.Cellsでは、スパークライングループのデータ範囲と場所を指定するための[**SparklineCollection.add(dataRange, row, column)**](https://reference.aspose.com/cells/java/com.aspose.cells/SparklineCollection)メソッドが提供されています。

### ソースファイルと出力ファイルのスクリーンショット

次のスクリーンショットは、コード内で使用されているソースExcelファイルを示しています。赤くハイライトされた領域は、「**グループの場所とデータの編集...**」オプションを示しており、スパークライングループのデータ範囲と場所を指定するために使用されます。セルP4にはAspose.Cellsを使用して黄色で塗られた他の四つのセルにコピーされるスパークラインが表示されています。

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_1.png)

次のスクリーンショットは、サンプルコードによって生成された出力Excelファイルを示しています。ご覧の通り、セルP4のスパークラインは、異なるデータ範囲を持つ隣接する四つのセルにコピーされています。

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_2.png)

### スパークライングループのデータ範囲と場所を指定してスパークラインをコピーするためのJavaコード

次のサンプルコードでは、前述のスクリーンショットに示されているソースExcelファイルを読み込み、スパークライングループにアクセスしてデータ範囲と場所を追加します。最後に、出力Excelファイルをディスクに書き込みます（これも前述のスクリーンショットに示されています）。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopySparkline-CopySparkline.java" >}}
{{< app/cells/assistant language="java" >}}
