---
title: ワークシートの管理
type: docs
weight: 10
url: /ja/python-java/manage-worksheets/
---

Aspose.Cells for Python via Java を使用してワークシートを管理することは非常に簡単です。この記事では、Aspose.Cells API を使用してワークシートを追加、アクセス、および削除する方法を示します。
## **新しいExcelファイルにワークシートを追加する**
新しいワークブックを作成するには、[Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook) クラスのオブジェクトを作成します。[Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook) クラスは Excel ファイルを表します。その後、[WorksheetCollection](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection) の [add](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#add\(\)) メソッドを使用して、Excel ファイルに新しいワークシートを追加します。最後に、新しく作成した Excel ファイルを保存するために、[Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook) クラスの [save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String\)) メソッドを呼び出します。

以下のコードスニペットは、新しい Excel ファイルを作成し、それにワークシートを追加する方法を示しています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **デザイナースプレッドシートにワークシートを追加する**
デザイナー スプレッドシートにワークシートを追加する場合、新しい Excel ファイルを作成する代わりに、[Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook) クラスで既存のファイルを開きます。

以下のコードスニペットは、デザイナー スプレッドシートにワークシートを追加する方法を示しています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **シート名を使用してワークシートにアクセスする**
ワークブックを読み込んだ後、開発者はインデックスや名前を使用して任意のワークシートにアクセスすることができます。以下のコードスニペットには、名前を使用してワークシートにアクセスする方法が示されています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **ワークシートの削除**
ワークブックから一部のシートを削除する必要がある場合があります。この場合、API は [WorksheetCollection.removeAt](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\)) メソッドを提供します。シートのインデックスまたはシートの名前を渡すことができます。次の例では、シートのインデックスとシートの名前を使用してワークシートを削除する方法が示されています。
### **Sheet Indexを使用してワークシートを削除する**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **シート名を使用してワークシートを削除する**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
