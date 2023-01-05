---
title: ファイルを開くさまざまな方法
type: docs
weight: 10
url: /ja/net/different-ways-to-open-files/
---
{{% alert color="primary" %}}

Aspose.Cells を使用すると、ファイルを開いてデータを取得したり、デザイナー テンプレートを使用して開発プロセスをスピードアップしたりすることが簡単になります。

{{% /alert %}}

## **パス経由でファイルを開く**

開発者は、ローカル コンピューター上のファイル パスを使用して Microsoft Excel ファイルを開くことができます。**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**クラス コンストラクタ。コンストラクターにパスを渡すだけです。*ストリング*Aspose.Cells は、ファイル形式の種類を自動的に検出します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

## **ストリーム経由でファイルを開く**

Excel ファイルをストリームとして開くのも簡単です。これを行うには、コンストラクターのオーバーロードされたバージョンを使用します。*ストリーム*ファイルを含むオブジェクト。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

## **データのみのファイルを開く**

データのみのファイルを開くには、**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**と**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**classes を使用して、ロードするテンプレート ファイルの関連する属性とクラスのオプションを設定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

## **表示されているシートのみを読み込んでいます**

読み込み中**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**ワークブック内の表示可能なワークシートのデータのみが必要な場合があります。 Aspose.Cells を使用すると、ワークブックの読み込み中に非表示のワークシートのデータをスキップできます。これを行うには、**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**クラスにそのインスタンスを渡します**[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)**財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

これがの実装です*CustomnLoad*上記のスニペットで参照されているクラス。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

Aspose.Cells までにネイティブでない Excel ファイルまたはその他のファイル形式 (PPT/PPTX、DOC/DOCX など) を開こうとすると、例外がスローされます。

{{% /alert %}} {{% alert color="primary" %}}

かなりの可能性があります**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**コンストラクターがスローする可能性があります*System.OutOfMemoryException*大きなスプレッドシートの読み込み中。この例外は、スプレッドシートをメモリに完全にロードするには使用可能なメモリが不足していることを示しているため、メモリ設定を有効にしてスプレッドシートをロードする必要があります。

{{% /alert %}}
