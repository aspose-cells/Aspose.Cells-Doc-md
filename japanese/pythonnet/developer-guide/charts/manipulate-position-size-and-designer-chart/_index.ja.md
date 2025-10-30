---
title: 位置、サイズ、およびデザインチャートを操作
description: Aspose.Cells for Python via .NETを使って、Microsoft Excelのチャートの位置、サイズ、デザイナーのチャートを効果的に操作する方法について解説します。レイアウトと視覚化の改善のためにこれらのプロパティを調整する方法を示します。
keywords: Aspose.Cells for Python via .NET、位置、サイズ、デザイナーチャート、Microsoft Excel、レイアウト、視覚化。
type: docs
weight: 45
url: /ja/python-net/manipulate-position-size-and-designer-chart/
---

## **チャートの位置とサイズ**
時には、新しいまたは既存のチャートの位置やサイズを変更したいことがあります。Aspose.Cells for Python via .NETは[Chart.chart_object](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/chart_object)プロパティを提供し、これを使って実現できます。このプロパティのサブプロパティを使って、チャートのサイズを新しい高さと幅に調整したり、XおよびYの座標を変更したりできます。
### **チャートの位置とサイズの制御**
チャートの位置（X、Y座標）またはサイズ（高さ、幅）を変更するには、これらのプロパティを使用します。

1. [Chart.chart_object.x](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/x)
1. [Chart.chart_object.y](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/y)
1. [Chart.chart_object.height](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/height)
1. [Chart.chart_object.width](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/width)

以下の例では、上記のAPIの使用方法を説明します。既存のブックをロードし、その最初のワークシートにチャートを含めます。その後、Aspose.Cells for Python via .NETを使用してチャートのサイズと位置を再調整します。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChangeChartPosition-1.py" >}}
## **デザイナーチャートの操作**
デザイナーテンプレートファイル内のチャートを操作または変更する必要がある場合があります。Aspose.Cells for Python via .NETは、デザイナーチャートの内容と要素の操作を完全にサポートしています。データ、チャート内容、背景画像、およびフォーマットを正確に保持できます。
### **テンプレートファイル内のデザイナーチャートを操作する**
テンプレートファイル内のデザイナーチャートを操作するには、チャート関連のAPIを使用してください。たとえば、Worksheet.Chartsプロパティを使用して、テンプレートファイル内の既存のチャートコレクションを取得できます。
#### **チャートの作成**
次の例は、ピラミッドチャートの作成方法を示しています。このチャートを後で操作します。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-HowToCreateChart-1.py" >}}
#### **チャートの操作**
次の例は、既存のチャートの操作方法を示しています。この例では、上記で作成したチャートを変更します。生成された出力では、1つのデータポイントの日付ラベルが 'United Kingdom, 30K' に設定されていることに注意してください。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-ModifyPieChart-1.py" >}}
#### **デザイナーテンプレート内の折れ線グラフの操作**
この例では、折れ線グラフを操作します。既存のチャートにいくつかのデータシリーズを追加し、それらの線の色を変更します。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-ModifyLineChart-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
