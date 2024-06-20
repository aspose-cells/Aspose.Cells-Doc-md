---
title: 循環参照の検出
description: Microsoft Excelで循環参照を検出するためにAspose.Cellsライブラリを使用する方法について紹介します。既存のExcelファイルを読み込むか、新しいファイルを作成することで、Aspose.Cellsが提供する方法を使用して循環参照を検出し、結果を取得し、最後に変更されたExcelファイルをディスクに保存します。
keywords: Aspose.Cells, Excel, 循環参照、検出
type: docs
weight: 70
url: /ja/net/detecting-circular-reference/
---

## **紹介**

ワークブックには循環参照が存在し、時々、循環参照があるかどうかを検出する必要があります。

## **循環参照の検出の概念**

循環参照は、式が計算される時にのみ検出されます。なぜなら、1つの式の参照は通常、他の部分や他の式の計算結果に依存するからです。そのため、この要件(循環参照を持つセルを収集するための)のために新しいAPIを提供しています。

[**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): 計算されている1つのセルに関する関連データの計算を表します

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): は、循環参照が発生したときに式計算エンジンによって呼び出されます。列挙子内の要素は、1つのサークル内のすべてのセルを表す[**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell)オブジェクトであり、返された値は、この呼び出し後に循環セルを計算する必要があるかどうかを示します。

ユーザーは、[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular)メソッドの実装でこれらの循環参照を収集することができます。

ソースのサンプルファイルは、次のリンクからダウンロードできます:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)クラスから派生した*CircularMonitor*クラスの定義は次のようになります:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
