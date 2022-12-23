---
title: データの検索または検索
type: docs
weight: 50
url: /ja/net/find-or-search-data/
---
{{% alert color="primary" %}}

Microsoft Excel では、指定されたデータを含むワークシート内のセルをユーザーが検索できます。

{{% /alert %}}

## **特定のデータを含む結果 Cells**

### **Microsoft エクセルを使う**

 Microsoft Excel では、指定されたデータを含むワークシート内のセルをユーザーが検索できます。選択した場合**編集**から**探す**Microsoft Excel のメニューをクリックすると、検索値を指定できるダイアログが表示されます。

ここでは、値「オレンジ」を探しています。 Aspose.Cells を使用すると、開発者は指定された値を含むワークシート内のセルを見つけることもできます。

### **Aspose.Cells を使用**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)ワークシート内のすべてのセルを表すコレクション。の[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection には、ユーザー指定のデータを含むワークシート内のセルを検索するためのメソッドがいくつか用意されています。これらの方法のいくつかについて、以下で詳しく説明します。

{{% alert color="primary" %}}

すべての Find メソッドは、検索する指定されたデータを含むセルの参照を返します。

{{% /alert %}}

## **数式を含む Cells の検索**

開発者は、を呼び出してワークシート内の指定された数式を見つけることができます。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**探す**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)方法。通常、[**探す**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)メソッドは 3 つのパラメーターを受け入れます。

- **物体：**検索するオブジェクト。タイプは、int、double、DateTime、string、bool である必要があります。
- **前のセル:**同じオブジェクトを持つ前のセル。最初から検索する場合、このパラメーターを null に設定できます。
- FindOptions: 必要なオブジェクトを見つけるためのオプション。

以下の例では、検索方法を練習するためにワークシート データを使用しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **FindOptions を使用したデータまたは数式の検索**

を使用して、指定された値を見つけることができます。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**探す**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)さまざまな方法[**検索オプション**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).通常、[**探す**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)メソッドは次のパラメーターを受け入れます。

- **検索値**、検索するデータまたは値。
- **前のセル**、同じ値を含む最後のセル。最初から検索する場合、このパラメーターを null に設定できます。
- **オプションを探す**、検索オプション。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **指定された文字列値または数値を含む Cells の検索**

同じを呼び出すことで、指定された文字列値を見つけることができます[**探す**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)で見つかったメソッド[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)色々とコレクション[**検索オプション**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

指定する[**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype)と[**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype)プロパティ。次のコード例は、これらのプロパティを使用して、さまざまな数の文字列を持つセルを検索する方法を示しています。**始まり**またはで**中心**またはで**終わり**セルの文字列の。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **先行トピック**
- [特定のスタイルで Cells を検索](/cells/ja/net/find-cells-with-specific-style/)
- [セル値が一重引用符で始まるかどうかを確認します](/cells/ja/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [元の値を使用してデータを検索する](/cells/ja/net/search-data-using-original-values/)
