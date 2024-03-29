---
title: Как добавить сводную диаграмму с помощью Aspose.Cells
linktitle: Сводная диаграмма
type: docs
weight: 100
url: /ru/net/how-to-add-pivot-chart/
description: Как добавить сводную диаграмму с помощью Aspose.Cells.
keywords: PivotChart
---
##  Что такое сводная диаграмма

Сводная диаграмма в Excel — это графическое представление данных, созданных на основе сводной таблицы. Он позволяет пользователям динамически визуализировать и анализировать данные, суммируя и отображая информацию в виде диаграмм. Сводные диаграммы интерактивны и могут быть легко изменены для отображения данных с разных точек зрения, что делает их мощным инструментом для анализа и представления данных в Excel.

##  Как добавить сводную диаграмму с помощью Aspose.Cells

###  **Добавление сводной таблицы**

Чтобы создать сводную таблицу с помощью Aspose.Cells:

1. Добавьте данные в ячейки листа, используя метод PutValue/setValue объекта Cell. Вы также используете файл шаблона, уже заполненный данными. Данные будут использоваться в качестве источника данных сводной таблицы.
1. Добавьте сводную таблицу на лист, вызвав метод add коллекции PivotTables (инкапсулированный в объекте Worksheet).
1. Получите доступ к новому объекту сводной таблицы из коллекции сводных таблиц, передав его индекс. # Используйте любой из объектов сводной таблицы, инкапсулированных в объект PivotTable, для управления таблицей.

Примеры кода приведены ниже.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

###  **Добавление сводной диаграммы**

Чтобы создать сводную диаграмму с использованием Aspose.Cells:

1. Добавьте диаграмму.
1. Установите PivotSource диаграммы для ссылки на существующую сводную таблицу в электронной таблице.
1. Установите другие атрибуты.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

