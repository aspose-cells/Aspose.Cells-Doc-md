---
title: Excelワークシートの先頭行を凍結する
linktitle: 行を凍結
type: docs
weight: 190
url: /ja/python-net/how-to-freeze-rows-of-excel-worksheet
description: この記事では、Aspose.Cells for Python via .NET APIを使用してExcelワークシートの最上行をプログラムで固定する方法について学びます。
keywords: Python Excelライブラリ、Python最上行固定、Python固定トップ行。
---

## **紹介**

この記事では、上の行（複数）を固定する方法について学びます。共通の見出しの下に大量のデータがある場合、ワークシートを垂直にスクロールすると見出しが見えなくなることがあります。上の行（複数）を固定しておくと、残りのデータをスクロールしているときでもその固定された部分を見ることができます。

## **Excelで行を固定する方法**

**![Excelで行を凍結](Freeze-Rows.png)**


1. 上部行を凍結したい場合は、まず、凍結する行の下にある行を選択します。
2. 表示 > ウィンドウ枠の固定をクリックします。
3. ドロップダウンメニューで「上部行を凍結」をクリックします。
4. 下にスクロールすると、最初の行が常に上部で表示されます。

**![行の凍結](Frozen-Row.png)**

見ての通り、1行目が凍結され、スクロールしても常に最上部に表示されます。

行を凍結すると、行ラベルを追跡することなく大きなデータを表示できます。




## **Aspose.Cells for Python Excelライブラリを使用した行固定の方法**
Aspose.Cells for Python via .NETを使えば、行(複数行も可)を固定するのは簡単です。[**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) メソッドを使用して選択した行を固定してください。
1. ファイルを開くためにワークブックを作成します。または空のファイルを作成します。
2. Worksheet.FreezePanes() メソッドを使用して最初の行を凍結します。
3. ファイルを保存します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Row.py" >}}

添付の[サンプルソースExcelファイル](../Freeze.xlsx)。
{{< app/cells/assistant language="python-net" >}}
