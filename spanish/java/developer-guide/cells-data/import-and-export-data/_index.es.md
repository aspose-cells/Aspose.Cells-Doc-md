---
title: Importar y exportar datos
type: docs
weight: 130
url: /es/java/import-and-export-data/
---
{{% alert color="primary" %}}

Este artículo analiza algunas técnicas de importación y exportación de datos a las que los desarrolladores tienen acceso a través del Aspose.Cells.

{{% /alert %}}

## Importar datos a la hoja de trabajo

Los datos representan el mundo tal como es. Para dar sentido a los datos, los analizamos y obtenemos una comprensión del mundo. Los datos se convierten en información.

Hay muchas formas de realizar análisis: poner datos en hojas de cálculo y manipularlos de diferentes maneras es un método común. Con Aspose.Cells, es fácil crear hojas de cálculo que toman datos de una variedad de fuentes externas y los preparan para el análisis.

Este artículo analiza algunas técnicas de importación de datos a las que los desarrolladores tienen acceso a través del Aspose.Cells.

### Importación de datos usando Aspose.Cells

Cuando abre un archivo de Excel con Aspose.Cells, todos los datos del archivo se importan automáticamente. Aspose.Cells también puede importar datos de otras fuentes de datos:

- [Formación](/cells/es/java/import-and-export-data/).
- [Lista de arreglo](/cells/es/java/import-and-export-data/).
- [Conjunto resultante](/cells/es/java/import-and-export-data/).
- [JSON](/cells/es/java/import-and-export-data/)

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene la colección[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) recopilación.[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)La recopilación proporciona métodos muy útiles para importar datos de otras fuentes de datos. En este artículo se explica cómo se pueden utilizar estos métodos.

#### Importación desde matriz

 Para importar datos a una hoja de cálculo desde una matriz, llame al método importArray del[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)recopilación. Hay muchas versiones sobrecargadas del método importArray pero una sobrecarga típica toma los siguientes parámetros:

- **Formación**, el objeto de matriz del que está importando contenido.
- **Numero de fila**el número de fila de la primera celda a la que se importarán los datos.
- **número de columna**, el número de columna de la primera celda a la que se importarán los datos.
- **es vertical**, un valor booleano que especifica si importar datos vertical u horizontalmente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### Importación desde matrices multidimensionales

 Para importar datos a una hoja de cálculo desde matrices multidimensionales, llame a la sobrecarga importArray relevante del[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)recopilación:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### Importar desde un ArrayList

 Para importar datos de un*Lista de arreglo* a las hojas de trabajo, llame al[**Importar ArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean) ) método de la[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) recopilación. los[**Importar ArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean)) método toma los siguientes parámetros:

- **Lista de arreglo** , la*Lista de arreglo*objeto cuyo contenido se importará.
- **Numero de fila**, el número de fila de la primera celda del rango de celdas desde el que se importará el contenido.
- **Número de columna**, el número de columna de la primera celda desde la que se importarán los datos.
- **es vertical**es un valor booleano que especifica si importar datos vertical u horizontalmente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Importación desde objetos personalizados al área fusionada

Para importar datos de una colección de objetos a una hoja de trabajo que contiene celdas combinadas, use[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)propiedad. Si la plantilla de Excel tiene celdas combinadas, establezca el valor de[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)propiedad a verdadera. Pasa el[**ImportTableOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions)objeto junto con la lista de columnas/propiedades del método para mostrar la lista deseada de objetos. El siguiente ejemplo de código demuestra el uso de[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)propiedad para importar datos de objetos personalizados a celdas combinadas. por favor vea lo adjunto[Excel fuente](90112035.xlsx)archivo y el[Excel de salida](90112036.xlsx)archivo de referencia.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Importación de datos desde JSON

 Aspose.Cells proporciona un[**JsonUtilidad**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) clase para procesar JSON.[**JsonUtilidad**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) la clase tiene un[**Datos de importacion**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions) ) método para importar datos JSON. Aspose.Cells también proporciona un[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)clase que representa las opciones del diseño JSON. los[**Datos de importacion**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions) ) método acepta[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) como parámetro. los[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) La clase proporciona las siguientes propiedades.

- [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable): Indica en la matriz que se debe procesar como una tabla o no.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate): Obtiene o establece un valor que indica si la cadena en JSON se va a convertir en numérica o en fecha.
- [**Formato de fecha**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat): Obtiene y establece el formato del valor de fecha.
- [**IgnorarArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle): Indica si ignorar el título si la propiedad del objeto es una matriz
- [**IgnorarNulo**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull): Indica si el valor nulo debe ignorarse o no.
- [**IgnoreObjectTitleIgnoreObjectTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle): Indica si ignorar el título si la propiedad del objeto es un objeto.
- [**Formato numérico**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat): Obtiene y establece el formato del valor numérico.
- [**TítuloEstilo**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle): Obtiene y establece el estilo del título.

 El código de ejemplo que se proporciona a continuación demuestra el uso de la[**JsonUtilidad**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) y[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) clases para importar datos JSON.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## Exportar datos desde la hoja de trabajo

Aspose.Cells no solo permite a sus usuarios importar datos a hojas de trabajo desde fuentes de datos externas, sino que también les permite exportar datos de hojas de trabajo a una matriz.

### Exportación de datos mediante Aspose.Cells - Exportación de datos a matriz

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene un[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) recopilación.

 Los datos se pueden exportar fácilmente a un objeto Array usando el[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) clase'[**exportarArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)) método.

#### Columnas que contienen datos fuertemente tipados

 Las hojas de cálculo almacenan datos como una secuencia de filas y columnas. Utilizar el[**exportarArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) ) para exportar los datos de una hoja de cálculo a una matriz.[**exportarArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) ) toma los siguientes parámetros para exportar datos de la hoja de trabajo como un*Formación* objeto:

- Número de fila, el número de fila de la primera celda desde la que se exportarán los datos.
- Número de columna, el número de columna de la primera celda desde donde se exportarán los datos
- Número de filas, el número de filas a exportar.
- Número de columnas, el número de columnas a exportar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **Temas avanzados**
- [Importar datos desde Microsoft Acceder al objeto ResultSet de la base de datos a la hoja de trabajo](/cells/es/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [Especificar campos de fórmula al importar datos a la hoja de trabajo](/cells/es/java/specify-formula-fields-while-importing-data-to-worksheet/)
