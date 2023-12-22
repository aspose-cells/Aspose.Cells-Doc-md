---
title: Cellの計算時間を短縮します。計算メソッド
description: この記事では、Aspose.Cells Excel のセル計算メソッドの計算時間を短縮するために、Aspose.Cells ライブラリを使用する方法を紹介します。既存の Excel ファイルをロードするか、新しい Excel ファイルを作成することで、Aspose.Cells が提供するメソッドを使用してセルの計算方法を最適化し、パフォーマンスを向上させることができます。最後に、変更した Excel ファイルをディスクに保存します。
keywords: Aspose.Cells, Excel, Cell calculation methods, optimization, performance, reduction of calculation time
type: docs
weight: 100
url: /ja/net/decrease-the-calculation-time-of-cell-calculate-method/
---
##  **考えられる使用シナリオ**

通常、ユーザーに電話することをお勧めします。[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)メソッドを 1 回実行してから、個々のセルの計算値を取得します。ただし、ユーザーがワークブック全体を計算したくない場合もあります。彼らは単一のセルを計算したいだけです。 Aspose.Cellsが提供します[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive)設定できるプロパティ**間違い**個々のセルの計算時間が大幅に短縮されます。再帰プロパティが *true** に設定されている場合、セルのすべての依存関係が呼び出しごとに再計算されるためです。ただし、再帰プロパティが *false** の場合、依存セルは 1 回だけ計算され、後続の呼び出しでは再計算されません。

##  **Cell.Calculate() メソッドの計算時間を短縮します。**

次のサンプル コードは、[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive)財産。指定されたコードを使用してこのコードを実行してください[サンプルエクセルファイル](5113710.xlsx)コンソール出力を確認してください。再帰プロパティを次のように設定していることがわかります。**間違い**計算時間が大幅に短縮されました。このプロパティをより深く理解するために、コメントもお読みください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

##  **コンソール出力**

これは、指定されたコマンドを使用して実行した場合の上記のサンプル コードのコンソール出力です。[サンプルエクセルファイル](5113710.xlsx)私たちのマシンで。出力は異なる場合がありますが、再帰プロパティを次のように設定した後の経過時間に注意してください。**間違い**常に *true** に設定するよりも小さくなります。

{{< highlight "java" >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
