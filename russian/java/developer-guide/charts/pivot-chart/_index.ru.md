---
title: Как добавить сводную диаграмму с помощью Aspose.Cells
linktitle: Сводная диаграмма
type: docs
weight: 100
url: /ru/java/how-to-add-pivot-chart/
description: Как добавить сводную диаграмму с помощью Aspose.Cells.
keywords: Сводная диаграмма
---
## Что такое сводная диаграмма

Сводная диаграмма в Excel - это графическое представление данных, созданное на основе сводной таблицы. Она позволяет пользователям визуализировать и анализировать данные динамически, суммируя и отображая информацию в виде диаграммы. Сводные диаграммы интерактивны и их легко изменять, чтобы показать различные перспективы данных, что делает их мощным инструментом для анализа и презентации данных в Excel.

Как добавить сводную диаграмму с помощью Aspose.Cells
### **Создание сводной таблицы**

Для создания сводной таблицы с использованием Aspose.Cells:

1. Добавьте некоторые данные в ячейки листа с помощью метода PutValue/setValue объекта Cell. Вы также можете использовать файл шаблона, уже заполненный данными. Данные будут использоваться в качестве источника данных сводной таблицы.
1. Добавьте сводную таблицу на лист с помощью метода add коллекции PivotTables (инкапсулированной в объекте Worksheet).
1. Обратитесь к новому объекту PivotTable из коллекции PivotTables, передав его индекс.
1. Используйте любой из объектов сводной таблицы, инкапсулированных в объекте PivotTable, для управления таблицей.

Приведен пример кода. Выполнение этого кода создает новый файл: pivotTable_test.xls.

**Входные данные** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**Выходная сводная таблица**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **Создание сводной диаграммы на основе сводной таблицы**

Для создания сводной диаграммы с помощью Aspose.Cells:

1. Добавьте диаграмму.
1. Установите источник данных диаграммы так, чтобы он ссылался на существующую сводную таблицу в электронной таблице.
1. Задайте другие атрибуты.

Ниже приведен код, используемый компонентом для выполнения этой задачи. Выполнение этого кода создает новый файл: pivotChart_test.xls.

**Лист сводной диаграммы**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Эта статья показывает, как создавать сводные таблицы и сводные диаграммы с использованием Aspose.Cells. Надеемся, это поможет вам использовать эти функции в ваших собственных сценариях.

Aspose.Cells воспользовался годами исследований, проектирования и тщательной настройки.

Мы ждем ваши вопросы, комментарии и предложения на [Форуме Aspose.Cells](https://forum.aspose.com/c/cells/9). Мы гарантируем оперативный ответ.

{{% /alert %}}
