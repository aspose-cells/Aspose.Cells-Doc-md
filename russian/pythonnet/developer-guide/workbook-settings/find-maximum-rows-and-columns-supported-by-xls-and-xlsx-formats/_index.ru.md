---
title: Найдите максимальное количество строк и столбцов, поддерживаемых форматами XLS и XLSX
type: docs
weight: 20
url: /ru/python-net/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Возможные сценарии использования**

Разные форматы Excel поддерживают разное количество строк и столбцов. Например, XLS поддерживает 65536 строк и 256 столбцов, а XLSX поддерживает 1048576 строк и 16384 столбца. Если вы хотите узнать, сколько строк и столбцов поддерживается данным форматом, вы можете использовать свойства [**WorkbookSettings.max_row**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_row) и [**Workbook.settings.max_column**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_column).

## **Найдите максимальное количество строк и столбцов, поддерживаемых форматами XLS и XLSX**

В следующем примере кода сначала создается рабочая книга в формате XLS, а затем в формате XLSX. После создания он печатает значения свойств [**Workbook.settings.max_row**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_row) и [**Workbook.settings.max_column**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_column). Пожалуйста, ознакомьтесь с выводом консоли приведенного ниже кода для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.py" >}}

## **Вывод в консоль**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
