---
title: Importar datos a la hoja de trabajo
type: docs
weight: 170
url: /es/net/import-data-into-worksheet/
---
{{% alert color="primary" %}}

Este artículo analiza algunas técnicas de importación de datos a las que los desarrolladores tienen acceso a través del Aspose.Cells.

{{% /alert %}}

## **Importar datos a la hoja de trabajo**

Cuando abre un archivo de Excel con Aspose.Cells, todos los datos del archivo se importan automáticamente. Aspose.Cells también puede importar datos de otras fuentes de datos.

Aspose.Cells proporciona un[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)clase que representa un archivo de Excel Microsoft. Él[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)colección que permite el acceso a cada hoja de trabajo en un archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. Él[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)recopilación.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)La recopilación proporciona métodos útiles para importar datos de diferentes fuentes de datos. En este artículo se explica cómo se pueden utilizar estos métodos.

## **Importación de datos en Excel con la interfaz ICellsDataTable**
 Implementar[ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) para envolver sus diversas fuentes de datos, luego use[Cells.Importar datos()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) para importar datos a la hoja de cálculo de Excel.
### **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

La implementación de*CustomerDataSource*, *Cliente*, y*Lista de clientes* las clases se dan a continuación

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


## **Importación desde matriz**

 Para importar datos a una hoja de cálculo desde una matriz, llame al[**Importar matriz**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) metodo de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. Hay muchas versiones sobrecargadas del[**Importar matriz**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)pero una sobrecarga típica toma los siguientes parámetros:

- **Formación**, el objeto de matriz del que está importando contenido.
- **Numero de fila**el número de fila de la primera celda a la que se importarán los datos.
- **número de columna**, el número de columna de la primera celda a la que se importarán los datos.
- **es vertical**, un valor booleano que especifica si importar datos vertical u horizontalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

## **Importando desde ArrayList**

 Para importar datos de un*Lista de arreglo* a las hojas de trabajo, llame al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección[**Importar ArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)método. El método ImportArray toma los siguientes parámetros:

- **Lista de arreglo** , representa el*Lista de arreglo*objeto que está importando.
- **Numero de fila**, representa el número de fila de la primera celda a la que se importarán los datos.
- **número de columna**, representa el número de columna de la primera celda a la que se importarán los datos.
- **es vertical**, un valor booleano que especifica si importar datos vertical u horizontalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

## **Importación desde objetos personalizados**

 Para importar datos de una colección de objetos a una hoja de trabajo, use[**Importar objetos personalizados**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). Proporcione una lista de columnas/propiedades al método para mostrar la lista de objetos deseada.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

## **Importación desde objetos personalizados al área fusionada**

Para importar datos de una colección de objetos a una hoja de trabajo que contiene celdas combinadas, use[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) propiedad. Si la plantilla de Excel tiene celdas combinadas, establezca el valor de[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)propiedad a verdadera. Pasa el[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) objeto junto con la lista de columnas/propiedades del método para mostrar la lista deseada de objetos. El siguiente ejemplo de código demuestra el uso de[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) propiedad para importar datos de objetos personalizados a celdas combinadas. por favor vea lo adjunto[Excel fuente](90112033.xlsx) archivo y el[Excel de salida](90112034.xlsx) archivo de referencia.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

## **Importando desde DataTable**

 Para importar datos de un*Tabla de datos* , llama a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) método. Hay muchas versiones sobrecargadas del[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)pero una sobrecarga típica toma los siguientes parámetros:

- **Tabla de datos** , el*Tabla de datos* objeto del que está importando el contenido.
- **¿Se muestra el nombre del campo?** , especifica si los nombres de los*Tabla de datos*las columnas deben importarse a la hoja de trabajo como una primera fila o no.
- **Celda de inicio** , representa el nombre de la celda de inicio (por ejemplo, "A1") desde donde importar el contenido del*Tabla de datos*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

## **Importación desde un objeto dinámico como fuente de datos**

Aspose.Cells proporciona funciones para trabajar con objetos dinámicos como fuente de datos. Ayuda a usar la fuente de datos donde las propiedades se agregan dinámicamente a los objetos. Una vez que se agregan las propiedades al objeto, Aspose.Cells considera la primera entrada como la plantilla y maneja el resto en consecuencia. Significa que si se agrega alguna propiedad dinámica solo a un primer elemento y no a otros objetos, Aspose.Cells considera que todos los elementos de la colección deben ser iguales.

