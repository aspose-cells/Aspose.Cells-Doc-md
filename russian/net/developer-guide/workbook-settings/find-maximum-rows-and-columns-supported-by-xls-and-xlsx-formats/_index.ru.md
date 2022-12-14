---
title: Найти максимальное количество строк и столбцов, поддерживаемых форматами XLS и XLSX
type: docs
weight: 20
url: /ru/net/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---
## **Возможные сценарии использования**

Форматы Excel поддерживают разное количество строк и столбцов. Например, XLS поддерживает 65 536 строк и 256 столбцов, а XLSX — 1048 576 строк и 16 384 столбца. Если вы хотите узнать, сколько строк и столбцов поддерживается данным форматом, вы можете использовать[**Рабочая книга.Настройки.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) а также[**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn)характеристики.

## **Найти максимальное количество строк и столбцов, поддерживаемых форматами XLS и XLSX**

Следующий пример кода создает книгу сначала в формате XLS, а затем в формате XLSX. После создания он печатает значения[**Рабочая книга.Настройки.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) а также[**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn)характеристики. Для справки см. консольный вывод кода, приведенного ниже.

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.cs" >}}

## **Консольный вывод**

{{< highlight "java" >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
