---
title: ExcelまたはOpenOfficeにハイパーリンクを挿入する
linktitle: ハイパーリンクの管理
type: docs
weight: 160
url: /ja/java/insert-hyperlinks-to-excel/
---

## **データにリンクを追加する**
{{% alert color="primary" %}} 

ハイパーリンクは、2つのエンティティ間のリンクを作成するために使用されます。特にウェブサイトを含め、誰もがハイパーリンクの使用に慣れています。

Aspose.Cellsを使用することで、開発者はMicrosoft Excelファイルでさまざまな種類のハイパーリンクを作成することができます。このトピックではAspose.Cellsでサポートされているハイパーリンクの種類と、Excelファイルでどのように使用できるかについて説明しています。

{{% /alert %}} 
## **ハイパーリンクの追加**
Aspose.Cellsを使用してセルには3種類のハイパーリンクを追加することができます:

- [URLへのリンクの追加](/cells/ja/java/working-with-hyperlinks-to-link-data/)
-[同じファイル内の別のセルへのリンクの追加](/cells/ja/java/working-with-hyperlinks-to-link-data/)
- [外部ファイルへのリンクの追加](/cells/ja/java/working-with-hyperlinks-to-link-data/)

Aspose.Cellsを使用すると、APIを使用するか[デザイナースプレッドシート](/cells/ja/java/what-is-a-designer-spreadsheet/)(ハイパーリンクが手動で作成され、Aspose.Cellsが他のスプレッドシートにインポートされるスプレッドシート)を使用して、Excelファイルにハイパーリンクを追加できます。

Aspose.Cellsは、Microsoft Excelファイルを表すクラスである[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)を提供します。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには、Excelファイルの各ワークシートにアクセスできる[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)が含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスによって表されます。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには、Excelファイルにさまざまなハイパーリンクを追加するための異なるメソッドが用意されています。
## **URLへのリンクの追加**
[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスは、[Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection)コレクションを含みます。各アイテムは、[Hyperlink](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink)を表します。URLにハイパーリンクを追加するには、[Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Hyperlinks)コレクションの[Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add-int-int-int-int-java.lang.String-)メソッドを呼び出します。[Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add-int-int-int-int-java.lang.String-)メソッドのパラメータは次の通りです。

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
- URL、URLアドレス。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


上記の例では、空のセル**A1**にURLへのハイパーリンクが追加されています。このような場合、セルが空の場合、その空のセルにもURLアドレスが値として追加されます。セルが空でなく、ハイパーリンクが追加された場合、セルの値はプレーンテキストのようになります。ハイパーリンクのように見えるようにするには、そのセルに適切な書式設定を適用してください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **同じファイル内のセルへのリンクの追加**
同じExcelファイル内のセルにハイパーリンクを追加するには、[Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection)コレクションの[Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add-int-int-int-int-java.lang.String-)メソッドを呼び出します。[Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add-int-int-int-int-java.lang.String-)メソッドは、内部リンクと外部リンクの両方に対応しています。オーバーロードされたメソッドの一つのバージョンは、次のパラメータを取ります：

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
- URL、対象セルのアドレス。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **外部ファイルへのリンクの追加**
外部Excelファイルへのハイパーリンクを追加するには、[Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection)コレクションの[Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add-int-int-int-int-java.lang.String-)メソッドを呼び出します。[Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add-int-int-int-int-java.lang.String-)メソッドは、次のパラメータを取ります：

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
 - URL、対象のアドレス、外部のExcelファイル。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **高度なトピック**
- [画像ハイパーリンクを追加する](/cells/ja/java/add-image-hyperlinks/)
- [ハイパーリンクのタイプの検出](/cells/ja/java/detect-hyperlink-type/)
- [ワークシートのハイパーリンクの編集](/cells/ja/java/editing-hyperlinks-of-worksheet/)
- [範囲内のハイパーリンクを取得](/cells/ja/java/get-hyperlinks-in-range/)


{{< app/cells/assistant language="java" >}}
