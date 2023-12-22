---
title: データの検索または検索
type: docs
weight: 50
url: /ja/net/find-or-search-data/
description: Aspose.Cells for .NET API を通じて、指定したデータを含むワークシート内のセルを検索または検索する方法を学習します。
keywords: Find data, Search data, Find Cells Containing a Formula, Search Cells Containing a Formula, Find Data or Formulas using FindOptions, Search Data or Formulas using FindOptions, Find or Search Cells Containing Specified String Value or Number, Find or Search cells contains specified data
---
{{% alert color="primary" %}}

Microsoft Excel を使用すると、ユーザーは指定されたデータを含むワークシート内のセルを検索できます。

{{% /alert %}}

##  **指定されたデータを含む Cells の検索**

###  **Microsoft Excelの使用**

Microsoft Excel を使用すると、ユーザーは指定されたデータを含むワークシート内のセルを検索できます。選択した場合**編集**から**探す**Microsoft Excel のメニューをクリックすると、検索値を指定できるダイアログが表示されます。

ここでは、値「Oranges」を探しています。 Aspose.Cells を使用すると、開発者は指定された値を含むワークシート内のセルを検索することもできます。

###  **Aspose.Cellsを使用する**

Aspose.Cells はクラスを提供します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、これは Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。ワークシートは次のように表されます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供するのは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)ワークシート内のすべてのセルを表すコレクション。の[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection には、ユーザー指定のデータを含むワークシート内のセルを検索するためのいくつかのメソッドが用意されています。これらの方法のいくつかについては、以下で詳しく説明します。

{{% alert color="primary" %}}

すべての Find メソッドは、検索対象として指定されたデータを含むセルの参照を返します。

{{% /alert %}}

##  **数式を含む Cells の検索**

開発者は、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**探す**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)方法。通常、[**探す**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)メソッドは 3 つのパラメータを受け取ります。

- **物体：**検索するオブジェクト。型は int、double、DateTime、string、bool である必要があります。
- **前のセル:**同じオブジェクトを持つ前のセル。最初から検索する場合、このパラメータは null に設定できます。
- FindOptions: 必要なオブジェクトを検索するためのオプション。

以下の例では、ワークシート データを使用して find メソッドを練習します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

##  **FindOptions を使用したデータまたは数式の検索**

を使用して指定された値を見つけることができます。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**探す**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)さまざまな方法で[**検索オプション**](https://reference.aspose.com/cells/net/aspose.cells/findoptions)。通常、[**探す**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)メソッドは次のパラメータを受け入れます。

- *検索値**、検索するデータまたは値。
- *前のセル**、同じ値が含まれていた最後のセル。最初から検索する場合、このパラメータは null に設定できます。
- *検索オプション**、検索オプション。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

##  **指定された文字列値または数値を含む Cells の検索**

同じものを呼び出すことで、指定された文字列値を見つけることができます[**探す**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)で見つかったメソッド[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)いろいろなコレクション[**検索オプション**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

を指定します[**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype)そして[**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype)プロパティ。次のコード例は、これらのプロパティを使用して、さまざまな数の文字列を含むセルを検索する方法を示しています。**始まり**またはで**中心**またはで**終わり**セルの文字列の。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

##  **アドバンストトピック**
- [特定のスタイルで Cells を検索](/cells/ja/net/find-cells-with-specific-style/)
- [セル値が一重引用符で始まるかどうかを確認します](/cells/ja/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [元の値を使用したデータの検索](/cells/ja/net/search-data-using-original-values/)
