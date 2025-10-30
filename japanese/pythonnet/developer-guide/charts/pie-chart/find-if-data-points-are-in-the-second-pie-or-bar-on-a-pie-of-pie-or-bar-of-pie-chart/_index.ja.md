---
title: パイオブパイチャートまたはバーオブパイチャートでデータポイントが第2パイまたは棒にあるかどうかを見つける
description: Aspose.Cells for Python via .NETを使って、円や棒のパイオブパイまたはパイオブパイチャートでデータポイントが第二の円や棒にあるかどうかを見つける方法を学びましょう。ガイドでは、複合チャートの二次的な円や棒にアクセスし、データを分析・操作する方法を示します。
keywords: Aspose.Cells for Python via .NET、パイ・オブ・パイチャート、バー・オブ・パイチャート、セカンダリーパイ、セカンダリーバー、データ分析、データ操作。
type: docs
weight: 180
url: /ja/python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **可能な使用シナリオ**
Aspose.Cells for Python via .NETを使って、*Pie of Pie*チャートや*Bar of Pie*チャートの二次的な円やバーにデータポイントがあるかどうかを判定できます。 [ChartPoint.is_in_secondary_plot](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/is_in_secondary_plot) プロパティを使用してください。

以下のサンプルコードで作成されたコンソール出力を参照してください。サンプルコードで使用される[サンプルエクセルファイル](5115193.xlsx) を開くと、10未満のすべてのデータポイントが *バーオブパイ* チャートの内部にあることが、コンソール出力にも示されています。

## **パイオブパイチャートまたはバーオブパイチャートでデータポイントが第2パイまたは棒にあるかどうかを見つける**
以下のサンプルコードは、*Pie of Pie*または*Bar of Pie*チャートでデータポイントが第2パイまたは棒にあるかどうかを見つける方法を示しています。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-FindDataPointsInPieBar.py" >}}
## **コンソール出力**
上記のサンプルコードと[サンプルExcelファイル](5115193.xlsx)を実行した後に生成されるコンソール出力をご覧ください。[is_in_secondary_plot](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/is_in_secondary_plot/)が**false**の場合、そのデータポイントはパイまたはバー内にあります。**true**の場合、そのデータポイントは二次的な円またはバー内にあります。



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
{{< app/cells/assistant language="python-net" >}}
