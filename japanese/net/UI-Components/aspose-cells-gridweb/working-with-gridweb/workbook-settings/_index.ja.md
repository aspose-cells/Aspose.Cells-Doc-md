---
title: ワークブックの設定
type: docs
weight: 250
url: /ja/net/aspose-cells-gridweb/aspose-cells-gridweb/workbook-settings/
description: この記事では、GridWebのワークブック設定について説明しています。
keywords: GridWeb,設定
---


GridWorkbookSettingsで指定できるいくつかの設定があります :


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/GridWorkbookSettings)

|**名前** |**説明** |
| :- | :- |
|MaxIteration |循環参照を解決するための最大反復回数を取得または設定します。デフォルト値は100です。
|Iteration |循環参照を解決するために反復を使用するかどうかを取得または設定します。
|ForceFullCalculate |計算がトリガーされるたびに常に完全に計算するかどうかを取得または設定します。
|CreateCalcChain |計算された数式チェーンを作成するかどうかを取得または設定します。デフォルトはfalseです。
|ReCalculateOnOpen |ファイルを開くときにすべての数式を再計算するかどうかを取得または設定します。
|PrecisionAsDisplayed |このブック内の計算が、表示されている数値の精度のみを使用して実行される場合にtrue。
|Date1904 |ブックで1904年日付システムを使用するかどうかを取得または設定します。
|CheckCustomNumberFormat |Style.Customを設定する際にカスタム数字書式をチェックするかどうかを取得または設定します。
|Author |ファイルの作者を取得および設定します。



たとえば、次のコードはReCalculateOnOpenをfalseに設定して、ファイルを開くときの計算を停止します :

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

 次のコードは、ファイルの作成者を設定します :

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}


