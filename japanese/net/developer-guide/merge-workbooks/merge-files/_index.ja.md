---
title: ファイルをマージ
type: docs
weight: 20
url: /ja/net/merge-files/
---
## **序章**

Aspose.Cells は、ファイルをマージするためのさまざまな方法を提供します。データ、フォーマット、数式を含む単純なファイルの場合、[**Workbook.Combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine)メソッドを使用して、複数のワークブックを組み合わせることができます。[**Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index)メソッドを使用して、ワークシートを新しいブックにコピーできます。これらの方法は使いやすく効果的ですが、マージするファイルが多数ある場合は、多くのシステム リソースが必要になることがあります。これを回避するには、[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)静的メソッド、複数のファイルをマージするより効率的な方法。

## **Aspose.Cells を使用してファイルをマージする**

次のサンプル コードは、[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)方法。 Book1.xls と Book2.xls という 2 つの単純ですが大きなファイルが必要です。ファイルには、書式設定されたデータと数式のみが含まれています。

{{% alert color="primary" %}}

の[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)メソッドは、データ、スタイル、書式設定、および数式のマージのみをサポートします。チャート、写真、コメント、その他のオブジェクトなどのオブジェクトは、この方法では結合されない場合があります。さらに、キャッシュされたファイルは、プロセスの一時データを格納するために使用されます。

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}
