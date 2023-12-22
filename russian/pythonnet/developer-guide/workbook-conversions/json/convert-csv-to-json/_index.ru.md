---
title: Преобразовать CSV в JSON
type: docs
weight: 220
url: /ru/python-net/convert-csv-to-json/
description: Преобразуйте CSV в JSON, используя Aspose.Cells for Python via .NET API.
keywords: Convert CVS to JSON, Convert CSV to JSON in Python via NET, Python convert CSV to JSON, Save CSV to JSON
---
##  **Преобразовать CSV в JSON**

Aspose.Cells for Python via .NET поддерживает преобразование CSV в JSON. Для этого API обеспечивает**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**и**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** занятия.**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**Класс предоставляет возможности экспорта диапазона до JSON.**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**класс имеет следующие свойства.

- *[экспорт_ас_строка](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/)**: это экспортирует строковое значение ячеек в JSON.
- *[has_header_row](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/)**: указывает, содержит ли диапазон строку заголовка.
- *[отступ](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/)**: Обозначает отступ.

**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**класс экспортирует JSON, используя параметры экспорта, установленные с помощью**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**сорт.

В следующем примере кода показано использование**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**и**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** классы для загрузки[исходный файл CSV](104398879.csv)и печатает вывод JSON в консоли.

###  **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

###  **Консольный вывод**
```json
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
```