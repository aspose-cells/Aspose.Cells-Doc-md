---
title: Конвертировать CSV в JSON
type: docs
weight: 220
url: /ru/net/convert-csv-to-json/
description: Преобразуйте файл CSF в JSON с помощью простого в использовании Aspose.Cells for .NET API.
keywords: Convert, Convert CVS to JSON, CSV to JSON, CSV, JSON, Convert CSV to JSON CSharp, c# code to convert CSV to JSON
---
## **Конвертировать CSV в JSON**

Aspose.Cells поддерживает преобразование CSV в JSON. Для этого API предоставляет**[ExportRangeToJsonOptions] (https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**а также**[JsonUtility] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** классы.**[ExportRangeToJsonOptions] (https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**class предоставляет параметры для экспорта диапазона в JSON.**[ExportRangeToJsonOptions] (https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**класс имеет следующие свойства.

- **[ExportAsString](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/exportasstring)**это экспортирует строковое значение ячеек в JSON.
- **[HasHeaderRow] (https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow)**: указывает, содержит ли диапазон строку заголовка.
- **[Отступ](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/indent)**: указывает отступ.

**[JsonUtility] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**class экспортирует JSON, используя параметры экспорта, установленные с помощью**[ExportRangeToJsonOptions] (https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**учебный класс.

В следующем примере кода показано использование**[ExportRangeToJsonOptions] (https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**а также**[JsonUtility] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**классы для загрузки[исходный CSV-файл](104398879.csv)и выводит вывод JSON в консоль.

### **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.cs" >}}

### **Консольный вывод**
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