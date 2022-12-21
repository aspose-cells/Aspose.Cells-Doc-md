---
title: パブリック API Aspose.Cells 8.0.1 の変更点
type: docs
weight: 20
url: /ja/net/public-api-changes-in-aspose-cells-8-0-1/
---
{{% alert color="primary" %}} 

これらのページには、Aspose.Cells 8.0.1 で導入された public API の変更がリストされています。これには、新しいパブリック メソッドと廃止されたパブリック メソッドだけでなく、既存のコードに影響を与える可能性のある Aspose.Cells の舞台裏での動作の変更の説明も含まれています。回帰と見なされ、既存の動作を変更する可能性のある導入された動作は特に重要であり、ここに文書化されています。

{{% /alert %}} 
## **Cells クラスに追加された MemorySetting プロパティ**
Cells クラスには、セル データのメモリ使用量を最適化するために使用できる MemorySetting プロパティが公開されているため、全体的なメモリ コストが削減されます。次の例は、最適化モードで大きなデータをワークシートに書き込む方法を示しています。

**C#**

{{< highlight "csharp" >}}

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

Workbook オブジェクトによって自動的に作成された既定のシートでは、メモリ設定は機能しません。既存のシートのメモリ設定を変更するには、データ操作を実行する前にメモリ設定を手動で適用してください。

{{% alert color="primary" %}} 

の詳細記事をご確認ください[大規模なデータ セットを操作する際のメモリの最適化](/cells/ja/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
