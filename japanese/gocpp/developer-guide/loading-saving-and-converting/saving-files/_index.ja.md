---
title: ファイルの保存
type: docs
weight: 20
url: /ja/go-cpp/saving-files/
---

{{% alert color="primary" %}}

Aspose.Cellsは、ファイルの作成や保存、既存のファイルの操作を可能にします。この記事では、ファイルを保存するさまざまな方法について説明します。

{{% /alert %}}

## **ファイルを保存する異なる方法**

Aspose.Cellsは、[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)を提供し、これはMicrosoft Excelファイルを表し、Excelファイルを操作するためのメソッドを備えています。[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)クラスは、[Save](https://reference.aspose.com/cells/go-cpp/workbook/save/)メソッドを提供し、これを使用してExcelファイルを保存します。[Save](https://reference.aspose.com/cells/go-cpp/workbook/save/)メソッドはいくつかのオーバーロードを持ち、さまざまな方法でファイルを保存します。保存されるファイルのフォーマットは、[SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/)列挙体によって決まります。

## **ファイルを任意の場所に保存する**

ファイルをストレージ場所に保存するには、ファイル名（ストレージパスを含む）と希望のファイルフォーマット（[SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/)列挙体から選択）を指定して、[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)オブジェクトの[Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/)メソッドを呼び出します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToSomeLocation.go" >}}

## **ストリームにファイルを保存する**

ストリームにファイルを保存するには、MemoryStreamまたはFileStreamオブジェクトを作成し、[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)オブジェクトの[Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/)メソッドを呼び出して、そのストリームオブジェクトに保存します。希望のファイルフォーマットを[SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/)列挙体を使用して指定します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToStream.go" >}}

## **PDFにファイルを保存する**

Aspose.Cells for Go via C++ライブラリを使用して、希望の内容をPDFファイルに保存するには、新規の [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) オブジェクトを作成するか、既存のExcelファイルを読み込んで [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) で構築し、その後 [save](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveOptions/) メソッドを呼び出してPDFに保存します。 Saveメソッドを呼び出す際には、[SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) 列挙を使用して希望のファイル形式を指定します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToPdf.go" >}}
