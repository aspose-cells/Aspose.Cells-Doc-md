---
title: Excel ファイルを開く
type: docs
weight: 10
url: /ja/net/opening-an-excel-file/
---
{{% alert color="primary" %}} 

Aspose.Cells Grid Suite のユニークな機能は、Excel ファイルとの互換性です。このトピックでは、ユーザーが Aspose.Cells.GridDesktop コントロールを使用して Windows アプリケーションで Excel ファイルを開く方法を示します。

{{% /alert %}} 
## **序章**
 Aspose.Cells.GridDesktop を使用して Excel ファイルを開くには、GridDesktop コントロールを含むデスクトップ アプリケーションを作成する必要があります。 Aspose.Cells.GridDesktop コントロールを Windows フォームに追加する方法がわからない場合は、以下を参照してください。[Aspose.Cells.GridDesktop の使い方](/cells/ja/net/how-to-use-aspose-cells-griddesktop/)

Aspose.Cells.GridDesktop は、Excel ファイルを開くための次の 3 つの異なる方法を提供します。

1. **ファイルから開く**
1. **CSV ファイルを開く**
1. **ストリームから開く**
## **Excelファイルを開く**
この例では、デスクトップ アプリケーションを作成し、次の操作を行います。

- 1 つの GridControl コントロールをフォームに追加します。
- テキスト プロパティが次のように設定された 3 つのボタンを追加します。
  - **Excelファイルを開く**
  - **CSV ファイルを開く**
  - **ストリームから開く**
### **ファイルから開く**
Excel ファイルから Aspose.Cells.GridDesktop コントロールにコンテンツをロードするには、コントロールのメソッドを呼び出して、Excel ファイルのパスを指定する必要があります。その後、Aspose.Cells.GridDesktop コントロールは、指定されたパスからファイルを自動的に検索し、その内容を表示します。次の例は、Excel ファイルの内容を読み込むためのコード スニペットを示しています。の Click イベントを作成します。**Excelファイルを開く**ボタンをクリックして、その中に次のコードを貼り付けます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}


上記のコード スニペットは、開発者が任意の方法で使用できます。たとえば、Windows フォームの読み込み時に Excel ファイルを自動的に読み込みたい場合は、フォームの Load イベントの下にこのコードを追加できます。
### **CSV ファイルを開く**
Aspose.Cells.GridDesktop コントロールは、CSV ファイルの読み込みもサポートします。の Click イベントを作成します。**CSV ファイルを開く**ボタンをクリックして、その中に次のコードを貼り付けます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}
### **ストリームから開く**
上記の説明では、ファイル パスを使用して Excel ファイルを読み込むことについて説明しましたが、Aspose.Cells.GridDesktop コントロールは、ストリームからの Excel ファイルの読み込みもサポートしています。の Click イベントを作成します。**ストリームから開く**ボタンをクリックして、その中に次のコードを貼り付けます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}



ファイルをストリームとして使用することは、ストリームを閉じることによってファイルへのすべての接続を確実に閉じることができるため、あらゆる種類のファイル アクセスまたは共有違反の問題を防止するためのより良い方法です。

{{% alert color="primary" %}} 

重要: 重要な点は、Aspose.Cells.GridDesktop コントロールにも LoadFromExcel という名前のメソッドが含まれていることです。このメソッドは、Excel ファイルの内容をグリッドにロードするためにも使用されます。しかし、この方法は現在廃止されています。したがって、すべての開発者は、廃止されたメソッドよりも堅牢で効率的な ImportExcelFile メソッドを使用することをお勧めします。

{{% /alert %}}
