---
title: Создание сводных таблиц и сводных графиков
type: docs
weight: 20
url: /ru/net/create-pivot-tables-and-pivot-charts/
---

{{% alert color="primary" %}}

Сводная таблица - это интерактивная сводка записей. Например, у вас может быть сотни записей о счетах-фактурах в списке на листе. Сводная таблица может подсчитать счета-фактуры по клиенту, продукту или дате. С помощью Microsoft Excel можно быстро переставить информацию в сводной таблице, перетаскивая кнопки на новую позицию.

Сводный график - это интерактивное графическое представление данных в сводной таблице. Сводные графики были введены в Excel 2000. Использование сводного графика делает понимание данных еще проще, поскольку сводная таблица автоматически создает итоги и подитоги.

Aspose.Cells поддерживает [сводные таблицы](/cells/ru/net/create-pivot-tables-and-pivot-charts/) и [сводные диаграммы](/cells/ru/net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Добавление сводных таблиц и графиков**

Aspose.Cells предоставляет специальный набор классов, используемых для создания сводных таблиц. Эти классы используются для создания и установки объектов PivotTable, которые выступают в качестве основных строительных блоков объекта PivotTable:

- PivotField, поле в отчете сводной таблицы.
- PivotFields, коллекция всех объектов PivotField в сводной таблице.
- PivotTable, отчет PivotTable на листе.
- PivotTables, коллекция всех объектов PivotTable на листе.

### **Подготовка к использованию Aspose.Cells**

1. Скачайте и установите Aspose.Cells:
   1. [Загрузите Aspose.Cells](https://downloads.aspose.com/cells/net).
   1. Установите его на вашем компьютере для разработки.
      Все [компоненты Aspose](http://www.aspose.com/), установленные, работают в режиме оценки. Режим оценки не имеет временных ограничений и только внедряет водяные знаки в созданные документы. Чтобы работать с компонентом в полной мере, вам действительно нужна действительная лицензия.
1. Создайте проект:
   1. Запустите Visual Studio.Net.
   1. Создайте новое консольное приложение.
1. Добавьте ссылки:
   Добавьте ссылку на компонент Aspose.Cells в ваш проект, например ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Добавление сводной таблицы**

Для создания сводной таблицы с использованием Aspose.Cells:

1. Добавьте некоторые данные в ячейки листа с помощью метода PutValue/setValue объекта Cell. Вы также можете использовать файл шаблона, уже заполненный данными. Данные будут использоваться в качестве источника данных сводной таблицы.
1. Добавьте сводную таблицу на лист с помощью метода add коллекции PivotTables (инкапсулированной в объекте Worksheet).
1. Обратитесь к новому объекту PivotTable из коллекции PivotTables, передав его индекс. # Используйте любые из инкапсулированных объектов сводной таблицы в объекте PivotTable для управления таблицей.

Приведены примеры кода ниже.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **Добавление сводной диаграммы**

Чтобы создать сводную диаграмму с использованием Aspose.Cells:

1. Добавьте диаграмму.
1. Установите источник данных диаграммы так, чтобы он ссылался на существующую сводную таблицу в электронной таблице.
1. Задайте другие атрибуты.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
