---
title: Преобразовать CSV в JSON
type: docs
weight: 220
url: /ru/python-net/convert-csv-to-json/
description: Преобразование CSV в JSON с использованием Aspose.Cells для Python via .NET API.
keywords: Преобразовать CVS в JSON, Преобразовать CSV в JSON в Python via NET, Преобразование CSV в JSON, Сохранение CSV в JSON
---

## **Преобразовать CSV в JSON**

Aspose.Cells для Python via .NET поддерживает преобразование CSV в JSON. Для этого API предоставляет классы [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) и [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility). Класс [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) предоставляет параметры для экспорта диапазона в JSON. Класс [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) имеет следующие свойства.

- [**export_as_string**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/): Это экспортирует строковое значение ячеек в JSON.
- [**has_header_row**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/): Это указывает, содержит ли диапазон заголовок строки.
- [**indent**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/): Указывает отступ.

Класс [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) экспортирует JSON с использованием параметров экспорта, установленных с помощью класса [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions).

Приведенный ниже образец кода демонстрирует использование классов [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) и [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) для загрузки [исходного файла CSV](104398879.csv) и печати JSON-вывода в консоль.

### **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

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
