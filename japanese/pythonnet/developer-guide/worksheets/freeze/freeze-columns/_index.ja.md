---
title: Excelワークシートの最初の列を固定する
linktitle: 列を固定する
type: docs
weight: 190
url: /ja/python-net/how-to-freeze-columns-of-excel-worksheet
description: この記事では、Aspose.Cells for Python via .NET APIを使用してExcelワークシートの左側の列をプログラムで固定する方法について学ぶことができます。
keywords: Python Excelライブラリ、Python左側の列を固定、Python最初の列を固定、Python列をロックする。
---

## **紹介**

この記事では、左の列（複数）を固定する方法について学びます。行に大量のデータがある場合、ワークシートを水平にスクロールすると左の列が見えなくなることがあります。最初の列（複数）を固定してロックすると、残りのデータをスクロールしているときでもその固定された部分を見ることができます。


## **Excelで列を固定する方法**

**![Excelで左列を固定する](freeze-columns.png)**


1. 左の列を固定したい列の下にある列をまず選択します
2. 表示 > ウィンドウ枠の固定をクリックします。
3. ドロップダウンメニューで「最初の列を固定」をクリックします。
4. 下にスクロールしても、最初の列が常に左側に表示されます。

**![固定された列](frozen-columns.png)**

1列が固定されている様子がわかります。横にスクロールしても、1列目は常に表示されます。

フリーズ列を使用すると、最初の列を追跡することなく長いデータを表示できます。




## **Aspose.Cellsを使用してPython Excelライブラリで列を固定する方法**
Aspose.Cells for Python via .NETを使用して最初の列を簡単に固定できます。選択した列で[**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int)　メソッドを使用して列を固定してください。
1. ファイルを開くためにワークブックを作成します。または空のファイルを作成します。
2. Worksheet.FreezePanes() メソッドを使用して最初の列を凍結します。
3. ファイルを保存します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Column.py" >}}

添付 [サンプルExcelファイル](Freeze.xlsx)。
