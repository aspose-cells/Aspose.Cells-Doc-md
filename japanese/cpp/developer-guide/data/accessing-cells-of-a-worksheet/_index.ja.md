---
title: ワークシートの Cells へのアクセス
type: docs
weight: 10
url: /ja/cpp/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

すべてのワークシートには、基本的にセル (ワークシートを構成するセル) に格納されるデータが含まれる可能性があることがわかっています。セルはワークシートの基本部分であり、ワークシート全体を一連の行と列として構築するために使用されます。ワークシートのデータにアクセスする前に、そのセルにアクセスする必要があります。したがって、このトピックでは、Aspose.Cells を使用して実行時にワークシートのセルにアクセスするためのいくつかの基本的なアプローチについて説明します。

{{% /alert %}} 
##  **Cellsにアクセス中**
Aspose.Cells はクラスを提供します[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Excel ファイル内の各ワークシートにアクセスできるようにするコレクション。ワークシートは次のように表されます。[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。の[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスが提供するのは[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)ワークシート内のすべてのセルを表すコレクション。

使用できます[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)ワークシート内のセルにアクセスするためのコレクション。 Aspose.Cells では、ワークシート内のセルにアクセスするための 3 つの基本的なアプローチを提供しています。

1. セル名を使用します。
1. セルの行と列のインデックスを使用します。
1. でのセルインデックスの使用[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクション

{{% alert color="primary" %}} 

番目のアプローチが最も速く、1 番目のアプローチが最も遅いと述べました。各アプローチ間のパフォーマンスの違いは非常に小さいため、どのアプローチを使用してもパフォーマンスの低下を心配する必要はありません。

{{% /alert %}} 
###  **Cell の名前を使用する**
開発者は、セル名を[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)のコレクション[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスをインデックスとして使用します。

開始時に空のワークシートを作成すると、[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションはゼロです。この方法を使用してセルにアクセスすると、このセルがコレクション内に存在するかどうかがチェックされます。 「はい」の場合、コレクション内のセル オブジェクトを返します。それ以外の場合、新しいセル オブジェクトを作成します。[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)オブジェクト、オブジェクトを[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションを作成し、そのオブジェクトを返します。 Microsoft Excel に慣れている場合、このアプローチはセルにアクセスする最も簡単な方法ですが、他のアプローチと比較すると最も遅い方法です。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName-new.cpp" >}}
###  **Cell の行と列のインデックスを使用する**
開発者は、行と列のインデックスをセルに渡すことで、特定のセルにアクセスできます。[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)のコレクション[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。このアプローチは、最初のアプローチと同じように機能します。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell-new.cpp" >}}
##  **ワークシートの最大表示範囲へのアクセス**
Aspose.Cells を使用すると、開発者はワークシートの最大表示範囲にアクセスできます。最大表示範囲 (内容を含む最初のセルと最後のセルの間のセルの範囲) は、ワークシートの内容全体を画像内でコピー、選択、または表示する必要がある場合に便利です。

次を使用してワークシートの最大表示範囲にアクセスできます。[最大表示範囲](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/)の方法[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクション。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet-new.cpp" >}}
