---
title: データ ポイントが円グラフまたは円グラフの 2 番目の円または棒にあるかどうかを確認する
description: Aspose.Cells for .NET を使用して、円グラフまたは円グラフの 2 番目の円または棒にデータ ポイントがあるかどうかを確認する方法を説明します。このガイドでは、複合グラフ上の 2 番目の円または棒を特定してアクセスし、データを効果的に分析および操作できるようにする方法を説明します。
keywords: Aspose.Cells for .NET, Pie of Pie Chart, Bar of Pie Chart, Secondary Pie, Secondary Bar, Data Analysis, Data Manipulation.
type: docs
weight: 180
url: /ja/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---
##  **考えられる使用シナリオ**
系列のデータ ポイントが 2 番目の円にあるかどうかを確認できます。*パイ・オブ・パイ*チャートまたはバーで*バー・オブ・パイ*Aspose.Cells を使用したチャート。[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)プロパティを使用して決定します。

ダウンロードしてください[サンプルエクセルファイル](5115193.xlsx)次のサンプル コードで使用されているので、そのコンソール出力を確認してください。開けると、[サンプルエクセルファイル](5115193.xlsx) 10 未満のすべてのデータ ポイントがバーの内側にあることがわかります。*バー・オブ・パイ*コンソール出力にも表示されるグラフ。
##  **データ ポイントが円グラフまたは円グラフの 2 番目の円または棒にあるかどうかを確認する**
次のサンプル コードは、データ ポイントが 2 番目の円または棒にあるかどうかを確認する方法を示しています。*パイ・オブ・パイ*または*バー・オブ・パイ*チャート。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
##  **コンソール出力**
上記のサンプル コードを実行した後に生成される次のコンソール出力を参照してください。[サンプルエクセルファイル](5115193.xlsx) 。もし[IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)*false** の場合、データ ポイントは円グラフの内側にあり、*true** の場合、データ ポイントは棒グラフの内側にあります。



{{< highlight "java" >}}

 Value: 15

IsInSecondaryPlot: False

Value: 9

IsInSecondaryPlot: True

Value: 2

IsInSecondaryPlot: True

Value: 40

IsInSecondaryPlot: False

Value: 5

IsInSecondaryPlot: True

Value: 4

IsInSecondaryPlot: True

Value: 25

IsInSecondaryPlot: False

{{< /highlight >}}
