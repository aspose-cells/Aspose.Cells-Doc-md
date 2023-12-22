---
title: Importar datos a la hoja de trabajo
type: docs
weight: 170
url: /es/net/import-data-into-worksheet/
description: Aprenda cómo importar datos a la hoja de trabajo a través del Aspose.Cells for .NET API.
keywords: C# Import Data into Worksheet, Import data into Excel with ICellsDataTable interface, Import data from Array, Import Data from ArrayList, Import Data from Custom Objects, Import Data from Custom Objects to merged area, Import Data from DataTable, Import Data from dynamic object as data source, Import Data from DataColumn, Import Data from DataView, Import Data from DataGrid, Import Data from GridView, Import HTML formatted data, Import Data Data from JSON
---
{{% alert color="primary" %}}

Este artículo analiza algunas técnicas de importación de datos a las que los desarrolladores tienen acceso a través de Aspose.Cells.

{{% /alert %}}

##  **Cómo importar datos a una hoja de trabajo**

Cuando abre un archivo de Excel con Aspose.Cells, todos los datos del archivo se importan automáticamente. Aspose.Cells también puede importar datos de otras fuentes de datos.

Aspose.Cells proporciona un[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)clase que representa un archivo Excel Microsoft. El[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)colección que permite el acceso a cada hoja de cálculo en un archivo Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. El[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)recopilación.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)La recopilación proporciona métodos útiles para importar datos de diferentes fuentes de datos. Este artículo explica cómo se pueden utilizar estos métodos.

##  **Cómo importar datos a Excel con la interfaz ICellsDataTable**
 Implementar[ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) para envolver sus diversas fuentes de datos, luego use[Cells.ImportarDatos()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) para importar datos a una hoja de cálculo de Excel.
###  **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

La implementación de*CustomerDataSource*, *Cliente* y *ClienteLista* las clases se dan a continuación

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


##  **Cómo importar datos a Excel desde una matriz**

 Para importar datos a una hoja de cálculo desde una matriz, llame al[**Importar matriz**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) método de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)recopilación. Hay muchas versiones sobrecargadas del[**Importar matriz**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)método, pero una sobrecarga típica toma los siguientes parámetros:

- *Array**, el objeto de matriz desde el que estás importando contenido.
- *Número de fila**, el número de fila de la primera celda a la que se importarán los datos.
- *Número de columna**, el número de columna de la primera celda a la que se importarán los datos.
- *Es vertical**, un valor booleano que especifica si se importan datos vertical u horizontalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

##  **Cómo importar datos a Excel desde ArrayList**

 Para importar datos desde un*Lista de arreglo* a las hojas de trabajo, llame al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección[**Importar lista de matrices**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)método. El método ImportArray toma los siguientes parámetros:

-  *Lista de matriz**, representa la*Lista de arreglo*objeto que estás importando.
- *Número de fila**, representa el número de fila de la primera celda a la que se importarán los datos.
- *Número de columna**, representa el número de columna de la primera celda a la que se importarán los datos.
- *Es vertical**, un valor booleano que especifica si se importan datos vertical u horizontalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

##  **Cómo importar datos a Excel desde objetos personalizados**

 Para importar datos de una colección de objetos a una hoja de trabajo, use[**Importar objetos personalizados**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). Proporcione una lista de columnas/propiedades al método para mostrar la lista deseada de objetos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

##  **Cómo importar datos a Excel desde objetos personalizados al área fusionada**

Para importar datos de una colección de objetos a una hoja de trabajo que contiene celdas combinadas, use[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) propiedad. Si la plantilla de Excel tiene celdas fusionadas, establezca el valor de[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)propiedad a verdadera. Pasa el[**Importar opciones de tabla**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) objeto junto con la lista de columnas/propiedades del método para mostrar la lista deseada de objetos. El siguiente ejemplo de código demuestra el uso de[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) propiedad para importar datos de objetos personalizados a celdas combinadas. por favor vea lo adjunto[fuente Excel](90112033.xlsx) archivo y el[salida Excel](90112034.xlsx) archivo para referencia.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

##  **Cómo importar datos a Excel desde DataTable**

Para importar datos desde una *DataTable*, llame al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección[**Importar tabla de datos**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) método. Hay muchas versiones sobrecargadas del[**Importar tabla de datos**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)método, pero una sobrecarga típica toma los siguientes parámetros:

-  *Tabla de datos**, la*Tabla de datos* objeto desde el que estás importando el contenido.
-  *Se muestra el nombre del campo**, especifica si los nombres de los*Tabla de datos*Las columnas deben importarse a la hoja de trabajo como una primera fila o no.
- *Celda de inicio**, representa el nombre de la celda de inicio (por ejemplo "A1") desde donde importar el contenido de la *DataTable*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

##  **Cómo importar datos a Excel desde un objeto dinámico como fuente de datos**

Aspose.Cells proporciona funciones para trabajar con objetos dinámicos como fuente de datos. Ayuda a utilizar la fuente de datos donde las propiedades se agregan dinámicamente a los objetos. Una vez que se agregan las propiedades al objeto, Aspose.Cells considera la primera entrada como plantilla y maneja el resto en consecuencia. Significa que si se agrega alguna propiedad dinámica solo al primer elemento y no a otros objetos, Aspose.Cells considera que todos los elementos de la colección deben ser iguales.

