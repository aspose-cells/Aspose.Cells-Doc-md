---
title: カラーパレットの使い方
type: docs
weight: 80
url: /ja/net/excel-color-palette/
description: C# パレットにカスタム カラーを追加し、Excel カラー パレットを使用するためのコード Aspose.Cells for .NET API
keywords: c# add custom colors to the palette, c# programmatically excel color palette, programmatically how to use color palette in workbook, c# how to use color palette in excel
---
##  **色とパレット**

パレットとは、画像の作成に使用できる色の数です。プレゼンテーションで標準化されたパレットを使用すると、ユーザーは一貫した外観を作成できます。各 Microsoft Excel (97-2003) ファイルには、グラフ内のセル、フォント、グリッド線、グラフィック オブジェクト、塗りつぶし、線に適用できる 56 色のパレットがあります。

Aspose.Cells を使用すると、パレットの既存の色だけでなく、カスタム カラーも使用できます。カスタム カラーを使用する前に、まずパレットに追加します。

このトピックでは、カスタム カラーをパレットに追加する方法について説明します。

##  **カスタムカラーをパレットに追加**

Aspose.Cells は Microsoft Excel の 56 カラー パレットをサポートします。パレットで定義されていないカスタム カラーを使用するには、そのカラーをパレットに追加します。

Aspose.Cells はクラスを提供します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、これは Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスが提供するのは[**パレットの変更**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette)このメソッドは次のパラメーターを受け取り、カスタム カラーを追加してパレットを変更します。

- カスタムカラー、追加するカスタムカラー。
- インデックス。カスタム カラーで置き換えられるパレット内の色のインデックス。 0 ～ 55 の間である必要があります。

以下の例では、カスタム カラー (Orchid) をフォントに適用する前にパレットに追加します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

パレットに保持できる色は 56 色のみです。カスタム カラーをパレットに追加すると、パレットが変更され、以前のカラーでフォーマットされたファイル内の要素が変更されます。したがって、パレットを変更するときは十分に注意してください。さらに、これは XLS (Excel 97 ～ 2003) ファイル形式のみの制限であり、XLSX またはその他の高度な MS Excel (2007/2010 または 2013) ファイル形式にはそのような制限はありません。

{{% /alert %}}