---
title: 行または列の固定解除
linktitle: ペインの固定解除
type: docs
weight: 190
url: /ja/python-net/unfreeze-rows-or-columns-of-excel-worksheet
description: この資料では、Aspose.Cells for Python via .NET APIを使用してExcelワークシートの行、列、ペインの固定解除をプログラム的に行う方法について説明します。
keywords: Python Excelライブラリ、Pythonペイン解除、Python行の固定解除、Python列の固定解除、Pythonウィンドウの固定解除。
---

## **紹介**

この記事では、Excelファイルの行や列、またはウィンドウを非固定にする方法について学びます。Excelファイルのワークシートが凍結されている場合、ワークシートを非固定にするか凍結された行や列を調整したいことがあります。


## **Excelで行または列の固定を解除する方法**

1. 表示タブ > 固定ウィンドウ > 固定ウィンドウの解除 をクリックします。

**![Excel でのペインの固定解除](Unfreeze-Panes.png)**




## ** Aspose.Cells for Python via .NETを使えば、行や列、ペインの固定を解除するのは簡単です。{0}メソッドを使います。**
Aspose.Cells for Python via .NETを使えば、ペインの固定解除は簡単です。[**Worksheet.un_freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/un_freeze_panes/) メソッドを使用してください。

1. 凍結したファイルを開くためにワークブックを作成します。
2. Worksheet.UnFreezePanes() メソッドを使用してペインを固定解除します。
3. ファイルを保存します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Unfreeze-Pane.py" >}}

添付 [サンプルソースの Excel ファイル](Frozen.xlsx) です。
{{< app/cells/assistant language="python-net" >}}
