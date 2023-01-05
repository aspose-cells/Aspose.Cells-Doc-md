---
title: ワークシートの管理
linktitle: ワークシート
type: docs
weight: 60
url: /ja/java/manage-worksheets/
---
{{% alert color="primary" %}}

開発者は、柔軟な Aspose.Cells の API を使用して、Excel ファイルでワークシートを簡単に作成および管理できます。このトピックでは、Excel ファイルでワークシートを追加および削除するいくつかの方法について説明します。

{{% /alert %}}

Aspose.Cells を使用したワークシートの管理は、ABC と同じくらい簡単です。このセクションでは、次の方法について説明します。

1. 新しい Excel ファイルをゼロから作成し、それにワークシートを追加する
1. ワークシートをデザイナー スプレッドシートに追加する
1. シート名を使用してワークシートにアクセスする
1. シート名を使用して Excel ファイルからワークシートを削除する
1. シート インデックスを使用して Excel ファイルからワークシートを削除する

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)これは Excel ファイルを表します。[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[**ワークシート コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。これらの基本的な API セットをどのように利用できるか見てみましょう。

## **新しい Excel ファイルへのワークシートの追加**

プログラムで新しい Excel ファイルを作成するには、開発者は次のオブジェクトを作成する必要があります。[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Excel ファイルを表すクラス。その後、開発者は呼び出すことができます[**追加**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add() ) の方法[**ワークシート コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection).電話すると[**追加**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add() メソッドを使用すると、空のワークシートが Excel ファイルに自動的に追加されます。これは、新しく追加されたワークシートのシート インデックスを[**ワークシート コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection).ワークシート参照を取得したら、開発者は要件に従ってワークシートで作業できます。ワークシートでの作業が完了したら、開発者は を呼び出して、新しく作成した Excel ファイルを新しいワークシートと共に保存できます。[**セーブ**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) の方法[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラス。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **Designer スプレッドシートへのワークシートの追加**

デザイナー スプレッドシートにワークシートを追加するプロセスは、Excel ファイルが既に作成されており、ワークシートを追加する前にまずその Excel ファイルを開く必要があることを除いて、上記のアプローチのプロセスとまったく同じです。デザイナー スプレッドシートは、初期化中にファイル パスまたはストリームを渡すことで開くことができます。[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラス。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **シート名を使用してワークシートにアクセスする**

開発者は、ワークシートの名前またはインデックスを指定して、任意のワークシートにアクセスまたは取得できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **シート名を使用してワークシートを削除する**

場合によっては、開発者が既存の Excel ファイルからワークシートを削除する必要がある場合があります。そのタスクは、[**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String) ) の方法[**ワークシート コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)コレクション。シート名を[**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)メソッドを使用して、特定のワークシートを削除します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **シート インデックスを使用してワークシートを削除する**

ワークシートを削除する上記のアプローチは、開発者が削除するワークシートのシート名を既に知っている場合にうまく機能します。しかし、Excel ファイルから削除したいワークシートのシート名がわからない場合はどうすればよいでしょうか?

そのような状況では、開発者はオーバーロードされたバージョンの[**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(int)シート名の代わりにワークシートのシート インデックスを取得するメソッド。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **先行トピック**
- [シートのアクティブ化とワークシートでの Cell のアクティブ化](/cells/ja/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [ワークブック内およびワークブック間でワークシートをコピーおよび移動する](/cells/ja/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [ワークシートのコピーと移動](/cells/ja/java/copying-and-moving-worksheets/)
- [ワークシート内のセルの数を数える](/cells/ja/java/count-number-of-cells-in-the-worksheet/)
- [空のワークシートの検出](/cells/ja/java/detecting-empty-worksheets/)
- [ワークシートがダイアログ シートかどうかを調べる](/cells/ja/java/find-if-the-worksheet-is-dialog-sheet/)
- [ワークシートの一意の ID を取得する](/cells/ja/java/get-worksheet-unique-id/)
- [背景画像を Excel に挿入](/cells/ja/java/insert-background-image-to-excel/)
- [ワークシートからのシナリオの作成、操作、または削除](/cells/ja/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [改ページの管理](/cells/ja/java/managing-page-breaks/)
- [ページ設定機能](/cells/ja/java/page-setup-features/)
- [ワークシートの空白の列と行を削除しながら、他のワークシートの参照を更新する](/cells/ja/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [Aspose.Cells を使用して OpenXml の Sheet.SheetId プロパティを利用する](/cells/ja/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [ODS ファイルの背景の操作](/cells/ja/java/working-with-background-in-ods-files/)
- [ワークシート ビュー](/cells/ja/java/worksheet-views/)
