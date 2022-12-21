---
title: ファイルを開くさまざまな方法
type: docs
weight: 10
url: /ja/python-java/different-ways-to-open-files/
---
{{% alert color="primary" %}}

Aspose.Cells を使用すると、ファイルを開いてデータを取得したり、デザイナー テンプレートを使用して開発プロセスをスピードアップしたりすることが簡単になります。

{{% /alert %}}

## **パス経由でファイルを開く**

開発者は、ローカル コンピューター上のファイル パスを使用して Microsoft Excel ファイルを開くことができます。**[ワークブック](https://reference.aspose.com/cells/python-java/asposecells.api/ワークブック)**クラス コンストラクタ。コンストラクターにパスを渡すだけです。*ストリング*Aspose.Cells は、ファイル形式の種類を自動的に検出します。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaPath.py" >}}

## **ストリーム経由でファイルを開く**

Excel ファイルをストリームとして開くのも簡単です。これを行うには、コンストラクターのオーバーロードされたバージョンを使用します。*バッファストリーム*ファイルを含むオブジェクト。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaStream.py" >}}

## **データのみのファイルを開く**

データのみのファイルを開くには、**[LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)**と**[LoadFilter](https://reference.aspose.com/cells/python-java/asposecells.api/LoadFilter)**classes を使用して、ロードするテンプレート ファイルの関連する属性とクラスのオプションを設定します。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Aspose.Cells までにネイティブでない Excel ファイルまたはその他のファイル形式 (PPT/PPTX、DOC/DOCX など) を開こうとすると、例外がスローされます。

{{% /alert %}} {{% alert color="primary" %}}

かなりの可能性があります**[ワークブック](https://reference.aspose.com/cells/python-java/asposecells.api/ワークブック)**コンストラクターがスローする可能性があります*System.OutOfMemoryException*大きなスプレッドシートの読み込み中。この例外は、スプレッドシートをメモリに完全にロードするには使用可能なメモリが不足していることを示しているため、メモリ設定を有効にしてスプレッドシートをロードする必要があります。

{{% /alert %}}
