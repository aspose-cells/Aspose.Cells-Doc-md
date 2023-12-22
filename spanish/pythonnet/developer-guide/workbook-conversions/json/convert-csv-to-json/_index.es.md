---
title: Convertir CSV a JSON
type: docs
weight: 220
url: /es/python-net/convert-csv-to-json/
description: Convierta CSV a JSON usando Aspose.Cells for Python via .NET API.
keywords: Convert CVS to JSON, Convert CSV to JSON in Python via NET, Python convert CSV to JSON, Save CSV to JSON
---
##  **Convertir CSV a JSON**

Aspose.Cells for Python via .NET admite la conversión de CSV a JSON. Para ello, API proporciona**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**y**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** clases. El**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**La clase proporciona opciones para exportar el rango a JSON.**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**La clase tiene las siguientes propiedades.

- *[exportar_como_cadena](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/)**: Esto exporta el valor de cadena de las celdas a JSON.
- *[has_header_row](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/)**: Esto indica si el rango contiene una fila de encabezado.
- *[sangrar](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/)**: Indica la sangría.

El**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**La clase exporta el JSON usando las opciones de exportación configuradas con el**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**clase.

El siguiente ejemplo de código demuestra el uso de**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**y**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** clases para cargar el[fuente CSV archivo](104398879.csv)e imprime la salida JSON en la consola.

###  **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

###  **Salida de consola**
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