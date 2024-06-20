---
title: Игнорирование скрытых столбцов при экспорте данных листа в таблицу данных
type: docs
weight: 330
url: /ru/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/
description: Узнайте, как игнорировать скрытые столбцы при экспорте данных листа в таблицу данных через API Aspose.Cells for .NET.
keywords: Экспорт данных видимых столбцов в DataTable, Экспорт невидимых столбцов в DataTable, Экспорт столбцов в DataTable и Исключение скрытых столбцов, Игнорирование скрытых столбцов при экспорте данных листа в DataTable
---

{{% alert color="primary" %}}

Иногда вам нужно игнорировать скрытые столбцы при экспорте данных листа в таблицу данных. Это можно сделать с помощью Aspose.Cells, установив [**ExportTableOptions.PlotVisibleColumns**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblecolumns) в **true**. По умолчанию его значение **false**, поэтому вам нужно задать **true**, чтобы игнорировать скрытые столбцы.

{{% /alert %}}

Приведенный ниже образец кода объясняет использование свойства [**ExportTableOptions.PlotVisibleColumns**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblecolumns) для игнорирования скрытых столбцов при экспорте всего содержимого листа данных в таблицу данных.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-IgnoreHiddenColumnsDataTable-1.cs" >}}
