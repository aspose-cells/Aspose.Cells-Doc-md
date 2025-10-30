---
title: ExcelまたはOpenOfficeにハイパーリンクを挿入する
linktitle: ハイパーリンクの管理
type: docs
weight: 45
url: /ja/nodejs-cpp/insert-hyperlinks-to-excel/
description: MS Excelを使用せずにNode.js via C++を使ってExcelファイルにハイパーリンクを挿入する方法
keywords: Node.js via C++でハイパーリンクを挿入、追加または挿入、URLへリンクの追加または挿入、セルへリンクの追加または挿入、外部ファイルへのリンク追加または挿入
---

{{% alert color="primary" %}} 

ハイパーリンクは、2つのエンティティ間のリンクを作成するために使用されます。特にウェブサイトを含め、誰もがハイパーリンクの使用に慣れています。
Aspose.Cellsを使用することで、開発者はMicrosoft Excelファイルでさまざまな種類のハイパーリンクを作成することができます。このトピックではAspose.Cellsでサポートされているハイパーリンクの種類と、Excelファイルでどのように使用できるかについて説明しています。

{{% /alert %}} 

## **ハイパーリンクの追加**
Aspose.Cellsは、APIまたはデザイナースプレッドシート（手動でハイパーリンクを作成し、それを他のスプレッドシートにインポートするためにAspose.Cellsを使用する）を使って、開発者がExcelファイルにハイパーリンクを追加できるようにします。

Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスを提供します。[Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセス可能にする[WorksheetCollection](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)が含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスで表されます。[Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは、Excelファイルにさまざまなハイパーリンクを追加するためのさまざまなメソッドを提供します。
## **URLへのリンクの追加**
[Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスには、[getHyperlinks()](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHyperlinks--)コレクションがあります。各アイテムは[Hyperlink](https://reference.aspose.com/cells/nodejs-cpp/hyperlink)を表します。[getHyperlinks()](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHyperlinks--)コレクションの[add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-)メソッドを呼び出すことで、URLへのハイパーリンクを追加できます。[add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-)メソッドは、以下のパラメータを取ります。

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
- URL、URLアドレス。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToURL.js" >}}


{{% alert color="primary" %}} 

上記の例では、空のセル**A1**にURLへのハイパーリンクが追加されます。このような場合、セルが空の場合、URLアドレスもその空のセルの値として追加されます。セルが空でない場合は、ハイパーリンクが追加されても、セルの値はプレーンテキストのように見えます。それをハイパーリンクのように見えるようにするには、そのセルに適切な書式設定を適用します。

{{% /alert %}} 
## **同じファイル内のセルへのリンクの追加**
Excelファイル内のセルにハイパーリンクを追加することができます。これは、Hyperlinksコレクションのaddメソッドを呼び出すことで実現します。addメソッドは内部リンクと外部リンクの両方に対応しています。オーバーロードされたバージョンの一つは次のパラメータを取ります：

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
- URL、対象セルのアドレス。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToCell.js" >}}


## **外部ファイルへのリンクの追加**
Excelファイルの外部にハイパーリンクを追加するには、Hyperlinksコレクションのaddメソッドを呼び出します。addメソッドは次のパラメータを取ります：

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
 - URL、対象のアドレス、外部のExcelファイル。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToExternalFile.js" >}}



## **高度なトピック**
- [画像ハイパーリンクを追加する](/cells/ja/nodejs-cpp/add-image-hyperlinks/)
- [ハイパーリンクのタイプの検出](/cells/ja/nodejs-cpp/detect-hyperlink-type/)
- [ワークシートのハイパーリンクの編集](/cells/ja/nodejs-cpp/editing-hyperlinks-of-worksheet/)
- [範囲内のハイパーリンクを取得](/cells/ja/nodejs-cpp/get-hyperlinks-in-range/)

{{< app/cells/assistant language="nodejs-cpp" >}}
