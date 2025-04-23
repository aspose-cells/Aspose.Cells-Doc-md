---
title: Aspose.Cells 8.0.1での公開API変更
type: docs
weight: 20
url: /ja/net/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

Aspose.Cells 8.0.1で導入された公開APIの変更をリストアップしています。新しいメソッドや廃止された公開メソッドだけでなく、Aspose.Cellsの背後にある動作に変更がある場合についても説明しており、既存のコードに影響を与える可能性がある場合に特に重要です。

{{% /alert %}} 
## **CellsクラスにMemorySettingプロパティが追加されました**
Cellsクラスに公開されたMemorySettingプロパティは、セルデータのメモリ使用を最適化し、全体的なメモリコストを減らすために使用できます。次の例は、最適化モードで大量のデータをワークシートに書き込む方法を示しています。

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences

book.Settings.MemorySetting = MemorySetting.MemoryPreference;

//To change the memory setting of existing sheets, please change memory setting for them manually:

Cells cells = book.Worksheets[0].Cells;

cells.MemorySetting = MemorySetting.MemoryPreference;

//Input large dataset into the cells of the worksheet

//Your code goes here

{{< /highlight >}}

メモリ設定は、Workbookオブジェクトによって自動的に作成されるデフォルトのシートには自動的に適用されません。既存のシートのメモリ設定を変更するには、データ操作を行う前にメモリ設定を手動で適用してください。

{{% alert color="primary" %}} 

[大規模なデータセットを使用する際のメモリ使用量の最適化](/cells/ja/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)に関する詳細な記事をご覧ください。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
