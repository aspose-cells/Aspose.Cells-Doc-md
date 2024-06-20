---
title: ファイルを開くさまざまな方法
type: docs
weight: 10
url: /ja/net/different-ways-to-open-files/
description: Aspose.Cells for .NET APIを使用してExcelファイルを開く方法を説明します。
keywords: ExcelなしでExcelファイルを開くC#
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すれば、たとえばデータを取得したり、開発プロセスを高速化するためのデザイナー テンプレートを使用したりするために、ファイルを開くことは簡単です。

{{% /alert %}}

## **パスを使用してExcelファイルを開く方法**

開発者は、*string*としてパスをコンストラクタに指定することで、ローカルコンピュータ上のMicrosoft Excelファイルを開くことができます。Aspose.Cellsは自動的にファイル形式を検出します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

## **ストリームを使用してExcelファイルを開く方法**

また、ストリームとしてExcelファイルを開くことも簡単です。ファイルを含む*Stream*オブジェクトを引数に取るコンストラクタのオーバーロードバージョンを使用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

## **データだけを含むファイルを開く方法**

データのみを含むファイルを開くには、関連する属性とオプションを設定するために、[**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)および[**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)クラスを使用して、ロードするテンプレートファイルのクラスの関連属性とオプションを設定してください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

## **表示されているシートのみを読み込む方法**

ワークブック内の表示されているワークシートのデータのみを読み込む際、[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)をロードする際に表示されていないワークシートのデータをスキップする必要がある場合があります。Aspose.Cellsでは、ワークブックを読み込む際に表示されていないワークシートのデータをスキップするため、カスタム関数を作成し、そのインスタンスを[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)プロパティに渡すことができます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

上記のスニペットで参照される*CustomnLoad*クラスの実装はこちらです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

大規模なスプレッドシートをロードする際に、{0}コンストラクタが*System.OutOfMemoryException*をスローする可能性がかなり高いです。この例外は、利用可能なメモリが不十分であるため、スプレッドシート全体を完全にメモリに読み込むことができず、メモリ設定を有効にしてスプレッドシートをロードする必要があることを示しています。

{{% /alert %}} {{% alert color="primary" %}}

[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)コンストラクタが大規模なスプレッドシートをロードする際に*System.OutOfMemoryException*をスローする可能性がかなり高いです。この例外は、利用可能なメモリが不足していることを示しており、スプレッドシートを完全にロードするために必要なメモリが不足している可能性があるため、メモリ設定を有効にしてスプレッドシートをロードする必要があります。

{{% /alert %}}
