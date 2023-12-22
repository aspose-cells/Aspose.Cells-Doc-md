---
title: ファイルを開くさまざまな方法
linktitle: ファイルを開くさまざまな方法
type: docs
weight: 10
url: /ja/cpp/different-ways-to-open-files/
---
{{% alert color="primary" %}} 

Aspose.Cells を使用すると、ファイルを開いてデータを取得したり、デザイナー テンプレートを使用して開発プロセスをスピードアップしたりすることができます。 Aspose.Cells は、Microsoft Excel スプレッドシート (XLS、XLSX、XLSM、XLSB)、CSV または TabDelimited ファイルなど、さまざまなファイルを開くことができます。

{{% /alert %}} 
##  **パス経由でファイルを開く**
開発者は、ローカル コンピュータ上のファイル パスを使用して Microsoft Excel ファイルを開くことができます。[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスコンストラクター。コンストラクターにパスを文字列として渡すだけです。 Aspose.Cells はファイル形式の種類を自動的に検出します。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath-new.cpp" >}}

##  **ストリームを使用してファイルを開く**
Excel ファイルをストリームとして開くこともできます。これを行うには、コンストラクターのオーバーロードされたバージョンを使用します。*ストリーム*ファイルを含むオブジェクト。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream-new.cpp" >}}

