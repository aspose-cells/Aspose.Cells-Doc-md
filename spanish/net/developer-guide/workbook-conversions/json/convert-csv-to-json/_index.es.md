---
title: Convertir CSV a JSON
type: docs
weight: 220
url: /es/net/convert-csv-to-json/
description: Convertir archivo CSF a JSON usando la API simple de usar Aspose.Cells for .NET.
keywords: Convertir, Convertir CSV a JSON, CSV a JSON, CSV, JSON, Convertir CSV a JSON en CSharp, código c# para convertir CSV a JSON
---

## **Convertir CSV a JSON**

Aspose.Cells admite la conversión de CSV a JSON. Para esto, la API proporciona las clases [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) y [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility). La clase [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) ofrece las opciones para exportar rango a JSON. La clase [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) tiene las siguientes propiedades.

- [**ExportAsString**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/exportasstring): Esto exporta el valor de cadena de las celdas a JSON.
- [**HasHeaderRow**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow): Esto indica si el rango contiene una fila de encabezado.
- [**Indent**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/indent): Indica la sangría.

La clase [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) exporta el JSON utilizando las opciones de exportación configuradas con la clase [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions).

El siguiente ejemplo de código demuestra el uso de las clases [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) y [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) para cargar el [archivo CSV fuente](104398879.csv) e imprimir la salida JSON en la consola.

### **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.cs" >}}

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
