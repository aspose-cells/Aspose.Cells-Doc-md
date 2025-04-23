---
title: AbstractCalculationEngineを使用して値の範囲を返す
description: この記事では、Aspose.Cellsライブラリを使用してMicrosoft Excelで値の範囲を返す抽象計算エンジンを紹介しています。既存のExcelファイルを読み込むか新しいExcelファイルを作成し、Aspose.Cellsが提供するメソッドを使用して値の範囲を取得し、結果を返すことができます。最後に、変更したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、値の範囲を返す抽象計算エンジン
type: docs
weight: 55
url: /ja/net/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cellsは、Microsoft Excelの組み込み関数としてサポートされていないユーザー定義またはカスタム関数を実装するために使用される[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)クラスを提供します。

この記事では、[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)から値の範囲を返す方法について説明します。

{{% /alert %}}

次のコードは、[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) クラスの使用をデモンストレーションし、そのメソッドを通じて値の範囲を返します。

関数*CalculateCustomFunction*を持つクラスを作成します。このクラスでは[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)を実装します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-CustomFunctionStaticValue.cs" >}}

上記の関数をプログラムで使用する

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
