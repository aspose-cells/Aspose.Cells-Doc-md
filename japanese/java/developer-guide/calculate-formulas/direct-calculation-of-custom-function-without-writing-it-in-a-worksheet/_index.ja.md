---
title: カスタム関数をワークシートに書かずに直接計算
type: docs
weight: 650
url: /ja/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
{{% alert color="primary" %}} 

この記事では、カスタム関数を最初にワークシートに記述せずに直接計算する方法について説明します。をご利用ください[Worksheet.calculateFormula(文字列式、CalculationOptions オプション)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula\(java.lang.String,%20com.aspose.cells.CalculationOptions\)) この目的のためのメソッド。

{{% /alert %}} 
## **カスタム関数をワークシートに書かずに直接計算**
このメソッドの使用法を示す次のサンプル コードを参照してください。という名前のカスタム関数を使用しました*MyCompany.CustomFunction()*その値を「Aspose.Cells」と計算します。この値は、計算エンジンによって「Welcome to」であるセル A1 の値と自動的に連結され、最終的に計算された値は「Welcome to Aspose.Cells.」として返されます。コードでわかるように、カスタム関数はワークシートのどこにも記述されておらず、独自のカスタム ロジックによって直接計算されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
## **コンソール出力**
以下は、上記のサンプル コードのコンソール出力です。

{{< highlight "java" >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
## **関連記事**
{{% alert color="primary" %}} 

- [カスタム計算エンジンを実装して、Aspose.Cells のデフォルト計算エンジンを拡張します](/cells/ja/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
