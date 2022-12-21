---
title: 行または範囲のコピー中にチャートのデータ ソースを宛先ワークシートに変更する
type: docs
weight: 850
url: /ja/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
## **考えられる使用シナリオ**
チャートを含む行または範囲を新しいワークシートにコピーしても、チャートのデータ ソースは変更されません。たとえば、グラフのデータ ソースが =Sheet1!$A$1:$B$4 の場合、行または範囲を新しいワークシートにコピーした後、データ ソースは同じままになります (つまり、=Sheet1!$A$1:$B$4)。それはまだ古いワークシート、つまりSheet1を参照しています。これは、Microsoft Excel の動作でもあります。ただし、新しい宛先ワークシートを参照する場合は、CopyOptions.ReferToDestinationSheet プロパティを使用し、Cells.CopyRows() メソッドを呼び出すときに true に設定してください。宛先ワークシートが DestSheet の場合、グラフのデータ ソースは =Sheet1!$A$1:$B$4 から =DestSheet!$A$1:$B$4 に変更されます。
## **行または範囲のコピー中にチャートのデータ ソースを宛先ワークシートに変更する**
次のサンプル コードは、チャートを含む行または範囲を新しいワークシートにコピーする際の CopyOptions.ReferToDestinationSheet プロパティの使用方法を説明しています。コードは、[サンプルエクセルファイル](5472284.xlsx)を生成し、[出力エクセルファイル](5472283.xlsx) .スクリーンショットは、チャートのデータ ソースが[出力エクセルファイル](5472283.xlsx)Sheet1 の代わりに DestSheet を参照するようになりました。

![todo:画像_代替_文章](change-data-source-of-the-chart_1.png)







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeDataSource-ChangeDataSource.java" >}}






