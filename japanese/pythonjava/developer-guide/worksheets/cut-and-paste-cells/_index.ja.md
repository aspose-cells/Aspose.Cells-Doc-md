---
title: セルの切り取りと貼り付け
type: docs
weight: 30
url: /ja/python-java/cut-and-paste-cells/
---

## **セルの切り取りと貼り付け**
Aspose.Cells for Python via Java では、セルの切り取りと貼り付けを行う機能を提供します。これには、[Cells](https://reference.aspose.com/cells/python/asposecells.api/Cells) コレクションの [insertCutCells](https://reference.aspose.com/cells/python/asposecells.api/cells#insertCutCells\(com.aspose.cells.Range,%20int,%20int,%20int\)) メソッドがあります。[insertCutCells](https://reference.aspose.com/cells/python/asposecells.api/cells#insertCutCells\(com.aspose.cells.Range,%20int,%20int,%20int\)) メソッドは、次のパラメータを受け取ります。

- [Range](https://reference.aspose.com/cells/python/asposecells.api/Range): 切り取るセルの範囲。
- 行インデックス: セルを挿入する行のインデックス
- 列インデックス: セルを挿入する列のインデックス
- [ShiftType](https://reference.aspose.com/cells/python/asposecells.api/ShiftType): 列のシフト方向。

次のコードスニペットは、ワークシート内でセルの切り取りと貼り付けをする方法を示しています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CutAndPasteCells.py" >}}
