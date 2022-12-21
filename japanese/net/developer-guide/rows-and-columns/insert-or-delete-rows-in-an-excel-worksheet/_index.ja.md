---
title: Excel ワークシートでの行の挿入または削除
type: docs
weight: 20
url: /ja/net/insert-or-delete-rows-in-an-excel-worksheet/
description: この記事では、Excel ワークシートで行を挿入および削除する C# コードを提供します。
keywords: c# insert or delete rows in excel worksheet, c# insert or delete rows in excel, c# insert rows in excel, c# delete rows in excel, insert or delete rows in excel worksheet with c#, insert or delete rows in excel with c#, insert rows in excel with c#, delete rows in excel with c#
---
{{% alert color="primary" %}}

新しいワークシートを作成するとき、または既存のワークシートを操作するときに、データを格納するために余分な行または列を追加する必要がある場合があります。また、ワークシートの指定した位置から行または列を削除する必要がある場合もあります。

{{% /alert %}}

 Aspose.Cells は、行を挿入および削除するための 2 つの方法を提供します。[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index)と[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index).これらのメソッドは、パフォーマンスのために最適化されており、ジョブを非常に迅速に実行します。

複数の行を挿入または削除するには、常に[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index)と[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index)メソッドを使用する代わりに[**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)また[**行の削除**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow)ループ内のメソッド。

Aspose.Cells は、Microsoft Excel と同じように機能します。行または列が追加されると、ワークシートの内容が右下に移動します。行または列が削除されると、ワークシートの内容が上または左に移動します。行が追加または削除されると、他のワークシートおよびセル内のすべての参照が更新されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}
