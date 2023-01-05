---
title: ワークシートの Cells へのアクセス
type: docs
weight: 10
url: /ja/net/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}}

すべてのワークシートには、基本的にセル (ワークシートを構成するセル) に格納されているデータが含まれている可能性があることがわかっています。セルは、一連の行と列としてワークシート全体を構築するために使用されるワークシートの基本的な部分です。ワークシートからデータにアクセスする前に、そのセルにアクセスする必要があります。したがって、このトピックでは、実行時に Aspose.Cells を使用してワークシート セルにアクセスするための基本的な方法について説明します。

{{% /alert %}}

## **Cellsにアクセス**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)これは Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート コレクション**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)ワークシート内のすべてのセルを表すコレクション。

使用できます[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)ワークシートのセルにアクセスするためのコレクション。 Aspose.Cells は、ワークシート内のセルにアクセスするための 3 つの基本的な方法を提供します。

1. セル名の使用。
1. セルの行と列のインデックスを使用します。
1. でのセル インデックスの使用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション

**重要：** 番目のアプローチが最も速く、1 番目のアプローチが最も遅いと述べました。アプローチ間のパフォーマンスの違いは非常に小さいため、どちらのアプローチを使用してもパフォーマンスの低下を心配する必要はありません。

### **Cell名を使用**

開発者は、セル名を[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)のコレクション[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)インデックスとしてのクラス。

最初に空白のワークシートを作成すると、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションはゼロです。このアプローチを使用してセルにアクセスすると、このセルがコレクションに存在するかどうかがチェックされます。はいの場合、コレクション内のセル オブジェクトを返します。それ以外の場合は、新しいセル オブジェクトを作成します。[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)オブジェクト、オブジェクトを[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションを作成し、オブジェクトを返します。このアプローチは、Microsoft Excel に慣れている場合にセルにアクセスする最も簡単な方法ですが、他のアプローチと比較して最も遅い方法です。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

### **Cell の行と列のインデックスを使用する**

開発者は、行と列のインデックスを[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)のコレクション[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。

このアプローチは、最初のアプローチと同じように機能します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

### **Cells コレクションでの Cell インデックスの使用**

セルの数値インデックスを[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション。

このアプローチを使用してセルにアクセスすると、セルの数値インデックスが範囲外の場合に例外がスローされる可能性があります。このアプローチは、セルにアクセスするための最速のアプローチですが、知っておくべき重要なことは、このアプローチを使用してセル オブジェクトにアクセスする場合、新しいセルがオブジェクトに追加された後に数値インデックスが変更される可能性があることです。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション。のセル オブジェクト[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションは行インデックスと列インデックスで内部的にソートされます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

## **ワークシートの最大表示範囲へのアクセス**

Aspose.Cells を使用すると、開発者はワークシートの最大表示範囲にアクセスできます。最大表示範囲 (内容のある最初のセルと最後のセルの間のセルの範囲) は、ワークシートの内容全体をイメージでコピー、選択、または表示する必要がある場合に役立ちます。

を使用して、ワークシートの最大表示範囲にアクセスできます。[**Worksheet.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) .次のサンプル コードは、[**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
