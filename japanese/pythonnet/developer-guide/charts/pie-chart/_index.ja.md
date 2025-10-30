---
title: リーダーライン付きの円グラフの作成
description: Microsoft Excelでリーダー線付きの円グラフを作成するために、Aspose.Cells for Python via .NETを使用する方法を学びましょう。ガイドでは、データポイントを凡例に接続するリーダー線を追加し、チャート全体の視認性を向上させる方法を示します。
keywords: Aspose.Cells for Python via .NET、円グラフ、リーダー線、Microsoft Excel、データビジュアライゼーション、チャートカスタマイズ。
linktitle: 円グラフ
type: docs
weight: 45
url: /ja/python-net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

この記事では、Aspose.Cells for Python via .NET APIを使用して、リーダー線付きの円グラフをゼロから作成する方法を説明します。Excelでは、「リーダー線を表示」オプションはデフォルトで設定されているため、Excelで円グラフを作成するとリーダー線が表示されます。ただし、Aspose.Cells for Python via .NET APIを使って同様のグラフを作成する場合、[**Series.has_leader_lines**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/has_leader_lines)プロパティを明示的に設定する必要があります。

{{% /alert %}}

Aspose.Cells for Python via .NET APIを使用してリーダー線付きの円グラフを作成する方法を示すために、まず新しい[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)を作成し、シリーズデータソースとして使用するデータを入力します。データが配置されたら、[**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart)の種類[**ChartType.PIE**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype/)をコレクションのチャートに追加し、そのさまざまな側面を設定して目的のチャートビューを得ます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateWorkbook.py" >}}

これまでに円グラフを作成し、異なる側面を設定しました。これからは、チャートのリーダーラインをオンにします。リーダーラインを表示するには、データラベルを少し移動する必要があります。

次のコードは、リーダーラインをオンにし、チャートを更新し、それからデータラベルの位置を計算して適切に移動します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-TurnOnLeaderLines.py" >}}

最後に、次のコードでチャートを画像形式で保存し、ワークブックをXLSX形式で保存します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SaveChartInImageAndWorkbookInXLSX.py" >}}

|**作成された円グラフ**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **高度なトピック**
- [円グラフでのカスタムスライスまたはセクターの色](/cells/ja/python-net/custom-slice-or-sector-colors-in-pie-chart/)
- [パイオブパイチャートまたはバーオブパイチャートでデータポイントが第2パイまたは棒にあるかどうかを見つける](/cells/ja/python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## 関連記事

- [チャートの作成](/cells/ja/python-net/creating-charts/)
- [グラフのカスタマイズ](/cells/ja/python-net/customizing-charts/)
- [グラフのデータ整形](/cells/ja/python-net/data-formatting-in-charts/)
- [グラフの外観設定](/cells/ja/python-net/setting-chart-appearance/)

{{< app/cells/assistant language="python-net" >}}
