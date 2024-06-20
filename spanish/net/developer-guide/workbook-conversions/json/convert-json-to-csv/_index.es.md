---
title: Convertir JSON a CSV
type: docs
weight: 210
url: /es/net/convert-json-to-csv/
---

## **Convertir JSON a CSV**

Aspose.Cells admite la conversión de JSON simple y anidado a CSV. Para esto, la API proporciona las clases [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) y [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility). La clase [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) proporciona opciones para la disposición del JSON como [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle) (ignora el título si el array es una propiedad de un objeto) o [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable) (procesa el array como una tabla). La clase [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) procesa el JSON utilizando las opciones de presentación establecidas con la clase [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)

El siguiente ejemplo de código demuestra el uso de las clases [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) y [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) para cargar el [archivo JSON fuente](104398869.json) y generar el [archivo CSV de salida](104398870.csv).

### **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.cs" >}}
