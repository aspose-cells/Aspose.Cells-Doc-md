---
title: Microsoft Excelファイルのワークシートを管理します。
linktitle: ワークシート
type: docs
weight: 90
url: /ja/python-net/manage-worksheets/
description: この記事では、Aspose.Cells for Python via .NETのAPIを使用してMicrosoft Excelファイルのワークシートを管理する方法について説明します。
keywords: Python Excel ライブラリ、Python で Microsoft Excel ファイルのワークシートを管理する方法、Python でワークシートを追加する方法、Python でワークシートを削除する方法、Python で新しい Excel ファイルにワークシートを追加する方法、Python でデザイナースプレッドシートにワークシートを追加する方法、シート名を使用してワークシートにアクセスする方法、シート名を使用してワークシートを削除する方法、シートインデックスを使用してワークシートを削除する方法、シートをアクティブにし、セルをアクティブにする方法について説明されています。
---


{{% alert color="primary" %}}

Aspose.Cellsの柔軟なAPIを使用して、Microsoft Excelファイルでワークシートを簡単に作成、管理できます。このトピックでは、Microsoft Excelファイルにワークシートを追加および削除する方法について説明します。

{{% /alert %}}

Aspose.Cellsは、Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイルの各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスには、ワークシートを管理するための多くのプロパティやメソッドが用意されています。

## **新しい Excel ファイルにワークシートを追加する方法**

プログラムで新しいExcelファイルを作成するには：

1. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスのオブジェクトを作成します。
1. [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection)クラスの[**add**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add/#str)メソッドを呼び出します。空のワークシートがExcelファイルに自動的に追加されます。新しいワークシートのシートインデックスを[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)コレクションに渡すことで参照できます。
1. ワークシートの参照を取得します。
1. ワークシートで作業を実行します。
1. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスの[**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)メソッドを呼び出して、新しいワークシートで新しいExcelファイルを保存します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToNewExcelFile-1.py" >}}

## **デザイナースプレッドシートにワークシートを追加する方法**

デザイナースプレッドシートにワークシートを追加するプロセスは、新しいワークシートを追加するプロセスと同じですが、既存のExcelファイルがあるため、ワークシートを追加する前に開く必要があります。デザイナースプレッドシートは、[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスによって開くことができます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.py" >}}

## **シート名を使用してワークシートにアクセスする方法**

名前またはインデックスを指定して任意のワークシートにアクセスできます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AccessingWorksheetsusingSheetName-1.py" >}}

## **シート名を使用してワークシートを削除する方法**

ファイルからワークシートを削除するには、[**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection)クラスの[**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str)メソッドを呼び出します。特定のワークシートを削除するには、[**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str)メソッドにシート名を渡します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetName-1.py" >}}

## **シートインデックスを使用してワークシートを削除する方法**

ワークシートの名前がわかっている場合は、名前を使用してワークシートを削除できます。ワークシートの名前がわからない場合は、シート名の代わりにワークシートのシートインデックスを取る [**remove_by_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_index/#int) メソッドを使用します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.py" >}}

## **シートをアクティブにし、ワークシート内のセルをアクティブにする方法**

時々、ユーザーがMicrosoft ExcelファイルをExcelで開いたときに特定のワークシートをアクティブで表示する必要があります。同様に、特定のセルをアクティブにし、スクロールバーをアクティブなセルを表示するように設定することがあります。
Aspose.Cellsはこれらのすべてのタスクを実行できます。

**アクティブなシート**とは、作業中のシートのことです。タブ上のアクティブなシートの名前は、デフォルトで太字になります。

**アクティブなセル**は選択されたセルであり、タイプを始めるとデータが入力されるセルです。1度に1つのセルがアクティブです。アクティブなセルは太い枠で強調表示されます。

### **シートをアクティブにし、セルをアクティブにする方法**

Aspose.Cellsには、シートとセルをアクティブにするための特定のAPI呼び出しが用意されています。たとえば、ブック内でアクティブなシートを設定するのに[**Aspose.Cells.WorksheetCollection.active_sheet_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/active_sheet_index/)プロパティが役立ちます。
同様に、[**Aspose.Cells.Worksheet.active_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/active_cell/)プロパティはワークシート内のアクティブなセルを設定および取得するために使用されます。

水平または垂直のスクロールバーが特定のデータを表示するために行および列の索引位置にあることを確認するには、[**Aspose.Cells.Worksheet.first_visible_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_row/)および[**Aspose.Cells.Worksheet.first_visible_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_column/)プロパティを使用します。

次の例は、ワークシートをアクティブ化し、その中のアクティブなセルにします。生成された出力では、スクロールバーは、2行と2列を最初に表示されるようにスクロールします。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-MakeCellActive-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
