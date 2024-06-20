---
title: ICustomFunctionを使用して値の範囲を返す
type: docs
weight: 270
url: /ja/java/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)はAspose.Cells for Java 20.8のリリース以降非推奨となりました。代わりに[**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)クラスを使用してください。[**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)クラスの使用方法については、次の記事で説明しています。

[AbstractCalculationEngineを使用して値の範囲を返す](/cells/ja/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cellsは、Microsoft Excelの組み込み関数としてサポートされていないユーザー定義またはカスタム関数を実装するために使用される[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)インターフェースを提供します。

[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)インターフェースのメソッドを実装する場合、通常は単一のセル値を返す必要があります。ただし、場合によっては値の範囲を返す必要があります。この記事では、[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)から値の範囲を返す方法について説明します。

{{% /alert %}}

## **ICustomFunctionを使用して値の範囲を返す**

次のコードは[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)を実装し、そのメソッドを介して値の範囲を返します。コードで生成された[出力Excelファイル](5472922.xlsx)および[PDF](5472925.pdf)を参照してください。

関数*CalculateCustomFunction*を持つクラスを作成します。このクラスは[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)を実装します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

次に、上記の関数をプログラムに使用します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
