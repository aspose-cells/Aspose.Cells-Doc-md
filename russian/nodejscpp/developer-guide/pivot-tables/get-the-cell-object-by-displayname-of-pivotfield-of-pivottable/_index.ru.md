---
title: Получение объекта ячейки по отображаемому имени поля сводной таблицы
type: docs
weight: 70
url: /ru/nodejs-cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: Как получить объект ячейки по DisplayName поля сводной таблицы с помощью Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, библиотека Excel Node.js, Получить объект ячейки по DisplayName поля сводной таблицы с помощью Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ предоставляет метод [**PivotTable.getCellByDisplayName(string)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getCellByDisplayName-string-), который можно использовать для доступа к объекту ячейки по отображаемому имени поля сводной таблицы. Этот метод полезен, если нужно выделить или отформатировать заголовок поля сводной таблицы. Эта статья объясняет, как извлечь объект ячейки по отображаемому имени поля данных и применить к нему форматирование.

{{% /alert %}}

## **Как получить объект ячейки по отображаемому имени поля сводной таблицы**

Приведенный ниже код получает доступ к первой сводной таблице на листе, а затем получает ячейку по отображаемому имени второго поля данных сводной таблицы. Затем он меняет цвет заливки и цвет шрифта ячейки на голубой и черный соответственно. Ниже приведены скриншоты, показывающие, как выглядит сводная таблица до и после выполнения кода.

|**СводнаяТаблица - До**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-GetCellByDisplayName-GetCellObjectByDisplayName.js" >}}

|**СводнаяТаблица - После**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
{{< app/cells/assistant language="nodejs-cpp" >}}
