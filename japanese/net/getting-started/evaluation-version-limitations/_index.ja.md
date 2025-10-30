---
title: 評価版の制限
type: docs
weight: 110
url: /ja/net/evaluation-version-limitations/
description: Aspose.Cells for .NET では、購入用の異なるプランを提供したり、Free Trial や評価用の30日間の仮ライセンスを提供したりすることができます。
keywords: 評価版の制限、評価版の開いているファイル数、評価版を使用した評価の途中に表示されるウォーターマーク。
---

## **Aspose.Cellsの評価版を入手する方法**

以下の例を見てください。これは**Aspose.Cells**のNETの評価版をMavenリポジトリの[ダウンロードページ](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells)でダウンロードできます。評価版は、製品のライセンス版とまったく同じ機能を提供します。さらに、評価版は、ライセンスを購入しコードに適用することでライセンス版となります。

**Aspose.Cells**の評価をご満足いただけたら、[ライセンスを購入](https://purchase.aspose.com)してください。提供されている異なるサブスクリプションタイプについて詳しく知ってください。ご質問がある場合は、Asposeの営業チームにご遠慮なくお問い合わせください。

Asposeのライセンスには、新しいバージョンや修正版が登場した場合に1年間の無料アップグレード資格が含まれています。テクニカルサポートは、ライセンスを取得したユーザーと評価ユーザーの両方に対して無料で無制限で提供されます。

## **評価版制限のないAspose.Cellsのテスト方法**

評価版の制限


## **評価版の制限**

ライセンスが指定されていない**Aspose.Cells**製品の評価版は、製品の全機能を提供しますが、1つのプログラムで100ファイルを開くことと評価用ウォーターマークが追加されるワークシートが制限されています。

制限は以下の通りです:

### **制限は以下の通りです:**

1つ目の制限：開いたファイルの数

### **プログラムを実行する際に、Excelファイルを100個しか開くことができません。アプリケーションがこの数を超えると、例外がスローされます。**
2つ目の制限：評価ウォーターマークの付いたワークシート
<br>
<image src="1.png" width="70%" />
<br>

### **3つ目の制限: 評価情報が追加されたプレーンテキスト**
Aspose.Cellsの出力プレーンテキストファイルには、評価情報がドキュメントの最後に追加されます。ファイルをプレーンテキスト（CSVやTSV形式など）として保存する場合は、最初のワークシートの内容のみ出力されます。
<br>
<image src="2.png" width="70%" />
<br>

### **4つ目の制限: 評価用ウォーターマークが追加されたPDFおよびイメージ**
Aspose.CellsによるPDFまたは画像ファイルには、評価用の透かし文字が文書/画像の上部に貼り付けられます。これはGridWebコントロールにおいても評価著作権の警告（追加のワークシート）を非表示にすることはできません、常に（ワークシートタブの）最後に追加されます。
<br>
<image src="3.png" width="70%" />
<br>

### **5つ目の制限: 設定ファイル設定（Aspose.Cells.GridWeb）**
次のコード行を構成セクションに追加してスクリプトパスを再指定することはできません（例えば、web.configファイル内）。acw_clientは内部構成を管理するために使用されます。組み込みのクライアントリソース（画像、スクリプトなど）の使用を制御するために、configファイルを使用します。また、web.configファイル内のこの構成設定は、コントロールのライセンス版でのみ効果を発揮します。

**XML**
{{< highlight csharp >}}
<appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

Aspose.Cells.GridWebコントロールをファイルシステムWebサイトやMS Ajax拡張などで使用している場合、これらの設定は場合によっては必須です。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
