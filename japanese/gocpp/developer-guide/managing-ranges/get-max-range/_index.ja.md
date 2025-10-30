---
title: Golango経由でワークシートの最大範囲を取得
linktitle: ワークシート内の最大範囲を取得する
type: docs
weight: 360
url: /ja/go-cpp/get-max-range-in-a-worksheet/
description: この記事は、Aspose.Cells for C++ライブラリを使用してExcelファイルの最大範囲、最大データ範囲、最大表示範囲を取得する方法について説明します。
---

{{% alert color="primary" %}} 

ワークシートからデータを読み取る場合、最大範囲を知る必要があります。

ワークシートからすべてのデータをコピーする場合、最大範囲を知る必要があります。

HTMLおよびPDFに指定された範囲をエクスポートする際、最大範囲を把握する必要があります。

Aspose.Cells for C++には、ワークシートの最大範囲を見つけるさまざまな方法が含まれています。 

{{% /alert %}} 

## **最大範囲を取得する**
Aspose.Cellsでは、[**Row**](https://reference.aspose.com/cells/go-cpp/row/)と[**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/)オブジェクトが初期化されている場合、空の行や列にデータがなくても、これらの行と列が最大範囲としてカウントされます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange.go" >}}
## **最大データ範囲を取得する**
ほとんどの場合、空のセルが範囲外にある場合でも、すべてのデータを含むすべての範囲を取得する必要があります。
また、シェイプ、テーブル、ピボットテーブルに関する設定は無視されます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange-1.go" >}}
## **最大表示範囲を取得する**
ワークシートからすべてのデータをHTML、PDF、または画像にエクスポートする場合、データ、スタイル、グラフィック、表、およびピボットテーブルを含むすべての可視オブジェクトを含むエリアを取得する必要があります。
以下のコードは、最大表示範囲をHTMLにレンダリングする方法を示しています：

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange-2.go" >}}
以下は[ソースエクセルファイル](Book1.xlsx)です。
