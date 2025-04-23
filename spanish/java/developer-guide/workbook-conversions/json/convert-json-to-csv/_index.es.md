---
title: Convertir JSON a CSV
type: docs
weight: 160
url: /es/java/convert-json-to-csv/
---

Aspose.Cells admite la conversión de JSON simple y anidado a CSV. Para esto, la API proporciona las clases [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) y [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility). La clase [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) proporciona opciones para el diseño JSON como [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle) (ignora el título si el array es una propiedad de un objeto) o [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable) (procesa el array como una tabla). La clase [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) procesa el JSON utilizando las opciones de diseño establecidas con la clase [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions).

El siguiente ejemplo de código muestra el uso de las clases [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) y [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) para cargar el [archivo JSON fuente](SampleJson.json) y generar el [archivo CSV de salida](SampleJson_out.csv).

## Código de Muestra

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
{{< app/cells/assistant language="java" >}}
