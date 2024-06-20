---
title: ファイルの結合
type: docs
weight: 20
url: /ja/net/merge-files/
---

## **紹介**

Aspose.Cellsでは、ファイルを結合するための異なる方法が提供されています。データ、書式、数式を含む単純なファイルの場合は、[**Workbook.Combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine)メソッドを使用して複数のブックを結合し、[**Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index)メソッドを使用してワークシートを新しいブックにコピーすることができます。これらの方法は使いやすく効果的ですが、多くのファイルを結合する場合は、多くのシステムリソースを消費する可能性があります。このような場合は、より効率的な方法である[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)静的メソッドを使用します。

## **Aspose.Cellsを使用してファイルをマージする**

次のサンプルコードは、[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)メソッドを使用して大きなファイルを結合する方法を説明しています。単純ながらも大きなBook1.xlsとBook2.xlsという2つの大きなファイルが含まれています。これらのファイルには、フォーマット済みのデータと数式のみが含まれています。

{{% alert color="primary" %}}

[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)メソッドは、データ、スタイル、書式、数式の結合のみをサポートしています。チャート、図、コメントなどのオブジェクトは、このメソッドを使用して結合することはできません。さらに、一時的なデータを処理するためのキャッシュファイルが使用されます。

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}
