---
title: ワークシートを追加または挿入する
type: docs
weight: 20
url: /ja/net/add-or-insert-a-worksheet/
---
{{% alert color="primary" %}} 

このトピックでは、Aspose.Cells.GridDesktop を使用して Excel ファイルにワークシートを追加または挿入する手法について説明します。ワークシートの追加と挿入の違いは、さらに、ワークシートは Excel ファイルのワークシート コレクションの最後に追加されるだけですが、挿入とはワークシート コレクション内の特定の位置にワークシートを追加することを意味します。

{{% /alert %}} 
## **ワークシートの追加**
Aspose.Cells.GridDesktop を使用してワークシートを追加するには、次の手順に従ってください。

1. Aspose.Cells.GridDesktop コントロールをフォームに追加します。
1. GridDesktop コントロールで Worksheet コレクションの Add メソッドを呼び出します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheet.cs" >}}


Add メソッドのオーバーロードされたバージョンが多数用意されています。たとえば、上記のオーバーロードされたバージョンを使用すると、デフォルトのシート名でワークシートが Excel ファイルに追加されます。 Add メソッドの他のオーバーロードされたバージョンを使用すると、以下の例に示すように名前を定義できます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheetWithName.cs" >}}
## **ワークシートの挿入**
Aspose.Cells.GridDesktop を使用してワークシートを挿入するには、次の手順に従ってください。

1. Aspose.Cells.GridDesktop コントロールをフォームに追加します。
1. GridDesktop コントロールで Worksheets コレクションの Insert メソッドを呼び出します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-InsertingWorksheet.cs" >}}

{{% alert color="primary" %}} 

重要: Microsoft Excel (97-2003 XLS) は、最大 65,536 行および 256 列の Excel シートをサポートします。 Aspose.Cells.GridDesktop も同じ基準に従います。 Aspose.Cells.GridDesktop コントロールでは、開発者は標準の制限よりも多くの行と列を持つワークシートを追加または挿入できますが、グリッド データを Excel ファイルに保存しようとすると、例外がスローされます。これは、Aspose.Cells.GridDesktop を使用して 65,536 行 256 列に含まれるデータのみが Excel XLS ファイルに保存できることを意味します。ただし、XLSX (MS Excel 2007/2010) ファイル形式を使用する場合、そのような制限はありません。

{{% /alert %}}
