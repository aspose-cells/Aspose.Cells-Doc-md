---
title: Aspose.Cells での FormulaText 関数の使用
description: この記事では、Aspose.Cells ライブラリの FormulaText 関数を使用して、Microsoft Excel で数式を処理する方法を紹介します。既存の Excel ファイルをロードするか、新しい Excel ファイルを作成することで、Aspose.Cells で提供されるメソッドを使用してセルの数式テキストを取得および設定し、結果を取得できます。最後に、変更した Excel ファイルをディスクに保存します。
keywords: Aspose.Cells, Excel, FormulaText functions
type: docs
weight: 60
url: /ja/net/using-formulatext-function-in-aspose-cells/
---
{{% alert color="primary" %}} 

FormulaText は Excel 2013 以降の関数です。 Excel 2010 や 2007 などの以前のバージョンではサポートされていません。その名前が示すように、指定されたセルに存在する数式のテキストを印刷します。この記事では、Aspose.Cellsを使ってこの機能を利用する方法を紹介します。

{{% /alert %}} 

次のサンプル コードは、Aspose.Cells での FormulaText の使用法を示しています。このコードは、最初にセル A1 に数式を書き込み、次にセル A2 の FormulaText を使用して数式のテキストを印刷します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingFormulaTextFunction-UsingFormulaTextFunction.cs" >}}
##  **コンソール出力**
上記のサンプルコードのコンソール出力を次に示します。

{{< highlight "java" >}}

 =SUM(B1:B10)

{{< /highlight >}}
