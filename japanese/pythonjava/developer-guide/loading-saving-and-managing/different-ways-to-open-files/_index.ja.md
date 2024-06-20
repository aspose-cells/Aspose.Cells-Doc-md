---
title: ファイルを開くさまざまな方法
type: docs
weight: 10
url: /ja/python-java/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すれば、たとえばデータを取得したり、開発プロセスを高速化するためのデザイナー テンプレートを使用したりするために、ファイルを開くことは簡単です。

{{% /alert %}}

## **パスを介してファイルを開く**

開発者は、*string*としてパスをコンストラクタに指定することで、ローカルコンピュータ上のMicrosoft Excelファイルを開くことができます。Aspose.Cellsは自動的にファイル形式を検出します。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaPath.py" >}}

## **ストリームを介してファイルを開く**

Excelファイルをストリームとして簡単に開くこともできます。ファイルを含む*BufferStream*オブジェクトを使用するオーバーロードされたコンストラクターを使用します。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaStream.py" >}}

## **データのみでファイルを開く**

データのみを含むファイルを開くには、関連する属性とオプションを設定するために、[**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)および[**LoadFilter**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadFilter)クラスを使用して、ロードするテンプレートファイルのクラスの関連属性とオプションを設定してください。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

大規模なスプレッドシートをロードする際に、{0}コンストラクタが*System.OutOfMemoryException*をスローする可能性がかなり高いです。この例外は、利用可能なメモリが不十分であるため、スプレッドシート全体を完全にメモリに読み込むことができず、メモリ設定を有効にしてスプレッドシートをロードする必要があることを示しています。

{{% /alert %}} {{% alert color="primary" %}}

[**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)コンストラクタが大規模なスプレッドシートをロードする際に*System.OutOfMemoryException*をスローする可能性がかなり高いです。この例外は、利用可能なメモリが不足していることを示しており、スプレッドシートを完全にロードするために必要なメモリが不足している可能性があるため、メモリ設定を有効にしてスプレッドシートをロードする必要があります。

{{% /alert %}}
