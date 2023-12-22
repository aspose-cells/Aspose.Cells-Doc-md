---
title: ICustomFunction を使用して値の範囲を返す
description: この記事では、Aspose.Cells ライブラリを使用して、Microsoft Excel の ICustomFunction で値の範囲を返す方法について説明します。既存の Excel ファイルをロードするか、新しい Excel ファイルを作成することで、Aspose.Cells が提供するメソッドを使用して値の範囲を取得し、結果を返すことができます。最後に、変更した Excel ファイルをディスクに保存します。
keywords: Aspose.Cells, Excel, ICustomFunction, returns a series of values
type: docs
weight: 50
url: /ja/net/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

の[**Iカスタム関数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)Aspose.Cells for Java 20.8 のリリース以降、非推奨になりました。をご利用ください。[**抽象的な計算エンジン**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)クラス。の使用[**抽象的な計算エンジン**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)クラスについては以下の記事で解説しています。

[AbstractCalculationEngine を使用して値の範囲を返す](/cells/ja/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 Aspose.Cellsが提供します[**Iカスタム関数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)Microsoft Excel で組み込み関数としてサポートされていないユーザー定義関数またはカスタム関数を実装するために使用されるインターフェイス。

ほとんどの場合、実装するときは、[**Iカスタム関数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)インターフェイス メソッドでは、単一のセル値を返す必要があります。ただし、場合によっては、ある範囲の値を返す必要があります。この記事では、値の範囲を返す方法について説明します。[**Iカスタム関数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

次のコードは実装します[**Iカスタム関数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)そしてそのメソッドを介して値の範囲を返します。

関数 *CalculateCustomFunction* を使用してクラスを作成します。このクラスが実装するのは、[**Iカスタム関数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

上記の関数をプログラムに使用してください

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
