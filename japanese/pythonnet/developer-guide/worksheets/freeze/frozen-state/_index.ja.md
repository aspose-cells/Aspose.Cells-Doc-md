---
title: Excelなしで固定状態をチェックする方法
linktitle: 凍結状態
type: docs
weight: 190
url: /ja/python-net/how-to-check-frozen-state-of-excel-worksheet
description: この記事では、Aspose.Cells for Python via .NET APIを使用してExcelワークシートの凍結状態をプログラムで確認する方法について学ぶことができます。
keywords: Python Excelライブラリ、Excelなしで凍結状態を確認する方法、PythonでExcelなしで凍結状態を確認する、PythonでExcelなしで凍結状態をチェックする。
---

## **紹介**

この記事では、Excelワークシートの凍結状態をプログラムで確認する方法について学びます。MS Excelでは、ワークシートが凍結されているかどうか、または分割されているかどうかを簡単に見つけることができます。しかし、CSharpでそれが凍結されているかどうか、または分割されているかどうかを見つける方法はありますか。それはAspose.Cells for Python via .NETを使用して簡単に行うことができます。

## **凍結状態を確認する方法**
Aspose.Cells for Python via .NETを使用して、ウィンドウが凍結されているかどうか、いくつの行と列がロックされているかを確認できます。

ウィンドウペインの状態をチェックするには[**Worksheet.pane_state**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/pane_state/)プロパティを使用してください 
また、[**Worksheet.get_freezed_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/get_freezed_panes/#any-any-any-any)メソッドを使用してロックされた行と列を取得できます。
1. ファイルを開くためのワークブックを作成します。
2. ワークシートが凍結しているかどうかを確認します。
3. ロックされた行および列を取得します

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Is-Worksheet-Frozen.py" >}}