En este ejemplo, se utiliza un modelo de plantilla que inicialmente contiene solo dos variables. Esta Lista se convierte en Lista de objetos dinámicos. Luego se agrega un campo adicional y finalmente se carga en el libro de trabajo. El libro de trabajo selecciona solo aquellos valores que están en el archivo de plantilla XLSX. Este libro de plantilla utiliza marcadores inteligentes que también contienen parámetros. Los parámetros le permiten modificar cómo se presenta la información. Los detalles sobre los marcadores inteligentes se pueden obtener en el siguiente artículo:

[Uso de marcadores inteligentes](/cells/es/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

## **Importando desde DataColumn (.NET)**

A*Tabla de datos*o*vista de datos*objeto se compone de una o más columnas. Los desarrolladores también pueden importar datos de cualquier Columna/Columnas del*Tabla de datos*o*vista de datos*llamando al[**Datos de importacion**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) metodo de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)recopilación. Él[**Datos de importacion**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)método acepta un parámetro de tipo[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions). Él[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) la clase proporciona un[**índices de columna**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)propiedad que acepta una matriz de índices de columnas.

El código de ejemplo que se proporciona a continuación demuestra el uso de[**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) para importar columnas selectivas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

## **Importando desde DataView (.NET)**

 Para importar datos de un*vista de datos* , llama a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección[**Datos de importacion**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) método. Hay muchas versiones sobrecargadas del[**Datos de importacion**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)pero el de DataView toma los siguientes parámetros:

- **Vista de datos:** Él*vista de datos*objeto del que está a punto de importar contenido.
- **Primera fila:**el número de fila de la primera celda a la que se importarán los datos.
- **Primera columna:**el número de columna de la primera celda a la que se importarán los datos.
- **Opciones de importación de tabla:**Las opciones de importación.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

## **Importación desde DataGrid (.NET)**

 Es posible importar datos desde un*Cuadrícula de datos* llamando al[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) metodo de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. Hay muchas versiones sobrecargadas del[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)pero una sobrecarga típica toma los siguientes parámetros:

- **Cuadrícula de datos** , el*Cuadrícula de datos*objeto del que está importando contenido.
- **Numero de fila**el número de fila de la primera celda a la que se importarán los datos.
- **Número de columna**, el número de columna de la primera celda a la que se importarán los datos.
- **Insertar filas**, una propiedad booleana que indica si se deben agregar filas adicionales a la hoja de trabajo para ajustar los datos o no.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

## **Importación desde GridView**

 Para importar datos de un*Vista en cuadrícula* controle, llame al[**Importar vista de cuadrícula**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) metodo de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)recopilación.

Aspose.Cells nos permite respetar los valores con formato HTML al importar datos a la hoja de cálculo. Cuando el análisis HTML está habilitado durante la importación de datos, Aspose.Cells convierte el HTML en el formato de celda correspondiente.

## **Importación de datos con formato HTML**

 Aspose.Cells proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)clase que proporciona métodos muy útiles para importar datos de fuentes de datos externas. Este artículo muestra cómo analizar texto con formato HTML al importar datos y convertir HTML en valores de celda con formato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

## **Importación de datos desde JSON**

Aspose.Cells proporciona un[**JsonUtilidad**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) clase para procesamiento JSON.[**JsonUtilidad**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) la clase tiene un[**Datos de importacion**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) método para importar datos JSON. Aspose.Cells también proporciona un[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) clase que representa las opciones del diseño JSON. Él[**Datos de importacion**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)método acepta[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)como parámetro. Él[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)La clase proporciona las siguientes propiedades.

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): Indica en la matriz que se debe procesar como una tabla o no.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): Obtiene o establece un valor que indica si la cadena en JSON se va a convertir en numérico o de fecha.
- [**Formato de fecha**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): Obtiene y establece el formato del valor de fecha.
- [**IgnorarArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): Indica si ignorar el título si la propiedad del objeto es una matriz
- [**IgnorarNulo**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): Indica si el valor nulo debe ignorarse o no.
- [**IgnoreObjectTitleIgnoreObjectTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): Indica si ignorar el título si la propiedad del objeto es un objeto.
- [**Formato numérico**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Obtiene y establece el formato del valor numérico.
- [**TítuloEstilo**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Obtiene y establece el estilo del título.

El código de ejemplo que se proporciona a continuación demuestra el uso de la[**JsonUtilidad**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) y[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) clases para importar JSON datos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

## **Temas avanzados**
- [Especificar campos de fórmula al importar datos a la hoja de trabajo](/cells/es/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Desplace la primera fila hacia abajo al insertar Cells Filas de la tabla de datos](/cells/es/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
