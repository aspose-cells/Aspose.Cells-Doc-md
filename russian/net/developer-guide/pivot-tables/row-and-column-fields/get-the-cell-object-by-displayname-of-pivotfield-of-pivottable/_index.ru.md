---
title: Получение объекта ячейки по отображаемому имени поля сводной таблицы
type: docs
weight: 70
url: /ru/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет метод [**PivotTable.GetCellByDisplayName()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getcellbydisplayname), который можно использовать для доступа к объекту ячейки по отображаемому имени поля сводной таблицы. Этот метод полезен, когда требуется выделить или форматировать заголовок поля сводной таблицы. В этой статье объясняется, как получить объект ячейки по отображаемому имени поля данных, а затем применить к нему форматирование.

{{% /alert %}}

## **Получить объект ячейки по отображаемому имени поля сводной таблицы**

Приведенный ниже код получает доступ к первой сводной таблице на листе, а затем получает ячейку по отображаемому имени второго поля данных сводной таблицы. Затем он меняет цвет заливки и цвет шрифта ячейки на голубой и черный соответственно. Ниже приведены скриншоты, показывающие, как выглядит сводная таблица до и после выполнения кода.

|**СводнаяТаблица - До**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-GetCellByDisplayName-GetCellObjectByDisplayName.cs" >}}

|**СводнаяТаблица - После**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
{{< app/cells/assistant language="csharp" >}}
