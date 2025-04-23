---
title: ExcelまたはOpenOfficeにハイパーリンクを挿入する
linktitle: ハイパーリンクの管理
type: docs
weight: 45
url: /ja/net/insert-hyperlinks-to-excel/
description: Aspose.Cellsライブラリを使用してExcelファイルにハイパーリンクを挿入する方法
keywords: Excelにハイパーリンクを挿入する、またはハイパーリンクを追加または挿入する、URLにリンクを追加または挿入する、セルにリンクを追加または挿入する、外部ファイルにリンクを追加
---

{{% alert color="primary" %}} 

ハイパーリンクは、2つのエンティティ間のリンクを作成するために使用されます。特にウェブサイトを含め、誰もがハイパーリンクの使用に慣れています。
Aspose.Cellsを使用することで、開発者はMicrosoft Excelファイルでさまざまな種類のハイパーリンクを作成することができます。このトピックではAspose.Cellsでサポートされているハイパーリンクの種類と、Excelファイルでどのように使用できるかについて説明しています。

{{% /alert %}} 
## **ハイパーリンクの追加**
Aspose.Cellsを使用すると、開発者はAPIまたはデザイナースプレッドシート（ハイパーリンクが手動で作成され、Aspose.Cellsが他のスプレッドシートに取り込まれるスプレッドシート）を使用して、Excelファイルにハイパーリンクを追加できます。

Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供しています。[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[WorksheetCollection](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)が含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。[Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、Excelファイルにさまざまなハイパーリンクを追加するためのさまざまなメソッドが用意されています。
## **URLへのリンクの追加**
[Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには[Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks)コレクションが含まれています。[Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks)コレクションの各アイテムは[Hyperl
  link](https://reference.aspose.com/cells/net/aspose.cells/hyperlink)を表します。[Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection)コレクションの[Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)メソッドを呼び出すことで、URLへのハイパーリンクを追加します。[Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)メソッドは、以下のパラメータを受け取ります。

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
- URL、URLアドレス。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

上記の例では、空のセル**A1**にURLへのハイパーリンクが追加されます。このような場合、セルが空の場合、URLアドレスもその空のセルの値として追加されます。セルが空でない場合は、ハイパーリンクが追加されても、セルの値はプレーンテキストのように見えます。それをハイパーリンクのように見えるようにするには、そのセルに適切な書式設定を適用します。

{{% /alert %}} 
## **同じファイル内のセルへのリンクの追加**
同じExcelファイルのセルにハイパーリンクを追加することが可能です。[Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)メソッドは内部ハイパーリンクと外部ハイパーリンクの両方で動作します。オーバーロードされたメソッドの1つは、以下のパラメータを受け取ります。

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
- URL、対象セルのアドレス。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
## **外部ファイルへのリンクの追加**
外部Excelファイルへのハイパーリンクを追加することが可能です。[Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)メソッドは、以下のパラメータを受け取ります。

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
 - URL、対象のアドレス、外部のExcelファイル。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

## **高度なトピック**
- [画像ハイパーリンクを追加する](/cells/ja/net/add-image-hyperlinks/)
- [ハイパーリンクのタイプの検出](/cells/ja/net/detect-hyperlink-type/)
- [ワークシートのハイパーリンクの編集](/cells/ja/net/editing-hyperlinks-of-worksheet/)
- [範囲内のハイパーリンクを取得](/cells/ja/net/get-hyperlinks-in-range/)

{{< app/cells/assistant language="csharp" >}}
