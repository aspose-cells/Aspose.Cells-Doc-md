---
title: Преобразовать CSV в JSON
type: docs
weight: 220
url: /ru/net/convert-csv-to-json/
description: Конвертировать файл CSF в JSON, используя простой в использовании API Aspose.Cells for .NET.
keywords: Конвертировать, конвертировать CVS в JSON, CSV в JSON, CSV, JSON, Конвертировать CSV в JSON на CSharp, c# код для конвертации CSV в JSON
---

## **Преобразовать CSV в JSON**

Aspose.Cells поддерживает преобразование CSV в JSON. Для этого API предоставляет классы [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) и [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility). Класс [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) предоставляет параметры экспорта диапазона в JSON. Класс [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) имеет следующие свойства.

- [**ExportAsString**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/exportasstring): Это экспортирует строковое значение ячеек в JSON.
- [**HasHeaderRow**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow): Это указывает, содержит ли диапазон заголовок строки.
- [**Indent**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/indent): Указывает отступ.

Класс [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) экспортирует JSON с использованием параметров экспорта, установленных с помощью класса [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions).

Приведенный ниже образец кода демонстрирует использование классов [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) и [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) для загрузки [исходного файла CSV](104398879.csv) и печати JSON-вывода в консоль.

### **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.cs" >}}

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
{{< app/cells/assistant language="csharp" >}}
