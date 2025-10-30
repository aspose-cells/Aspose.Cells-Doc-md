---
title: Excelワークシートのウィンドウ枠の固定
linktitle: ウィンドウ枠の固定
type: docs
weight: 190
url: /ja/python-net/how-to-freeze-panes-of-excel-worksheet
description: この記事では、Aspose.Cells for Python via .NET APIを使用してExcelワークシートのペーンをプログラムで固定してスクロールする方法について学びます。
keywords: Python Excelライブラリ、Pythonでペーンを固定、ウィンドウを固定 in Python。
---

## **紹介**

この記事では、ペインの固定方法を学びます。共通の見出しの下に大量のデータがあるときには、ワークシートをスクロールしても見出しを見ることができません。そして、各レコードには多くのデータが含まれています。ペインを固定すると、スクロールしても凍結された部分を見ることができます。上部行や最初の列のヘッダーを簡単に見ることができます。ペインを固定または解除すると、データ自体は変わらず、表示だけが変わります。

## ***Excelでペーンを固定する方法**

**![Excelでのウィンドウ枠の固定](Freeze-panes.png)**


1. ウィンドウ枠を固定し、行と列を固定する場合は、まずセルを選択します（例えばB2など）
2. 表示 > ウィンドウ枠の固定をクリックします。
3. ドロップダウンメニューで、ウィンドウ枠の固定をクリックします。
4. 下にスクロールするか、右にスクロールすると、最初の行と列が固定されます。

**![ウィンドウ枠の凍結](Frozen-Panes.png)**

1行目と列Aが凍結されていることがわかります。2行目は32で、2番目の表示可能な列はDです。 

ウィンドウ枠を固定すると、大きなデータを行または列のラベルを追跡せずに表示できます。




## **Aspose.Cells for Python via .NETを使用してペーンを固定する方法**
Aspose.Cells for Python via .NETを使用すると、選択したセルにペーンを固定して固定ウィンドウを作成するのは簡単です。[**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int)メソッドを使用してください。
1. ファイルを開くためにワークブックを作成します。または空のファイルを作成します。
2. Worksheet.FreezePanes()メソッドを使用してウィンドウ枠を固定します。
3. ファイルを保存します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Pane.py" >}}

添付 [サンプルExcelファイル](Freeze.xlsx)。
{{< app/cells/assistant language="python-net" >}}
