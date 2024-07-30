---
title: 行または範囲をコピーする際、チャートを新しいワークシートにコピーすると、チャートのデータソースは変更されません。
type: docs
weight: 850
url: /ja/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **可能な使用シナリオ**
行または範囲を新しいワークシートにコピーする際、チャートのデータソースが変更されないことがあります。
## **行や範囲をコピーする際に、チャートのデータソースを宛先ワークシートに変更する**
行または範囲に含まれるチャートを新しいワークシートにコピーする際にCopyOptions.ReferToDestinationSheetプロパティの使用方法を示したサンプルコードです。コードでは[サンプルエクセルファイル](5472284.xlsx)が使用され、[出力エクセルファイル](5472283.xlsx)が生成されます。スクリーンショットでは、[出力エクセルファイル](5472283.xlsx)内のチャートのデータソースがSheet1ではなくDestSheetを参照していることが示されています。

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeDataSource-ChangeDataSource.java" >}}






