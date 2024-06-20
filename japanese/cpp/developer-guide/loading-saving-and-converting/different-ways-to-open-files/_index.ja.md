---
title: ファイルを開くさまざまな方法
linktitle: ファイルを開くさまざまな方法
type: docs
weight: 10
url: /ja/cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}} 

Aspose.Cellsを使用すると、データを取得したり、開発プロセスをスピードアップするためにデザイナーテンプレートを使用したりするために、ファイルを開くことが可能です。 Aspose.Cellsは、Microsoft Excelスプレッドシート（XLS、XLSX、XLSM、XLSB）、CSV、またはタブ区切りファイルなど、さまざまな種類のファイルを開くことができます。

{{% /alert %}} 
## **パスを介してファイルを開く**
開発者は、[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスのコンストラクタでそれを指定することによって、ローカルコンピュータ上のMicrosoft Excelファイルを開くことができます。 単純にパスを文字列としてコンストラクタに渡します。 Aspose.Cellsは自動的にファイル形式を検出します。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath-new.cpp" >}}

## **ストリームを使用してファイルを開く**
Excelファイルをストリームとして開くことも可能です。 これを行うには、ファイルを含む*Stream*オブジェクトを使用するコンストラクタのオーバーロードバージョンを使用します。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream-new.cpp" >}}

