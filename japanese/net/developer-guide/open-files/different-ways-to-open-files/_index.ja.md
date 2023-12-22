---
title: ファイルを開くさまざまな方法
type: docs
weight: 10
url: /ja/net/different-ways-to-open-files/
description: この記事では、Aspose.Cells for .NET API を使用して Excel ファイルを開く方法を説明します。
keywords: C# Open an Excel file without Excel, How do I open an Excel File.
---
{{% alert color="primary" %}}

Aspose.Cells を使用すると、ファイルを開いてデータを取得したり、デザイナー テンプレートを使用して開発プロセスをスピードアップしたりすることが簡単になります。

{{% /alert %}}

##  **パス経由で Excel ファイルを開く方法**

開発者は、ローカル コンピュータ上のファイル パスを使用して Microsoft Excel ファイルを開くことができます。**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**クラスコンストラクター。コンストラクターにパスを *string* として渡すだけです。 Aspose.Cells はファイル形式の種類を自動的に検出します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

##  **ストリーム経由で Excel ファイルを開く方法**

Excel ファイルをストリームとして開くことも簡単です。これを行うには、コンストラクターのオーバーロードされたバージョンを使用します。*ストリーム*ファイルを含むオブジェクト。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

##  **データのみを含むファイルを開く方法**

データのみを含むファイルを開くには、**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**そして**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**クラスを使用して、ロードするテンプレート ファイルのクラスの関連属性とオプションを設定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

##  **表示されているシートのみをロードする方法**

ロード中、**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**場合によっては、ワークブック内の表示されているワークシートのデータのみが必要な場合があります。 Aspose.Cells を使用すると、ワークブックのロード中に非表示のワークシートのデータをスキップできます。これを行うには、**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**クラスを作成し、そのインスタンスをに渡します**[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)**財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

ここでの実装は、*カスタムロード*上記のスニペットで参照されているクラス。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

Aspose.Cells によって非ネイティブ Excel ファイルまたは他のファイル形式 (PPT/PPTX、DOC/DOCX など) を開こうとすると、例外がスローされます。

{{% /alert %}} {{% alert color="primary" %}}

かなりの確率で、**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**コンストラクターはスローする可能性があります*System.OutOfMemoryException*大きなスプレッドシートをロードしているとき。この例外は、使用可能なメモリがスプレッドシートをメモリに完全にロードするには不十分であることを示しているため、メモリ設定を有効にしてスプレッドシートをロードする必要があります。

{{% /alert %}}
