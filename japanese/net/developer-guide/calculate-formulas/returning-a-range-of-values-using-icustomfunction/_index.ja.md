---
title: ICustomFunctionを使用して値の範囲を返す
description: この記事では、Aspose.Cellsライブラリを使用してMicrosoft ExcelでICustomFunctionを使用して値の範囲を返す方法について説明しています。既存のExcelファイルを読み込むか新しいExcelファイルを作成し、Aspose.Cellsが提供するメソッドを使用して値の範囲を取得し、結果を返すことができます。最後に、変更したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、ICustomFunction、値の範囲を返すシリーズ
type: docs
weight: 50
url: /ja/net/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)はAspose.Cells for Java 20.8のリリース以降非推奨となりました。代わりに[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)クラスを使用してください。[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)クラスの使用方法については、次の記事で説明しています。

[AbstractCalculationEngine を使用した値の範囲を返す](/cells/ja/net/returning-a-range-of-values-using-abstractcalculationengine/)。

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cellsは、Microsoft Excelの組み込み関数としてサポートされていないユーザー定義またはカスタム関数を実装するために使用される[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)インターフェースを提供します。

[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)インターフェースのメソッドを実装する場合、通常は単一のセル値を返す必要があります。ただし、場合によっては値の範囲を返す必要があります。この記事では、[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)から値の範囲を返す方法について説明します。

{{% /alert %}}

次のコードは、[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) を実装し、そのメソッドを通じて値の範囲を返します。

関数*CalculateCustomFunction*を持つクラスを作成します。このクラスでは[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)を実装します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

上記の関数をプログラムで使用する

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
