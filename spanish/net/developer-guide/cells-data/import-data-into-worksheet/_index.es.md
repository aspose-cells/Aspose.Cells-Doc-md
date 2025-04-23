---
title: Importar datos en hoja de cálculo
type: docs
weight: 170
url: /es/net/import-data-into-worksheet/
description: Aprende cómo importar datos en la hoja de cálculo a través de la API Aspose.Cells for .NET.
keywords: Importar datos en la hoja de cálculo con C#, Importar datos en Excel con la interfaz ICellsDataTable, Importar datos desde Array, Importar datos desde ArrayList, Importar datos desde Objetos Personalizados, Importar datos desde Objetos Personalizados a un área combinada, Importar datos desde DataTable, Importar datos desde objeto dinámico como fuente de datos, Importar datos desde columna de datos, Importar datos desde DataView, Importar datos desde DataGrid, Importar datos desde GridView, Importar datos formateados en HTML, Importar datos de JSON
---

{{% alert color="primary" %}}

Este artículo trata sobre algunas técnicas de importación de datos a las que los desarrolladores tienen acceso a través de Aspose.Cells.

{{% /alert %}}

## **Cómo Importar Datos en una Hoja de Cálculo**

Cuando abres un archivo de Excel con Aspose.Cells, todos los datos en el archivo se importan automáticamente. Aspose.Cells también puede importar datos de otras fuentes de datos.

Aspose.Cells proporciona una clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). La colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) proporciona métodos útiles para importar datos desde diferentes fuentes de datos. Este artículo explica cómo se pueden utilizar estos métodos.

## **Cómo Importar datos en Excel con la interfaz ICellsDataTable**
Implementa [ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) para envolver tus diversas fuentes de datos, luego usa [Cells.ImportData()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) para importar datos en la hoja de cálculo de Excel.
### **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

A continuación se presenta la implementación de las clases *CustomerDataSource*, *Customer* y *CustomerList*

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


## **Cómo Importar Datos en Excel desde un Array**

