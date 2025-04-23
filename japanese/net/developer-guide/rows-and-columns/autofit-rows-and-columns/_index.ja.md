---
title: 行と列の自動調整
type: docs
weight: 20
url: /ja/net/autofit-rows-and-columns/
description: この記事では、Aspose.Cells for .NET APIを使用してセルの幅と高さを自動調整する方法について説明します。
keywords: 行を自動調整、列を自動調整、セル範囲内の行を自動調整、結合されたセルの行を自動調整
---

{{% alert color="primary" %}}

Microsoft Excelは、セルの幅と高さをそのコンテンツに合わせて自動的にサイズ変更する機能を提供しています。この機能は、Aspose.Cellsを通じても利用できるため、開発者は実行時にセルの寸法を自動的にサイズ変更できます。

{{% /alert %}}

## **自動調整**

Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが提供されています。この記事では、[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスを使用して行あるいは列を自動調整する方法について説明します。

### **行の自動調整 - シンプル**

行の幅と高さを自動的にサイズ変更する最も簡単な方法は、[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスの[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)メソッドを呼び出すことです。[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)メソッドは、リサイズする行のインデックスをパラメータとして受け取ります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **セル範囲内の行を自動調整する方法**

行は複数の列から構成されています。Aspose.Cellsでは、[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)メソッドのオーバーロードバージョンを呼び出すことで、セル範囲内のコンテンツに基づいて行を自動調整することが可能です。このメソッドは、以下のパラメータを受け取ります:

- **行インデックス**：自動調整される行のインデックス。
- **最初の列インデックス**：行の最初の列のインデックス。
- **最後の列インデックス**：行の最後の列のインデックス。

[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)メソッドは、行のすべての列の内容を確認してから行を自動調整します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **セル範囲内の列を自動調整する方法**

列は複数の行から構成されています。列内のセル範囲のコンテンツに基づいて列を自動調整することが可能です。このためには、以下のパラメータを受け取る[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)メソッドのオーバーロードバージョンを呼び出すことができます:

- **列インデックス**：自動調整される列のインデックス。
- **最初の行インデックス**：列の最初の行のインデックス。
- **最後の行インデックス**：列の最後の行のインデックス。

[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)メソッドは、列のすべての行の内容を確認してから列を自動調整します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **結合セルの行を自動調整する方法**

Aspose.Cellsでは、[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) APIを使用して結合されたセルの行を自動的にサイズ変更することが可能です。[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)クラスは、結合セルの行を自動調整するために使用できる[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)プロパティを提供しています。[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)は[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype)列挙体を受け入れ、以下のメンバーを持っています。

- None: 結合セルを無視します。
- FirstLine: 最初の行の高さのみを拡張します。
- LastLine: 最後の行の高さのみを拡張します。
- EachLine: 各行の高さのみを拡張します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

また、選択した行/列を自動調整するために、[**AutoFitRows**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows)および[**AutoFitColumns**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns)メソッドのオーバーロードバージョンを使用し、必要に応じて[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)インスタンスを指定することもできます。

前述のメソッドのシグネチャは次のとおりです:

1. AutoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) options)
1. AutoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) options)

{{% /alert %}}

## **重要なこと**

{{% alert color="primary" %}}

セルが結合されている場合、AutoFitメソッドは適用されません。これはMicrosoft Excelと同じ動作です。これを回避するには、自動フィルタAPIを使用します。また、セル内のテキストが折り返されている場合、AutoFitメソッドも適用されません。もう一つ覚えておくべきことは、AutoFitメソッドは時間がかかります。したがって、アプリケーションの効率を保証するために、これらのメソッドをできるだけまれに呼び出すべきです。

{{% /alert %}}

## **高度なトピック**
- [結合されたセルの行のAutoFit](/cells/ja/net/autofit-rows-for-merged-cells/)
{{< app/cells/assistant language="csharp" >}}
