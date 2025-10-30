---
title: Golang経由でC++を使いワークシートからピボットテーブルを削除
linktitle: ピボットテーブルを削除
type: docs
weight: 60
url: /ja/go-cpp/delete-pivot-table-from-a-worksheet/
description: Aspose.Cells を使ったC++コードによるエクセルワークシートからのピボットテーブル削除。
keywords: C++でワークシートからピボットテーブルを削除、C++でエクセルからピボットテーブルを削除、C++を使ったピボットテーブルの削除方法、ピボットテーブルを削除、エクセルからピボットテーブルを削除する方法、C++でピボットテーブルの削除、C++によるピボットテーブル削除、ピボットテーブルを削除
---

{{% alert color="primary" %}}

Aspose.Cellsでは、ワークシートからピボットテーブルを削除する機能が提供されています。ピボットテーブルオブジェクトやピボットテーブルの位置を使用して削除できます。

{{% /alert %}}

次のサンプルコードは、ワークシートから2つのピボットテーブルを削除します。最初に [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/go-cpp/pivottablecollection/remove_pivottable/) メソッドを使ってピボットテーブルを削除し、その後 [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) メソッドを使ってもう一つのピボットテーブルを削除します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeletePivotTableFromAWorksheet.go" >}}
