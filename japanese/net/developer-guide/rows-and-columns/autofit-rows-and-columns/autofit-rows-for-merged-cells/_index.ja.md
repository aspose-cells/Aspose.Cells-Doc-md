---
title: 結合された Cells の行の自動調整
type: docs
weight: 120
url: /ja/net/autofit-rows-for-merged-cells/
---
{{% alert color="primary" %}}

Microsoft Excel には、内容に応じてセルの高さを自動調整できる機能が備わっています。この機能は行の自動調整と呼ばれます。 Microsoft Excel は、結合されたセルに自動調整操作をネイティブに設定しません。この機能は、結合されたセルにも行の自動調整を実装する必要があるユーザーにとって不可欠になることがあります。

{{% /alert %}}

##  **AutoFitMergedCellsType を使用して行を自動調整する方法**
Aspose.Cells は、[**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype/)API。この API を使用すると、結合されたセルを含むワークシート内の行を自動調整することができます。以下は、自動調整される結合セルの可能なすべてのタイプのリストです。

- なし
- ファーストライン
- 最終行
- 各行

##  **結合された Cells の行の自動調整**

次のコードを参照してください。ワークブック オブジェクトを作成し、複数のワークシートを追加します。各ワークシートの自動調整操作には異なる方法を使用します。スクリーンショットは、サンプル コードの実行後の結果を示しています。

<br>
<img src="result.png" width=80% />

##  **C# サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AutoFitRowsMergedCells-1.cs" >}}
