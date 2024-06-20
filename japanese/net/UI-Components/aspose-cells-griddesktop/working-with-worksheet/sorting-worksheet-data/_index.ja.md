---
title: ワークシートデータのソート
type: docs
weight: 80
url: /ja/net/aspose-cells-griddesktop/sorting-worksheet-data/
keywords: GridDesktop,ソート,データのソート,データソート
description: この記事では、GridDesktop でワークシート内のデータをソートする方法について紹介します。
---

{{% alert color="primary" %}} 

ソートは、データ処理時にほとんどの場合使用する重要な日常的なタスクです。このトピックでは、シンプルな例を使って、ワークシートでデータをソートする方法について説明します。

{{% /alert %}} 
## **ワークシートデータのソート**
Aspose.Cells.GridDesktop の API を使用してワークシート内のデータをソートするには、以下の手順に従ってください:

- まず、**CellRange** のグローバルオブジェクトを作成し、クラスのスコープ内でいつでもアクセスできるようにします
- **GridDesktop** の **SelectedCellRangeChanged** イベントのイベントハンドラを作成します。**SelectedCellRangeChanged** イベントは、ユーザーによって選択されたセルの範囲が変更されるたびにトリガーされます。たとえば、ユーザーがデータを含むセルを選択した場合、その選択範囲が変更されるたびにこのイベントがトリガーされます。
- イベントハンドラは **CellRange** オブジェクトを提供し、このオブジェクトはユーザーによって選択されたセルの更新された範囲を提供します。したがって、このイベントハンドラ内で、この更新されたセル範囲をグローバル **CellRange** オブジェクトに割り当てます。これにより、コードの他の部分でもそれを使用できるようになります。セル範囲を失わないようにするために、イベントハンドラコードを条件の中に記述します
- これでワークシートデータをソートするコードを記述できます。まず、所望のワークシートにアクセスします
- データをソートするセルの範囲を保持する **SortRange** オブジェクトを作成します。**SortRange** のコンストラクタでは、ワークシート、開始行と列のインデックス、ソートする行数と列数、ソートの方向（上から下へまたは左から右へなど）などを指定できます。
- ここで、**SortRange** オブジェクトの **Sort** メソッドを呼び出してデータをソートします。**Sort** メソッドでは、ソートする列または行のインデックス、ソートの順序（**昇順** または **降順** など）を指定できます
- 最後に、**GridDesktop** の **Invalidate** メソッドを呼び出してセルを再描画します。

以下の例では、列内のデータをソートする方法について示しています。

**CellRange** のグローバルオブジェクトと **GridDesktop** の **SelectedCellRangeChanged** イベントを作成します。以下のコードを記述します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-CheckingCellRange.cs" >}}


さて、**昇順ソート**メソッドを記述します。**昇順ソート**のボタンを作成し、その**Click**イベント内に以下のコードを記述します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-AscendingSort.cs" >}}


最後に、**降順ソート**機能を実現するためのコードを記述します。**降順ソート**ボタンを作成し、その**Click**イベント内に以下のコードを記述します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-DescendingSort.cs" >}}
