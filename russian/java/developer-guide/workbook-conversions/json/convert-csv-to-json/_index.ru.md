---
title: Преобразовать CSV в JSON
type: docs
weight: 170
url: /ru/java/convert-csv-to-json/
---

## **Преобразовать CSV в JSON**

Aspose.Cells поддерживает преобразование CSV в JSON. Для этого API предоставляет классы [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) и [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility). Класс [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) предоставляет параметры для экспорта диапазона в JSON. Класс [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) имеет следующие свойства.

- [**ExportAsString**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString): Это экспортирует строковое значение ячеек в JSON.
- [**HasHeaderRow**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow): Это указывает, содержит ли диапазон заголовок строки.
- [**Indent**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent): Указывает отступ.

Класс [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) экспортирует JSON с использованием параметров экспорта, установленных с помощью класса [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions).

В следующем примере кода демонстрируется использование классов [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) и [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) для загрузки [исходного CSV-файла](SampleCsv.csv) и вывода [JSON](SampleJson_out.csv) в консоль.

### **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

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
{{< app/cells/assistant language="java" >}}
