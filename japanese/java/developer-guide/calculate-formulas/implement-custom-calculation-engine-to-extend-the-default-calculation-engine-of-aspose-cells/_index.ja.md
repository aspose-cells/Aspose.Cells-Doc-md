---
title: カスタム計算エンジンを実装して、Aspose.Cells のデフォルト計算エンジンを拡張します。
type: docs
weight: 590
url: /ja/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells には、ほぼすべての Microsoft Excel 式を計算できる強力な計算エンジンがあります。それにもかかわらず、デフォルトの計算エンジンを拡張することもでき、より優れた能力と柔軟性を提供します。

この機能の実装には、次のプロパティとクラスが使用されます。

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [抽象的な計算エンジン](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [計算データ](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
##  **カスタム計算エンジンの実装**
次のコードはカスタム計算エンジンを実装します。インターフェイスを実装します[抽象的な計算エンジン](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)メソッドが 1 つだけある[calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)）。このメソッドはすべての数式に対して呼び出されます。このメソッド内で、**TODAY**関数を使用して、システム日付に 1 日を追加します。したがって、現在の日付が 27/07/2023 の場合、カスタム エンジンは TODAY() を 28/07/2023 として計算します。

###  **プログラミングサンプル**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

###  **結果**

上記のサンプルコードのコンソール出力を確認してください。カスタム エンジンを使用した場合の A1 の値(日付時刻)は、カスタム エンジンを使用しない場合の結果より 1 日遅れているはずです。

###  **関連記事**
{{% alert color="primary" %}} 

- [カスタム関数をワークシートに記述せずに直接計算](/cells/ja/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
