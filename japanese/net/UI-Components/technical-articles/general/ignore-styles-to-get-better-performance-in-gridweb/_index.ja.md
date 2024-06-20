---
title: GridWebでパフォーマンスを向上させるためにスタイルを無視します
type: docs
weight: 1060
url: /ja/net/aspose-cells-gridweb/ignorestylewithnodata
description: この記事では、IgnoreStyleWithNoDataを使用してGridWebでパフォーマンスを向上する方法について説明します。
keywords: GridWeb,performance
---

## **可能な使用シナリオ**
ワークブックから必要な行/列を少なく読み込むために[GridWeb.IgnoreStyleWithNoData](https://reference.aspose.com/cells/net/aspose.cells.gridweb/mainweb/ignorestylewithnodata)プロパティを使用してください。

## **ワークブックの読み込み時にパフォーマンスを向上させる**
[サンプルExcelファイル](largerowswithstyle.xlsx)を確認してください 

IgnoreStyleWithNoData = true;と設定した場合、

ご覧のように、15行（まで）とL列（まで）が表示されます。そして、最後の連続したデータのない行と列は表示されません。したがって、読み込み時間が短くなります。

![スタイルを無視したワークブック](ignorestyletrue.png)


IgnoreStyleWithNoDataをfalseに設定すると、（デフォルト値はfalseです）

見ての通り、行（最大500行）と列（最大CZ列）が表示されます

行16から行500まで、一部のセルに枠線スタイルが設定されていますが、データは含まれていません

M列からCZ列まで、一部のセルに枠線スタイルが設定されていますが、データは含まれていません

![IgnoreStyleFalseワークブック](ignorestylefalse.png)



