---
title: Экспорт данных видимых строк из листа
type: docs
weight: 10
url: /ru/net/export-visible-rows-data-from-worksheet/
description: Узнайте, как экспортировать данные видимых строк из листа через API Aspose.Cells for .NET.
keywords: Экспорт данных видимых строк в DataTable, Экспорт невидимых строк в DataTable, Экспорт строк в DataTable и Исключение скрытых строк, Игнорирование скрытых строк при экспорте данных листа в DataTable
---

{{% alert color="primary" %}}

Вы можете экспортировать данные из листов в таблицы данных с помощью Aspose.Cells. Иногда вам нужно экспортировать данные только видимых строк. Aspose.Cells предоставляет способ достижения этой цели. Используйте [**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows), чтобы указать, что вы хотите экспортировать только данные видимых строк.

{{% /alert %}}

Этот пример показывает, как экспортировать данные из следующего листа. Строки 5, 6 и 7 скрыты.

|**Образец данных в листе, строки 5, 6 и 7 скрыты**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_1.png)|

Как только данные экспортируются в таблицу данных с использованием метода [**Worksheet.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) с опцией [**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows), это будет выглядеть так. Скрытые строки отображаются как пустые строки

|**Скрытые строки экспортируются в таблицу данных как пустые строки**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
