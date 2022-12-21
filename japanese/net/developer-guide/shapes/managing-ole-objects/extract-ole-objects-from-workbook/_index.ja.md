---
title: ブックから OLE オブジェクトを抽出する
type: docs
weight: 110
url: /ja/net/extract-ole-objects-from-workbook/
---
{{% alert color="primary" %}}

場合によっては、ブックから OLE オブジェクトを抽出する必要があります。 Aspose.Cells は、これらの Ole オブジェクトの抽出と保存をサポートしています。

この記事では、Visual Studio.Net でコンソール アプリケーションを作成し、数行の単純なコードを使用してブックからさまざまな OLE オブジェクトを抽出する方法を示します。

{{% /alert %}}

## **ブックから OLE オブジェクトを抽出する**

### **テンプレート ワークブックの作成**

1. Microsoft Excel でワークブックを作成しました。
1. 最初のワークシートに Microsoft Word ドキュメント、Excel ワークブック、および PDF ドキュメントを OLE オブジェクトとして追加します。

|**OLE オブジェクトを含むテンプレート ドキュメント (OleFile.xls)**|
|:- |
|![todo:画像_代替_文章](extract-ole-objects-from-workbook_1.png)|

次に、OLE オブジェクトを抽出し、それぞれのファイル タイプでハード ディスクに保存します。

### **Aspose.Cells をダウンロードしてインストールします**

1. [ダウンロード Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. 開発用コンピューターにインストールします。

Aspose コンポーネントはすべて、インストールすると評価モードで動作します。評価モードには時間制限がなく、生成されたドキュメントに透かしを挿入するだけです。

### **プロジェクトを作成する**

始める**Visual Studio.Net**新しいコンソール アプリケーションを作成します。この例では C# コンソール アプリケーションを示していますが、VB.NET も使用できます。

1. 参照を追加
 1. Aspose.Cells コンポーネントへの参照をプロジェクトに追加します。たとえば、...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll への参照を追加します。

### **OLE オブジェクトを抽出する**

以下のコードは、OLE オブジェクトを見つけて抽出する実際の作業を行います。 OLE オブジェクト (DOC、XLS、および PDF ファイル) がディスクに保存されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExtractOLEObjects-1.cs" >}}
