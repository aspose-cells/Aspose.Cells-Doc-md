---
title: ファイルを開くさまざまな方法
type: docs
weight: 10
url: /ja/python-net/different-ways-to-open-files/
---
{{% alert color="primary" %}}

Aspose.Cells を使用すると、ファイルを開いてデータを取得したり、デザイナー テンプレートを使用して開発プロセスをスピードアップしたりすることが簡単になります。

{{% /alert %}}

## **パス経由でファイルを開く**

開発者は、ローカル コンピューター上のファイル パスを使用して Microsoft Excel ファイルを開くことができます。**ワークブック**クラス コンストラクタ。コンストラクターにパスを渡すだけです。*ストリング*Aspose.Cells は、ファイル形式の種類を自動的に検出します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaPath.py" >}}

## **ストリーム経由でファイルを開く**

Excel ファイルをストリームとして開くのも簡単です。これを行うには、コンストラクターのオーバーロードされたバージョンを使用します。*バッファストリーム*ファイルを含むオブジェクト。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaStream.py" >}}

## **データのみのファイルを開く**

データのみのファイルを開くには、**読み込みオプション**と**LoadFilter**classes を使用して、ロードするテンプレート ファイルの関連する属性とクラスのオプションを設定します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Aspose.Cells までにネイティブでない Excel ファイルまたはその他のファイル形式 (PPT/PPTX、DOC/DOCX など) を開こうとすると、例外がスローされます。

{{% /alert %}} {{% alert color="primary" %}}

かなりの可能性があります**ワークブック**コンストラクターがスローする可能性があります*System.OutOfMemoryException*大きなスプレッドシートの読み込み中。この例外は、スプレッドシートをメモリに完全にロードするには使用可能なメモリが不足していることを示しているため、メモリ設定を有効にしてスプレッドシートをロードする必要があります。

{{% /alert %}}
