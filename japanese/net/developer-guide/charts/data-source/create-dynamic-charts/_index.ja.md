---
title: ダイナミック チャートの作成
type: docs
weight: 240
url: /ja/net/create-dynamic-charts/
---
{{% alert color="primary" %}}

動的 (または対話型) グラフには、データの範囲を変更すると変化する機能があります。つまり、動的グラフは、データ ソースが変更されたときに変更を自動的に反映できます。データ ソースの変更をトリガーするには、Excel テーブルのフィルター オプションを使用するか、ComboBox やドロップダウン リストなどのコントロールを使用できます。

この記事では、Aspose.Cells for .NET API を使用して、前述の両方のアプローチを使用して動的チャートを作成する方法を示します。

{{% /alert %}}

## **Excel テーブルの使用**

{{% alert color="primary" %}}

 Excel テーブルは Aspose.Cells' パースペクティブでは ListObjects と呼ばれるため、明確にするために「テーブル」ではなく「ListObject」という用語を使用します。詳しい方法をお読みください[ListObject を作成する](/cells/ja/net/create-and-format-table/)Aspose.Cells for .NET API で。

{{% /alert %}}

ListObjects は、ユーザーの操作に基づいてデータを並べ替えおよびフィルター処理する組み込み機能を提供します。並べ替えとフィルタリングの両方のオプションは、ヘッダー行に自動的に追加されるドロップダウン リストから提供されます。[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) .これらの機能 (並べ替えとフィルタリング) により、[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)並べ替えやフィルタリングが変更されると、チャート内のデータの表現が変更され、現在の状態を反映するため、ダイナミック チャートのデータ ソースとして機能するのに最適な候補と思われます。[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

デモンストレーションを理解しやすくするために、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)以下に概説するように、ゼロから一歩一歩前進します。

1. 空の作成[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. アクセス[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)最初の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)の中に[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. セルにデータを挿入します。
1. 作成[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)挿入されたデータに基づいています。
1. 作成[**チャート**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)のデータ範囲に基づく[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. 結果をディスクに保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

## **動的数式の使用**

ご利用を希望されない場合[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)ダイナミック チャートのデータ ソースとして、もう 1 つのオプションは、Excel 関数 (または数式) を使用してデータのダイナミック レンジを作成し、コントロール (ComboBox など) を使用してデータの変更をトリガーすることです。このシナリオでは、VLOOKUP 関数を使用して、ComboBox の選択に基づいて適切な値をフェッチします。選択が変更されると、VLOOKUP 関数はセルの値を更新します。セルの範囲が VLOOKUP 関数を使用している場合、ユーザーの操作で範囲全体を更新できるため、ダイナミック チャートのソースとして使用できます。

デモンストレーションを理解しやすくするために、ワークブックを最初から作成し、以下に概説するように段階的に進めます。

1. 空の作成[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. アクセス[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)最初の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)の中に[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. 名前付き範囲を作成して、セルにデータを挿入します。このデータは、ダイナミック チャートのシリーズとして機能します。
1. 作成[**コンボボックス**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)前の手順で作成した名前付き範囲に基づいています。
1. VLOOKUP 関数のソースとなるセルにさらにデータを挿入します。
1. VLOOKUP 関数を (適切なパラメーターを使用して) セル範囲に挿入します。この範囲は、ダイナミック チャートのソースとして機能します。
1. 作成[**チャート**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)前のステップで作成された範囲に基づいています。
1. 結果をディスクに保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
