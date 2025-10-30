---
title: Convertir CSV a JSON
type: docs
weight: 220
url: /es/python-net/convert-csv-to-json/
description: Convertir CSV a JSON utilizando Aspose.Cells para Python via .NET API.
keywords: Convertir CVS a JSON, Convertir CSV a JSON en Python via NET, Python convertir CSV a JSON, Guardar CSV como JSON
---

## **Convertir CSV a JSON**

Aspose.Cells para Python via .NET admite la conversión de CSV a JSON. Para esto, la API proporciona las clases [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) y [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility). La clase [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) proporciona las opciones para exportar el rango a JSON. La clase [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) tiene las siguientes propiedades.

- [**export_as_string**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/): Esto exporta el valor de cadena de las celdas a JSON.
- [**has_header_row**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/): Esto indica si el rango contiene una fila de encabezado.
- [**indent**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/): Indica la sangría.

La clase [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) exporta el JSON utilizando las opciones de exportación configuradas con la clase [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions).

El siguiente ejemplo de código demuestra el uso de las clases [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) y [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) para cargar el [archivo CSV fuente](104398879.csv) e imprimir la salida JSON en la consola.

### **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

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
{{< app/cells/assistant language="python-net" >}}
