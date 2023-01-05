---
title: Microsoft Excel ファイルのワークシートを管理します。
linktitle: ワークシート
type: docs
weight: 90
url: /ja/net/manage-worksheets/
description: Aspose.Cells を使用して、ワークシートを追加し、ワークシートとアクティブなシートを削除します。
---
{{% alert color="primary" %}}

開発者は、Aspose.Cells' フレキシブル API を使用して、プログラムで Microsoft Excel ファイルのワークシートを簡単に作成および管理できます。このトピックでは、Microsoft Excel ファイルでワークシートを追加および削除する方法について説明します。

{{% /alert %}}

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)これは Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。

## **新しい Excel ファイルへのワークシートの追加**

プログラムで新しい Excel ファイルを作成するには:

1. のオブジェクトを作成します[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラス。
1. 電話する[**追加**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add)の方法[**ワークシート コレクション**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)クラス。空のワークシートが Excel ファイルに自動的に追加されます。新しいワークシートのシート インデックスを[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクション。
1. ワークシート参照を取得します。
1. ワークシートで作業を行います。
1. を呼び出して、新しいワークシートを含む新しい Excel ファイルを保存します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラス'[**セーブ**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **Designer スプレッドシートへのワークシートの追加**

ワークシートをデザイナー スプレッドシートに追加するプロセスは、新しいワークシートを追加するプロセスと同じですが、Excel ファイルが既に存在するため、ワークシートを追加する前に開く必要があります。デザイナー スプレッドシートは、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラス。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **シート名を使用してワークシートにアクセスする**

名前またはインデックスを指定して、任意のワークシートにアクセスします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **シート名を使用してワークシートを削除する**

ファイルからワークシートを削除するには、[**削除場所**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index)方法[**ワークシート コレクション**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)クラス。シート名を[**削除場所**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1)特定のワークシートを削除するメソッド。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **シート インデックスを使用してワークシートを削除する**

名前によるワークシートの削除は、ワークシートの名前がわかっている場合にうまく機能します。ワークシートの名前がわからない場合は、オーバーロードされたバージョンの[**削除場所**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat)シート名の代わりにワークシートのシート インデックスを取得するメソッド。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **シートをアクティブ化し、ワークシートで Cell をアクティブにする**

ユーザーが Excel で Microsoft Excel ファイルを開いたときに、特定のワークシートをアクティブにして表示する必要がある場合があります。同様に、特定のセルをアクティブにして、アクティブ セルを表示するようにスクロール バーを設定することもできます。
Aspose.Cells は、これらすべてのタスクを実行できます。

アン**アクティブシート**は作業中のシートです。タブ上のアクティブなシートの名前は、デフォルトで太字になっています。

アン**アクティブセル**選択されたセル (入力を開始したときにデータが入力されるセル) です。一度にアクティブになるセルは 1 つだけです。アクティブ セルは、太い境界線で強調表示されます。

### **シートのアクティブ化と Cell のアクティブ化**

Aspose.Cells は、シートとセルをアクティブ化するための特定の API 呼び出しを提供します。たとえば、[**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex)プロパティは、ワークブックのアクティブ シートを設定するのに役立ちます。
同様に、[**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell)プロパティは、ワークシート内のアクティブ セルを設定および取得するために使用されます。

水平または垂直スクロールバーが、特定のデータを表示したい行と列のインデックス位置にあることを確認するには、[**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow)と[**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn)プロパティ。

次の例は、ワークシートをアクティブにして、その中にアクティブ セルを作成する方法を示しています。生成された出力では、スクロールバーがスクロールされて、2 番目の行と 2 番目の列が最初に表示される行と列になります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **先行トピック**
- [ワークシートのコピーと移動](/cells/ja/net/copying-and-moving-worksheets/)
- [ワークシート内のセルの数を数える](/cells/ja/net/count-number-of-cells-in-the-worksheet/)
- [空のワークシートの検出](/cells/ja/net/detecting-empty-worksheets/)
- [ワークシートがダイアログ シートかどうかを調べる](/cells/ja/net/find-if-the-worksheet-is-dialog-sheet/)
- [ワークシートの一意の ID を取得する](/cells/ja/net/get-worksheet-unique-id/)
- [ワークシートからのシナリオの作成、操作、または削除](/cells/ja/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [改ページの管理](/cells/ja/net/managing-page-breaks/)
- [ページ設定機能](/cells/ja/net/page-setup-features/)
- [ワークシートを複数部印刷する](/cells/ja/net/print-multiple-copies-of-a-worksheet/)
- [Aspose.Cells を使用して OpenXml の Sheet.SheetId プロパティを利用する](/cells/ja/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [ワークシート ビュー](/cells/ja/net/worksheet-views/)

