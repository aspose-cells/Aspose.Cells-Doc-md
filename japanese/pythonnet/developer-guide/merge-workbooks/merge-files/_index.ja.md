---
title: ファイルの結合
type: docs
weight: 20
url: /ja/python-net/merge-files/
---

## **紹介**

Aspose.Cells for Python via .NETは、ファイルをマージするさまざまな方法を提供します。データ、書式設定、式が含まれるシンプルなファイルの場合、[**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine)メソッドを使用して複数のブックを結合し、[**Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy)メソッドを使用してワークシートを新しいブックにコピーできます。これらの方法は使いやすく効果的ですが、多くのファイルをマージする場合、システムリソースを多く消費することがあります。これを避けるために、より効率的な静的メソッド[**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files)を使用してください。

## **Aspose.Cells for Python via .NETを使ったファイル統合**

次のサンプルコードは、[**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files)メソッドを使用して大きなファイルを結合する方法を説明しています。単純ながらも大きなBook1.xlsとBook2.xlsという2つの大きなファイルが含まれています。これらのファイルには、フォーマット済みのデータと数式のみが含まれています。

{{% alert color="primary" %}}

[**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files)メソッドは、データ、スタイル、書式、数式の結合のみをサポートしています。チャート、図、コメントなどのオブジェクトは、このメソッドを使用して結合することはできません。さらに、一時的なデータを処理するためのキャッシュファイルが使用されます。

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CellsHelperClass-MergeFiles-1.py" >}}

