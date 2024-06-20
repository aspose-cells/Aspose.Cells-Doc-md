---
title: ワークシートの管理
type: docs
weight: 20
url: /ja/cpp/manage-worksheets/
---

{{% alert color="primary" %}} 

開発者は、Aspose.Cellsの柔軟なAPIを使用してMicrosoft Excelファイルでワークシートを簡単に作成および管理できます。このトピックでは、Microsoft Excelファイルでワークシートを追加および削除する方法について説明します。

{{% /alert %}} 

Aspose.Cellsは、Excelファイルを表す[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスを提供しており、[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスにはExcelファイル内の各ワークシートにアクセスできる[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) コレクションが含まれています。

ワークシートは、[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスで表されます。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスには、ワークシートを管理するための幅広いメソッドが提供されています。
## **新しいExcelファイルにワークシートを追加する**
プログラムで新しいExcelファイルを作成するには：

1. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスのオブジェクトを作成します。
1. [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) コレクションの[Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) メソッドを呼び出します。空のワークシートがExcelファイルに自動的に追加されます。新しいワークシートのシートインデックスを[WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) コレクションに渡すことで参照できます。
1. ワークシートの参照を取得します。
1. ワークシートで作業を実行します。
1. 新しいワークシートを含む新しいExcelファイルを[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスの [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) メソッドを呼び出して保存します。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
## **Sheet Indexを使用してワークシートにアクセスする**
次のサンプルコードは、インデックスを指定して任意のワークシートにアクセスまたは取得する方法を示しています。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
## **Sheet Indexを使用してワークシートを削除する**
ワークシートの名前がわかっている場合は、ワークシートの名前を使用してワークシートを削除することができます。ワークシートの名前がわからない場合は、ワークシートの名前の代わりにワークシートのシートインデックスを取る[RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat) メソッドのオーバーロードバージョンを使用します。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}
