---
title: Excel または OpenOffice にハイパーリンクを挿入する
linktitle: ハイパーリンクの管理
type: docs
weight: 160
url: /ja/java/insert-hyperlinks-to-excel/
---
## **リンク データへのハイパーリンクの追加**
{{% alert color="primary" %}} 

ハイパーリンクは、2 つのエンティティ間のリンクを作成するために使用されます。特に Web サイトでは、誰もがハイパーリンクの使用に慣れています。

Aspose.Cells を使用すると、開発者は Microsoft Excel ファイルにさまざまな種類のハイパーリンクを作成できます。このトピックでは、Aspose.Cells でサポートされているハイパーリンクの種類と、それらを Excel ファイルで使用する方法について説明します。

{{% /alert %}} 
## **ハイパーリンクの追加**
Aspose.Cells を使用して、3 種類のハイパーリンクをセルに追加できます。

- [URL へのリンクの追加](/cells/ja/java/working-with-hyperlinks-to-link-data/).
- [同じファイル内の別のセルへのリンクを追加する](/cells/ja/java/working-with-hyperlinks-to-link-data/).
- [外部ファイルへのリンクの追加](/cells/ja/java/working-with-hyperlinks-to-link-data/).

Aspose.Cells を使用すると、開発者は API または[デザイナー スプレッドシート](/cells/ja/java/what-is-a-designer-spreadsheet/)(ハイパーリンクが手動で作成され、他のスプレッドシートにインポートするために Aspose.Cells が使用されるスプレッドシート)。

Aspose.Cells はクラスを提供し、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[ワークシート コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには、さまざまなハイパーリンクを Excel ファイルに追加するためのさまざまなメソッドが用意されています。
## **URL へのリンクの追加**
の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには[ハイパーリンク](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection)コレクション。の各項目[ハイパーリンク](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection)コレクションは[ハイパーリンク](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink).を呼び出して URL にハイパーリンクを追加します。[ハイパーリンク](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Hyperlinks)コレクションの[追加](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)）方法。の[追加](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)メソッドは、次のパラメーターを取ります。

- Cell name、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数
- URL、URL アドレス。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


上記の例では、空のセルの URL にハイパーリンクが追加され、**A1**.このような場合、セルが空の場合、URL アドレスもその空のセルに値として追加されます。セルが空ではなく、ハイパーリンクが追加されている場合、セルの値はプレーン テキストのように見えます。ハイパーリンクのように見せるには、そのセルに適切な書式設定を適用します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **同じファイルに Cell へのリンクを追加する**
を呼び出して、同じ Excel ファイル内のセルにハイパーリンクを追加することができます。[ハイパーリンク](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection)コレクションの[追加](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)）方法。の[追加](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))メソッドは、内部ハイパーリンクと外部ハイパーリンクの両方で機能します。オーバーロードされたメソッドの 1 つのバージョンは、次のパラメーターを取ります。

- Cell name、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲内の列数。
- URL、ターゲット セルのアドレス。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **外部ファイルへのリンクの追加**
を呼び出して、外部の Excel ファイルにハイパーリンクを追加することができます。[ハイパーリンク](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection)コレクションの[追加](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)）方法。の[追加](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)メソッドは、次のパラメーターを取ります。

- Cell name、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲内の列数。
- URL、ターゲットのアドレス、外部 Excel ファイル。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **先行トピック**
- [画像のハイパーリンクを追加](/cells/ja/java/add-image-hyperlinks/)
- [ハイパーリンク タイプの検出](/cells/ja/java/detect-hyperlink-type/)
- [ワークシートのハイパーリンクの編集](/cells/ja/java/editing-hyperlinks-of-worksheet/)
- [範囲内のハイパーリンクを取得](/cells/ja/java/get-hyperlinks-in-range/)


