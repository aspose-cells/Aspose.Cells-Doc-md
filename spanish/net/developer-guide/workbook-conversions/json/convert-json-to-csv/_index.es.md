---
title: Convertir JSON a CSV
type: docs
weight: 210
url: /es/net/convert-json-to-csv/
---
## **Convertir JSON a CSV**

Aspose.Cells admite la conversión simple y anidada de JSON a CSV. Para esto, API proporciona**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)** y**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** clases Él**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**class proporciona las opciones para el diseño JSON como**[IgnorarTituloArray](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle)**(ignora el título si la matriz es una propiedad de un objeto) o**[ArrayAsTable](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable)**(procesa la matriz como una tabla). Él**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**La clase procesa el JSON usando las opciones de diseño establecidas con el**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**clase.

El siguiente ejemplo de código demuestra el uso de**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**y**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** Clases para cargar el[fuente JSON archivo](104398869.json) y genera la[archivo de salida CSV](104398870.csv).

### **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.cs" >}}
