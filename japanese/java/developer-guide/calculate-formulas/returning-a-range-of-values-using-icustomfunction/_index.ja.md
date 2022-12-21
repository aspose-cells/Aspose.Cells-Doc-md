---
title: ICustomFunction を使用して値の範囲を返す
type: docs
weight: 270
url: /ja/java/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

の[**カスタム関数**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)Aspose.Cells for Java 20.8 のリリース以降は非推奨です。をご利用ください[**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)クラス。の使用[**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)クラスについては以下の記事で説明しています。

[AbstractCalculationEngine を使用して値の範囲を返す](/cells/ja/java/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells提供[**カスタム関数**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)Microsoft Excel で組み込み関数としてサポートされていないユーザー定義関数またはカスタム関数を実装するために使用されるインターフェイス。

ほとんどの場合、[**カスタム関数**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)インターフェイス メソッドでは、単一のセル値を返す必要があります。ただし、値の範囲を返す必要がある場合もあります。この記事では、値の範囲を返す方法について説明します[**カスタム関数**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{% /alert %}}

## **ICustomFunction を使用して値の範囲を返す**

次のコードは実装します[**カスタム関数**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)メソッドを介して値の範囲を返します。を確認してください[出力エクセルファイル](5472922.xlsx)と[pdf](5472925.pdf)参照用のコードで生成されます。

関数を持つクラスを作成する*CalculateCustomFunction*.このクラスは実装します[**カスタム関数**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

上記の関数をプログラムで使用します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
