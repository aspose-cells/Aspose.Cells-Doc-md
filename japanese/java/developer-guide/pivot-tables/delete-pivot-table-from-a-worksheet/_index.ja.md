---
title: ワークシートからのピボットテーブルの削除
type: docs
weight: 50
url: /ja/java/delete-pivot-table-from-a-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cellsは、ワークシートからのピボットテーブルの削除や除去を行う機能を提供しています。ピボットテーブルオブジェクトまたはピボットテーブルの位置を使用してピボットテーブルを削除できます。ピボットテーブルオブジェクトを使用してピボットテーブルを削除するには、[**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable))メソッドを使用し、ピボットテーブルの位置を使用してピボットテーブルオブジェクトを削除するには、[**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int))メソッドを使用してください。

{{% /alert %}}

## **例**

次のサンプルコードは、ワークシートから2つのピボットテーブルを削除します。最初に、[**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable))メソッドを使用してピボットテーブルを削除し、次に、[**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int))メソッドを使用してピボットテーブルを削除します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeletePivotTableFromWorksheet-DeletePivotTableFromWorksheet.java" >}}
