---
title: ピボット テーブルを作成する
type: docs
weight: 10
url: /ja/python-java/create-a-pivot-table/
---
## **ピボット テーブルを作成する**
Aspose.Cells for Python via Java は、ピボット テーブルを作成する機能を提供します。 Aspose.Cells を使用してピボット テーブルを作成するには、次の手順に従ってください。

1. を使用してワークシートのセルにデータを追加します。[Cell](https://reference.aspose.com/cells/python/asposecells.api/Cell)オブジェクトの[setValue](https://reference.aspose.com/cells/python/asposecells.api/cell#Value)財産。このデータは、ピボット テーブルのデータ ソースとして使用されます。
1. を呼び出して、ワークシートにピボット テーブルを追加します。[ピボットテーブル コレクション](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)[追加](https://reference.aspose.com/cells/python/asposecells.api/pivottablecollection#add\(java.lang.Object\)メソッド、カプセル化された[ワークシート](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)物体。
1. アクセス[ピボットテーブル](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)からのオブジェクト[ピボットテーブル コレクション](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)を渡すことで[ピボットテーブル](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)索引。
1. にカプセル化されたピボット テーブル オブジェクト (上記で説明) のいずれかを使用します。[ピボットテーブル コレクション](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)ピボット テーブルを管理するオブジェクト。

次のコード スニペットは、Aspose.Cells API を使用してピボット テーブルを作成する方法を示しています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-CreatePivotTable.py" >}}
