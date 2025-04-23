---
title: 位置、サイズ、およびデザインチャートを操作
description: Aspose.Cells for .NETを使用してMicrosoft Excelでポジション、サイズ、および設計チャートを効果的に操作する方法を学びます。ガイドでは、これらのプロパティを調整してレイアウトと視覚化を改善する方法を実証します。
keywords: Aspose.Cells for .NET、位置、サイズ、デザインチャート、Microsoft Excel、レイアウト、視覚化。
type: docs
weight: 45
url: /ja/net/manipulate-position-size-and-designer-chart/
---

## **チャートの位置とサイズ**
時には、ワークシート内で新しいチャートまたは既存のチャートの位置またはサイズを変更したいことがあります。 Aspose.Cellsはこれを実現するための [Chart.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) プロパティを提供しています。 新しい **高さ** と **幅** を使用してグラフのサイズを変更したり、新しい **X** と **Y** 座標を使用して再配置したりできます。
### **チャートの位置とサイズの制御**
チャートの位置（X、Y座標）またはサイズ（高さ、幅）を変更するには、これらのプロパティを使用します。

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Chart.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

上記のAPIの使用方法を説明する以下の例は、最初のワークシートにチャートが含まれる既存のワークブックを読み込みます。そして、Aspose.Cellsを使用して、チャートのサイズを変更し、再配置します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
## **デザイナーチャートの操作**
デザイナーテンプレートファイルでチャートを操作したり変更する必要がある場合があります。Aspose.Cellsはデザイナーチャートのコンテンツと要素を完全にサポートしています。データ、チャートのコンテンツ、背景画像、およびフォーマットは正確に保持されます。
### **テンプレートファイル内のデザイナーチャートを操作する**
テンプレートファイル内のデザイナーチャートを操作するには、チャート関連のAPIを使用してください。たとえば、Worksheet.Chartsプロパティを使用して、テンプレートファイル内の既存のチャートコレクションを取得できます。
#### **チャートの作成**
次の例は、ピラミッドチャートの作成方法を示しています。このチャートを後で操作します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
#### **チャートの操作**
次の例は、既存のチャートの操作方法を示しています。この例では、上記で作成したチャートを変更します。生成された出力では、1つのデータポイントの日付ラベルが 'United Kingdom, 30K' に設定されていることに注意してください。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
#### **デザイナーテンプレート内の折れ線グラフの操作**
この例では、折れ線グラフを操作します。既存のチャートにいくつかのデータシリーズを追加し、それらの線の色を変更します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
