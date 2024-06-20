---
title: ファイルの結合
type: docs
weight: 10
url: /ja/java/merge-files/
---

## **紹介**

Aspose.Cellsでは、ファイルをマージするための異なる方法が提供されています。単純なデータ、書式、および数式を含むファイルの場合は、[**Workbook.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook))メソッドを使用して複数のワークブックを結合したり、[**Worksheet.copy(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet))メソッドを使用してワークシートを新しいワークブックにコピーしたりできます。これらの方法は使いやすく効果的ですが、多くのファイルをマージする必要がある場合、システムリソースをかなり消費することがあります。このような場合は、より効率的なファイルのマージ方法であるCellsHelper.mergeFiles静的メソッドを使用してください。

## **Aspose.Cellsを使用してファイルをマージする**

次のサンプルコードは、CellsHelper.mergeFiles メソッドを使用して大きなファイルをマージする方法を示しています。単純ですが大きなMyBook1.xlsおよびMyBook2.xlsという2つのファイルを含みます。ファイルには、書式設定されたデータと数式のみが含まれます。

{{% alert color="primary" %}}

CellsHelper.mergeFilesメソッドは、データ、スタイル、書式、および数式のみを結合できます。このメソッドでは、グラフ、画像、コメントなどのオブジェクトは結合できない場合があります。さらに、一時データを格納するためにキャッシュファイルが使用されます。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
