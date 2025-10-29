---
title: Создание сводных таблиц и сводных графиков
type: docs
weight: 20
url: /ru/python-net/create-pivot-tables-and-pivot-charts/
description: Как добавить сводные таблицы и сводные диаграммы с помощью Aspose.Cells для Python via .NET.
keywords: Aspose.Cells для Python Excel, библиотека Excel Python, Добавление сводных таблиц и сводных диаграмм с использованием Aspose.Cells для Python Excel Library.
---

{{% alert color="primary" %}}

Сводная таблица - это интерактивная сводка записей. Например, у вас может быть сотни записей о счетах-фактурах в списке на листе. Сводная таблица может подсчитать счета-фактуры по клиенту, продукту или дате. С помощью Microsoft Excel можно быстро переставить информацию в сводной таблице, перетаскивая кнопки на новую позицию.

Сводный график - это интерактивное графическое представление данных в сводной таблице. Сводные графики были введены в Excel 2000. Использование сводного графика делает понимание данных еще проще, поскольку сводная таблица автоматически создает итоги и подитоги.

Aspose.Cells для Python via .NET поддерживает [сводные таблицы](/cells/ru/python-net/create-pivot-tables-and-pivot-charts/) и [сводные диаграммы](/cells/ru/python-net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Добавление сводных таблиц и диаграмм с использованием Aspose.Cells для Python Excel Library.**

Aspose.Cells для Python via .NET предоставляет особый набор классов, используемых для создания сводных таблиц. Эти классы используются для создания и установки объектов PivotTable, которые являются основными строительными блоками объекта PivotTable:

- PivotField, поле в отчете сводной таблицы.
- PivotFields, коллекция всех объектов PivotField в сводной таблице.
- PivotTable, отчет PivotTable на листе.
- PivotTables, коллекция всех объектов PivotTable на листе.

### **Подготовка к использованию Aspose.Cells для Python via .NET**
1. Установите Aspose.Cells для Python via .NET с [pypi](https://pypi.org/project/aspose-cells-python/), используя команду: $ pip install aspose-cells-python.
1. Вы также можете следовать пошаговым инструкциям о том, как установить “Aspose.Cells для Python via .NET” в свою среду разработки.


### **Как добавить сводную таблицу, используя Aspose.Cells для Python Excel Library**

Чтобы создать сводную таблицу с помощью Aspose.Cells для Python via .NET:

1. Добавьте некоторые данные в ячейки листа книги Excel с помощью метода put_value объекта Cell. Вы также можете использовать файл-шаблон, уже заполненный данными. Данные будут использоваться в качестве источника данных для сводной таблицы.
1. Добавьте сводную таблицу на лист с помощью метода add коллекции PivotTables (инкапсулированной в объекте Worksheet).
1. Обратитесь к новому объекту PivotTable из коллекции PivotTables, передав его индекс. # Используйте любые из инкапсулированных объектов сводной таблицы в объекте PivotTable для управления таблицей.

Приведены примеры кода ниже.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

### **Как добавить сводную диаграмму с использованием Aspose.Cells для Python Excel Library**

Чтобы создать сводную диаграмму с помощью Aspose.Cells для Python via .NET:

1. Добавьте диаграмму.
1. Установите источник данных диаграммы так, чтобы он ссылался на существующую сводную таблицу в электронной таблице.
1. Задайте другие атрибуты.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
