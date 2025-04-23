---
title: Importar y Exportar Datos
type: docs
weight: 130
url: /es/java/import-and-export-data/
---

{{% alert color="primary" %}}

Este artículo discute algunas técnicas de importación y exportación de datos a las que los desarrolladores tienen acceso a través de Aspose.Cells.

{{% /alert %}}

## Importar Datos en una Hoja de Cálculo

Los datos representan el mundo tal como es. Para dar sentido a los datos, los analizamos y obtenemos una comprensión del mundo. Los datos se convierten en información.

Hay muchas formas de realizar análisis: poner datos en hojas de cálculo y manipularlos de diferentes maneras es un método común. Con Aspose.Cells, es fácil crear hojas de cálculo que toman datos de una variedad de fuentes externas y los preparan para su análisis.

Este artículo trata sobre algunas técnicas de importación de datos a las que los desarrolladores tienen acceso a través de Aspose.Cells.

### Importar Datos Usando Aspose.Cells

Cuando abres un archivo de Excel con Aspose.Cells, todos los datos del archivo se importan automáticamente. Aspose.Cells también puede importar datos de otras fuentes de datos:

- [Matriz](/cells/es/java/import-and-export-data/).
- [Lista de arreglos](/cells/es/java/import-and-export-data/).
- [Conjunto de resultados](/cells/es/java/import-and-export-data/).
- [JSON](/cells/es/java/import-and-export-data/)

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene la colección [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). La colección [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) proporciona métodos muy útiles para importar datos de otras fuentes de datos. Este artículo explica cómo se pueden usar estos métodos.

#### Importar desde un Arreglo

Para importar datos a una hoja de cálculo desde un arreglo, llama al método importArray de la colección [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). Hay muchas versiones sobrecargadas del método importArray pero una sobrecarga típica toma los siguientes parámetros:

- **Array**, el objeto array desde el que estás importando contenido.
- **Número de fila**, el número de fila de la primera celda a la que se importarán los datos.
- **Número de columna**, el número de columna de la primera celda a la que se importarán los datos.
- **Es vertical**, un valor booleano que especifica si se importarán los datos vertical u horizontalmente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### Importar desde Arreglos Multidimensionales

Para importar datos a una hoja de cálculo desde arreglos multidimensionales, llama a la sobrecarga relevante de importArray de la colección [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### Importación desde un ArrayList

Para importar datos de un *ArrayList* a las hojas de cálculo, llame al método [**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList-java.util.ArrayList-int-int-boolean-) de la colección [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). El método [**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList-java.util.ArrayList-int-int-boolean-) toma los siguientes parámetros:

- **ArrayList**, el objeto *ArrayList* cuyo contenido se importará.
- **Número de fila**, el número de fila de la primera celda del rango de celdas desde el cual se importarán los contenidos.
- **Número de columna**, el número de columna de la primera celda desde la cual se importarán los datos.
- **Es Vertical**, es un valor booleano que especifica si importar datos vertical u horizontalmente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Importación desde Objetos Personalizados a un área fusionada

Para importar datos de una colección de objetos a una hoja de cálculo que contiene celdas fusionadas, use la propiedad [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells). Si la plantilla de Excel tiene celdas fusionadas, establezca el valor de la propiedad [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells) en true. Pase el objeto [**ImportTableOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions) junto con la lista de columnas/propiedades al método para mostrar su lista deseada de objetos. El siguiente ejemplo de código demuestra el uso de la propiedad [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells) para importar datos de Objetos Personalizados a celdas fusionadas. Consulte el archivo de Excel fuente adjunto (90112035.xlsx) y el archivo de Excel de salida (90112036.xlsx) para obtener referencias.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Importación de Datos desde JSON

Aspose.Cells proporciona una clase [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) para procesar JSON. La clase [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) tiene un método [**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData-java.lang.String-com.aspose.cells.Cells-int-int-com.aspose.cells.JsonLayoutOptions-) para importar datos JSON. Aspose.Cells también proporciona una clase [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) que representa las opciones del diseño JSON. El método [**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData-java.lang.String-com.aspose.cells.Cells-int-int-com.aspose.cells.JsonLayoutOptions-) acepta [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) como parámetro. La clase [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) proporciona las siguientes propiedades.

- [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable): Indica si el arreglo debe procesarse como una tabla o no.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate): Obtiene o establece un valor que indica si la cadena en JSON debe convertirse a numérico o fecha.
- [**DateFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat): Obtiene y establece el formato del valor de fecha.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle): Indica si se debe ignorar el título si la propiedad del objeto es un array.
- [**IgnoreNull**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull): Indica si el valor nulo debe ser ignorado o no.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle): Indica si se debe ignorar el título si la propiedad del objeto es un objeto.
- [**NumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat): Obtiene y establece el formato del valor numérico.
- [**TitleStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle): Obtiene y establece el estilo del título.

El código de muestra a continuación demuestra el uso de las clases [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) y [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) para importar datos JSON.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## Exportar Datos desde la Hoja de Cálculo

Aspose.Cells no solo permite a sus usuarios importar datos a las hojas de cálculo desde fuentes de datos externas, sino que también les permite exportar datos de la hoja de cálculo a un array.

### Exportar datos usando Aspose.Cells - Exportar datos a un array

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) que permite el acceso a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells).

Los datos pueden exportarse fácilmente a un objeto Array usando el método [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-) de la clase [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells).

#### Columnas que contienen datos de tipo fuertemente tipado

Las hojas de cálculo almacenan datos como una secuencia de filas y columnas. Use el método [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-) para exportar los datos de una hoja de cálculo a un array. [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-) toma los siguientes parámetros para exportar los datos de la hoja de cálculo como un objeto *Array*:

- Número de fila, el número de fila de la primera celda desde la cual se exportarán los datos.
- Número de columna, el número de columna de la primera celda desde donde se exportarán los datos.
- Número de filas, el número de filas a exportar.
- Número de columnas, el número de columnas a exportar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **Temas avanzados**
- [Importar datos desde el objeto ResultSet de la base de datos Microsoft Access a la hoja de cálculo](/cells/es/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [Especificar Campos de Fórmula al Importar Datos a la Hoja de Cálculo](/cells/es/java/specify-formula-fields-while-importing-data-to-worksheet/)
{{< app/cells/assistant language="java" >}}
