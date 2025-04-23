---
title: Convertir CSV a JSON
type: docs
weight: 170
url: /es/java/convert-csv-to-json/
---

## **Convertir CSV a JSON**

Aspose.Cells admite la conversión de CSV a JSON. Para esto, la API proporciona las clases [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) y [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility). La clase [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) proporciona las opciones para exportar rango a JSON. La clase [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) tiene las siguientes propiedades.

- [**ExportAsString**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString): Esto exporta el valor de cadena de las celdas a JSON.
- [**HasHeaderRow**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow): Esto indica si el rango contiene una fila de encabezado.
- [**Indent**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent): Indica la sangría.

La clase [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) exporta el JSON utilizando las opciones de exportación configuradas con la clase [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions).

El siguiente ejemplo de código demuestra el uso de las clases [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) y [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) para cargar el [archivo CSV de origen](SampleCsv.csv) e imprime la salida de [JSON](SampleJson_out.csv) en la consola.

### **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

### **Salida de la consola**

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
