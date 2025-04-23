---
title: Получить дату обновления сводной таблицы и информацию о том, кем она обновлялась
type: docs
weight: 100
url: /ru/nodejs-cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: Как получить дату обновления сводной таблицы и информацию о том, кто ее обновил с помощью Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells для Node.js Excel, библиотека Excel Node.js, Получить дату обновления сводной таблицы и информацию о том, кто ее обновил с помощью Aspose.Cells для Node.js Excel Library.
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ теперь поддерживает получение информации о дате обновления и пользователе, выполнившем обновление, посредством извлечения данных из рабочей книги.

{{% /alert %}}

## **Как получить дату обновления сводной таблицы и информацию о том, кем было выполнено обновление**
[**PivotTable.getRefreshDate()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getRefreshDate--) возвращает дату последнего обновления сводного отчета. Аналогично свойство [**PivotTable.getRefreshedByWho()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getRefreshedByWho--) возвращает имя пользователя, который последний раз обновлял отчет. Приведенный ниже пример демонстрирует эту функцию, и образец файла можно загрузить по следующей ссылке.

[SourcePivotTable.xlsx](77496335.xlsx)

**Пример кода**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-GetPivotTableRefreshDate-1.js" >}}
