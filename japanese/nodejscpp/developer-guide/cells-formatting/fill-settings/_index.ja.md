---  
title: 塗りつぶし設定
linktitle: 塗りつぶし設定  
description: Node.jsのためのAspose.Cellsライブラリを使って、セルの塗りつぶし設定、背景、スタイルをカスタマイズする方法を学びます。  
keywords: Aspose.Cells、セル、塗りつぶし設定、背景、スタイル、Node.jsをC++経由で  
type: docs  
weight: 50  
url: /ja/nodejs-cpp/cells-fill-settings/  
---  

## **色と背景パターン**  

Microsoft Excel では、セルの前景（輪郭）と背景（塗りつぶし）の色、および背景パターンを設定できます。  

Aspose.Cells もこれらの機能を柔軟にサポートしています。このトピックでは、Aspose.Cells を使用してこれらの機能を使用する方法について学びます。  

### **色と背景パターンの設定**  

Aspose.CellsはMicrosoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)を提供しています。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスは、Excelファイル内の各ワークシートにアクセス可能な[**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションを含みます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションを提供し、[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションの各アイテムは[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスのオブジェクトを表します。  

[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)は、セルの書式設定を取得・設定するための[**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--)および[**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-)メソッドを持ちます。[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)クラスはセルの前景色と背景色のプロパティを提供します。Aspose.Cellsは、以下に示す一連の事前定義された背景パターンのタイプを含む[**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype)列挙型を提供します。  

|**背景パターン**|**説明**|  
| :- | :- |  
|DiagonalCrosshatch| 対角線のかすかな格子状のパターンを表します|  
|DiagonalStripe| 対角線のストライプパターンを表します|  
|Gray6| 6.25% グレーのパターンを表します|  
|Gray12| 12.5% グレーのパターンを表します|  
|Gray25| 25% グレーのパターンを表します|  
|Gray50| 50% グレーのパターンを表します|  
|Gray75| 75% グレーのパターンを表します|  
|HorizontalStripe|水平ストライプパターンを表します|  
|None|背景なしを表します|  
|ReverseDiagonalStripe|反対角ストライプパターンを表します|  
|Solid|ソリッドパターンを表します|  
|ThickDiagonalCrosshatch|太い斜めクロスハッチパターンを表します|  
|ThinDiagonalCrosshatch|細い斜めクロスハッチパターンを表します|  
|ThinDiagonalStripe|細い斜めストライプパターンを表します|  
|ThinHorizontalCrosshatch|細い水平クロスハッチパターンを表します|  
|ThinHorizontalStripe|細い水平ストライプパターンを表します|  
|ThinReverseDiagonalStripe|細い逆斜めストライプパターンを表します|  
|ThinVerticalStripe|細い垂直ストライプパターンを表します|  
|VerticalStripe|垂直ストライプパターンを表します|  

以下の例では、A1セルの前景色が設定されていますが、A2は前景色と背景色の両方を垂直ストライプの背景パターンで構成するように設定されています。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-SetColorsAndBackgroundPatterns.js" >}}


### **重要なこと**  

{{% alert color="primary" %}}  

- セルの前景色または背景色を設定するには、[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトの[**setForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundColor-color-)または[**setBackgroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setBackgroundColor-color-)メソッドを使用します。これらのメソッドは、[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトの[**Pattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-)プロパティが設定されている場合にのみ有効です。  
- [**setForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundColor-color-)メソッドはセルのシェード色を設定します。  
  [**setPattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-)メソッドは、前景または背景色に使用される背景パターンのタイプを指定します。Aspose.Cellsは、一連の事前定義された背景パターンのタイプを含む[**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype)列挙型を提供します。  
- [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype)列挙型から*BackgroundType.None*を選択すると、前景色は適用されません。  
  同様に、*BackgroundType.None* または *BackgroundType.Solid* 値を選択すると、背景色は適用されません。  
- セルのシェード／塗りつぶし色を取得する場合、[**Style.setPattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) が *BackgroundType.None* であれば、[**Style.getForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#getForegroundColor--) は *Color.Empty* を返します。  

{{% /alert %}}  

### **グラデーション塗りつぶし効果の適用**  

セルにグラデーション塗りつぶし効果を適用するには、[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトの適切な[**setTwoColorGradient**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTwoColorGradient-color-color-gradientstyletype-number-)メソッドを使用します。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-ApplyGradientFillEffects.js" >}}


## **色とパレット**  

パレットとは、画像を作成するために使用可能な色の数です。プレゼンテーションで標準化されたパレットを使用することで、ユーザーは一貫した外観を作成できます。各 Microsoft Excel (97-2003) ファイルには、セル、フォント、グリッド線、グラフィックオブジェクト、塗りつぶし、およびグラフの線に適用できる 56 色のパレットがあります。  

Aspose.Cells を使用すると、パレットの既存の色だけでなく、カスタム色も使用できます。カスタム色を使用する前に、まずパレットに色を追加します。  

このトピックでは、パレットにカスタム色を追加する方法について説明します。  

### **パレットにカスタム色を追加**  

Aspose.Cells は Microsoft Excel の 56 色のパレットをサポートしています。パレットに定義されていないカスタム色を使用するには、その色をパレットに追加します。  

Aspose.CellsはMicrosoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、カスタムカラーを追加してパレットを変更するための[**changePalette**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette-color-number-)メソッドがあり、引数は次の通りです：  

- カスタムカラー、追加するカスタムカラー。  
カスタムカラーが置き換えるパレット内の色のインデックスです。0〜55の間である必要があります。  

以下の例では、カスタムカラー（Orchid）をパレットに追加し、フォントに適用する前に追加します。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-AddCustomColorsToPalette.js" >}}


{{% alert color="primary" %}}  

パレットには56色しか保持できません。パレットにカスタムカラーを追加すると、パレットが変更され、前の色でフォーマットされたファイル内の要素が変更されます。したがって、パレットを変更する際は非常に注意してください。さらに、これはXLS（Excel 97-2003）ファイル形式の制限のみであり、XLSXまたはその他の高度なMS Excel（2007/2010または2013）ファイル形式ではこのような制限はありません。  

{{% /alert %}}  

