---
title: ワークブックの設定
type: docs
weight: 250
url: /ja/net/aspose-cells-gridweb/workbook-settings/
description: この記事では、GridWeb のブック設定について説明します。
keywords: settings
---
set GridWorkbookSettings で指定できる設定がいくつかあります。

 
- **[GridWorkbookSettings](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/GridWorkbookSettings)**

|**名前** |**説明** |
|:- |:- |
| MaxIteration|循環参照を解決するための最大反復回数を取得または設定します。既定値は 100 です。|
|反復|繰り返しを使用して循環参照を解決するかどうかを取得または設定します。|
| ForceFullCalculate|計算がトリガーされるたびに完全に計算するかどうかを取得または設定します。|
| CreateCalcChain|計算式チェーンを作成するかどうかを取得または設定します。デフォルトは false です。|
| ReCalculateOnOpen|ファイルを開くときにすべての数式を再計算するかどうかを取得または設定します。|
| PrecisionAsDisplayed|このブックの計算が、表示されている数値の精度のみを使用して実行される場合は True|
| 1904年|ブックが 1904 日付システムを使用しているかどうかを表す値を取得または設定します。|
| CheckCustomNumberFormat| Style.Custom を設定するときにカスタム数値形式をチェックするかどうかを取得または設定します。|
|著者|ファイルの作成者を取得および設定します。|
 


たとえば、次のコードは ReCalculateOnOpen を false に設定して、ファイルを開くときに caculate を停止します。

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

次のコードは、ファイルの作成者を設定します。

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}
 
 