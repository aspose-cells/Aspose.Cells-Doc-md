---
title: Convertir CSV a JSON
type: docs
weight: 170
url: /es/java/convert-csv-to-json/
---
## **Convertir CSV a JSON**

Aspose.Cells admite la conversión de CSV a JSON. Para esto, el API proporciona[**ExportRangeToJsonOptionsExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)y[**JsonUtilidad**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)clases los[**ExportRangeToJsonOptionsExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)class proporciona las opciones para exportar el rango a JSON. los[**ExportRangeToJsonOptionsExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)clase tiene las siguientes propiedades.

- [**Exportar como cadena**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString)Esto exporta el valor de cadena de las celdas a JSON.
- [**HasHeaderRow**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow): Esto indica si el rango contiene una fila de encabezado.
- [**Sangrar**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent): Indica la sangría.

los[**JsonUtilidad**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)class exporta el JSON usando las opciones de exportación establecidas con el[**ExportRangeToJsonOptionsExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)clase.

El siguiente ejemplo de código demuestra el uso de[**ExportRangeToJsonOptionsExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)y[**JsonUtilidad**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)Clases para cargar el[archivo CSV de origen](SampleCsv.csv)e imprime el[JSON](SampleJson_out.csv) salida en la consola.

### **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

### **Salida de consola**

[ { "id": 1, "idioma": "Java", "edición": "tercera", "autor": "Herbert Schildt", "dirección de la calle": 126, "ciudad": "San Jone", "estado": "CA", "código postal": 394221 }, { "id": 2, "idioma": "C++", "edición": "segunda", "autor": "EAAAA", "dirección de la calle": 126, "ciudad": "San Jone", "estado": "CA", "código postal": 394221 }, { "id": 3 , "idioma": ".Net", "edición": "segunda", "autor": "E.Balagurusamy", "streetAddress": 126, "ciudad": "San Jone", " estado": "CA", "código postal": 394221 } ]