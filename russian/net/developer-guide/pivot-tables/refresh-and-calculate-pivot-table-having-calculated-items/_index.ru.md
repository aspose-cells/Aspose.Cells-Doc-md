---
title: Обновление и вычисление сводной таблицы с вычисляемыми элементами
type: docs
weight: 40
url: /ru/net/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells теперь поддерживает обновление и вычисление сводной таблицы с использованием вычислимых элементов. Пожалуйста, используйте [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/refreshdata) и [**PivotTable.CaclulateData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/calculatedata) как обычно, чтобы выполнить эту функцию.

{{% /alert %}}

## **Обновление и вычисление сводной таблицы с вычисляемыми элементами**

В следующем образце кода загружается [исходный файл Excel](5115238.xlsx), содержащий сводную таблицу с тремя вычислимыми элементами, такими как "add", "div", "div2". Мы сначала меняем значение ячейки D2 на 20, а затем обновляем и вычисляем сводную таблицу с помощью API Aspose.Cells и сохраняем книгу в формате PDF. Результаты в [выходном файле PDF](5115229.pdf) показывают, что Aspose.Cells успешно обновил и вычислил сводную таблицу с вычисляемыми элементами. Вы можете проверить это, используя Microsoft Excel, вручную вводя значение 20 в ячейку D2, а затем обновляя сводную таблицу через сочетание клавиш Alt+F5 или нажатием кнопки обновления сводной таблицы.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-RefreshAndCalculateItems-1.cs" >}}
