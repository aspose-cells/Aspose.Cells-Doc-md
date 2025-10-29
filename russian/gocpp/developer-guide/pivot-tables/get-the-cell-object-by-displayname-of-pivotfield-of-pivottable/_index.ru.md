---
title: Получить объект ячейки по DisplayName поля сводной таблицы с Golang через C++
linktitle: Получить объект ячейки по DisplayName поле PivotTable
type: docs
weight: 70
url: /ru/go-cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: Узнайте, как получить объект ячейки по отображаемому имени поля сводной таблицы и применить форматирование с использованием Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет метод [**PivotTable::GetCellByDisplayName()**](https://reference.aspose.com/cells/go-cpp/pivottable/getcellbydisplayname/), который можно использовать для доступа к объекту ячейки по отображаемому имени поля сводной таблицы. Этот метод полезен, когда нужно выделить или отформатировать заголовок поля сводной таблицы. Эта статья объясняет, как получить объект ячейки по отображаемому имени поля данных и применить к нему форматирование.

{{% /alert %}}

## **Получить объект ячейки по DisplayName поле PivotTable**

Следующий код обращается к первой сводной таблице на листе и затем извлекает ячейку по отображаемому имени второго поля данных этой таблицы. Затем он изменяет цвет заливки и цвет шрифта на светло-голубой и черный соответственно. Ниже приведены скриншоты, показывающие, как выглядит сводная таблица до и после выполнения кода.

|**СводнаяТаблица - До**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetTheCellObjectByDisplaynameOfPivotfieldOfPivottable.go" >}}
|**СводнаяТаблица - После**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
