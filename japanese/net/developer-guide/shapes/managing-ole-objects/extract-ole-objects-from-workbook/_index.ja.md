---
title: ワークブックからOLEオブジェクトを抽出
type: docs
weight: 110
url: /ja/net/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}

時には、ブックからOLEオブジェクトを抽出する必要があります。Aspose.CellsはこれらのOLEオブジェクトを抽出して保存する機能をサポートしています。

この記事は、少数のコード行でVisual Studio.Netでコンソールアプリケーションを作成し、ワークブックから異なるOLEオブジェクトを抽出する方法を示しています。

{{% /alert %}}

## **ワークブックからOLEオブジェクトを抽出**

### **テンプレートワークブックの作成**

1. Microsoft Excelでワークブックを作成しました。
1. 最初のワークシートにMicrosoft Wordドキュメント、Excelワークブック、PDFドキュメントをOLEオブジェクトとして追加しました。

|**OLEオブジェクトを含むテンプレートドキュメント（OleFile.xls）**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

次に、OLEオブジェクトを抽出し、それらをそれぞれのファイルタイプでハードディスクに保存します。

### **Aspose.Cellsをダウンロードしてインストールする**

1. [ダウンロード Aspose.Cells for .NET](https://downloads.aspose.com/cells/net)。
1. 開発コンピュータにインストールします。

すべてのAsposeのコンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限はなく、生成された文書にウォーターマークを注入するだけです。

### **プロジェクトを作成する**

Visual Studio.Netを起動し、新しいコンソールアプリケーションを作成します。この例ではC#コンソールアプリケーションを示しますが、VB.NETも利用できます。

1. 参照を追加
   1. プロジェクトにAspose.Cellsコンポーネントの参照を追加します。たとえば、...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dllに参照を追加します。

### **OLE オブジェクトの抽出**

以下のコードは実際にOLEオブジェクトを検出して抽出する実際の作業を行います。OLEオブジェクト（DOC、XLS、PDFファイル）はディスクに保存されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExtractOLEObjects-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
