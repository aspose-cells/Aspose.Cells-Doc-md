---
title: Экспорт данных Excel в DataTable без форматирования
type: docs
weight: 280
url: /ru/net/export-excel-data-to-datatable-without-any-formatting/
---
{{% alert color="primary" %}}

Иногда пользователи хотят экспортировать данные Excel в таблицу данных без какого-либо форматирования. Например, если какая-то ячейка имеет значение 0,012345 и отформатирована для отображения двух знаков после запятой, то когда пользователь будет экспортировать данные Excel в таблицу данных, они будут экспортированы как 0,01, а не как 0,012345. Чтобы решить эту проблему, Aspose.Cells предоставил[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) свойство, которое может принимать одно из этих трех значений

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

 Если вы установите его на[**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy), то он будет экспортировать данные без какого-либо форматирования.

{{% /alert %}}

## Образец кода

 В следующем примере объясняется использование[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)свойство для экспорта данных Excel с форматированием и без него.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

## **Консольный вывод**

Ниже приведен вывод отладки консоли приведенного выше примера кода.

{{< highlight "java" >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}
