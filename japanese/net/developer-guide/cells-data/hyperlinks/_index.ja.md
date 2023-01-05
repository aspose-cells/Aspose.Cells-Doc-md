---
title: Excel または OpenOffice にハイパーリンクを挿入する
linktitle: ハイパーリンクの管理
type: docs
weight: 45
url: /ja/net/insert-hyperlinks-to-excel/
description: MS Excel を使用せずに Aspose.Cells ライブラリを使用して Excel ファイルにハイパーリンクを挿入する方法。
---
{{% alert color="primary" %}} 

ハイパーリンクは、2 つのエンティティ間のリンクを作成するために使用されます。特に Web サイトでは、誰もがハイパーリンクの使用に慣れています。
Aspose.Cells を使用すると、開発者は Microsoft Excel ファイルにさまざまな種類のハイパーリンクを作成できます。このトピックでは、Aspose.Cells でサポートされているハイパーリンクの種類と、それらを Excel ファイルで使用する方法について説明します。

{{% /alert %}} 
## **ハイパーリンクの追加**
Aspose.Cells を使用すると、開発者は API またはデザイナー スプレッドシート (ハイパーリンクを手動で作成し、Aspose.Cells を使用して他のスプレッドシートにインポートするスプレッドシート) を使用して Excel ファイルにハイパーリンクを追加できます。

Aspose.Cells はクラスを提供し、[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[ワークシート コレクション](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。ワークシートは、[ワークシート](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、さまざまなハイパーリンクを Excel ファイルに追加するためのさまざまなメソッドが用意されています。
## **URL へのリンクの追加**
の[ワークシート](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには[ハイパーリンク](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks)コレクション。の各項目[ハイパーリンク](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks)コレクションは[ハイパーリンク](https://reference.aspose.com/cells/net/aspose.cells/hyperlink).を呼び出して URL にハイパーリンクを追加します。[ハイパーリンク](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection)コレクションの[追加](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)方法。の[追加](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)メソッドは次のパラメータを取ります。

- Cell name、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数
- URL、URL アドレス。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

上記の例では、空のセルの URL にハイパーリンクが追加され、**A1**.このような場合、セルが空の場合、URL アドレスもその空のセルに値として追加されます。セルが空ではなく、ハイパーリンクが追加されている場合、セルの値はプレーン テキストのように見えます。ハイパーリンクのように見せるには、そのセルに適切な書式設定を適用します。

{{% /alert %}} 
## **同じファイルに Cell へのリンクを追加する**
を呼び出して、同じ Excel ファイル内のセルにハイパーリンクを追加することができます。[ハイパーリンク](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection)コレクションの[追加](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)方法。の[追加](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)メソッドは、内部ハイパーリンクと外部ハイパーリンクの両方で機能します。オーバーロードされたメソッドの 1 つのバージョンは、次のパラメーターを取ります。

- Cell name,ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲内の列数。
- URL、ターゲット セルのアドレス。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
## **外部ファイルへのリンクの追加**
を呼び出して、外部の Excel ファイルにハイパーリンクを追加することができます。[ハイパーリンク](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection)コレクションの[追加](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)方法。の[追加](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)メソッドは次のパラメータを取ります。

- Cell name、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲内の列数。
- URL、ターゲットのアドレス、外部 Excel ファイル。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

## **先行トピック**
- [画像のハイパーリンクを追加](/cells/ja/net/add-image-hyperlinks/)
- [ハイパーリンク タイプの検出](/cells/ja/net/detect-hyperlink-type/)
- [ワークシートのハイパーリンクの編集](/cells/ja/net/editing-hyperlinks-of-worksheet/)
- [範囲内のハイパーリンクを取得](/cells/ja/net/get-hyperlinks-in-range/)

