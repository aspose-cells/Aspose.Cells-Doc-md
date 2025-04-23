---
title: 範囲の切り取りと貼り付け
type: docs
weight: 150
url: /ja/java/cut-and-paste-cells/
---

## **セルの切り取りと貼り付け**

Aspose.Cellsを使用してワークシート内でセルの切り取りと貼り付けをする能力を提供します。[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションの[**insertCutCells**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertCutCells-com.aspose.cells.Range-int-int-int-)メソッドを使用します。[**insertCutCells**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertCutCells-com.aspose.cells.Range-int-int-int-)は、次のパラメータを受け入れます。

- [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range): 切り取るセルの範囲
- 行インデックス: セルを挿入する行のインデックス
- 列インデックス: セルを挿入する列のインデックス
- [**ShiftType**](https://reference.aspose.com/cells/java/com.aspose.cells/ShiftType): 列のシフト方向

次の例は、ワークシート内でセルを切り取り、貼り付ける方法を示しています。

## サンプルコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-CutAndPasteCells-1.java" >}}
{{< app/cells/assistant language="java" >}}
