---
title: Aspose.Cells 8.0.1での公開API変更
type: docs
weight: 30
url: /ja/java/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

Aspose.Cells 8.0.1で導入された公開APIの変更をリストアップしています。新しいメソッドや廃止された公開メソッドだけでなく、Aspose.Cellsの背後にある動作に変更がある場合についても説明しており、既存のコードに影響を与える可能性がある場合に特に重要です。

{{% /alert %}} 
## **CellsクラスにMemorySettingプロパティを追加しました**
Cellsクラスは、セルデータのメモリ使用量を最適化するためにsetMemorySettingおよびgetMemorySettingメソッドを公開し、全体的なメモリコストを削減することができます。次の例は、最適化モードで大量のデータをワークシートに書き込む方法を示しています。

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//To change the memory setting of existing sheets, please change memory setting for them manually:

Cells cells = book.getWorksheets().get(0).getCells();

cells.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large dataset into the cells of the worksheet.

//Your code goes here

{{< /highlight >}}

{{% alert color="primary" %}} 

メモリ設定は、ワークブックによって自動的に作成されるデフォルトのシートには適用されません。既存のシートのメモリ設定を変更するには、データ操作を行う前にメモリ設定を手動で適用してください。 

{{% /alert %}} {{% alert color="primary" %}} 

詳細な記事は、[大規模なデータセットを操作する際のメモリの最適化](/cells/ja/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)をご覧ください。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
