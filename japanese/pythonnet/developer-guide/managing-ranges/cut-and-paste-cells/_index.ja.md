---
title: 範囲の切り取りと貼り付け
type: docs
weight: 130
url: /ja/python-net/cut-and-paste-cells/
description: この記事では、Aspose.Cells for Python via .NET ライブラリを使用して、範囲の切り取りと貼り付けについて説明します。
keywords: Python Excel ライブラリ、Python での範囲の切り取りと貼り付け方法、Python でのセルの切り取りと貼り付け方法。
---

## **セルの切り取りと貼り付け**

Aspose.Cellsを使用すると、ワークシート内でセルを切り取り、貼り付けることができます。[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) コレクションの[**insert_cut_cells **](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_cut_cells/) メソッドを使用して、以下のパラメータを受け入れます。

- [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range): 切り取るセルの範囲
- 行インデックス: セルを挿入する行のインデックス
- 列インデックス: セルを挿入する列のインデックス
- [**ShiftType**](https://reference.aspose.com/cells/python-net/aspose.cells/shifttype): 列のシフト方向

次の例は、ワークシート内でセルを切り取り、貼り付ける方法を示しています。

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Worksheets-CutAndPasteCells-1.py" >}}
