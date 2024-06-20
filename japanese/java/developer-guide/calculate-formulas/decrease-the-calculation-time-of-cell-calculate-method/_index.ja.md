---
title: Cell.Calculateメソッドの計算時間の短縮
type: docs
weight: 860
url: /ja/java/decrease-the-calculation-time-of-cell-calculate-method/
---


可能な使用シナリオ

通常、私たちはユーザーに[Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\)) メソッドを1回呼び出してから個々のセルの計算値を取得することをお勧めしています。しかし、時々、ユーザーはワークブック全体を計算したくないことがあります。彼らは単に単一のセルを計算したいだけです。Aspose.Cellsは[CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) プロパティを提供しており、それを**false**に設定すると、個別のセルの計算時間が著しく短縮されます。なぜなら、recursiveプロパティが**true**に設定されていると、依存セルは各呼び出しで再計算されるからです。しかし、recursiveプロパティが**false**に設定されていると、依存セルは1回だけ計算され、後続の呼び出しで再計算されません。
## **Cell.Calculate() メソッドの計算時間を短縮する**
次のサンプルコードは[CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) プロパティの使用例を示しています。このコードを指定された[サンプルエクセルファイル](5472288.xlsx)と一緒に実行して、そのコンソール出力を確認してください。recursiveプロパティを**false**に設定すると、計算時間が著しく減少していることが分かります。このプロパティの理解を深めるために、コメントもお読みください。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **コンソール出力**
これは上記のサンプルコードを私たちの機械で指定された[サンプルエクセルファイル](5472288.xlsx)で実行したときのコンソール出力です。ご注意ください、出力は異なる場合がありますが、recursiveプロパティを**false**に設定した後の経過時間は常に**true**に設定した場合よりも短くなります。



{{< highlight java >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
