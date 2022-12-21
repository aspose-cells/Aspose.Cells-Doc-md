---
title: ICustomFunction 機能の使用
type: docs
weight: 20
url: /ja/cpp/using-icustomfunction-feature/
---
## **序章**
この記事では、ICustomFunction 機能を使用して、Aspose.Cells API でカスタム関数を実装する方法について説明します。

ICustomFunction インターフェイスを使用すると、特定の要件を満たすために、Aspose.Cells コア計算エンジンを拡張するカスタム数式計算関数を追加できます。この機能は、カスタム (ユーザー定義) 関数をテンプレート ファイルまたはコードで定義する場合に便利です。カスタム関数は、他の既定の Microsoft Excel 関数と同様に、Aspose.Cells API を使用して実装および評価できます。
## **ICustomFunction 機能の使用**
次のサンプル コードは、2 つのカスタム関数、つまり MySampleFunc() と YourSampleFunc() の値を評価して返す ICustomFunction インターフェイスを実装します。これらのカスタム関数は、それぞれセル A1 と A2 内にあります。次に、IWorkbook.CalculateFormula(false, ICustomFunction) メソッドを呼び出して、ICustomFunction.CalculateCustomFunction() メソッドの実装を呼び出します。次に、実際には ICustomFunction.CalculateCustomFunction() によって返される値である A1 と A2 の値をコンソールに出力します。詳細については、以下のサンプル コードのコンソール出力を参照してください。
## **サンプルコード**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingICustomFunctionFeature.cpp" >}}


## **コンソール出力**
{{< highlight "java" >}}

 Value of A1: MY sample function was called successfully.

Value of A2: YOUR sample function was called successfully.

{{< /highlight >}}
