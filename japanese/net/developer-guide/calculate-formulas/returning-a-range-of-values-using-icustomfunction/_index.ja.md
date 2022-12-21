---
title: ICustomFunction を使用して値の範囲を返す
type: docs
weight: 50
url: /ja/net/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

の[**カスタム関数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)Aspose.Cells for Java 20.8 のリリース以降は非推奨です。をご利用ください[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)クラス。の使用[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)クラスについては以下の記事で説明しています。

[AbstractCalculationEngine を使用して値の範囲を返す](/cells/ja/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells提供[**カスタム関数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)Microsoft Excel で組み込み関数としてサポートされていないユーザー定義関数またはカスタム関数を実装するために使用されるインターフェイス。

ほとんどの場合、[**カスタム関数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)インターフェイス メソッドでは、単一のセル値を返す必要があります。ただし、値の範囲を返す必要がある場合もあります。この記事では、値の範囲を返す方法について説明します[**カスタム関数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

次のコードは実装します[**カスタム関数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)メソッドを介して値の範囲を返します。

関数を持つクラスを作成する*CalculateCustomFunction*.このクラスは実装します[**カスタム関数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

上記の関数をプログラムに使用します

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
