---
title: Вырезать и вставить диапазон с помощью Golang через C++
linktitle: Вырезать и вставить диапазон
type: docs
weight: 130
url: /ru/go-cpp/cut-and-paste-cells/
description: Узнайте, как вырезать и вставлять ячейки внутри рабочего листа с помощью Aspose.Cells for C++.
---

## **Вырезать и вставить ячейки**

Aspose.Cells позволяет вам вырезать и вставлять ячейки внутри рабочего листа, используя метод [**InsertCutCells**](https://reference.aspose.com/cells/go-cpp/cells/insertcutcells/) коллекции [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Метод [**InsertCutCells**](https://reference.aspose.com/cells/go-cpp/cells/insertcutcells/) принимает следующие параметры:

- [**Range**](https://reference.aspose.com/cells/go-cpp/range/): Диапазон ячеек для вырезания.
- Индекс строки: Индекс строки для вставки ячеек.
- Индекс столбца: Индекс столбца для вставки ячеек.
- [**ShiftType**](https://reference.aspose.com/cells/go-cpp/shifttype/): Направление сдвига столбцов.

В следующем примере показано, как вырезать и вставить ячейки в пределах рабочего листа.

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CutAndPasteCells.go" >}}