En este ejemplo, se utiliza un modelo de plantilla que inicialmente contiene sólo dos variables. Esta Lista se convierte en Lista de objetos dinámicos. Luego se le agrega un campo adicional y finalmente se carga en el libro de trabajo. El libro de trabajo selecciona solo aquellos valores que están en el archivo de plantilla XLSX. Este libro de plantilla utiliza marcadores inteligentes que también contienen parámetros. Los parámetros le permiten modificar cómo se presenta la información. Los detalles sobre los marcadores inteligentes se pueden obtener en el siguiente artículo:

[Usando marcadores inteligentes](/cells/es/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

##  **Cómo importar datos a Excel desde DataColumn (.NET)**

A *Tabla de datos*o*Vista de datos*El objeto se compone de una o más columnas. Los desarrolladores también pueden importar datos de cualquier columna/columnas del*Tabla de datos*o*Vista de datos*llamando al[**Datos de importacion**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) método de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)recopilación. El[**Datos de importacion**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)El método acepta un parámetro de tipo.[**Importar opciones de tabla**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions). El[**Importar opciones de tabla**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) clase proporciona un[**Índices de columnas**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)Propiedad que acepta una matriz de índices de columnas.

El código de muestra que se proporciona a continuación demuestra el uso de[**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)para importar columnas selectivas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

##  **Cómo importar datos a Excel desde DataView (.NET)**

 Para importar datos desde un *DataView*, llame al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección[**Datos de importacion**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) método. Hay muchas versiones sobrecargadas del[**Datos de importacion**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)método pero el de DataView toma los siguientes parámetros:

- **Vista de datos:** El*Vista de datos*objeto desde el que está a punto de importar contenido.
- **Primera fila:**el número de fila de la primera celda a la que se importarán los datos.
- **Primera columna:**el número de columna de la primera celda a la que se importarán los datos.
- **Importar opciones de tabla:**Las opciones de importación.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

##  **Cómo importar datos a Excel desde DataGrid (.NET)**

 Es posible importar datos desde un*Cuadrícula de datos* llamando al[**Importar cuadrícula de datos**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) método de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)recopilación. Hay muchas versiones sobrecargadas del[**Importar cuadrícula de datos**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)método, pero una sobrecarga típica toma los siguientes parámetros:

-  *cuadrícula de datos**, el*Cuadrícula de datos*objeto desde el que estás importando contenido.
- *Número de fila**, el número de fila de la primera celda a la que se importarán los datos.
- *Número de columna**, el número de columna de la primera celda a la que se importarán los datos.
- *Insertar filas**, una propiedad booleana que indica si se deben agregar filas adicionales a la hoja de cálculo para ajustar los datos o no.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

##  **Cómo importar datos a Excel desde GridView**

 Para importar datos desde un*Vista en cuadrícula* controlar, llame al[**ImportarGridView**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) método de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)recopilación.

Aspose.Cells nos permite respetar los valores formateados HTML al importar datos a la hoja de cálculo. Cuando el análisis HTML está habilitado al importar datos, Aspose.Cells convierte HTML al formato de celda correspondiente.

##  **Cómo importar datos formateados HTML a Excel**

 Aspose.Cells proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)clase que proporciona métodos muy útiles para importar datos desde fuentes de datos externas. Este artículo muestra cómo analizar el texto formateado HTML mientras se importan datos y convertir el HTML en valores de celda formateados.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

##  **Cómo importar datos a Excel desde JSON**

Aspose.Cells proporciona un[**JsonUtilidad**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) clase para procesar JSON.[**JsonUtilidad**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) la clase tiene un[**Datos de importacion**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) método para importar datos JSON. Aspose.Cells también proporciona un[**Opciones de diseño Json**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) clase que representa las opciones del diseño JSON. El[**Datos de importacion**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)el método acepta[**Opciones de diseño Json**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)como parámetro. El[**Opciones de diseño Json**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)La clase proporciona las siguientes propiedades.

- [**matrizcomotabla**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): Indica que la matriz debe procesarse como una tabla o no.
- [**ConvertirNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): Obtiene o establece un valor que indica si la cadena en JSON se va a convertir a numérica o a fecha.
- [**Formato de fecha**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): Obtiene y establece el formato del valor de fecha.
- [**Ignorar título de matriz**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): Indica si se ignora el título si la propiedad del objeto es una matriz
- [**Ignorar nulo**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): Indica si el valor nulo debe ignorarse o no.
- [**Ignorar título del objeto**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): Indica si se ignora el título si la propiedad del objeto es un objeto.
- [**Formato numérico**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Obtiene y establece el formato del valor numérico.
- [**TítuloEstilo**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Obtiene y establece el estilo del título.

El código de muestra que se proporciona a continuación demuestra el uso de la[**JsonUtilidad**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) y[**Opciones de diseño Json**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)clases para importar datos JSON.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

##  **Temas avanzados**
- [Especificar campos de fórmula al importar datos a la hoja de trabajo](/cells/es/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Desplace la primera fila hacia abajo al insertar Cells filas de la tabla de datos](/cells/es/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
