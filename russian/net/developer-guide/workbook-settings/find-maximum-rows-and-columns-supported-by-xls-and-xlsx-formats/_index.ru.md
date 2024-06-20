---
title: Найдите максимальное количество строк и столбцов, поддерживаемых форматами XLS и XLSX
type: docs
weight: 20
url: /ru/net/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Возможные сценарии использования**

Разные форматы Excel поддерживают разное количество строк и столбцов. Например, XLS поддерживает 65536 строк и 256 столбцов, а XLSX поддерживает 1048576 строк и 16384 столбца. Если вы хотите узнать, сколько строк и столбцов поддерживается данным форматом, вы можете использовать свойства [**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) и [**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn).

## **Найдите максимальное количество строк и столбцов, поддерживаемых форматами XLS и XLSX**

В следующем примере кода сначала создается рабочая книга в формате XLS, а затем в формате XLSX. После создания он печатает значения свойств [**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) и [**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn). Пожалуйста, ознакомьтесь с выводом консоли приведенного ниже кода для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.cs" >}}

## **Вывод в консоль**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
