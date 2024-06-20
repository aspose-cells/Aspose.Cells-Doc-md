---
title: Экспорт данных из Excel в DataTable без какого либо форматирования
type: docs
weight: 280
url: /ru/net/export-excel-data-to-datatable-without-any-formatting/
description: Узнайте, как экспортировать данные из Excel в DataTable без какого либо форматирования через API Aspose.Cells for .NET.
keywords: Экспорт данных из Excel в DataTable без какого либо форматирования, Указать стратегию форматирования значений ячеек, Добавить стратегию форматирования при экспорте данных в DataTable. 
---

{{% alert color="primary" %}}

Иногда пользователи хотят экспортировать данные из Excel в таблицу данных без какого-либо форматирования. Например, если у какой-то ячейки значение 0.012345 и она форматирована, чтобы отображать два знака после запятой, то, когда пользователь экспортирует данные из Excel в таблицу данных, они будут экспортированы как 0.01, а не как 0.012345. Чтобы решить эту проблему, Aspose.Cells предоставил свойство [**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy), которое может принимать одно из трех значений

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

Если вы установите его на [**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy), то данные будут экспортироваться без какого-либо форматирования.

{{% /alert %}}

## Образец кода

Нижеследующий пример объясняет использование свойства [**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) для экспорта данных из Excel с форматированием и без него.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

## **Вывод в консоль**

Ниже приведен вывод отладки консоли вышеприведенного образца кода

{{< highlight java >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}
