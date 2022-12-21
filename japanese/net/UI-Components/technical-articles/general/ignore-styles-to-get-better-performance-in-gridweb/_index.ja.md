---
title: GridWeb でのパフォーマンスを向上させるためにスタイルを無視する
type: docs
weight: 1060
url: /ja/net/aspose-cells-gridweb/ignorestylewithnodata
description: この記事では、IgnoreStyleWithNoData を使用して Aspose.Cells.GridWeb ライブラリのパフォーマンスを向上させる方法について説明します。
keywords: performance
---
## **考えられる使用シナリオ**
使ってください[GridWeb.IgnoreStyleWithNoData](https://reference.aspose.com/cells/net/aspose.cells.gridweb/mainweb/ignorestylewithnodata)ワークブックから必要性の低い行/列をロードするプロパティ。
 
## **ワークブックの読み込み中にパフォーマンスを向上させる**
を確認してください[サンプルエクセルファイル](largerowswithstyle.xlsx) 

IgnoreStyleWithNoData = true に設定した場合。

ご覧のとおり、行 (15 まで) と列 (L まで) が表示されます。セルにデータがない最後の連続行と列は表示されません。したがって、ロード時間は短くなります。

![スタイルを無視するワークブック](ignorestyletrue.png)


IgnoreStyleWithNoData = false; に設定した場合 (デフォルト値は false)

ご覧のとおり、はるかに多くの行 (500 まで) と列 (CZ まで) を示しています。

行 16 から行 500 まで、いくつかのセルは罫線スタイルを設定していますが、セルにはデータが含まれていません。

列 M から列 CZ まで、いくつかのセルに境界線スタイルが設定されていますが、セルにはデータが含まれていません。

![スタイルを無視しないワークブック](ignorestylefalse.png)
 
 
 