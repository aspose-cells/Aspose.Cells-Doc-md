---
title: 円グラフまたは円グラフの棒グラフの 2 番目の円または棒にデータ ポイントがあるかどうかを調べる
type: docs
weight: 910
url: /ja/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---
## **考えられる使用シナリオ**
系列のデータ ポイントが 2 番目の円にあるかどうかを確認できます。*パイのパイ*チャートまたはバー*バー・オブ・パイ*Aspose.Cellsを使用したチャート。[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot)それを決定するプロパティ。

をダウンロードしてください[サンプルエクセルファイル](5473373.xlsx)次のサンプル コードで使用され、そのコンソール出力を参照してください。開くと[サンプルエクセルファイル](5473373.xlsx)、10未満のすべてのデータポイントがバーの内側にあることがわかります*バー・オブ・パイ*コンソール出力にも表示されるグラフ。
## **円グラフまたは円グラフの棒グラフの 2 番目の円または棒にデータ ポイントがあるかどうかを調べる**
次のサンプル コードは、データ ポイントがグラフの 2 番目の円グラフまたは棒グラフにあるかどうかを確認する方法を示しています。*パイのパイ*また*バー・オブ・パイ*チャート。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindDataPoints-FindDataPoints.java" >}}
## **コンソール出力**
上記のサンプル コードを実行した後に生成される次のコンソール出力を参照してください。[サンプルエクセルファイル](5473373.xlsx).もしも[IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot)は**間違い**の場合、データ ポイントは円の内側にあるか、円の内側にある場合**真実**の場合、データ ポイントはバーの内側にあります。

{{< highlight "java" >}}

 Value: 15

IsInSecondaryPlot: false

Value: 9

IsInSecondaryPlot: true

Value: 2

IsInSecondaryPlot: true

Value: 40

IsInSecondaryPlot: false

Value: 5

IsInSecondaryPlot: true

Value: 4

IsInSecondaryPlot: true

Value: 25

IsInSecondaryPlot: false

{{< /highlight >}}
