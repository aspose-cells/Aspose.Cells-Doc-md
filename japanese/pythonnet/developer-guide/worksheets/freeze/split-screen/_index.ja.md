---
title: Excelワークシートの画面分割
linktitle: 画面分割
type: docs
weight: 190
url: /ja/python-net/how-to-split-screen-of-excel-worksheet
description: この記事では、Aspose.Cells for Python via .NET APIを使用して、ワークシートをプログラムによって分割し、特定の行と/または列を別々のペインに表示する方法を学びます。
keywords: Python Excelライブラリ、Pythonトップ行をフリーズ、Pythonトップ行をフリーズ、Python列でワークシートを垂直に分割、Python行でワークシートを水平に分割、Pythonを4つに分割するPython、分割を削除する方法。
---

## **紹介**

この記事では、ワークシートを2つまたは4つの部分に分割し、特定の行や列を別々のウィンドウで表示する方法について学びます。大規模なデータセットを扱うときには、同じワークシートのいくつかの領域を同時に見る必要があることがあります。分割表示機能を使用して、必要な領域を比較するために同じワークシートの異なる部分を見ることができます。

## **Excelで画面を分割する方法**
ワークシートを2つまたは4つの部分に分割するには、次のようにします:

1. 分割を配置したい行/列/セルを選択します。
2. [表示]タブの[ウィンドウ]グループで、[分割]ボタンをクリックします。

**![画面分割](Split-Screen.png)**

## **列でワークシートを垂直に分割する方法**

スプレッドシートの2つの領域を垂直に分割するには、分割を表示したい列の右側の列を選択し、Excelの[分割]ボタンをクリックします。

Aspose.Cells for Python via .NETを使用して、プログラムによって簡単に列でワークシートを垂直に分割する方法は、トップ行のセルをアクティブセルとして選択するだけです。
method [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/) で分割します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Vertically-Split.py" >}}

## **行単位でワークシートを横に分割する方法**
Excelウィンドウを水平に分割するには、Excelで分割が発生する行の下の行を選択します。

Aspose.Cells for Python via .NETを使用して、プログラムによって簡単に行でワークシートを水平に分割する方法は、左側の列のセルをアクティブセルとして選択するだけです。
method [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/) で分割します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Horizontally-Split.py" >}}

## **ワークシートを4つに分割する方法**
同じワークシートの4つの異なるセクションを同時に表示するには、Excelで画面を縦横に分割します。

Aspose.Cells for Python via .NETを使用して、プログラムによって簡単に列でワークシートを垂直に分割する方法は、最初の行と列以外のセルをアクティブセルとして選択するだけです。
method [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/) で分割します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Split-Four.py" >}}

## **分割を解除する方法**
ワークシートの分割を解除するには、再び分割ボタンをクリックします。

Aspose.Cells for Python via .NETは、分割設定を削除するための[**Worksheet.remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split/)メソッドを提供しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Remove-Split.py" >}}
