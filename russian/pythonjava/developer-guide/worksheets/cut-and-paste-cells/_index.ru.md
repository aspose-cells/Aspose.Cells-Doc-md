---
title: Вырезать и вставить ячейки
type: docs
weight: 30
url: /ru/python-java/cut-and-paste-cells/
---

## **Вырезать и вставить ячейки**
Aspose.Cells для Python via Java предоставляет возможность вырезать и вставить ячейки. Для этого API предоставляет метод [insertCutCells](https://reference.aspose.com/cells/python/asposecells.api/cells#insertCutCells\(com.aspose.cells.Range,%20int,%20int,%20int\)) коллекции [Cells](https://reference.aspose.com/cells/python/asposecells.api/Cells). Метод [insertCutCells](https://reference.aspose.com/cells/python/asposecells.api/cells#insertCutCells\(com.aspose.cells.Range,%20int,%20int,%20int\)) принимает следующие параметры.

- [Диапазон](https://reference.aspose.com/cells/python/asposecells.api/Range): Диапазон ячеек для вырезания.
- Индекс строки: Индекс строки для вставки ячеек.
- Индекс столбца: Индекс столбца для вставки ячеек.
- [ShiftType](https://reference.aspose.com/cells/python/asposecells.api/ShiftType): Направление сдвига столбцов.

В следующем фрагменте кода демонстрируется, как вырезать и вставить ячейки внутри листа.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CutAndPasteCells.py" >}}
