---
title: パイオブパイチャートまたはバーオブパイチャートでデータポイントが第2パイまたは棒にあるかどうかを見つける
description: Aspose.Cells for .NETを使用して、データポイントを2番目のパイや棒の中に含むかどうかを見つける方法を学びます。ガイドでは、複合チャートの2次パイや棒を特定してアクセスし、データを効果的に分析および操作する方法を示します。
keywords: Aspose.Cells for .NET、パイオブパイチャート、バーオブパイチャート、セカンダリーパイ、セカンダリーバー、データ解析、データ操作。
type: docs
weight: 180
url: /ja/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **可能な使用シナリオ**
Aspose.Cellsを使用して、*パイオブパイ* チャートの2番目のパイやバーオブ *バーオブパイ* チャートのデータポイントを見つけることができます。[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)プロパティを使用して、それを判断してください。

以下のサンプルコードで作成されたコンソール出力を参照してください。サンプルコードで使用される[サンプルエクセルファイル](5115193.xlsx) を開くと、10未満のすべてのデータポイントが *バーオブパイ* チャートの内部にあることが、コンソール出力にも示されています。
## **パイオブパイチャートまたはバーオブパイチャートでデータポイントが第2パイまたは棒にあるかどうかを見つける**
以下のサンプルコードは、*Pie of Pie*または*Bar of Pie*チャートでデータポイントが第2パイまたは棒にあるかどうかを見つける方法を示しています。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
## **コンソール出力**
[5115193.xlsx](https://example.com) を使用した上記のサンプルコードを実行した後に生成されたコンソール出力を参照してください。 [IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)が **false** の場合、データポイントはパイの内部にあり、**true** の場合、データポイントはバーの内部にあります。



{{< highlight java >}}

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
{{< app/cells/assistant language="csharp" >}}
