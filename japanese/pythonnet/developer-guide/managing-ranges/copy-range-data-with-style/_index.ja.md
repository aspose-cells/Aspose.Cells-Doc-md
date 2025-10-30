---
title: スタイル付きの範囲のデータをコピーします。
type: docs
weight: 610
url: /ja/python-net/copy-range-data-with-style/
description: この記事では、Aspose.Cells for Python via .NETライブラリを使用してスタイル付きで範囲のデータをコピーする方法について説明します。
keywords: Python Excelライブラリ、スタイル付きで範囲のデータをコピーする方法、Python Excelライブラリを使用してスタイル付きで範囲のデータをコピーする方法。
---

{{% alert color="primary" %}}

[データのみをコピー](/cells/ja/python-net/copy-range-data-only/)では、セル範囲から別の範囲にデータをコピーする方法について説明し、具体的には新しいスタイルのセットを適用しました。 Aspose.Cells for Python via .NETでは、書式付きで範囲をコピーすることもできます。この記事ではその方法について説明します。

{{% /alert %}}

Aspose.Cells for Python via .NETでは、範囲を操作するためのさまざまなクラスとメソッドが提供されています。たとえば、[**create_range(upper_left_cell, lower_right_cell)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str)、[**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag)、および[**apply_style(style, flag)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/apply_style/#aspose.cells.Style-aspose.cells.StyleFlag)。

この例:

1. ワークブックを作成します。
1. 最初のワークシートのいくつかのセルにデータを入力します。
1. [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)を作成します。
1. 指定した書式属性で[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)オブジェクトを作成します。
1. データ範囲にスタイルを適用します。
1. 別のセルの範囲を作成します。
1. 最初の範囲から2番目の範囲にデータと書式をコピーします。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CopyRangeDataWithStyle-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
