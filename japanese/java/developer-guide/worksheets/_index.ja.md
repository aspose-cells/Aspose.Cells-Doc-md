---
title: ワークシートの管理
linktitle: ワークシート
type: docs
weight: 60
url: /ja/java/manage-worksheets/
---

{{% alert color="primary" %}}

Aspose.Cellsの柔軟なAPIを使用して、Excelファイルのワークシートをプログラムで簡単に作成および管理できます。このトピックでは、Excelファイルにワークシートを追加および削除するいくつかの方法について説明します。

{{% /alert %}}

Aspose.Cellsを使用してワークシートを管理することは非常に簡単です。このセクションでは、以下の方法について説明します。

1.ゼロから新しいExcelファイルを作成し、ワークシートを追加する
1. デザイナースプレッドシートにワークシートを追加する
1. シート名を使用してワークシートにアクセスする
1. シート名を使用してExcelファイルからワークシートを削除する
1. シートインデックスを使用してExcelファイルからワークシートを削除する

Aspose.CellsはExcelファイルを表す[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには各ワークシートにアクセスできる[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)が含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスにはワークシートを管理するための幅広いプロパティとメソッドが提供されています。これらの基本的なAPIを使用する方法を見てみましょう。

## **新しいExcelファイルにワークシートを追加する**

プログラムで新しいExcelファイルを作成するには、Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスのオブジェクトを作成する必要があります。その後、開発者は[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)の[**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add--)メソッドを呼び出すことができます。[**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add--)メソッドを呼び出すと、空のワークシートがExcelファイルに自動的に追加されます。その後、[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)に新しく追加されたワークシートのシートインデックスを渡すことで、ワークシートに参照できます。ワークシートの参照を取得した後、開発者は要件に応じてワークシート上で作業することができます。ワークシートで作業が完了した後、開発者は[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスの[**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))メソッドを呼び出すことで、新しく作成されたExcelファイルに新しいワークシートを保存することができます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **デザイナースプレッドシートにワークシートを追加する**

デザイナースプレッドシートにワークシートを追加するプロセスは、上記の手順とまったく同じですが、Excelファイルがすでに作成されており、ワークシートを追加する前にそのExcelファイルを開く必要があります。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを初期化する際に、ファイルパスまたはストリームを渡すことでデザイナースプレッドシートを開くことができます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **シート名を使用してワークシートにアクセスする**

開発者は名前またはインデックスを指定して任意のワークシートにアクセスまたは取得できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **シート名を使用してワークシートを削除する**

時々、開発者は既存のExcelファイルからワークシートを削除する必要があり、そのタスクは[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)コレクションの[**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String))メソッドを呼び出すことで実行できます。[**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String))メソッドにシート名を渡すことで特定のワークシートを削除できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **Sheet Indexを使用してワークシートを削除する**

上記のワークシートを削除する方法は、削除するワークシートのシート名が既にわかっている場合にうまく機能します。しかし、Excelファイルから削除したいワークシートのシート名がわからない場合はどうすればよいでしょうか？

そのような状況で、開発者は[**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(int))メソッドのオーバーロードバージョンを使用できます。このバージョンでは、ワークシートのシートインデックスを使用してワークシートを削除します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **高度なトピック**
- [シートのアクティブ化およびワークシートでセルのアクティブ化](/cells/ja/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [ブック間およびブック内でワークシートをコピーおよび移動する](/cells/ja/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [ワークシートのコピーおよび移動](/cells/ja/java/copying-and-moving-worksheets/)
- [ワークシート内のセル数を数える](/cells/ja/java/count-number-of-cells-in-the-worksheet/)
- [空のワークシートを検出する](/cells/ja/java/detecting-empty-worksheets/)
- [ワークシートがダイアログシートであるかを検索する](/cells/ja/java/find-if-the-worksheet-is-dialog-sheet/)
- [ワークシートの一意のIDを取得](/cells/ja/java/get-worksheet-unique-id/)
- [Excel に背景画像を挿入](/cells/ja/java/insert-background-image-to-excel/)
- [シナリオを作成、操作、またはワークシートから削除する](/cells/ja/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [ページ区切りの管理](/cells/ja/java/managing-page-breaks/)
- [ページ設定機能](/cells/ja/java/page-setup-features/)
- [ワークシート内の空白の列と行を削除する際に、他のワークシートの参照を更新する](/cells/ja/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [Aspose.Cellsを使用したOpenXmlのSheet.SheetIdプロパティを利用する](/cells/ja/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [ODSファイルで背景を操作する](/cells/ja/java/working-with-background-in-ods-files/)
- [ワークシートビュー](/cells/ja/java/worksheet-views/)
