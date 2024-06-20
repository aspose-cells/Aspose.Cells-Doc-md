---
title: Обновление и вычисление сводной таблицы с вычисляемыми элементами
type: docs
weight: 130
url: /ru/java/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Теперь Aspose.Cells поддерживает обновление и вычисление сводной таблицы с вычисляемыми элементами. Пожалуйста, используйте [**PivotTable.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--) и [**PivotTable.caclulateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--) как обычно, чтобы выполнить эту функцию.

{{% /alert %}}

## **Обновление и вычисление сводной таблицы с вычисляемыми элементами**

В следующем примере кода загружается [исходный файл Excel](5473428.xlsx), который содержит сводную таблицу с тремя вычисляемыми элементами, такими как "сложение", "деление", "деление2". Сначала мы изменяем значение ячейки D2 на 20, а затем обновляем и вычисляем сводную таблицу с использованием API Aspose.Cells и сохраняем книгу в формате PDF. Результаты в [выходном файле PDF](5473431.pdf) показывают, что Aspose.Cells успешно обновил и вычислил сводную таблицу с вычисляемыми элементами. Вы можете проверить это, используя Microsoft Excel, вручную вводя значение 20 в ячейку D2, а затем обновляя сводную таблицу с помощью комбинации клавиш Alt+F5 или нажимая кнопку обновления сводной таблицы.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}
