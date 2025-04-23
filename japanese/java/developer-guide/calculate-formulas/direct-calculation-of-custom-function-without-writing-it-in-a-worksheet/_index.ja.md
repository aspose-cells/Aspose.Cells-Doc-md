---
title: ワークシートに書き込まずにカスタム関数を直接計算する
type: docs
weight: 650
url: /ja/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

{{% alert color="primary" %}} 

この記事では、ワークシートに書き込まずにカスタム関数を直接計算する方法を説明します。本目的には [Worksheet.calculateFormula(string formula, CalculationOptions opts)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula-java.lang.String-com.aspose.cells.CalculationOptions-) メソッドを使用してください。

{{% /alert %}} 
## **ワークシートに書き込まずにカスタム機能を直接計算する**
このメソッドの使用例を示す以下のサンプルコードをご覧ください。私たちは*MyCompany.CustomFunction()*というカスタム関数を使用し、その値を自分で"Aspose.Cells."として計算し、その後に計算エンジンがセルA1の値"Welcome to "と自動的に連結して最終的な計算値"Welcome to Aspose.Cells."を返します。コードに示す通り、カスタム関数をワークシートに書き込んでいないため、独自のカスタムロジックによって直接計算されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
## **コンソール出力**
上記のサンプルコードのコンソール出力は以下の通りです。

{{< highlight java >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
## **関連記事**
{{% alert color="primary" %}} 

- [Aspose.Cellsのデフォルトの計算エンジンを拡張するためにカスタム計算エンジンを実装する](/cells/ja/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
