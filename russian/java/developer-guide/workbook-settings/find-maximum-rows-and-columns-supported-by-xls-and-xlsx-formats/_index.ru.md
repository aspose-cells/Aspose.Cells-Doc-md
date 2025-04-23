---
title: Найдите максимальное количество строк и столбцов, поддерживаемых форматами XLS и XLSX
type: docs
weight: 60
url: /ru/java/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Возможные сценарии использования**
Форматы Excel поддерживают разное количество строк и столбцов. Например, XLS поддерживает 65536 строк и 256 столбцов, в то время как XLSX поддерживает 1048576 строк и 16384 столбца. Если вы хотите узнать, сколько строк и столбцов поддерживается данным форматом, вы можете использовать свойства [Workbook.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow) и [Workbook.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn).
## **Найдите максимальное количество строк и столбцов, поддерживаемых форматами XLS и XLSX**
Следующий образец кода сначала создает рабочую книгу в формате XLS, а затем в формате XLSX. После создания он выводит значения свойств [Workbook.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow) и [Workbook.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn). Пожалуйста, см. вывод консоли приведенный ниже для вашего ориентира.
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.java" >}}

Вывод в консоль

{{< highlight java >}}

 Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
