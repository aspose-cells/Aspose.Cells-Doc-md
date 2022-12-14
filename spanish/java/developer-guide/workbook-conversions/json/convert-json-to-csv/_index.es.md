---
title: Convertir JSON a CSV
type: docs
weight: 160
url: /es/java/convert-json-to-csv/
---
Aspose.Cells admite la conversión de JSON simple y anidado a CSV. Para esto, el API proporciona[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)y[**JsonUtilidad**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)clases los[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)class proporciona las opciones para el diseño JSON como[**IgnorarArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle)(ignora el título si la matriz es una propiedad de un objeto) o[**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable)(procesa la matriz como una tabla). los[**JsonUtilidad**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)La clase procesa el JSON usando las opciones de diseño establecidas con el[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)clase.

El siguiente ejemplo de código demuestra el uso de[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)y[**JsonUtilidad**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)Clases para cargar el[archivo JSON de origen](SampleJson.json)y genera la[archivo CSV de salida](SampleJson_out.csv).

## Código de muestra

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
