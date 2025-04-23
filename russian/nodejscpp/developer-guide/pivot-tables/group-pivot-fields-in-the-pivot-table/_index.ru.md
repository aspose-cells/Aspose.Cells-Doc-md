---
title: Группировка полей сводной таблицы
type: docs
weight: 80
url: /ru/nodejs-cpp/group-pivot-fields-in-the-pivot-table/
description: Как группировать поля сводной таблицы в сводной таблице с помощью Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, библиотека Excel Node.js, Как группировать поля сводной таблицы в сводной таблице с использованием Aspose.Cells for Node.js via C++.
---

## **Возможные сценарии использования**

Microsoft Excel позволяет группировать поля сводной таблицы. Когда данных по полю много, их часто удобно сгруппировать по разделам. Aspose.Cells for Node.js via C++ также предоставляет эту функцию с помощью метода [**PivotTable.groupBy()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-).

## **Как сгруппировать поля сводной таблицы**

Приведенный ниже образец кода загружает [образец файла Excel](64716818.xlsx) и выполняет группировку по первому полю сводной таблицы с помощью метода [**PivotTable.groupBy()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-). Затем он обновляет и вычисляет данные сводной таблицы и сохраняет книгу Excel как [выходной файл Excel](64716817.xlsx). На скриншоте показан эффект образца кода на образцовый файл Excel. Как видно на скриншоте, первое поле сводной таблицы теперь сгруппировано по месяцам и кварталам.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-GroupPivotFieldsInPivotTable.js" >}}
