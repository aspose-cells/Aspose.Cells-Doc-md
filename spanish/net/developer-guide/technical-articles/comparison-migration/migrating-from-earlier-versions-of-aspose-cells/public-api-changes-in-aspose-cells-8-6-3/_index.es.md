---
title: Público API Cambios en Aspose.Cells 8.6.3
type: docs
weight: 220
url: /es/net/public-api-changes-in-aspose-cells-8-6-3/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.6.2 a la 8.6.3 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Compatibilidad con el análisis HTML durante la importación de datos**
Esta versión de Aspose.Cells for .NET API ha expuesto la propiedad ImportTableOptions.IsHtmlString que indica a API que analice las etiquetas HTML al importar datos en la hoja de trabajo y establezca el resultado analizado como valor de celda. Tenga en cuenta que las API Aspose.Cells ya proporcionan Cell.HtmlString para realizar esta tarea para una sola celda; sin embargo, al importar datos de forma masiva, como desde DataTable, la propiedad ImportTableOptions.IsHtmlString (cuando se establece en true) intenta analizar todos los datos compatibles. HTML etiqueta y establece los resultados analizados en las celdas correspondientes.

Este es el escenario de uso más simple.

**C#**

{{< highlight "csharp" >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **Método Workbook.CreateBuiltinStyle agregado**
 Aspose.Cells for .NET 8.6.3 ha expuesto el método Workbook.CreateBuiltinStyle que se puede usar para crear un objeto de la clase Style que corresponde a uno de los[estilos integrados ofrecidos por la aplicación Excel](/cells/es/net/using-built-in-styles/)El método Workbook.CreateBuiltinStyle acepta una constante de la enumeración BuiltinStyleType. Tenga en cuenta que con las versiones anteriores de las API Aspose.Cells, la misma tarea se podría realizar a través del método StyleCollection.CreateBuiltinStyle, pero como las versiones recientes de las API Aspose.Cells han eliminado la clase StyleCollection, por lo tanto, el método Workbook.CreateBuiltinStyle recientemente expuesto se puede considerar como un enfoque alternativo para lograr lo mismo.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **Método Cells. ImportGridView agregado**
Aspose.Cells for .NET 8.6.3 ha expuesto una versión sobrecargada de Cells.ImportGridView que ahora puede aceptar una instancia de ImportTableOptions para dar más control sobre el proceso de importación.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions & set its various properties

var importOptions = new ImportTableOptions();

importOptions.IsHtmlString = true;

importOptions.IsFieldNameShown = true;

//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **Propiedad ImportTableOptions.ConvertGridStyle agregada**
En referencia a las mejoras mencionadas anteriormente, la última versión de Aspose.Cells for .NET API también ha expuesto la propiedad ImportTableOptions.ConvertGridStyle. Esta propiedad de tipo booleano permite a los desarrolladores controlar la apariencia de los datos importados, donde establecer la propiedad ImportTableOptions.ConvertGridStyle en verdadero indica que API aplicará el estilo de GridView a las celdas donde se importaron los datos.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set ConvertGridStyle property to true

importOptions.ConvertGridStyle = true;



//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **Propiedad LoadDataOption.OnlyVisibleWorksheet agregada**
 Aspose.Cells for .NET 8.6.3 ha expuesto la propiedad LoadDataOption.OnlyVisibleWorksheet que, al establecerse en verdadero, influirá en el mecanismo de carga de Aspose.Cells for .NET API, como resultado, solo se cargarán las hojas de trabajo visibles de una hoja de cálculo determinada. Por favor, checa el[artículo detallado](/cells/es/net/different-ways-to-open-files/) en esta asignatura.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of LoadDataOption

var loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.OnlyVisibleWorksheet = true;

//Create an instance of LoadOptions

var loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.LoadDataOptions = loadDataOptions;



//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

var book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **API obsoletas**
### **Método Worksheet.CopyConditionalFormatting Obsoleto**
Como alternativa al método Worksheet.CopyConditionalFormatting, se recomienda utilizar cualquiera de los métodos Cells.CopyRows o Range.Copy.
### **Propiedad Cells. Fin obsoleto**
Utilice la propiedad Cells.LastCell como alternativa a la propiedad Cells.End.
