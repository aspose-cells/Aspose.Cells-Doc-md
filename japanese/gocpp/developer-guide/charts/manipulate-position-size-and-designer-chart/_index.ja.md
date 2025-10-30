---
title: Go言語とC++を使ったデザイナーチャートの位置、サイズの操作
linktitle: 位置、サイズ、およびデザインチャートを操作
description: Microsoft Excelでレイアウトと可視化のために、Aspose.Cells for C++を使用して位置、サイズ、デザイナーチャートを効果的に操作する方法について学びます。ガイドでは、これらのプロパティを調整する方法を示します。
keywords: Aspose.Cells for C++、位置、サイズ、デザイナーチャート、Microsoft Excel、レイアウト、可視化。
type: docs
weight: 45
url: /ja/go-cpp/manipulate-position-size-and-designer-chart/
---

## **チャートの位置とサイズ**
時には、ワークシート内の新規または既存のチャートの位置やサイズを変更したい場合があります。Aspose.Cellsは [Chart.GetChartObject()](https://reference.aspose.com/cells/go-cpp/chart/getchartobject/) プロパティを提供しており、これを使用してチャートの高さや幅を新しい値にリサイズしたり、X座標とY座標で再配置したりできます。

### **チャートの位置とサイズの制御**
チャートの位置（X、Y座標）またはサイズ（高さ、幅）を変更するには、これらのプロパティを使用します。

1. [Chart.GetX()](https://reference.aspose.com/cells/go-cpp/shape/getx/)
1. [Chart.GetY()](https://reference.aspose.com/cells/go-cpp/shape/gety/)
1. [Chart.GetHeight()](https://reference.aspose.com/cells/go-cpp/shape/getheight/)
1. [Chart.GetWidth()](https://reference.aspose.com/cells/go-cpp/shape/getwidth/)

上記のAPIの使用方法を説明する以下の例は、最初のワークシートにチャートが含まれる既存のワークブックを読み込みます。そして、Aspose.Cellsを使用して、チャートのサイズを変更し、再配置します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart.go" >}}
## **デザイナーチャートの操作**
デザイナーテンプレートファイルでチャートを操作したり変更する必要がある場合があります。Aspose.Cellsはデザイナーチャートのコンテンツと要素を完全にサポートしています。データ、チャートのコンテンツ、背景画像、およびフォーマットは正確に保持されます。

### **テンプレートファイル内のデザイナーチャートを操作する**
テンプレートファイル内のデザイナーチャートを操作するには、チャート関連のAPIを使用してください。たとえば、Worksheet.Chartsプロパティを使用して、テンプレートファイル内の既存のチャートコレクションを取得できます。

#### **チャートの作成**
次の例は、ピラミッドチャートの作成方法を示しています。このチャートを後で操作します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-1.go" >}}
#### **チャートの操作**
次の例は、既存のチャートの操作方法を示しています。この例では、上記で作成したチャートを変更します。生成された出力では、1つのデータポイントの日付ラベルが 'United Kingdom, 30K' に設定されていることに注意してください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-2.go" >}}
#### **デザイナーテンプレート内の折れ線グラフの操作**
この例では、折れ線グラフを操作します。既存のチャートにいくつかのデータシリーズを追加し、それらの線の色を変更します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-3.go" >}}
