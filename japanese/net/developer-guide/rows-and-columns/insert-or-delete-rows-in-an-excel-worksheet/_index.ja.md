---
title: Excelワークシートで行を挿入または削除する
type: docs
weight: 20
url: /ja/net/insert-or-delete-rows-in-an-excel-worksheet/
description: 本記事では、Excelワークシートで行を挿入および削除するためのC#コードを提供します。
keywords: c# insertまたはdelete excel worksheet、c# insertまたはdelete excel、c# insert excel、c# delete excel、c# insertまたはdelete excel worksheet with c#、c# insertまたはdelete excel with c#、c# insert excel with c#、c# delete excel with c#
---

{{% alert color="primary" %}}

新しいワークシートを作成するか、既存のワークシートを操作する際に、データを収容するために余分な行または列を追加することがあります。別の時には、ワークシート内の指定された位置から行または列を削除する必要があります。

{{% /alert %}}

Aspose.Cellsでは、行を挿入したり削除するための2つのメソッドが提供されています: [**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) と [**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index)。これらのメソッドはパフォーマンスが最適化されており、非常に迅速に作業を行います。

行を挿入または削除する場合、[**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) や [**DeleteRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow) のメソッドをループ内で使用する代わりに、常に [**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) と [**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index) のメソッドを使用することをお勧めします。

Aspose.CellsはMicrosoft Excelと同様に動作します。行または列が追加されると、ワークシートの内容は下方向や右方向にシフトされます。行または列が削除されると、ワークシートの内容は上方向や左方向にシフトされます。行が追加または削除された場合、他のワークシートやセル内の参照が更新されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
