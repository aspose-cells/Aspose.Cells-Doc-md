---
title: ピボットテーブルでのデータフィールドの表示形式を操作する
type: docs
weight: 140
url: /ja/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Aspose.Cells for Python via .NETでPythonのPivot TableのDataFieldのデータ表示形式をどのように扱うか
keywords: Aspose.Cells for Python Excel、Excel Pythonライブラリ、PivotテーブルのDataFieldのデータ表示形式を扱う
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETはすべてのDataFieldのデータ表示形式をサポートしています

{{% /alert %}}

## **「最小から最大へのランク」と「最大から最小へのランク」の表示形式オプションを設定する方法**

Aspose.Cells for Python via .NETでは、ランク最大から最小への表示形式オプションを設定するために、[**PivotField.data_display_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/data_display_format/) プロパティが提供されています。最大から最小へのランクを設定するには、[**PivotField.data_display_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/data_display_format/) プロパティを[**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfielddatadisplayformat/) に設定することができます。次のコードスニペットは表示形式オプションの設定を示しています。

サンプルソースと出力ファイルは、テスト用のサンプルコードをダウンロードできます:

[ソースExcelファイル](101089332.xlsx)

[出力Excelファイル](101089333.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTableDataDisplayFormatRanking-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
