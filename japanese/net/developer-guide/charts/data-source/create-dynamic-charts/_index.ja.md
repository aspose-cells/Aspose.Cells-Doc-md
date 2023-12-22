---
title: 動的なチャートの作成
description: Aspose.Cells for .NET で動的グラフを作成する方法を学習します。このガイドでは、要件に基づいてグラフのデータ、系列、書式設定を動的に更新し、変化するデータをワークシートに視覚的に表示できるようにする方法を説明します。
keywords: Aspose.Cells for .NET, charting, dynamic charts, data, series, formatting, worksheets, updating.
type: docs
weight: 240
url: /ja/net/create-dynamic-charts/
---
{{% alert color="primary" %}}

動的 (または対話型) グラフには、データの範囲を変更すると変更される機能があります。つまり、データ ソースが変更されると、動的チャートはその変更を自動的に反映できます。データ ソースの変更をトリガーするには、Excel テーブルのフィルター オプションを使用するか、コンボ ボックスやドロップダウン リストなどのコントロールを使用します。

この記事では、Aspose.Cells for .NET API を使用して、前述の両方のアプローチを使用して動的グラフを作成する方法を示します。

{{% /alert %}}

##  **Excel テーブルの使用**

{{% alert color="primary" %}}

Excel テーブルは、Aspose.Cells の観点では ListObject として参照されるため、明確にするために「Table」ではなく「ListObject」という用語を使用します。詳しいやり方を読んでください[リストオブジェクトを作成する](/cells/ja/net/create-and-format-table/)Aspose.Cells for .NET API で。

{{% /alert %}}

 ListObjects は、ユーザーの操作に応じてデータを並べ替えたりフィルターしたりするための組み込み機能を提供します。並べ替えとフィルターの両方のオプションは、ヘッダー行に自動的に追加されるドロップダウン リストを通じて提供されます。[**リストオブジェクト**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) 。これらの機能 (並べ替えとフィルター) により、[**リストオブジェクト**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)並べ替えやフィルタリングが変更されると、グラフ内のデータの表現が現在の状態を反映するように変更されるため、動的グラフのデータ ソースとして機能するのに最適な候補であると思われます。[**リストオブジェクト**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

デモをわかりやすくするために、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)以下に概説するように、ゼロから一歩ずつ前進してください。

1. 空のを作成する[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. にアクセスしてください[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)最初の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)の中に[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. セルにデータを挿入します。
1. 作成する[**リストオブジェクト**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)挿入されたデータに基づいて。
1. 作成する[**チャート**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)データ範囲に基づいて[**リストオブジェクト**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. 結果をディスクに保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

##  **動的数式の使用**

ご利用を希望されない場合は、[**リストオブジェクト**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)動的チャートのデータ ソースとして使用することもできます。もう 1 つのオプションは、Excel 関数 (または数式) を使用してデータの動的な範囲を作成し、コントロール (ComboBox など) を使用してデータの変更をトリガーすることです。このシナリオでは、VLOOKUP 関数を使用して、ComboBox の選択に基づいて適切な値を取得します。選択が変更されると、VLOOKUP 関数によってセルの値が更新されます。セル範囲で VLOOKUP 関数を使用している場合、ユーザー操作時に範囲全体を更新できるため、動的チャートのソースとして使用できます。

デモをわかりやすくするために、ワークブックを最初から作成し、以下に示すように段階的に進めていきます。

1. 空のを作成する[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. にアクセスしてください[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)最初の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)の中に[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. 名前付き範囲を作成して、セルにデータを挿入します。このデータは、動的チャートのシリーズとして機能します。
1. 作成する[**コンボボックス**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)前の手順で作成した名前付き範囲に基づきます。
1. VLOOKUP 関数のソースとして機能するセルにさらにデータを挿入します。
1. VLOOKUP 関数 (適切なパラメーターを含む) をセル範囲に挿入します。この範囲は、動的チャートのソースとして機能します。
1. 作成する[**チャート**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)前のステップで作成した範囲に基づきます。
1. 結果をディスクに保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
