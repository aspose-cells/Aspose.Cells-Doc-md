---
title: ワークシートの追加または挿入
type: docs
weight: 20
url: /ja/net/aspose-cells-griddesktop/add-or-insert-a-worksheet/
keywords: GridDesktop、挿入、ワークシート、ワークシートの挿入
description: この記事では、GridDesktopにワークシートを追加または挿入する方法について紹介します。
---

{{% alert color="primary" %}} 

このトピックでは、Aspose.Cells.GridDesktopを使用してExcelファイルにワークシートを追加または挿入する技術について説明します。追加と挿入の違いは、追加は単にワークシートがExcelファイルのワークシートコレクションの末尾に追加されるという点ですが、挿入はワークシートをワークシートコレクション内の特定の位置に追加することを意味します。

{{% /alert %}} 
## **ワークシートの追加**
Aspose.Cells.GridDesktopを使用してワークシートを追加するには、次の手順に従ってください。

1. フォームにAspose.Cells.GridDesktopコントロールを追加します。
1. GridDesktopコントロールのワークシートコレクションのAddメソッドを呼び出します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheet.cs" >}}


多くのオーバーロードされたAddメソッドのバージョンが利用可能です。上記のオーバーロードされたバージョンを使用すると、たとえば、ワークシートがデフォルトのシート名でExcelファイルに追加されます。Addメソッドの他のオーバーロードされたバージョンを使用すると、次に示すように名前を定義することができます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheetWithName.cs" >}}
## **ワークシートの挿入**
Aspose.Cells.GridDesktopを使用してワークシートを挿入するには、次の手順に従ってください。

1. Aspose.Cells.GridDesktopコントロールをフォームに追加します。
1. GridDesktopコントロールのワークシートコレクションのInsertメソッドを呼び出します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-InsertingWorksheet.cs" >}}

{{% alert color="primary" %}} 

重要: Microsoft Excel（97-2003 XLS）は、最大65,536行および256列のExcelシートをサポートしています。Aspose.Cells.GridDesktopも同じ基準に従います。Aspose.Cells.GridDesktopコントロールでは、標準制限を超えた行数や列数のワークシートを追加または挿入できますが、GridデータをExcelファイルに保存しようとすると例外がスローされます。つまり、Aspose.Cells.GridDesktopを使用してExcel XLSファイルに保存できるのは、65,536行と256列に含まれるデータだけであり、XLSX（MS Excel 2007/2010）ファイル形式を使用する場合は、そのような制限はありません。

{{% /alert %}}
