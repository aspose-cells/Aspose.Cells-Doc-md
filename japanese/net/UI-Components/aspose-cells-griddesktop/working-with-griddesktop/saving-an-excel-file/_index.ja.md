---
title: Excel ファイルの保存
type: docs
weight: 20
url: /ja/net/saving-an-excel-file/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop コントロールを使用すると、ユーザーは新しい Excel ファイルを作成できるだけでなく、既存のファイルを管理することもできます。ただし、どちらの場合も、Aspose.Cells.GridDesktop の内容を保存する必要があります。したがって、これは、グリッドの内容を Excel ファイルとして保存する方法をユーザーに知らせるために、現在私たちが議論しているトピックです。

{{% /alert %}} 
## **序章**
Aspose.Cells.GridDesktop コントロールの内容を Excel ファイルとして保存するために、Aspose.Cells.GridDesktop は次のメソッドを提供します。

1. **ファイルとして保存する**
1. **ストリームとして保存**
## **ファイルの保存**
デスクトップ アプリケーションを作成し、GridControl コントロールを含む 2 つのボタンをフォームに追加します。ボタンのテキスト プロパティを次のように設定します。**ファイルとして保存**と**ストリームとして保存**それぞれ。
### **ファイルとして保存する**
の Click イベントを作成します。**ファイルとして保存**ボタンをクリックして、その中に次のコードを貼り付けます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingAFile.cs" >}}

{{% alert color="primary" %}} 

重要: 重要な点は、Aspose.Cells.GridDesktop コントロールには SaveToExcel という名前のメソッドも含まれていることです。このメソッドは、Excel ファイルの内容をグリッドにロードするためにも使用されます。しかし、この方法は現在廃止されています。したがって、すべての開発者は、廃止されたものよりも堅牢で効率的な ExportExcelFile メソッドを使用することをお勧めします。

{{% /alert %}} 
### **ストリームとして保存**
場合によっては、開発者がグリッド コンテンツをストリーム (たとえば、MemoryStream) に保存する必要がある場合があります。このタスクを容易にするために、Aspose.Cells.GridDesktop コントロールは、グリッド データのストリームへの保存もサポートしています。の Click イベントを作成します。**ストリームとして保存**ボタンをクリックして、その中に次のコードを貼り付けます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingUsingStream.cs" >}}

{{% alert color="primary" %}} 

重要: Microsoft Excel のサポート Excel シートには、最大 65,536 行と 256 列を含めることができます。 Aspose.Cells.GridDesktop も同じ基準に従っています。 Aspose.Cells.GridDesktop コントロールでは、開発者は標準の制限よりも多くの行と列を作成できますが、グリッド データを Excel ファイルに保存すると、例外がスローされます。これは、Aspose.Cells.GridDesktop を使用して、65,536 行 256 列に含まれるデータのみを Excel ファイルに保存できることを意味します。

{{% /alert %}}
