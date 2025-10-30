---
title: GolangをC++経由で使用したボーダー設定
linktitle: 罫線設定
description: C++でAspose.Cellsライブラリを使用してセルのボーダースタイルと色を設定する方法。幅、スタイル、色を調整してセルの外観と表示を制御します。
keywords: Aspose.Cells、セルの枠線設定、C++、枠線の幅、スタイル、色
type: docs
weight: 40
url: /ja/go-cpp/cells-border-settings/
---

## **セルにボーダーを追加する**

Microsoft Excelでは、セルに枠線を追加してセルの書式設定を行えます。枠線の種類は追加場所によって異なります。例えば、上枠線はセルのトップ位置に追加されます。ユーザーは線のスタイルや色も変更可能です。

Aspose.Cellsを使用すると、開発者はMicrosoft Excelと同様に柔軟に罫線を追加し、見た目をカスタマイズできます。

### **セルにボーダーを追加する**

Aspose.Cellsは、Microsoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)を提供します。[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)クラスにはExcelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションが含まれます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクション内の各アイテムは[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスのオブジェクトです。

Aspose.Cellsは、[**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/)メソッドを[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスに提供します。この[**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)メソッドはセルの書式設定を行うために使用されます。[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)クラスはセルに枠線を追加するためのプロパティを提供します。

#### **セルに罫線を追加**

開発者は、[**Style**](https://reference.aspose.com/cells/go-cpp/style/)オブジェクトの[**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/)コレクションを使ってセルに枠線を追加できます。枠線のタイプはインデックスとして[**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/)コレクションに渡します。すべての枠線タイプは事前に定義された[**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/)列挙型に含まれています。

**境界の列挙**

| **枠線の種類** | **説明** |
|------------------|-----------------|
| 下罫線 | 下に線を引く |
| 斜め下 | 左上から右下への斜線 |
| 斜め上 | 左下から右上への斜線 |
| 左の境界線 | 左境界線 |
| 右の境界線 | 右境界線 |
| 上の境界線 | 上境界線 |

[**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/)コレクションはすべての枠線を格納します。[**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/)コレクション内の各枠線は[**Border**](https://reference.aspose.com/cells/cpp/aspose.cells/border/)オブジェクトで表され、二つのプロパティ[**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getcolor/)と[**GetLineStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getlinestyle/)を持ち、枠線の線の色とスタイルをそれぞれ設定できます。

境界線の線の色を設定するには、Color列挙体を使用して色を選び、それを境界線オブジェクトのColorプロパティに割り当てます。

枠線のラインスタイルは、[**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/)列挙型からスタイルを選択して設定します。

**CellBorderType列挙体**

| **線のスタイル** | **説明** |
|------------------------|-------------------------------|
| DashDot | 細い破線点線 |
| DashDotDot | 細い破線点線点線 |
| Dashed | 破線 |
| Dotted | 点線 |
| Double | 二重線 |
| Hair | 細い線 |
| MediumDashDot | 中太破線点線 |
| MediumDashDotDot | 中太破線点線点線 |
| MediumDashed | 中太破線 |
| None | なし |
| Medium | 中程度の線 |
| SlantedDashDot | 傾斜した中太破線点線 |
| Thick | 太線 |
| Thin | 細線 |

線スタイルを一つ選び、それを[**Border**](https://reference.aspose.com/cells/go-cpp/border/)オブジェクトの[**GetLineStyle()**](https://reference.aspose.com/cells/go-cpp/border/getlinestyle/)プロパティに割り当てます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-BorderSettings.go" >}}
{{% alert color="primary" %}}

線のスタイルと色は同時に設定すべきです。斜めの二つの枠線は同じ線スタイルと色にします。

{{% /alert %}}

#### **セルの範囲に境界線を追加する**

1つのセルだけでなく、範囲に対して枠線を追加することも可能です。そのためには、最初に[**Cells**](https://reference.aspose.com/cells/go-cpp/cells/)コレクションの[**CreateRange**](https://reference.aspose.com/cells/go-cpp/cells/createrange/)メソッドを呼び出し、セル範囲を作成します。引数は以下の通りです：

- 最初の行、範囲の最初の行。
- 最初の列、範囲の最初の列を表す。
- 行数、範囲内の行数。
- 列数、範囲内の列数。

[**CreateRange**](https://reference.aspose.com/cells/go-cpp/cells/createrange_string_string/)メソッドは、指定されたセル範囲を含む[**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)オブジェクトを返します。[**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)オブジェクトは、範囲に枠線を追加するための引数を取る[**SetOutlineBorder**](https://reference.aspose.com/cells/cpp/aspose.cells/range/setoutlineborder/)メソッドを提供します：

- **枠線タイプ**：[**BorderType**](https://reference.aspose.com/cells/go-cpp/bordertype/)列挙型から選ばれる枠線タイプ。
- **ラインスタイル**：枠線のラインスタイル。[**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/)列挙型から選択。
- **色**、Color 列挙型から選択した線の色。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-BorderSettings-1.go" >}}
