---
title: ワークシートのセルへのアクセス
type: docs
weight: 10
url: /ja/cpp/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

すべてのワークシートには基本的にセル（ワークシートが構成されている）に格納されているデータが含まれることを知っています。セルはワークシートの基本部分であり、ワークシート全体を行と列の連続として構築するために使用されます。ワークシートからデータにアクセスしようとする前に、そのセルにアクセスする必要があります。したがって、このトピックでは、Aspose.Cellsを使用して実行時にワークシートのセルにアクセスするための基本的なアプローチについて説明します。

{{% /alert %}} 
## **セルへのアクセス**
Aspose.CellsはExcelファイルを表す[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスを提供します。 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには、Excelファイル内の各ワークシートにアクセスすることを可能にする[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションが含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスによって表されます。 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、ワークシート内のすべてのセルを表す[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションを提供しています。

[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションを使用してワークシート内のセルにアクセスすることができます。Aspose.Cellsでは、ワークシート内のセルにアクセスするための3つの基本的なアプローチを提供しています：

1. セル名を使用します。
1. セルの行と列のインデックスを使用します。
1. [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクション内のセルインデックスを使用します。

{{% alert color="primary" %}} 

3番目のアプローチが最速であり、1番目のアプローチが最も遅いことを述べました。アプローチ間のパフォーマンスの違いは非常に小さいため、使用するアプローチに関してはパフォーマンスの低下を心配する必要はありません。

{{% /alert %}} 
### **セル名の使用**
開発者は、[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスの[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションにセル名をインデックスとして渡すことで、任意の特定のセルにアクセスできます。

最初に空白のワークシートを作成すると、[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションの数はゼロになります。このアプローチを使用してセルにアクセスする場合、このセルがコレクション内に存在するかどうかをチェックします。はいの場合は、コレクション内のセルオブジェクトを返し、さもなければ新しい[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)オブジェクトを作成し、そのオブジェクトを[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションに追加してからそのオブジェクトを返します。このアプローチは、Microsoft Excelに精通している場合にセルにアクセスするための最も簡単な方法ですが、他のアプローチと比較して最も遅いアプローチです。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName-new.cpp" >}}
### **セルの行と列のインデックスの使用**
開発者は、[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスの[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションにセルの行と列のインデックスを渡すことで、任意の特定のセルにアクセスできます。このアプローチは、第1のアプローチと同じ方法で機能します。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell-new.cpp" >}}
## **ワークシートの最大表示範囲へのアクセス**
Aspose.Cellsを使用すると、開発者はワークシートの最大表示範囲にアクセスできます。最大表示範囲（内容を持つ最初のセルと最後のセルの間のセル範囲）は、ワークシート全体の内容を画像でコピー、選択、表示する必要がある場合に便利です。

ワークシートの最大表示範囲には、[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/)メソッドを使用してアクセスできます。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet-new.cpp" >}}
