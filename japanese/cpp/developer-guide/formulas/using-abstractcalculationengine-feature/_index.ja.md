---
title: AbstractCalculationEngine機能の使用
type: docs
weight: 20
url: /ja/cpp/using-abstractcalculationengine-feature/
---


## **紹介**
この記事では、Aspose.Cells APIを使用してAbstractCalculationEngine機能を実装してカスタム関数を作成する方法について理解を提供します。

AbstractCalculationEngineインターフェースを使用すると、特定の要件を満たすためにAspose.Cellsコア計算エンジンを拡張するカスタム数式計算関数を追加できます。この機能は、テンプレートファイル内またはカスタム関数を実装し、Aspose.Cells APIを使用して評価する場合に、テンプレートファイル内またはカスタム関数を評価するために非常に便利です。

## **AbstractCalculationEngine機能の利用 - 1**

次のサンプルコードでは、AbstractCalculationEngineインターフェースを実装し、MySampleFunc()とYourSampleFunc()という2つのカスタム関数の値を評価して返します。これらのカスタム関数はそれぞれセルA1とA2にあります。それから、Workbook.CalculateFormula(const CalculationOptions& options)メソッドを呼び出してAbstractCalculationEngine .Calculate(CalculationData& data)メソッドの実装を呼び出します。その後、コンソールにA1とA2の値を出力します。詳細については、以下のサンプルコードのコンソール出力をご覧ください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingAbstractCalculationEngine.cpp" >}}


## **コンソール出力**
{{< highlight java >}}

MySampleFunc-Test called successfully.
YourSampleFunc-Test called successfully.
Value of A1 is : 1
Value of A2 is : 2

{{< /highlight >}}

## **AbstractCalculationEngine機能の利用 - 2**

次のサンプルコードは、サンプルファイルからカスタム関数を読み取り、Workbook.CalculateFormula(const CalculationOptions& options)メソッドを呼び出して、AbstractCalculationEngine .Calculate(CalculationData& data)メソッドをさらに処理する例を示します。

サンプルファイル：[sample-file.xlsx](sample-file.xlsx)

## **サンプルコード**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingAbstractCalculationEngine2.cpp" >}}
