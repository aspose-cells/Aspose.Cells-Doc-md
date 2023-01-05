---
title: ワークシートの管理
type: docs
weight: 10
url: /ja/python-java/manage-worksheets/
---
Aspose.Cells for Python via Java を使用したワークシートの管理は非常に簡単です。この記事では、Aspose.Cells API を使用したワークシートの追加、アクセス、および削除について説明します。
## **新しい Excel ファイルへのワークシートの追加**
新しい Workbook を作成するには、[ワークブック](https://reference.aspose.com/cells/python/asposecells.api/Workbook)クラス。の[ワークブック](https://reference.aspose.com/cells/python/asposecells.api/Workbook)クラスは Excel ファイルを表します。次に、[追加](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#add\(\) の方法[ワークシート コレクション](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection) 、新しいワークシートが Excel ファイルに追加されます。最後に、新しく作成した Excel ファイルを保存するには、[セーブ](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String\) の方法[ワークブック](https://reference.aspose.com/cells/python/asposecells.api/Workbook)クラス。

次のコード スニペットは、新しい Excel ファイルを作成し、それにワークシートを追加する方法を示しています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **Designer スプレッドシートへのワークシートの追加**
ワークシートをデザイナー スプレッドシートに追加することは、ワークシートを新しい Excel ファイルに追加することとまったく同じです。唯一の違いは、新しい Excel ファイルを作成する代わりに、既存のファイルを開くことです。[ワークブック](https://reference.aspose.com/cells/python/asposecells.api/Workbook)クラス。

次のコード スニペットは、ワークシートをデザイナー スプレッドシートに追加する方法を示しています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **シート名を使用してワークシートにアクセスする**
ワークブックを読み込んだ後、開発者はインデックスまたは名前を使用して任意のワークシートにアクセスできます。次のコード スニペットは、名前を使用してワークシートにアクセスする方法を示しています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **ワークシートの削除**
一部のシートがワークブックから削除される場合があります。このために、API は[WorksheetCollection.removeAt](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\)） 方法。削除するシートのシート インデックスまたはシート名を渡すことができます。次の例は、シート インデックスとシート名を使用してワークシートを削除する方法を示しています。
### **シート インデックスを使用してワークシートを削除する**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **シート名を使用してワークシートを削除する**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
