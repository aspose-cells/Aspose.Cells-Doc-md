---
title: Обновление и вычисление сводной таблицы с расчетными элементами на Golang через C++
linktitle: Обновление и вычисление сводной таблицы с вычисляемыми элементами
type: docs
weight: 40
url: /ru/go-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: Обновление и вычисление сводной таблицы с расчетными элементами с помощью Aspose.Cells на Golang через C++.
---

{{% alert color="primary" %}}

Aspose.Cells теперь поддерживает обновление и вычисление сводной таблицы с использованием вычислимых элементов. Пожалуйста, используйте [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/go-cpp/pivottable/refreshdata/) и [**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) как обычно, чтобы выполнить эту функцию.

{{% /alert %}}

## **Обновление и вычисление сводной таблицы с вычисляемыми элементами**

Следующий пример кода загружает [исходный файл Excel](5115238.xlsx), содержащий сводную таблицу с тремя рассчитанными элементами, такими как "add", "div", "div2". Сначала мы изменяем значение ячейки D2 на 20, затем обновляем и пересчитываем сводную таблицу с помощью API Aspose.Cells и сохраняем рабочую книгу в формате PDF. Результаты в [выходном PDF](5115229.pdf) показывают, что Aspose.Cells успешно обновил и пересчитал сводную таблицу с рассчитанными элементами. Вы можете проверить это вручную, установив значение 20 в ячейке D2 в Excel и обновив сводную таблицу с помощью сочетания клавиш Alt+F5 или кнопки обновления сводной таблицы.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RefreshAndCalculatePivotTableHavingCalculatedItems.go" >}}
