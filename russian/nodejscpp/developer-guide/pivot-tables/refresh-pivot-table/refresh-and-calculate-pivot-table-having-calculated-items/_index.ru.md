---
title: Обновление и вычисление сводной таблицы с вычисляемыми элементами
type: docs
weight: 40
url: /ru/nodejs-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ теперь поддерживает обновление и расчет сводных таблиц с вычисляемыми элементами. Пожалуйста, используйте [**PivotTable.refreshData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#refreshdata--) и [**PivotTable.calculateData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#calculatedata--) как обычно для выполнения этой функции.

{{% /alert %}}

## **Обновление и вычисление сводной таблицы с вычисляемыми элементами**

Следующий пример кода загружает исходный Excel-файл (source excel file), содержащий сводную таблицу с тремя вычисляемыми элементами, такими как "add", "div", "div2". Мы сначала изменяем значение ячейки D2 на 20, затем обновляем и пересчитываем сводную таблицу с помощью API Aspose.Cells for Node.js via C++ и сохраняем рабочую книгу в PDF. В результате полученного PDF-файла видно, что Aspose.Cells for Node.js via C++ успешно обновил и пересчитал сводную таблицу с вычисляемыми элементами. Вы можете проверить это вручную, вставив значение 20 в ячейку D2 и обновив сводную таблицу через сочетание клавиш Alt+F5 или нажав кнопку обновления сводной таблицы.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTable-RefreshAndCalculateItems-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
