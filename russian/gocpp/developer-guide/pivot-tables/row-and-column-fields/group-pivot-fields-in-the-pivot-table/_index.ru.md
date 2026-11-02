---
title: Группировка полей сводной таблицы с помощью Golang через C++
linktitle: Группировка полей сводной таблицы с помощью Golang через C++
description: Узнайте, как группировать поля сводной таблицы с помощью Aspose.Cells for Go via C++.
keywords: Aspose.Cells, Aspose.Cells for Go via C++, сводная таблица, поле сводной таблицы, группировка полей сводной таблицы, GroupBy, PivotField, группировка дат, Go
type: docs
weight: 80
url: /ru/go-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Microsoft Excel позволяет группировать поля сводной таблицы **в** сводной таблице. При большом объеме данных, связанных с полем сводной таблицы, часто целесообразно группировать поля по разделам. Aspose.Cells также предоставляет эту функцию с помощью метода [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/go-cpp/pivotfield/groupby_double_bool/).

## **Группировка полей сводной таблицы**
В следующем примере кода загружается [образец файла Excel](64716818.xlsx) и выполняется группировка первого поля сводной таблицы с помощью метода [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/go-cpp/pivotfield/groupby_double_bool/). Затем обновляется сводная таблица, пересчитываются ее данные, а рабочая книга сохраняется как [выходной файл Excel](64716817.xlsx). На снимке экрана показан результат применения примера кода к файлу Excel. Как видно на снимке экрана, первое поле сводной таблицы теперь сгруппировано по месяцам и кварталам.
![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Пример кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupPivotFieldsInThePivotTable.go" >}}

{{< app/cells/assistant language="go" >}}