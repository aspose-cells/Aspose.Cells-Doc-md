---
title: カスタム計算エンジンを実装して、Aspose.Cells のデフォルト計算エンジンを拡張します。
description: この記事では、Aspose.Cells ライブラリを使用してカスタム計算エンジンを実装することにより、デフォルトの計算エンジンを拡張する方法について説明します。既存の Excel ファイルをロードするか、新しい Excel ファイルを作成することで、Aspose.Cells が提供するメソッドを使用してカスタム計算エンジンを実装し、結果を取得できます。最後に、変更した Excel ファイルをディスクに保存します。
keywords: Aspose.Cells, Excel, Custom Calculation Engine, extends the default calculation engine
type: docs
weight: 80
url: /ja/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
##  **カスタム計算エンジンの実装**

Aspose.Cells には、ほぼすべての Microsoft Excel 式を計算できる強力な計算エンジンがあります。それにもかかわらず、デフォルトの計算エンジンを拡張することもでき、より優れた能力と柔軟性を提供します。

この機能の実装には、次のプロパティとクラスが使用されます。

- **[CalculationOptions.CustomEngine](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[計算データ](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

次のコードはカスタム計算エンジンを実装します。インターフェイスを実装します**[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**を持っている**[Calculate(CalculationData データ)](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)**方法。このメソッドはすべての数式に対して呼び出されます。このメソッド内で、**TODAY**関数を使用して、システム日付に 1 日を追加します。したがって、現在の日付が 27/07/2023 の場合、カスタム エンジンは TODAY() を 28/07/2023 として計算します。

###  **プログラミングサンプル**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

###  **結果**

上記のサンプルコードのコンソール出力を確認してください。カスタム エンジンを使用した場合の A1 の値(日付時刻)は、カスタム エンジンを使用しない場合の結果より 1 日遅れているはずです。

###  **関連記事**

{{% alert color="primary" %}}

[カスタム関数をワークシートに記述せずに直接計算](/cells/ja/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
