---
title: 行と列の自動調整
type: docs
weight: 20
url: /ja/python-net/autofit-rows-and-columns/
description: この記事では、Aspose.Cells for Python via .NET APIを使用して行、列、結合セルの行、セル範囲の行を自動調整する方法を示します。
keywords: Python Excelライブラリ、Pythonの行の自動調整、Pythonの列の自動調整、セル範囲の行の自動調整、Pythonの結合セルの行の自動調整
---

{{% alert color="primary" %}}

Microsoft Excelでは、セルの幅と高さを内容に応じて自動的にサイズ変更することができます。この機能はAspose.Cells for Python via .NETを介しても利用できるため、開発者はセルの寸法を実行時に自動的にサイズ変更できます。

{{% /alert %}}

## **自動調整**

Aspose.Cells for Python via .NETにはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスが提供されています。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスにはMicrosoft Excelファイルの各ワークシートにアクセスを許可する[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスにはワークシートを管理するための多くのプロパティとメソッドが提供されています。この記事では、[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスを使用して行または列の自動調整を行う方法について説明します。

### **行の自動調整 - シンプル**

行の幅と高さを自動的にサイズ変更する最も簡単な方法は、[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスの[**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int)メソッドを呼び出すことです。[**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int)メソッドは、リサイズする行のインデックスをパラメータとして受け取ります。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsandColumns-1.py" >}}

### **セル範囲内の行を自動調整する方法**

行は多くの列から構成されています。Aspose.Cells for Python via .NETでは、[**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int)メソッドのオーバーロードバージョンを呼び出すことで、行内のセル範囲の内容に基づいて行を自動調整することができます。以下のパラメーターが必要です:

- **行インデックス**：自動調整される行のインデックス。
- **最初の列インデックス**：行の最初の列のインデックス。
- **最後の列インデックス**：行の最後の列のインデックス。

[**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int)メソッドは、行のすべての列の内容を確認してから行を自動調整します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowinSpecificRange-1.py" >}}

### **セル範囲内の列を自動調整する方法**

列は複数の行から構成されています。列内のセル範囲のコンテンツに基づいて列を自動調整することが可能です。このためには、以下のパラメータを受け取る[**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int)メソッドのオーバーロードバージョンを呼び出すことができます:

- **列インデックス**：自動調整される列のインデックス。
- **最初の行インデックス**：列の最初の行のインデックス。
- **最後の行インデックス**：列の最後の行のインデックス。

[**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int)メソッドは、列のすべての行の内容を確認してから列を自動調整します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitColumninSpecificRange-1.py" >}}

### **結合セルの行を自動調整する方法**

Aspose.Cells for Python via .NET では、[**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) API を使用してマージされたセルの行の自動調整が可能です。 [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) クラスは、マージされたセルの行を自動調整するために使用できる [**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/) プロパティを提供しています。 [**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/) は、以下のメンバーを持つ [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype) 列挙体を受け入れます。

- NONE: マージされたセルを無視します。
- FIRST_LINE: 最初の行の高さのみ拡大します。
- LAST_LINE: 最後の行の高さのみ拡大します。
- EACH_LINE: 各行の高さのみ拡大します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsforMergedCells-1.py" >}}

{{% alert color="primary" %}}

また、選択した行/列を自動調整するために、[**auto_fit_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_rows/#int-int-aspose.cells.AutoFitterOptions)および[**auto_fit_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_columns/#int-int-aspose.cells.AutoFitterOptions)メソッドのオーバーロードバージョンを使用し、必要に応じて[**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions)インスタンスを指定することもできます。

前述のメソッドのシグネチャは次のとおりです:

1. auto_fit_rows(start_row, end_row, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) オプション)
1. auto_fit_columns(first_column, last_column, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions))

{{% /alert %}}

## **重要なこと**

{{% alert color="primary" %}}

セルが結合されている場合、AutoFitメソッドは適用されません。これはMicrosoft Excelと同じ動作です。これを回避するには、自動フィルタAPIを使用します。また、セル内のテキストが折り返されている場合、AutoFitメソッドも適用されません。もう一つ覚えておくべきことは、AutoFitメソッドは時間がかかります。したがって、アプリケーションの効率を保証するために、これらのメソッドをできるだけまれに呼び出すべきです。

{{% /alert %}}

## **高度なトピック**
- [結合されたセルの行のAutoFit](/cells/ja/python-net/autofit-rows-for-merged-cells/)
{{< app/cells/assistant language="python-net" >}}
