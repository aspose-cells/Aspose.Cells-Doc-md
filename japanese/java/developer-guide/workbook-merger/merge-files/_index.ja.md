---
title: ファイルをマージ
type: docs
weight: 10
url: /ja/java/merge-files/
---
## **序章**

Aspose.Cells は、ファイルをマージするためのさまざまな方法を提供します。データ、フォーマット、数式を含む単純なファイルの場合、[**Workbook.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook) メソッドを使用して、複数のワークブックを結合できます。[**Worksheet.copy(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)) メソッドを使用して、ワークシートを新しいワークブックにコピーできます。これらの方法は使いやすく効果的ですが、マージするファイルが多数ある場合は、多くのシステム リソースが必要になることがあります。これを回避するには、複数のファイルをマージするより効率的な方法である CellsHelper.mergeFiles 静的メソッドを使用します。

## **Aspose.Cells を使用してファイルをマージする**

次のサンプル コードは、CellsHelper.mergeFiles メソッドを使用して大きなファイルをマージする方法を示しています。 MyBook1.xls と MyBook2.xls という 2 つの単純だが大きなファイルが必要です。ファイルには、書式設定されたデータと数式のみが含まれています。

{{% alert color="primary" %}}

CellsHelper.mergeFiles メソッドは、データ、スタイル、書式設定、および数式のマージのみをサポートしています。チャート、写真、コメント、その他のオブジェクトなどのオブジェクトは、この方法では結合されない場合があります。さらに、キャッシュされたファイルは、プロセスの一時データを格納するために使用されます。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
