---
title: マージされたセルの自動調整|
type: docs
weight: 120
url: /ja/python-net/autofit-rows-for-merged-cells/
description: この記事では、Aspose.Cells for Python via .NET API を使用してマージセルの行を自動調整する方法を示しています。
keywords: Python Excel ライブラリ、Python 自動行の自動調整に AutoFitMergedCellsType の使用方法、Python でマージセルの行を自動調整。
---

{{% alert color="primary" %}}

Microsoft Excelには、セルの高さをその内容に合わせて自動的にサイズ変更する機能があります。この機能は自動行の調整と呼ばれます。Microsoft Excelは、マージされたセルに自動行調整を自然に設定しません。時には、この機能が本当に必要なユーザーにとって、マージされたセルに自動行の調整を実装するのが不可欠になります。

{{% /alert %}}

## **マージセルの自動調整タイプを行の自動調整に使用する方法**
Aspose.Cells for Python via .NET は [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype/) を使用してこの機能をサポートしています。この API を使用すると、マージセルを含むワークシートの行を自動的に調整することができます。以下に、マージセルの自動調整のすべての可能なタイプの一覧を示します。

- NONE
- 最初の行
- 最終行
- 各行

## **マージされたセルの行の自動調整**

マージセルの行の自動調整

<br>
<img src="result.png" width=80% />

## **C# サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutoFitRowsMergedCells-1.py" >}}
