---
title: ダイナミックチャートの作成
description: Aspose.Cells for Python via .NET で動的グラフを作成する方法を学びましょう。ガイドでは、データやシリーズ、書式設定をニーズに合わせて動的に更新する方法を示し、変化するデータを視覚的に表現できるようにします。
keywords: Aspose.Cells for Python via .NET、グラフ作成、動的グラフ、データ、シリーズ、書式設定、ワークシートの更新。
type: docs
weight: 240
url: /ja/python-net/create-dynamic-charts/
---

{{% alert color="primary" %}}

ダイナミック（またはインタラクティブ）チャートは、データのスコープを変更するとチャートが変わる能力を持っています。つまり、データソースが変更されると、動的なチャートは自動的に変更を反映できます。データソースの変更をトリガーするためには、Excelテーブルのフィルタリングオプションを使用するか、ComboBoxやドロップダウンリストなどのコントロールを使用することができます。

このこの記事は、前述の両方のアプローチを使用して動的グラフを作成するために Aspose.Cells for Python via .NET API の使用例を示します。

{{% /alert %}}

## **Excelテーブルの使用**

{{% alert color="primary" %}}

Excelのテーブルは、Aspose.Cellsの観点からListObjectsと呼ばれます。そのため、「Table」の代わりに「ListObject」という用語を使用して明確にします。 Aspose.Cells for Python via .NET APIでListObjectsを作成する方法について詳しく読むことをお勧めします。

{{% /alert %}}

ListObjectsは、ユーザー操作によりデータの並べ替えやフィルタリングを行うための組み込み機能を提供します。これらの並べ替えとフィルタリングのオプションは、自動的にヘッダー行に追加されるドロップダウンリストを通じて提供されます。これらの機能（並べ替えとフィルタリング）により、 [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) は動的チャートのデータソースとして理想的な候補となります。並べ替えやフィルタリングが変更されると、チャート内のデータの表現も変更され、現在の状態を反映します。

デモンストレーションを理解しやすくするために、以下に概説されているように始め、[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)を作成し、段階的に進めます。

1. 空の[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)を作成します。
1. 最初の[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)の[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)にアクセスします。
1. セルにデータを挿入します。
1. 挿入されたデータに基づいて[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)を作成します。
1. [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)のデータ範囲に基づいて[**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart)を作成します。
1. 結果をディスクに保存します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateDynamicCharts.py" >}}

## **動的な数式の使用**

[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) をデータソースとして使用しない場合、もう1つのオプションはExcelの関数（または数式）を使用して動的なデータ範囲を作成し、データの変更をトリガーするコントロール（ComboBoxなど）を使用することです。このシナリオでは、VLOOKUP関数を使用してComboBoxの選択に基づいて適切な値を取得します。選択が変更されると、VLOOKUP関数はセルの値を更新します。セル範囲がVLOOKUP関数を使用している場合、ユーザーの操作によって範囲全体が更新されます。したがって、ダイナミックチャートのデータソースとして使用できます。

デモンストレーションを理解しやすくするために、以下に概説されているように始め、Workbookを作成し、段階的に進めます。

1. 空の[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)を作成します。
1. 最初の[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)の[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)にアクセスします。
1. 名前付き範囲を作成してセルにデータを挿入します。このデータはダイナミックチャートのシリーズとして機能します。
1. 前のステップで作成した名前付き範囲に基づいて[**ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox)を作成します。
1. VLOOKUP関数のデータソースとして機能する範囲を作成するためにセルにさらなるデータを挿入します。
1. 適切なパラメータでVLOOKUP関数（VLOOKUP関数）をセル範囲に挿入します。この範囲はダイナミックチャートのデータソースとして機能します。
1. 前のステップで作成した範囲に基づいて[**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart)を作成します。
1. 結果をディスクに保存します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateDynamicChartsUsingDynamicFormula.py" >}}
{{< app/cells/assistant language="python-net" >}}
