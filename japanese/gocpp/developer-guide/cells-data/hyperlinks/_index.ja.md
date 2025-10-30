---
title: Golang経由のC++でExcelやOpenOfficeにハイパーリンクを挿入
linktitle: ハイパーリンクの管理
type: docs
weight: 45
url: /ja/go-cpp/insert-hyperlinks-to-excel/
description: Aspose.Cellsライブラリを使って、MS Excelを使わずにExcelファイルにハイパーリンクを挿入する方法。
keywords: Excelにハイパーリンクを挿入する、またはハイパーリンクを追加または挿入する、URLにリンクを追加または挿入する、セルにリンクを追加または挿入する、外部ファイルにリンクを追加
---

{{% alert color="primary" %}} 

ハイパーリンクは、2つのエンティティ間のリンクを作成するために使用されます。特にウェブサイトを含め、誰もがハイパーリンクの使用に慣れています。
Aspose.Cellsを使用することで、開発者はMicrosoft Excelファイルでさまざまな種類のハイパーリンクを作成することができます。このトピックではAspose.Cellsでサポートされているハイパーリンクの種類と、Excelファイルでどのように使用できるかについて説明しています。

{{% /alert %}} 

## **ハイパーリンクの追加**
Aspose.Cellsは、APIまたはデザイナースプレッドシート（手動でハイパーリンクを作成し、それを他のスプレッドシートにインポートするためにAspose.Cellsを使用する）を使って、開発者がExcelファイルにハイパーリンクを追加できるようにします。

Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)クラスを提供します。[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)クラスには、Excelファイル内の各ワークシートにアクセスできる[WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)があります。ワークシートは[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスで表されます。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、Excelファイルにさまざまなハイパーリンクを追加するためのさまざまなメソッドを提供します。

## **URLへのリンクの追加**
[Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/)クラスには、[GetHyperlinks()](https://reference.aspose.com/cells/go-cpp/worksheet/gethyperlinks/)コレクションがあります。[GetHyperlinks()](https://reference.aspose.com/cells/go-cpp/worksheet/gethyperlinks/)コレクションの各アイテムは[Hyperlink](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/)を表します。URLへのハイパーリンクを追加するには、[Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/)コレクションの[Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/)メソッドを呼び出します。[Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/)メソッドは次のパラメータを取ります：

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
- URL、URLアドレス。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks.go" >}}
{{% alert color="primary" %}} 

上記の例では、空のセル**A1**にURLへのハイパーリンクが追加されます。このような場合、セルが空の場合、URLアドレスもその空のセルの値として追加されます。セルが空でない場合は、ハイパーリンクが追加されても、セルの値はプレーンテキストのように見えます。それをハイパーリンクのように見えるようにするには、そのセルに適切な書式設定を適用します。

{{% /alert %}} 

## **同じファイル内のセルへのリンクの追加**
[Hyperlinks](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/)コレクションの[Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/)メソッドを呼び出すことで、同じExcelファイル内のセルにハイパーリンクを追加できます。[Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/)メソッドは、内部ハイパーリンクと外部ハイパーリンクの両方に対応しています。オーバーロードされたメソッドの一つは、次のパラメータを取ります：

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
- URL、対象セルのアドレス。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks-1.go" >}}
## **外部ファイルへのリンクの追加**
外部Excelファイルへのハイパーリンクを追加するには、[Hyperlinks](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/)コレクションの[Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/)メソッドを呼び出します。[Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/)メソッドは次のパラメータを取ります：

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
 - URL、対象のアドレス、外部のExcelファイル。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks-2.go" >}}
## **高度なトピック**
- [画像ハイパーリンクを追加する](/cells/ja/cpp/add-image-hyperlinks/)
- [ハイパーリンクのタイプの検出](/cells/ja/cpp/detect-hyperlink-type/)
- [ワークシートのハイパーリンクの編集](/cells/ja/cpp/editing-hyperlinks-of-worksheet/)
- [範囲内のハイパーリンクを取得](/cells/ja/cpp/get-hyperlinks-in-range/)
