---
title: Excelを使わずに固定状態を確認する方法。
linktitle: 凍結状態
type: docs
weight: 190
url: /ja/python-net/how-to-check-frozen-state-of-excel-worksheet
description: この記事では、Aspose.Cells for Python via .NET APIを使用してExcelワークシートの固定状態をプログラムで確認する方法について学びます。
keywords: Python Excelライブラリ、Excelを使わずに固定状態を確認する方法、Pythonで固定状態を確認する方法。
---

## **紹介**

この記事では、Excelワークシートの固定状態をプログラムで確認する方法について学びます。MS Excelでは簡単に分割や固定を判別できますが、CSharpではどうでしょうか。Aspose.Cells for Python via .NETを使えば簡単にできます。

## **固定状態の確認方法**
Aspose.Cells for Python via .NETを使えば、ウィンドウの固定状態やロックされている行数・列数を確認できます。

ウィンドウペインの状態をチェックするには[**Worksheet.pane_state**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/pane_state/)プロパティを使用してください 
また、[**Worksheet.get_freezed_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/get_freezed_panes/#any-any-any-any)メソッドを使用してロックされた行と列を取得できます。
1. ファイルを開くためのワークブックを作成します。
2. ワークシートが凍結しているかどうかを確認します。
3. ロックされた行および列を取得します

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Is-Worksheet-Frozen.py" >}}
{{< app/cells/assistant language="python-net" >}}
