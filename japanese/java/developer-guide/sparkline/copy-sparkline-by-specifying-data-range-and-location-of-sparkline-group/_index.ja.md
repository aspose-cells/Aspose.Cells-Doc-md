---
title: スパークライン グループのデータ範囲と場所を指定してスパークラインをコピーする
type: docs
weight: 120
url: /ja/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---
MS Excel でスパークライン グループのデータ範囲と場所を指定してスパークラインをコピーする

Microsoft Excel では、スパークライン グループのデータ範囲と場所を指定して、スパークラインをコピーできます。次の手順に従って、スパークラインを他のセルにコピーします。

- スパークラインを含むセルを選択します。
- 選択する**データの編集**から**スパークライン**セクション内**デザイン**タブ
- 選ぶ**グループの場所とデータを編集...**
- データ範囲と場所を指定し、[OK] をクリックします。

## 例

Aspose.Cells は[**SparklineCollection.add(データ範囲、行、列)**](https://reference.aspose.com/cells/java/com.aspose.cells/SparklineCollection)メソッドを使用して、スパークライン グループのデータ範囲と場所を指定します。

### ソース ファイルと出力ファイルのスクリーンショット

次のスクリーンショットは、コード内で使用されるソース Excel ファイルを示しています。赤い強調表示された領域には、「**グループの場所とデータを編集...**" オプションを使用して、スパークライン グループのデータ範囲と場所を指定します。セル P4 は、Aspose.Cells を使用して黄色で塗りつぶされた他の 4 つのセルにコピーされるスパークラインを示しています。

![todo:画像_代替_文章](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_1.png)

次のスクリーンショットは、サンプル コードによって生成された出力 Excel ファイルを示しています。ご覧のとおり、セル P4 のスパークラインは、それぞれ異なるデータ範囲を持つ列 P の次の 4 つのセルにコピーされています。

![todo:画像_代替_文章](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_2.png)

### Java スパークライン グループのデータ範囲と場所を指定してスパークラインをコピーするコード

次のサンプル コードは、上のスクリーンショットに示すようにソース Excel ファイルを読み込み、最初のスパークライン グループにアクセスして、スパークライン グループ内にデータ範囲と場所を追加します。最後に、上のスクリーンショットにも示されているように、出力 Excel ファイルをディスクに書き込みます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopySparkline-CopySparkline.java" >}}
