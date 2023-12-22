---
title: Excel または OpenOffice にハイパーリンクを挿入する
linktitle: ハイパーリンクの管理
type: docs
weight: 45
url: /ja/net/insert-hyperlinks-to-excel/
description: MS Excelを使用せずにAspose.Cellsライブラリを使用してExcelファイルにハイパーリンクを挿入する方法。
keywords: Insert Hyperlinks into Excel, Add or Insert Hyperlinks, Add or Insert link to a URL, Add or Insert a Link to a Cell, Add a Link to an External File
---
{{% alert color="primary" %}} 

ハイパーリンクは、2 つのエンティティ間のリンクを作成するために使用されます。誰もが、特に Web サイトでのハイパーリンクの使用に精通しています。
Aspose.Cells を使用すると、開発者は Microsoft Excel ファイルにさまざまな種類のハイパーリンクを作成できます。このトピックでは、Aspose.Cells でサポートされているハイパーリンクの種類と、それらを Excel ファイルでどのように使用できるかについて説明します。

{{% /alert %}} 
##  **ハイパーリンクの追加**
Aspose.Cells を使用すると、開発者は API またはデザイナー スプレッドシート (ハイパーリンクが手動で作成され、他のスプレッドシートにインポートするために Aspose.Cells が使用されるスプレッドシート) を使用して Excel ファイルにハイパーリンクを追加できます。

Aspose.Cells はクラスを提供します。[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)これは Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[ワークシートコレクション](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)これにより、Excel ファイル内の各ワークシートにアクセスできるようになります。ワークシートは次のように表されます。[ワークシート](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは、Excel ファイルにさまざまなハイパーリンクを追加するためのさまざまなメソッドを提供します。
##  **URLへのリンクの追加**
の[ワークシート](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには[ハイパーリンク](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks)コレクション。の各項目[ハイパーリンク](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks)コレクションは、[ハイパーリンク](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) 。 URL にハイパーリンクを追加するには、[ハイパーリンク](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection)コレクションの[追加](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)方法。の[追加](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)メソッドは次のパラメータを受け取ります。

- Cell name、ハイパーリンクが追加されるセルの名前。
- 行数。このハイパーリンク範囲内の行数。
- 列数、このハイパーリンク範囲の列数
- URL、URL アドレス。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

上の例では、空のセル *A1** の URL にハイパーリンクが追加されます。このような場合、セルが空であれば、その空のセルに URL アドレスも値として追加されます。セルが空ではなくハイパーリンクが追加されている場合、セルの値はプレーン テキストのように見えます。ハイパーリンクのように見せるには、そのセルに適切な書式設定を適用します。

{{% /alert %}} 
##  **同じファイル内に Cell へのリンクを追加する**
同じ Excel ファイル内のセルにハイパーリンクを追加するには、[ハイパーリンク](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection)コレクションの[追加](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)方法。の[追加](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)このメソッドは、内部ハイパーリンクと外部ハイパーリンクの両方で機能します。オーバーロードされたメソッドの 1 つのバージョンは、次のパラメーターを受け取ります。

- Cell name、ハイパーリンクが追加されるセルの名前。
- 行数。このハイパーリンク範囲内の行数。
- 列の数、このハイパーリンク範囲内の列の数。
- URL、ターゲットセルのアドレス。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
##  **外部ファイルへのリンクの追加**
を呼び出すことで、外部 Excel ファイルにハイパーリンクを追加できます。[ハイパーリンク](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection)コレクションの[追加](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)方法。の[追加](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)メソッドは次のパラメータを受け取ります。

- Cell name、ハイパーリンクが追加されるセルの名前。
- 行数。このハイパーリンク範囲内の行数。
- 列の数、このハイパーリンク範囲内の列の数。
- URL、ターゲットの外部 Excel ファイルのアドレス。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

##  **アドバンストトピック**
- [画像のハイパーリンクを追加する](/cells/ja/net/add-image-hyperlinks/)
- [ハイパーリンクの種類の検出](/cells/ja/net/detect-hyperlink-type/)
- [ワークシートのハイパーリンクの編集](/cells/ja/net/editing-hyperlinks-of-worksheet/)
- [範囲内のハイパーリンクを取得](/cells/ja/net/get-hyperlinks-in-range/)

