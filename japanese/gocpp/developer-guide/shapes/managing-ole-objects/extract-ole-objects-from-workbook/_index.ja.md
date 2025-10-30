---
title: Golangを使用したC++でワークブックからOLEオブジェクトを抽出
linktitle: ワークブックからOLEオブジェクトを抽出
type: docs
weight: 110
url: /ja/go-cpp/extract-ole-objects-from-workbook/
description: Aspose.Cellsを使ってGolangを用いたC++によるワークブックからOLEオブジェクトを抽出する方法を学ぶ
---

{{% alert color="primary" %}}

時には、ワークブックからOLEオブジェクトを抽出する必要があります。Aspose.CellsはこれらのOLEオブジェクトの抽出と保存をサポートしています。

このガイドでは、Visual Studioでコンソールアプリケーションを作成し、少ないコード行数でワークブックからさまざまなOLEオブジェクトを抽出する方法を示します。

{{% /alert %}}

## **ワークブックからOLEオブジェクトを抽出**

### **テンプレートワークブックの作成**

1. Microsoft Excelでワークブックを作成します。
1. 最初のシートにOLEオブジェクトとしてMicrosoft Wordドキュメント、Excelワークブック、およびPDFドキュメントを追加します。

|**OLEオブジェクトを含むテンプレートドキュメント（OleFile.xls）**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

次に、OLEオブジェクトを抽出し、それぞれのファイルタイプでハードディスクに保存します。

### **Aspose.Cellsをダウンロードしてインストールする**

1. [Aspose.Cells for C++をダウンロード](https://downloads.aspose.com/cells/go-cpp/)。
1. 開発コンピュータにインストールします。

すべてのAsposeのコンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限はなく、生成された文書にウォーターマークを注入するだけです。

### **プロジェクトを作成する**

**Visual Studio**を起動し、新しいコンソールアプリケーションを作成します。この例はC++のコンソールアプリケーションです。

1. 参照を追加
   1. プロジェクトにAspose.Cellsコンポーネントを参照として追加します。例えば、...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dllに参照を追加します。

### **OLE オブジェクトの抽出**

以下のコードは、OLEオブジェクト（DOC、XLS、PDFファイル）を検索し抽出し、ディスクに保存します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractOleObjectsFromWorkbook.go" >}}
