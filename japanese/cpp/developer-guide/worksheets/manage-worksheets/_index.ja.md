---
title: ワークシートの管理
type: docs
weight: 20
url: /ja/cpp/manage-worksheets/
---
{{% alert color="primary" %}} 

開発者は、Aspose.Cells フレキシブル API を使用して、プログラムで Microsoft Excel ファイルのワークシートを簡単に作成および管理できます。このトピックでは、Microsoft Excel ファイルでワークシートを追加および削除する方法について説明します。

{{% /alert %}} 

Aspose.Cells はクラスを提供します[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)これは Excel ファイルを表します。の[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)クラスには[ワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス。の[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラスには、ワークシートを管理するためのさまざまなメソッドが用意されています。
## **新しい Excel ファイルへのワークシートの追加**
プログラムで新しい Excel ファイルを作成するには:

1. のオブジェクトを作成します[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス。
1. 電話する[追加](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa2bb166f57a4d8eba8e25ce1f99d0c55)の方法[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)コレクション。空のワークシートが Excel ファイルに自動的に追加されます。新しいワークシートのシート インデックスを[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)コレクション。
1. ワークシート参照を取得します。
1. ワークシートで作業を行います。
1. を呼び出して、新しいワークシートを含む新しい Excel ファイルを保存します。[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)クラス[セーブ](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)方法。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile.cpp" >}}
## **シート インデックスを使用したワークシートへのアクセス**
次のサンプル コードは、インデックスを指定して任意のワークシートにアクセスまたは取得する方法を示しています。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex.cpp" >}}
## **シート インデックスを使用してワークシートを削除する**
名前によるワークシートの削除は、ワークシートの名前がわかっている場合にうまく機能します。ワークシートの名前がわからない場合は、オーバーロードされたバージョンの[削除場所](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#addabcc7d7d76874694018fb3ba37b72c)シート名の代わりにワークシートのシート インデックスを取得するメソッド。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex.cpp" >}}
