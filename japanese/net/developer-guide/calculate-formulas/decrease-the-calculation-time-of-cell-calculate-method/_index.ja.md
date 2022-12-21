---
title: Cell.Calculateメソッドの計算時間を短縮
type: docs
weight: 100
url: /ja/net/decrease-the-calculation-time-of-cell-calculate-method/
---
## **考えられる使用シナリオ**

通常、ユーザーは電話することをお勧めします[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)メソッドを 1 回実行してから、個々のセルの計算値を取得します。しかし、ユーザーがワークブック全体を計算したくない場合があります。単一のセルを計算したいだけです。 Aspose.Cells提供[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive)設定できるプロパティ**間違い**個々のセルの計算時間を大幅に短縮します。 recursive プロパティが**真実**、その後、セルのすべての従属が各呼び出しで再計算されます。しかし、再帰プロパティが**間違い**の場合、依存セルは 1 回だけ計算され、その後の呼び出しでは再度計算されません。

## **Cell.Calculate()メソッドの計算時間を短縮**

次のサンプル コードは、[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive)財産。指定されたコードでこのコードを実行してください[サンプルエクセルファイル](5113710.xlsx)コンソール出力を確認します。再帰プロパティを**間違い**計算時間を大幅に短縮しました。このプロパティをよりよく理解するために、コメントもお読みください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

## **コンソール出力**

これは、指定されたコマンドで実行したときの上記のサンプル コードのコンソール出力です。[サンプルエクセルファイル](5113710.xlsx)私たちのマシンで。出力は異なる場合がありますが、再帰プロパティをに設定した後の経過時間に注意してください**間違い**に設定するよりも常に少なくなります。**真実**.

{{< highlight "java" >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
