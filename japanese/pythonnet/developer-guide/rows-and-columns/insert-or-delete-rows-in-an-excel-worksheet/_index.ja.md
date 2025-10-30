---
title: Excelワークシートで行を挿入または削除する
type: docs
weight: 20
url: /ja/python-net/insert-or-delete-rows-in-an-excel-worksheet/
description: この記事では、Aspose.Cells for Python via .NETライブラリを使用してExcelワークシートに行を挿入および削除するためのPythonコードを提供します。
keywords: Python Excelライブラリ、PythonによるExcelワークシートへの行の挿入または削除、PythonによるExcelワークシートへの行の挿入または削除、PythonによるExcelへの行の挿入、PythonによるExcelへの行の削除、PythonでのExcelワークシートへの行の挿入または削除、PythonでのExcelへの行の挿入または削除、PythonでのExcelへの行の挿入、PythonでのExcelへの行の削除
---

{{% alert color="primary" %}}

新しいワークシートを作成するか、既存のワークシートを操作する際に、データを収容するために余分な行または列を追加することがあります。別の時には、ワークシート内の指定された位置から行または列を削除する必要があります。

{{% /alert %}}

Aspose.Cells for Python via .NETは、行を挿入および削除するための2つの方法を提供しています：[**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/)および[**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/)。これらのメソッドはパフォーマンスが最適化されており、非常に迅速に作業を行います。

行を挿入または削除する場合、[**Cells.insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row) や [**delete_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_row) のメソッドをループ内で使用する代わりに、常に [**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/) と [**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/) のメソッドを使用することをお勧めします。

Aspose.Cells for Python via .NETは、Microsoft Excelと同様の方法で動作します。行または列が追加されると、ワークシートの内容は下方向および右方向にシフトされます。行または列が削除されると、ワークシートの内容は上方向または左方向にシフトされます。行が追加または削除されると、他のワークシートやセル内の参照が更新されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertDeleteRows-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
