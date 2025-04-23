---
title: パイオブパイチャートまたはバーオブパイチャートでデータポイントが第2パイまたは棒にあるかどうかを見つける
type: docs
weight: 910
url: /ja/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **可能な使用シナリオ**
Aspose.Cellsを使用して、*Pie of Pie*チャートの第2パイまたは*Bar of Pie*チャートの棒にシリーズのデータポイントがあるかどうかを見つけることができます。[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot)プロパティを使用してください。

以下のサンプルコードを使用して、[sample excel file](5473373.xlsx)をダウンロードし、そのコンソール出力を確認してください。[sample excel file](5473373.xlsx)を開くと、コンソール出力によっても示されているように、10未満のすべてのデータポイントが*Bar of Pie*チャートの内側にあります。
## **パイオブパイチャートまたはバーオブパイチャートでデータポイントが第2パイまたは棒にあるかどうかを見つける**
以下のサンプルコードは、*Pie of Pie*または*Bar of Pie*チャートでデータポイントが第2パイまたは棒にあるかどうかを見つける方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindDataPoints-FindDataPoints.java" >}}
## **コンソール出力**
以下は、上記のサンプルコードの実行後に生成されたコンソール出力です。[IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot)が**false**の場合、データポイントはパイの内側にあり、**true**の場合はデータポイントが棒の内側にあります。

{{< highlight java >}}

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
{{< app/cells/assistant language="java" >}}