Para importar datos a una hoja de cálculo desde un array, llama al método [**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Hay muchas versiones sobrecargadas del método [**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) pero una sobrecarga típica toma los siguientes parámetros:

- **Array**, el objeto array desde el que estás importando contenido.
- **Número de fila**, el número de fila de la primera celda a la que se importarán los datos.
- **Número de columna**, el número de columna de la primera celda a la que se importarán los datos.
- **Es vertical**, un valor booleano que especifica si se importarán los datos vertical u horizontalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

## **Cómo Importar Datos en Excel desde un ArrayList**

Para importar datos desde un *ArrayList* a hojas de cálculo, llama al método [**ImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). El método ImportArray toma los siguientes parámetros:

- **Lista de array**, representa el objeto *ArrayList* que estás importando.
- **Número de fila**, representa el número de fila de la primera celda a la que se importarán los datos.
- **Número de columna**, representa el número de columna de la primera celda a la que se importarán los datos.
- **Es vertical**, un valor booleano que especifica si se importarán los datos vertical u horizontalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

## **Cómo importar datos en Excel desde objetos personalizados**

Para importar datos de una colección de objetos a una hoja de cálculo, use [**ImportCustomObjects**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). Proporcione una lista de columnas/propiedades al método para mostrar su lista deseada de objetos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

## **Cómo importar datos en Excel desde objetos personalizados y verificar el área combinada**

Para importar datos de una colección de objetos a una hoja de cálculo que contiene celdas combinadas, use la propiedad [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells). Si la plantilla de Excel tiene celdas combinadas, establezca el valor de la propiedad [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) en true. Pase el objeto [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) junto con la lista de columnas/propiedades al método para mostrar su lista deseada de objetos. El siguiente ejemplo de código demuestra el uso de la propiedad [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) para importar datos de objetos personalizados a celdas combinadas. Consulte el archivo de Excel adjunto de origen (90112033.xlsx) y el archivo de Excel de salida (90112034.xlsx) para obtener más información.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

## **Cómo importar datos en Excel desde un DataTable**

Para importar datos desde un *DataTable*, llame al método [**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Existen muchas versiones sobrecargadas del método [**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index), pero una sobrecarga típica toma los siguientes parámetros:

- **DataTable**, el objeto *DataTable* desde el cual está importando el contenido.
- **Se muestra el nombre de campo**, especifica si los nombres de las columnas de *DataTable* deben importarse a la hoja de cálculo como primera fila o no.
- **Celda de inicio**, representa el nombre de la celda de inicio (por ejemplo, "A1") desde donde importar los contenidos de *DataTable*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

## **Cómo importar datos en Excel desde un objeto dinámico como fuente de datos**

Aspose.Cells proporciona características para trabajar con objetos dinámicos como fuente de datos. Esto ayuda en el uso de una fuente de datos donde las propiedades se agregan dinámicamente a los objetos. Una vez que las propiedades se agregan al objeto, Aspose.Cells considera la primera entrada como la plantilla y maneja el resto en consecuencia. Esto significa que si alguna propiedad dinámica se agrega solo a un primer elemento y no a otros objetos, Aspose.Cells considera que todos los elementos en la colección deberían ser iguales.

En este ejemplo, se utiliza un modelo de plantilla que inicialmente contiene solo dos variables. Esta lista se convierte en una lista de objetos dinámicos. Luego se agrega algún campo adicional y finalmente se carga en el libro de trabajo. El libro de trabajo recoge solo esos valores que están en el archivo XLSX de plantilla. Este libro de trabajo de plantilla utiliza Marcadores Inteligentes que también contienen parámetros. Los parámetros le permiten modificar cómo se muestra la información. Los detalles sobre los Marcadores Inteligentes se pueden obtener del siguiente artículo:

[Usando Marcadores Inteligentes](/cells/es/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

## **Cómo importar DataColumn en Excel**

Un objeto *DataTable* o *DataView* está compuesto por una o más columnas. Los desarrolladores también pueden importar datos de cualquier columna/columnas del *DataTable* o *DataView* llamando al método [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). El método [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) acepta un parámetro de tipo [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions). La clase [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) proporciona una propiedad [**ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) que acepta una matriz de índices de columnas.

El código de muestra a continuación demuestra el uso de [**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) para importar columnas selectivas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

## **Cómo importar DataView en Excel**

Para importar datos desde un *DataView*, llame al método [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Existen muchas versiones sobrecargadas del método [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index), pero la de DataView toma los siguientes parámetros:

- **DataView:** El objeto *DataView* del cual vas a importar contenido.
- **Primera fila:** el número de fila de la primera celda a la que se importarán los datos.
- **Primera columna:** el número de columna de la primera celda a la que se importarán los datos.
- **Opciones de importación de tabla:** Las opciones de importación.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

## **Cómo importar DataGrid a Excel**

Es posible importar datos de un *DataGrid* llamando al método [**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Hay muchas versiones sobrecargadas del método [**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) pero una sobrecarga típica toma los siguientes parámetros:

- **Data grid**, el objeto *DataGrid* del cual estás importando contenido.
- **Número de fila**, el número de fila de la primera celda a la que se importarán los datos.
- **Número de columna**, el número de columna de la primera celda a la que se importarán los datos.
- **Insertar filas**, una propiedad booleana que indica si se deben agregar filas adicionales a la hoja de cálculo para ajustar los datos o no.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

## **Cómo importar GridView a Excel**

Para importar datos desde un control *GridView*, llama al método [**ImportGridView**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells).

Aspose.Cells nos permite respetar los valores formateados en HTML al importar datos a la hoja de cálculo. Cuando se habilita el análisis de HTML al importar datos, Aspose.Cells convierte el HTML en el formato de celda correspondiente.

## **Cómo importar datos con formato HTML a Excel**

Aspose.Cells proporciona una clase [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) que ofrece métodos muy útiles para importar datos desde fuentes de datos externas. Este artículo muestra cómo analizar texto con formato HTML al importar datos y convertir el HTML en valores de celda formateados.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

## **Cómo importar datos a Excel desde JSON**

Aspose.Cells proporciona una clase [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) para procesar JSON. La clase [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) tiene un método [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) para importar datos JSON. Aspose.Cells también proporciona una clase [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) que representa las opciones del diseño JSON. El método [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) acepta [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) como parámetro. La clase [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) proporciona las siguientes propiedades.

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): Indica si el arreglo debe procesarse como una tabla o no.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): Obtiene o establece un valor que indica si la cadena en JSON debe convertirse a numérico o fecha.
- [**DateFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): Obtiene y establece el formato del valor de fecha.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): Indica si se debe omitir el título si la propiedad del objeto es un arreglo.
- [**IgnoreNull**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): Indica si el valor nulo debe ser ignorado o no.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): Indica si se debe ignorar el título si la propiedad del objeto es un objeto.
- [**NumberFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Obtiene y establece el formato del valor numérico.
- [**TitleStyle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Obtiene y establece el estilo del título.

El código de muestra que se muestra a continuación demuestra el uso de las clases [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) y [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) para importar datos JSON.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

## **Temas avanzados**
- [Especificar Campos de Fórmula al Importar Datos a la Hoja de Cálculo](/cells/es/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Desplazar la primera fila hacia abajo al insertar filas de tabla de datos de celdas](/cells/es/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
{{< app/cells/assistant language="csharp" >}}
