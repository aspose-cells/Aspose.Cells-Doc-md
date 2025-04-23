---
title: カラーパレットの使用方法
type: docs
weight: 80
url: /ja/net/excel-color-palette/
description: パレットにカスタムカラーを追加してAspose.Cells for .NET APIを使ってExcelのカラーパレットを使用するC#コード
keywords: カラーパレットにカスタムカラーを追加する、C#でプログラム的にExcelのカラーパレットを使用する、ワークブックでカラーパレットを使用する方法、C#でExcelのカラーパレットを使用する方法
---

## **色とパレット**

パレットとは、画像を作成するために使用可能な色の数です。プレゼンテーションで標準化されたパレットを使用することで、ユーザーは一貫した外観を作成できます。各 Microsoft Excel (97-2003) ファイルには、セル、フォント、グリッド線、グラフィックオブジェクト、塗りつぶし、およびグラフの線に適用できる 56 色のパレットがあります。

Aspose.Cells を使用すると、パレットの既存の色だけでなく、カスタム色も使用できます。カスタム色を使用する前に、まずパレットに色を追加します。

このトピックでは、パレットにカスタム色を追加する方法について説明します。

## **パレットにカスタムカラーを追加する**

Aspose.Cells は Microsoft Excel の 56 色のパレットをサポートしています。パレットに定義されていないカスタム色を使用するには、その色をパレットに追加します。

Aspose.Cells は、Microsoft Excel ファイルを表す [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) クラスには、パレットを変更するための [**ChangePalette**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) メソッドがあり、カスタム色を追加するために次のパラメータを取ります:

- カスタムカラー、追加するカスタムカラー。
カスタムカラーが置き換えるパレット内の色のインデックスです。0〜55の間である必要があります。

以下の例では、カスタムカラー（Orchid）をパレットに追加し、フォントに適用する前に追加します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

パレットには56色しか保持できません。パレットにカスタムカラーを追加すると、パレットが変更され、前の色でフォーマットされたファイル内の要素が変更されます。したがって、パレットを変更する際は非常に注意してください。さらに、これはXLS（Excel 97-2003）ファイル形式の制限のみであり、XLSXまたはその他の高度なMS Excel（2007/2010または2013）ファイル形式ではこのような制限はありません。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
