---
title: Convertir CSV a JSON
type: docs
weight: 220
url: /es/net/convert-csv-to-json/
description: Convierta el archivo CSF a JSON utilizando el sencillo Aspose.Cells for .NET API.
keywords: Convert, Convert CVS to JSON, CSV to JSON, CSV, JSON, Convert CSV to JSON CSharp, c# code to convert CSV to JSON
---
## **Convertir CSV a JSON**

Aspose.Cells admite la conversión de CSV a JSON. Para esto, el API proporciona**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**y**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** clases los**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**class proporciona las opciones para exportar el rango a JSON. los**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**clase tiene las siguientes propiedades.

- **[Exportar como cadena] (https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/exportasstring)**Esto exporta el valor de cadena de las celdas a JSON.
- **[HasHeaderRow](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow)**: Esto indica si el rango contiene una fila de encabezado.
- **[Sangría](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/indent)**: Indica la sangría.

los**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**class exporta el JSON usando las opciones de exportación establecidas con el**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**clase.

El siguiente ejemplo de código demuestra el uso de**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**y**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**Clases para cargar el[archivo CSV de origen](104398879.csv)e imprime la salida JSON en la consola.

### **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.cs" >}}

### **Salida de consola**
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