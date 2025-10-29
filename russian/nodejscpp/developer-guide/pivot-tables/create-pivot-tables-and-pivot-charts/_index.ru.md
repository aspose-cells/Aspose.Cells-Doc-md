---
title: Создание сводных таблиц и сводных графиков
type: docs
weight: 20
url: /ru/nodejs-cpp/create-pivot-tables-and-pivot-charts/
description: Как добавить сводные таблицы и сводные диаграммы с помощью Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, библиотека Excel Node.js, добавление сводных таблиц и сводных диаграмм с помощью библиотеки Excel Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Сводная таблица - это интерактивная сводка записей. Например, у вас может быть сотни записей о счетах-фактурах в списке на листе. Сводная таблица может подсчитать счета-фактуры по клиенту, продукту или дате. С помощью Microsoft Excel можно быстро переставить информацию в сводной таблице, перетаскивая кнопки на новую позицию.

Сводный график - это интерактивное графическое представление данных в сводной таблице. Сводные графики были введены в Excel 2000. Использование сводного графика делает понимание данных еще проще, поскольку сводная таблица автоматически создает итоги и подитоги.

Aspose.Cells for Node.js via C++ поддерживает [сводные таблицы](/cells/ru/nodejs-cpp/create-pivot-tables-and-pivot-charts/) и [сводные диаграммы](/cells/ru/nodejs-cpp/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Добавление сводных таблиц и диаграмм с помощью Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ предоставляет специальный набор классов, используемых для создания сводных таблиц. Эти классы предназначены для создания и настройки объектов сводной таблицы, которые являются основными строительными блоками сводной таблицы:

- PivotField, поле в отчете сводной таблицы.
- PivotFields, коллекция всех объектов PivotField в сводной таблице.
- PivotTable, отчет PivotTable на листе.
- PivotTables, коллекция всех объектов PivotTable на листе.

### **Подготовка к использованию Aspose.Cells for Node.js via C++**
1. Установите Aspose.Cells for Node.js via C++ из NPM, используйте команду: $ npm install aspose.cells.node.
1. Вы также можете следовать пошаговым инструкциям по установке “Aspose.Cells for Node.js via C++” в вашу среду разработки.


### **Как добавить сводную таблицу с помощью Aspose.Cells for Node.js via C++**

Для создания сводной таблицы с помощью Aspose.Cells for Node.js via C++:

1. Добавьте некоторые данные в ячейки листа книги Excel с помощью метода put_value объекта Cell. Вы также можете использовать файл-шаблон, уже заполненный данными. Данные будут использоваться в качестве источника данных для сводной таблицы.
1. Добавьте сводную таблицу на лист с помощью метода add коллекции PivotTables (инкапсулированной в объекте Worksheet).
1. Обратитесь к новому объекту PivotTable из коллекции PivotTables, передав его индекс. # Используйте любые из инкапсулированных объектов сводной таблицы в объекте PivotTable для управления таблицей.

Приведены примеры кода ниже.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.js" >}}

### **Как добавить сводную диаграмму с помощью библиотеки Aspose.Cells for Node.js via C++**

Для создания сводной диаграммы с помощью Aspose.Cells for Node.js via C++:

1. Добавьте диаграмму.
1. Установите источник данных диаграммы так, чтобы он ссылался на существующую сводную таблицу в электронной таблице.
1. Задайте другие атрибуты.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
