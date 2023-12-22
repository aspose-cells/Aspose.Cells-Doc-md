---
title: ワークシートの管理
type: docs
weight: 20
url: /ja/cpp/manage-worksheets/
---
{{% alert color="primary" %}} 

開発者は、Aspose.Cells フレキシブル API を使用して、プログラムで Microsoft Excel ファイルのワークシートを簡単に作成および管理できます。このトピックでは、Microsoft Excel ファイルのワークシートを追加および削除する方法について説明します。

{{% /alert %}} 

Aspose.Cells はクラスを提供します[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。

ワークシートは次のように表されます。[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。の[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、ワークシートを管理するための幅広いメソッドを提供します。
##  **新しい Excel ファイルへのワークシートの追加**
新しい Excel ファイルをプログラムで作成するには:

1. のオブジェクトを作成します。[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。
1. 電話してください[追加](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/)の方法[ワークシートコレクション](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクション。空のワークシートが Excel ファイルに自動的に追加されます。新しいワークシートのシート インデックスを[ワークシートコレクション](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクション。
1. ワークシート参照を取得します。
1. ワークシートで作業を実行します。
1. を呼び出して、新しいワークシートを含む新しい Excel ファイルを保存します。[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラス[保存](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
##  **シートインデックスを使用したワークシートへのアクセス**
次のサンプル コードは、インデックスを指定してワークシートにアクセスまたは取得する方法を示しています。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
##  **シートインデックスを使用したワークシートの削除**
ワークシートの名前がわかっている場合、名前によるワークシートの削除はうまく機能します。ワークシートの名前がわからない場合は、オーバーロードされたバージョンのワークシートを使用してください。[削除場所](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat)シート名の代わりにワークシートのシート インデックスを取得するメソッド。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}
