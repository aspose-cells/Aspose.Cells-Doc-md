---
title: ファイルを開くさまざまな方法
linktitle: ファイルを開くさまざまな方法
type: docs
weight: 10
url: /ja/go-cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、ファイルを開き、データを取得したり、開発を高速化するためのデザイナー形式を利用したりできます。Aspose.Cellsは、Microsoft Excelのスプレッドシート（XLS、XLSX、XLSM、XLSB）、CSV、またはタブ区切りファイルなど、さまざまな形式のファイルを開くことができます。

{{% /alert %}}

## **パスを介してファイルを開く**

開発者は、[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)クラスのコンストラクタにファイルパスを指定して、ローカルコンピュータ上のMicrosoft Excelファイルを開くことができます。パスを文字列として渡してください。Aspose.Cellsは自動的にファイル形式を検出します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingPath.go" >}}

## **ストリームを使用してファイルを開く方法**

Excelファイルをストリームとして開くことも可能です。 これを行うには、ファイルを含む*Stream*オブジェクトを使用するコンストラクタのオーバーロードバージョンを使用します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingStream.go" >}}
