---
title: マージされたセルの自動調整|
type: docs
weight: 120
url: /ja/net/autofit-rows-for-merged-cells/
---

{{% alert color="primary" %}}

Microsoft Excelには、セルの高さをその内容に合わせて自動的にサイズ変更する機能があります。この機能は自動行の調整と呼ばれます。Microsoft Excelは、マージされたセルに自動行調整を自然に設定しません。時には、この機能が本当に必要なユーザーにとって、マージされたセルに自動行の調整を実装するのが不可欠になります。

{{% /alert %}}

## **マージセルの自動調整タイプを行の自動調整に使用する方法**
Aspose.Cells は [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype/) API を介してこの機能をサポートしています。 この API を使用すると、マージセルを含むワークシートの行を自動的に調整することが可能です。 マージセルを自動調整する可能なタイプの一覧は次のとおりです：

- なし
- 先頭行
- 末尾行
- 各行

## **マージされたセルの行の自動調整**

マージセルの行の自動調整

<br>
<img src="result.png" width=80% />

## **C# サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AutoFitRowsMergedCells-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
