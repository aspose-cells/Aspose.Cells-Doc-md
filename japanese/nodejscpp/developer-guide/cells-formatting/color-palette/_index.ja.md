---  
title: カラーパレットの使用方法
linktitle: カラーパレットの使用方法  
type: docs  
weight: 80  
url: /ja/nodejs-cpp/excel-color-palette/  
description: Aspose.Cells for Node.js via C++を使用してパレットにカスタムカラーを追加し、Excelのカラーパレットを利用するNode.jsコード。  
keywords: node.jsでパレットにカスタム色を追加、Node.jsによるExcelカラーパレットのプログラムによる操作、カラーパレットの使い方、Node.jsでExcelのカラーパレットを使う方法  
---  

## **色とパレット**  

パレットとは、画像を作成するために使用可能な色の数です。プレゼンテーションで標準化されたパレットを使用することで、ユーザーは一貫した外観を作成できます。各 Microsoft Excel (97-2003) ファイルには、セル、フォント、グリッド線、グラフィックオブジェクト、塗りつぶし、およびグラフの線に適用できる 56 色のパレットがあります。  

Aspose.Cells for Node.js via C++を使えば、既存の色だけでなくカスタムカラーも使用可能です。カスタム色を使用する前に、まずパレットに追加します。  

このトピックでは、パレットにカスタム色を追加する方法について説明します。  

## **パレットにカスタムカラーを追加する**  

Aspose.Cells は Microsoft Excel の 56 色のパレットをサポートしています。パレットに定義されていないカスタム色を使用するには、その色をパレットに追加します。  

Aspose.CellsはMicrosoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/)を提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/)クラスには、カスタムカラーを追加してパレットを変更するための[**changePalette(Color, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette-color-number-)メソッドがあり、引数は次の通りです：  

- カスタムカラー、追加するカスタムカラー。  
カスタムカラーが置き換えるパレット内の色のインデックスです。0〜55の間である必要があります。  

以下の例では、カスタムカラー（Orchid）をパレットに追加し、フォントに適用する前に追加します。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ColorPalette.js" >}}


{{% alert color="primary" %}}  

パレットには56色しか保持できません。パレットにカスタムカラーを追加すると、パレットが変更され、前の色でフォーマットされたファイル内の要素が変更されます。したがって、パレットを変更する際は非常に注意してください。さらに、これはXLS（Excel 97-2003）ファイル形式の制限のみであり、XLSXまたはその他の高度なMS Excel（2007/2010または2013）ファイル形式ではこのような制限はありません。  

{{% /alert %}}  

