---
title: ワークシートの Cells へのアクセス
type: docs
weight: 10
url: /ja/net/accessing-cells-of-a-worksheet/
description: この記事では、ワークシートの最大表示範囲を取得し、Aspose.Cells for .NET API を通じてセルにアクセスする方法を説明します。
keywords: Get Cell object, Access Cells, Get maximum display range of worksheet. 
---
{{% alert color="primary" %}}

すべてのワークシートには、基本的にセル (ワークシートを構成するセル) に格納されるデータが含まれる可能性があることがわかっています。セルはワークシートの基本部分であり、ワークシート全体を一連の行と列として構築するために使用されます。ワークシートのデータにアクセスする前に、そのセルにアクセスする必要があります。したがって、このトピックでは、Aspose.Cells を使用して実行時にワークシートのセルにアクセスするためのいくつかの基本的なアプローチについて説明します。

{{% /alert %}}

##  **Cellsへのアクセス方法**

Aspose.Cells はクラスを提供します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシートコレクション**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)これにより、Excel ファイル内の各ワークシートにアクセスできるようになります。ワークシートは次のように表されます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供するのは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)ワークシート内のすべてのセルを表すコレクション。

使用できます[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)ワークシート内のセルにアクセスするためのコレクション。 Aspose.Cells では、ワークシート内のセルにアクセスするための 3 つの基本的なアプローチを提供しています。

1. セル名を使用します。
1. セルの行と列のインデックスを使用します。
1. でのセルインデックスの使用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション

**重要：** 番目のアプローチが最も速く、1 番目のアプローチが最も遅いと述べました。各アプローチ間のパフォーマンスの違いは非常に小さいため、どのアプローチを使用してもパフォーマンスの低下を心配する必要はありません。

###  **Cell 名前で Cell オブジェクトを取得する方法**

開発者は、セル名を[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)のコレクション[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスをインデックスとして使用します。

最初に空のワークシートを作成すると、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションはゼロです。この方法を使用してセルにアクセスすると、このセルがコレクション内に存在するかどうかがチェックされます。 「はい」の場合、コレクション内のセル オブジェクトを返します。それ以外の場合、新しいセル オブジェクトを作成します。[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)オブジェクト、オブジェクトを[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションを取得してオブジェクトを返します。 Microsoft Excel に慣れている場合、このアプローチはセルにアクセスする最も簡単な方法ですが、他のアプローチと比較すると最も遅い方法です。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

###  **Cellの行と列のインデックスからCellオブジェクトを取得する方法**

開発者は、行と列のインデックスをセルに渡すことで、特定のセルにアクセスできます。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)のコレクション[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。

このアプローチは、最初のアプローチと同じように機能します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

###  **Cells コレクションの Cell インデックスによって Cell オブジェクトを取得する方法**

セルの数値インデックスを[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション。

この方法を使用してセルにアクセスすると、セルの数値インデックスが範囲外の場合に例外がスローされる可能性があります。この方法はセルにアクセスするのに最も速い方法ですが、この方法を使用してセル オブジェクトにアクセスすると、新しいセルがセルに追加された後に数値インデックスが変更される可能性があることを知っておくことが重要です。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション。のセル オブジェクト[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションは行と列のインデックスによって内部的に並べ替えられます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

##  **ワークシートの最大表示範囲を取得する方法**

Aspose.Cells を使用すると、開発者はワークシートの最大表示範囲にアクセスできます。最大表示範囲 (内容を含む最初のセルと最後のセルの間のセルの範囲) は、ワークシートの内容全体を画像内でコピー、選択、または表示する必要がある場合に便利です。

次を使用してワークシートの最大表示範囲にアクセスできます。[**Worksheet.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) 。次のサンプル コードは、[**最大表示範囲**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
