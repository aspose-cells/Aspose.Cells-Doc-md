---
title: Microsoft Excelファイルのワークシートを管理します。
linktitle: ワークシート
type: docs
weight: 90
url: /ja/net/manage-worksheets/
description: Aspose.Cellsを使用して、ワークシートを追加、削除し、アクティブシートを追加することができます。
---


{{% alert color="primary" %}}

Aspose.Cellsの柔軟なAPIを使用して、Microsoft Excelファイルでワークシートを簡単に作成、管理できます。このトピックでは、Microsoft Excelファイルにワークシートを追加および削除する方法について説明します。

{{% /alert %}}

Aspose.Cellsは、Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excelファイルの各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシートを管理するための多くのプロパティやメソッドが用意されています。

## **新しいExcelファイルにワークシートを追加する**

プログラムで新しいExcelファイルを作成するには：

1. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスのオブジェクトを作成します。
1. [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)クラスの[**Add**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add)メソッドを呼び出します。空のワークシートがExcelファイルに自動的に追加されます。新しいワークシートのシートインデックスを[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションに渡すことで参照できます。
1. ワークシートの参照を取得します。
1. ワークシートで作業を実行します。
1. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスの[**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)メソッドを呼び出して、新しいワークシートで新しいExcelファイルを保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **デザイナースプレッドシートにワークシートを追加する**

デザイナースプレッドシートにワークシートを追加するプロセスは、新しいワークシートを追加するプロセスと同じですが、既存のExcelファイルがあるため、ワークシートを追加する前に開く必要があります。デザイナースプレッドシートは、[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスによって開くことができます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **シート名を使用してワークシートにアクセスする**

名前またはインデックスを指定して任意のワークシートにアクセスできます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **シート名を使用してワークシートを削除する**

ファイルからワークシートを削除するには、[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)クラスの[**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index)メソッドを呼び出します。特定のワークシートを削除するには、[**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1)メソッドにシート名を渡します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **Sheet Indexを使用してワークシートを削除する**

ワークシートの名前がわかっている場合は、ワークシートの名前を使用して削除する方法が適しています。ワークシートの名前を知らない場合は、シート名の代わりにシートのインデックスを取る[**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat)メソッドのオーバーロードバージョンを使用してください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **シートのアクティブ化およびワークシート内のアクティブセルを作成します**

時々、ユーザーがMicrosoft ExcelファイルをExcelで開いたときに特定のワークシートをアクティブで表示する必要があります。同様に、特定のセルをアクティブにし、スクロールバーをアクティブなセルを表示するように設定することがあります。
Aspose.Cellsはこれらのすべてのタスクを実行できます。

**アクティブなシート**とは、作業中のシートのことです。タブ上のアクティブなシートの名前は、デフォルトで太字になります。

**アクティブなセル**は選択されたセルであり、タイプを始めるとデータが入力されるセルです。1度に1つのセルがアクティブです。アクティブなセルは太い枠で強調表示されます。

### **シートのアクティブ化とセルをアクティブにする**

Aspose.Cellsには、シートとセルをアクティブにするための特定のAPI呼び出しが用意されています。たとえば、ブック内でアクティブなシートを設定するのに[**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex)プロパティが役立ちます。
同様に、[**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell)プロパティはワークシート内のアクティブなセルを設定および取得するために使用されます。

水平または垂直のスクロールバーが特定のデータを表示するために行および列の索引位置にあることを確認するには、[**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow)および[**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn)プロパティを使用します。

次の例は、ワークシートをアクティブ化し、その中のアクティブなセルにします。生成された出力では、スクロールバーは、2行と2列を最初に表示されるようにスクロールします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **高度なトピック**
- [ワークシートのコピーおよび移動](/cells/ja/net/copying-and-moving-worksheets/)
- [ワークシート内のセル数を数える](/cells/ja/net/count-number-of-cells-in-the-worksheet/)
- [空のワークシートを検出する](/cells/ja/net/detecting-empty-worksheets/)
- [ワークシートがダイアログシートであるかを検索する](/cells/ja/net/find-if-the-worksheet-is-dialog-sheet/)
- [ワークシートの一意のIDを取得](/cells/ja/net/get-worksheet-unique-id/)
- [シナリオを作成、操作、またはワークシートから削除する](/cells/ja/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [ページ区切りの管理](/cells/ja/net/managing-page-breaks/)
- [ページ設定機能](/cells/ja/net/page-setup-features/)
- [ワークシートの複数のコピーを印刷する](/cells/ja/net/print-multiple-copies-of-a-worksheet/)
- [Aspose.Cellsを使用したOpenXmlのSheet.SheetIdプロパティを利用する](/cells/ja/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [ワークシートビュー](/cells/ja/net/worksheet-views/)

{{< app/cells/assistant language="csharp" >}}
