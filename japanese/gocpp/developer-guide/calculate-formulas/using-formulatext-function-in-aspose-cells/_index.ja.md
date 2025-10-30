---
title: GolangをC++経由でAspose.CellsのFormulaText関数を使用する
linktitle: FormulaText関数の使用
description: この記事では、Aspose.Cellsライブラリを使用してMicrosoft Excelで式を処理するFormulaText関数の使用方法について紹介しています。既存のExcelファイルを読み込むか新しいExcelファイルを作成し、Aspose.Cellsが提供するメソッドを使用してセルの式テキストを取得し、結果を取得することができます。最後に、変更したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、FormulaText 関数
type: docs
weight: 60
url: /ja/go-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText はExcel 2013以降の関数です。Excel 2010や2007などの以前のバージョンではサポートされていません。その名前が示すように、指定されたセルにある式のテキストを出力します。この記事では、Aspose.Cellsを使用してこの関数をどのように利用するかを示します。

{{% /alert %}} 

次のサンプルコードは、FormulaTextをAspose.Cellsで使用する方法を示しています。このコードは、まずセルA1に式を書き込み、次にFormulaTextを使用してセルA2に式のテキストを出力しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UsingFormulatextFunctionInAsposeCells.go" >}}
## **コンソール出力**
上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
