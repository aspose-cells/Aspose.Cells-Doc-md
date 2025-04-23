---
title: ファイルの結合
type: docs
weight: 10
url: /ja/java/merge-files/
---

## **紹介**

Aspose.Cellsはファイルをマージするさまざまな方法を提供します。データ、フォーマット、数式が含まれるシンプルなファイルを結合するには [**Workbook.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine-com.aspose.cells.Workbook-) メソッドを使用し、[**Worksheet.copy(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy-com.aspose.cells.Worksheet-)メソッドでワークシートを新しいブックにコピーできます。これらの方法は簡単に使え効果的ですが、多くのファイルをマージする場合はシステムリソースを大量に使用する可能性があります。これを避けるために、CellsHelper.mergeFilesの静的メソッドを使用してください。これは複数のファイルを効果的にマージするより効率的な方法です。

## **Aspose.Cellsを使用してファイルをマージする**

次のサンプルコードは、CellsHelper.mergeFiles メソッドを使用して大きなファイルをマージする方法を示しています。単純ですが大きなMyBook1.xlsおよびMyBook2.xlsという2つのファイルを含みます。ファイルには、書式設定されたデータと数式のみが含まれます。

{{% alert color="primary" %}}

CellsHelper.mergeFilesメソッドは、データ、スタイル、書式、および数式のみを結合できます。このメソッドでは、グラフ、画像、コメントなどのオブジェクトは結合できない場合があります。さらに、一時データを格納するためにキャッシュファイルが使用されます。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
{{< app/cells/assistant language="java" >}}
