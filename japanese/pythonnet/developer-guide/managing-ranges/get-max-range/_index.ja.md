---
title: ワークシート内の最大範囲を取得する
type: docs
weight: 360
url: /ja/python-net/get-max-range-in-a-worksheet/
description: この記事では、Aspose.Cells for Python via .NET ライブラリを使用して、Excel ファイルの最大範囲、最大データ範囲、最大表示範囲を取得する方法について説明します。
keywords: Python Excel ライブラリ、Python で最大範囲を取得、Python で最大データ範囲を取得、Python で最大表示範囲を取得。
---

{{% alert color="primary" %}} 

ワークシートからデータを読み取る場合、最大範囲を知る必要があります。

ワークシートからすべてのデータをコピーする場合、最大範囲を知る必要があります。

指定された範囲をhtmlやpdfにエクスポートする場合、最大範囲を知る必要があります。

Aspose.Cells for Python via .NET には、ワークシート内の最大範囲を見つけるための異なる方法が含まれています。 


{{% /alert %}} 



## **最大範囲を取得する方法**
Aspose.Cells for Python via .NET では、[**row**](https://reference.aspose.com/cells/python-net/aspose.cells/row) および [**column**](https://reference.aspose.com/cells/python-net/aspose.cells/column) オブジェクトが初期化されている場合、これらの行と列が最大領域にカウントされます。空の行または列にデータがなくても、それらが含まれます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Range.py" >}}

## **最大データ範囲を取得する方法**
ほとんどの場合、空のセルが範囲外にある場合でも、すべてのデータを含むすべての範囲を取得する必要があります。
そして、図形、テーブル、ピボットテーブルに関する設定は無視されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Data-Range.py" >}}

## **最大表示範囲を取得する方法**
ワークシートからすべてのデータをHTML、PDF、または画像にエクスポートする場合、データ、スタイル、グラフィック、表、およびピボットテーブルを含むすべての可視オブジェクトを含むエリアを取得する必要があります。
次のコードは、最大表示範囲をhtmlにレンダリングする方法を示しています：

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Display-Range.py" >}}

以下は[ソースエクセルファイル](Book1.xlsx)です。
{{< app/cells/assistant language="python-net" >}}
