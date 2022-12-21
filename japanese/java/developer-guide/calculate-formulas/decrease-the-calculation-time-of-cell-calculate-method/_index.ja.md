---
title: Cell.Calculateメソッドの計算時間を短縮
type: docs
weight: 860
url: /ja/java/decrease-the-calculation-time-of-cell-calculate-method/
---
考えられる使用シナリオ

通常、ユーザーは電話することをお勧めします[Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\) ) メソッドを 1 回実行してから、個々のセルの計算値を取得します。しかし、ユーザーがワークブック全体を計算したくない場合があります。単一のセルを計算したいだけです。 Aspose.Cells提供[CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive)設定できるプロパティ**間違い**個々のセルの計算時間を大幅に短縮します。 recursive プロパティが**真実**、その後、セルのすべての従属が各呼び出しで再計算されます。ただし、再帰プロパティが設定されている場合**間違い**の場合、依存セルは 1 回だけ計算され、その後の呼び出しでは再度計算されません。
## **Cell.Calculate()メソッドの計算時間を短縮**
次のサンプル コードは、[CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive)財産。指定されたコードでこのコードを実行してください[サンプルエクセルファイル](5472288.xlsx)コンソール出力を確認します。再帰プロパティを**間違い**計算時間を大幅に短縮しました。このプロパティをよりよく理解するために、コメントもお読みください。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **コンソール出力**
これは、指定されたコマンドで実行したときの上記のサンプル コードのコンソール出力です。[サンプルエクセルファイル](5472288.xlsx)私たちのマシンで。出力は異なる場合がありますが、再帰プロパティをに設定した後の経過時間に注意してください**間違い**に設定するよりも常に少なくなります。**真実**.



{{< highlight "java" >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
