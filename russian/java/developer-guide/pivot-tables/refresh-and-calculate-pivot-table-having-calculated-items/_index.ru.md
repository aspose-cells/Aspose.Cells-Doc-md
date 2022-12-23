---
title: Обновить и рассчитать сводную таблицу с вычисляемыми элементами
type: docs
weight: 130
url: /ru/java/refresh-and-calculate-pivot-table-having-calculated-items/
---
{{% alert color="primary" %}}

 Aspose.Cells теперь поддерживает обновление и вычисление сводной таблицы с рассчитанными элементами. Пожалуйста, используйте[**Сводная таблица.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData() ) и[**Сводная таблица.caclulateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData()), как обычно, для выполнения этой функции.

{{% /alert %}}

## **Обновить и рассчитать сводную таблицу с вычисляемыми элементами**

 Следующий пример кода загружает[исходный файл excel](5473428.xlsx)который содержит сводную таблицу с тремя вычисляемыми элементами, такими как «добавить», «div», «div2». Сначала мы изменим значение ячейки D2 на 20, а затем обновим и вычислим сводную таблицу, используя API-интерфейсы Aspose.Cells, и сохраним книгу в формате PDF. Результаты в[вывод PDF](5473431.pdf) показывает, что Aspose.Cells обновил и вычислил сводную таблицу, успешно вычислив элементы. Вы можете проверить это с помощью Microsoft Excel, вручную поместив значение 20 в ячейку D2, а затем обновив сводную таблицу с помощью сочетания клавиш Alt + F5 или нажав кнопку «Обновить сводную таблицу».

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}
