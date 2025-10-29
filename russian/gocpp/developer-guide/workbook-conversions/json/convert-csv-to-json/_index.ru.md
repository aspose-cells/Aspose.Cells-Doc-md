---
title: Конвертировать CSV в JSON с помощью Golang через C++
linktitle: Преобразовать CSV в JSON
type: docs
weight: 220
url: /ru/go-cpp/convert-csv-to-json/
description: Преобразуйте CSV файл в JSON, используя простое API Aspose.Cells for C++.
keywords: Преобразование, Конвертация CSV в JSON, CSV в JSON, CSV, JSON, Преобразование CSV в JSON C++, код C++ для преобразования CSV в JSON
---

## **Преобразовать CSV в JSON**

Поддержка Aspose.Cells для преобразования CSV в JSON. Для этого API предоставляет классы [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) и [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/). Класс [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) предоставляет опции для экспорта диапазона в JSON. Класс [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) содержит следующие свойства.

- [**GetExportAsString()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/getexportasstring/): Это экспортирует строковое значение ячеек в JSON.
- [**GetHasHeaderRow()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/gethasheaderrow/): Указывает, содержит ли диапазон строку заголовка.
- [**GetIndent()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/getindent/): Указывает отступ.

Класс [**JsonUtility**](https://reference.aspose.com/cells/go-cpp/jsonutility/) экспортирует JSON с использованием настроек экспорта, установленных через класс [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/).

Следующий пример кода демонстрирует использование классов [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) и [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) для загрузки [исходного CSV-файла](104398879.csv) и вывода JSON в консоль.

### **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertCsvToJson.go" >}}
### **Вывод в консоль**
{{< highlight java >}}

[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 2,
"language": "C++",
"edition": "second",
"author": "EAAAA",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 3,
"language": ".Net",
"edition": "second",
"author": "E.Balagurusamy",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
}
]

{{< /highlight >}}
