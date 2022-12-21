---
title: ワークシートの Cells へのアクセス
type: docs
weight: 10
url: /ja/cpp/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

すべてのワークシートには、基本的にセル (ワークシートを構成するセル) に格納されているデータが含まれている可能性があることがわかっています。セルは、一連の行と列としてワークシート全体を構築するために使用されるワークシートの基本的な部分です。ワークシートからデータにアクセスする前に、そのセルにアクセスする必要があります。したがって、このトピックでは、実行時に Aspose.Cells を使用してワークシート セルにアクセスするための基本的な方法について説明します。

{{% /alert %}} 
## **Cellsにアクセス**
Aspose.Cells はクラスを提供します[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)これは Excel ファイルを表します。の[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)クラスには[ワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス。の[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラスは[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)ワークシート内のすべてのセルを表すコレクション。

使用できます[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)ワークシートのセルにアクセスするためのコレクション。 Aspose.Cells は、ワークシート内のセルにアクセスするための 3 つの基本的な方法を提供します。

1. セル名の使用。
1. セルの行と列のインデックスを使用します。
1. でのセル インデックスの使用[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクション

{{% alert color="primary" %}} 

番目のアプローチが最も速く、1 番目のアプローチが最も遅いと述べました。アプローチ間のパフォーマンスの違いは非常に小さいため、どちらのアプローチを使用してもパフォーマンスの低下を心配する必要はありません。

{{% /alert %}} 
### **Cell名を使用**
開発者は、セル名を[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)のコレクション[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)インデックスとしてのクラス。

開始時に空白のワークシートを作成すると、[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクションはゼロです。このアプローチを使用してセルにアクセスすると、このセルがコレクションに存在するかどうかがチェックされます。はいの場合、コレクション内のセル オブジェクトを返します。それ以外の場合は、新しいセル オブジェクトを作成します。[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)オブジェクト、オブジェクトを[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクションを作成し、そのオブジェクトを返します。このアプローチは、Microsoft Excel に慣れている場合にセルにアクセスする最も簡単な方法ですが、他のアプローチと比較して最も遅い方法です。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName.cpp" >}}
### **Cell の行と列のインデックスを使用する**
開発者は、行と列のインデックスを[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)のコレクション[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス。このアプローチは、最初のアプローチと同じように機能します。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell.cpp" >}}
## **ワークシートの最大表示範囲へのアクセス**
Aspose.Cells を使用すると、開発者はワークシートの最大表示範囲にアクセスできます。最大表示範囲 (内容のある最初のセルと最後のセルの間のセルの範囲) は、ワークシートの内容全体を画像でコピー、選択、または表示する必要がある場合に役立ちます。

を使用して、ワークシートの最大表示範囲にアクセスできます。[MaxDisplayIRange](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad351277ccaa0a4e1e8cd0693a1e2e988)の方法[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクション。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet.cpp" >}}
