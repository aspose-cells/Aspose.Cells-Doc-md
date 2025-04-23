---
title: ダイナミックチャートの作成
description: Aspose.Cells for .NETにダイナミックチャートを作成する方法を学びます。当ガイドは、ワークシートでデータ、シリーズ、および書式をダイナミックに更新し、変化するデータを視覚的に表示する方法を示します。
keywords: Aspose.Cells for .NET, チャート化, ダイナミックチャート, データ, シリーズ, 書式, ワークシート, 更新
type: docs
weight: 240
url: /ja/net/create-dynamic-charts/
---

{{% alert color="primary" %}}

ダイナミック（またはインタラクティブ）チャートは、データのスコープを変更するとチャートが変わる能力を持っています。つまり、データソースが変更されると、動的なチャートは自動的に変更を反映できます。データソースの変更をトリガーするためには、Excelテーブルのフィルタリングオプションを使用するか、ComboBoxやドロップダウンリストなどのコントロールを使用することができます。

この記事では、上記のアプローチの両方を使用してダイナミックチャートを作成するためにAspose.Cells for .NET APIの使用法を実証します。

{{% /alert %}}

## **Excelテーブルの使用**

{{% alert color="primary" %}}

Aspose.Cellsの観点では、ExcelテーブルはListObjectsとして参照されるため、明確にするために「テーブル」の代わりに「ListObject」という用語を使用します。 Aspose.Cells for .NET APIを使用して[ListObjectsの作成](/cells/ja/net/create-and-format-table/)方法について詳しくお読みください。

{{% /alert %}}

ListObjectsは、ユーザーの操作に基づいてデータをソートおよびフィルタリングするための組み込み機能を提供します。ソートおよびフィルタリングオプションは、ヘッダー行に自動的に追加されるドロップダウンリストを介して提供されます。これらの機能（ソートおよびフィルタリング）のため、ListObjectsはデータソースとしてダイナミックチャートに最適な候補のように見えます。ソートまたはフィルタリングが変更されると、チャート上のデータの表現も変更されて現在のListObjectの状態を反映します。

デモンストレーションを理解しやすくするために、以下に概説されているように始め、[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)を作成し、段階的に進めます。

1. 空の[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)を作成します。
1. 最初の[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)の[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)にアクセスします。
1. セルにデータを挿入します。
1. 挿入されたデータに基づいて[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)を作成します。
1. [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)のデータ範囲に基づいて[**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)を作成します。
1. 結果をディスクに保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

## **動的な数式の使用**

[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) をデータソースとして使用しない場合、もう1つのオプションはExcelの関数（または数式）を使用して動的なデータ範囲を作成し、データの変更をトリガーするコントロール（ComboBoxなど）を使用することです。このシナリオでは、VLOOKUP関数を使用してComboBoxの選択に基づいて適切な値を取得します。選択が変更されると、VLOOKUP関数はセルの値を更新します。セル範囲がVLOOKUP関数を使用している場合、ユーザーの操作によって範囲全体が更新されます。したがって、ダイナミックチャートのデータソースとして使用できます。

デモンストレーションを理解しやすくするために、以下に概説されているように始め、Workbookを作成し、段階的に進めます。

1. 空の[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)を作成します。
1. 最初の[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)の[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)にアクセスします。
1. 名前付き範囲を作成してセルにデータを挿入します。このデータはダイナミックチャートのシリーズとして機能します。
1. 前のステップで作成した名前付き範囲に基づいて[**ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)を作成します。
1. VLOOKUP関数のデータソースとして機能する範囲を作成するためにセルにさらなるデータを挿入します。
1. 適切なパラメータでVLOOKUP関数（VLOOKUP関数）をセル範囲に挿入します。この範囲はダイナミックチャートのデータソースとして機能します。
1. 前のステップで作成した範囲に基づいて[**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)を作成します。
1. 結果をディスクに保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
{{< app/cells/assistant language="csharp" >}}
