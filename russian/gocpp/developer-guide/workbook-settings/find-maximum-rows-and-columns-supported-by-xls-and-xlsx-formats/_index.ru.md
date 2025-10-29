---
title: Определение максимального количества строк и столбцов, поддерживаемых форматами XLS и XLSX, с помощью Golang через C++
linktitle: Найти максимальное количество строк и столбцов
type: docs
weight: 20
url: /ru/go-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
description: Научитесь находить максимальное количество строк и столбцов, поддерживаемых форматами XLS и XLSX, используя Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Различные форматы Excel поддерживают разное количество строк и столбцов. Например, XLS поддерживает 65536 строк и 256 столбцов, а XLSX — 1048576 строк и 16384 столбца. Если хотите узнать, сколько строк и столбцов поддерживает конкретный формат, используйте свойства [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getmaxrow/) и [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/).

## **Найдите максимальное количество строк и столбцов, поддерживаемых форматами XLS и XLSX**

Следующий пример создает рабочую книгу сначала в формате XLS, затем в XLSX. После создания он выводит значения свойств [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getmaxrow/) и [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/). Пожалуйста, ознакомьтесь с выводом в консоли приведенного ниже кода для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindMaximumRowsAndColumnsSupportedByXlsAndXlsxFormats.go" >}}
## **Вывод в консоль**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
