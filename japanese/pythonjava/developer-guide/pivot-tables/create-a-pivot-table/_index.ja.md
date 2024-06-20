---
title: ピボットテーブルを作成する
type: docs
weight: 10
url: /ja/python-java/create-a-pivot-table/
---

## **ピボットテーブルを作成する**
Aspose.Cells for Python via Javaには、ピボットテーブルを作成する機能が提供されています。Aspose.Cellsを使用してピボットテーブルを作成するには、以下の手順に従ってください：

1. [Cell](https://reference.aspose.com/cells/python/asposecells.api/Cell)オブジェクトの[setValue](https://reference.aspose.com/cells/python/asposecells.api/cell#Value)プロパティを使用して、ワークシートセルにいくつかのデータを追加します。このデータはピボットテーブルのデータソースとして使用されます。
1. [Worksheet](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)オブジェクトにカプセル化された[PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)[add](https://reference.aspose.com/cells/python/asposecells.api/pivottablecollection#add\(java.lang.Object\))メソッドを呼び出して、ワークシートにピボットテーブルを追加します。
1. [PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)オブジェクトを[PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)から[PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)インデックスを渡してアクセスします。
1. 上記で説明したピボットテーブルオブジェクトのいずれかを[PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)オブジェクトで使用してピボットテーブルを管理します。

次のコードスニペットは、Aspose.Cells APIを使用してピボットテーブルを作成する方法を示しています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-CreatePivotTable.py" >}}
