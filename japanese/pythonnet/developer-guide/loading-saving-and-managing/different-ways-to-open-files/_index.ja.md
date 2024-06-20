---
title: ファイルを開くさまざまな方法
type: docs
weight: 10
url: /ja/python-net/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すれば、たとえばデータを取得したり、開発プロセスを高速化するためのデザイナー テンプレートを使用したりするために、ファイルを開くことは簡単です。

{{% /alert %}}

## **パスを介してファイルを開く**

開発者は、**Workbook**クラスのコンストラクターでfile_pathを指定することで、ローカルコンピューター上のMicrosoft Excelファイルを開くことができます。コンストラクターにパスを*string*として渡すだけです。Aspose.Cellsは自動的にファイル形式を検出します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaPath.py" >}}

## **ストリームを介してファイルを開く**

Excelファイルをストリームとして簡単に開くこともできます。ファイルを含む*BufferStream*オブジェクトを使用するオーバーロードされたコンストラクターを使用します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaStream.py" >}}

## **データのみでファイルを開く**

データのみでファイルを開くには、**LoadOptions**および**LoadFilter**クラスを使用して、テンプレートファイルの関連属性とオプションを設定します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

大規模なスプレッドシートをロードする際に、{0}コンストラクタが*System.OutOfMemoryException*をスローする可能性がかなり高いです。この例外は、利用可能なメモリが不十分であるため、スプレッドシート全体を完全にメモリに読み込むことができず、メモリ設定を有効にしてスプレッドシートをロードする必要があることを示しています。

{{% /alert %}} {{% alert color="primary" %}}

**Workbook**のコンストラクターが大きなスプレッドシートを完全に読み込むための十分なメモリがないことを示す*System.OutOfMemoryException*をスローする可能性があります。これは利用可能なメモリが不十分であることを示唆し、スプレッドシートを完全に読み込むためにはメモリが有効になっている必要があるためです。

{{% /alert %}}
