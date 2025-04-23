---
title: カラーパレットの使用方法
type: docs
weight: 80
url: /ja/python-net/excel-color-palette/
description: Pythonコードでカスタム色をパレットに追加し、Aspose.Cells for Python via .NET APIのExcelカラーパレットを使用する方法
keywords: Pythonでカスタム色をパレットに追加する、Pythonでプログラム的にExcelのカラーパレットを操作、ワークブック内のカラーパレットの使い方、PythonでExcelのカラーパレットを操作する方法
---

## **色とパレット**

パレットとは、画像を作成するために使用可能な色の数です。プレゼンテーションで標準化されたパレットを使用することで、ユーザーは一貫した外観を作成できます。各 Microsoft Excel (97-2003) ファイルには、セル、フォント、グリッド線、グラフィックオブジェクト、塗りつぶし、およびグラフの線に適用できる 56 色のパレットがあります。

Aspose.Cells for Python via .NETを使用すれば、既存のパレットの色だけでなく、カスタムカラーも使用できます。カスタムカラーを使う前に、最初にパレットに追加してください。

このトピックでは、パレットにカスタム色を追加する方法について説明します。

## **パレットにカスタムカラーを追加する**

Aspose.Cells for Python via .NETは、Microsoft Excelの56色パレットをサポートしています。パレットに定義されていないカスタムカラーを使用するには、その色をパレットに追加してください。

Aspose.Cells for Python via .NETは、Microsoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、次のパラメータを受け取ってパレットを変更するカスタムカラーを追加するための[**change_palette**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/change_palette)メソッドがあります：

- カスタムカラー、追加するカスタムカラー。
カスタムカラーが置き換えるパレット内の色のインデックスです。0〜55の間である必要があります。

以下の例では、カスタムカラー（Orchid）をパレットに追加し、フォントに適用する前に追加します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndPalette-1.py" >}}

{{% alert color="primary" %}}

パレットには56色しか保持できません。パレットにカスタムカラーを追加すると、パレットが変更され、前の色でフォーマットされたファイル内の要素が変更されます。したがって、パレットを変更する際は非常に注意してください。さらに、これはXLS（Excel 97-2003）ファイル形式の制限のみであり、XLSXまたはその他の高度なMS Excel（2007/2010または2013）ファイル形式ではこのような制限はありません。

{{% /alert %}}

