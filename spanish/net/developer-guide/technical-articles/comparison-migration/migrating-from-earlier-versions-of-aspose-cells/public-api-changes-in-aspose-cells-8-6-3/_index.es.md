---
title: Cambios en la API pública en Aspose.Cells 8.6.3
type: docs
weight: 220
url: /es/net/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.6.2 a la 8.6.3 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, clases añadidas, sino también una descripción de cualquier cambio en el comportamiento tras bastidores de Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Soporte para Análisis HTML al Importar Datos**
Esta versión de la API Aspose.Cells for .NET ha expuesto la propiedad ImportTableOptions.IsHtmlString que indica a la API analizar las etiquetas HTML al importar datos en la hoja de cálculo y establecer el resultado analizado como valor de celda. Tenga en cuenta que las API de Aspose.Cells ya proporcionan Cell.HtmlString para realizar esta tarea para una sola celda, sin embargo, al importar datos en masa, como desde un DataTable, la propiedad ImportTableOptions.IsHtmlString (cuando se establece en true) intenta analizar todas las etiquetas HTML admitidas y establece los resultados analizados en las celdas correspondientes.

Aquí se presenta el escenario de uso más simple.

**C#**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **Se agregó el método Workbook.CreateBuiltinStyle**
Aspose.Cells for .NET 8.6.3 ha expuesto el método Workbook.CreateBuiltinStyle que se puede utilizar para crear un objeto de la clase Style que corresponde a uno de los [estilos integrados ofrecidos por la aplicación Excel](/cells/es/net/using-built-in-styles/). El método Workbook.CreateBuiltinStyle acepta una constante de la enumeración BuiltinStyleType. Por favor, tenga en cuenta que, con versiones anteriores de las APIs de Aspose.Cells, la misma tarea se podía lograr a través del método StyleCollection.CreateBuiltinStyle pero como las versiones recientes de las APIs de Aspose.Cells han eliminado la clase StyleCollection, por lo tanto el método Workbook.CreateBuiltinStyle recientemente expuesto puede considerarse como un enfoque alternativo para lograr lo mismo.

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **Agregado método Cells.ImportGridView**
Aspose.Cells for .NET 8.6.3 ha expuesto una versión sobrecargada de Cells.ImportGridView que ahora puede aceptar una instancia de ImportTableOptions para tener más control sobre el proceso de importación.

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

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


### **Agregada propiedad ImportTableOptions.ConvertGridStyle**
En referencia a las mejoras mencionadas anteriormente, la última versión de la API Aspose.Cells for .NET también ha expuesto la propiedad ImportTableOptions.ConvertGridStyle. Esta propiedad de tipo Boolean permite a los desarrolladores controlar la apariencia de los datos importados, donde establecer la propiedad ImportTableOptions.ConvertGridStyle en true indica que la API aplicará el estilo del GridView a las celdas donde se han importado los datos.

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

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


### **Agregada propiedad LoadDataOption.OnlyVisibleWorksheet**
Aspose.Cells for .NET 8.6.3 ha expuesto la propiedad LoadDataOption.OnlyVisibleWorksheet la cual, al establecerse en true, influirá en el mecanismo de carga de la API Aspose.Cells for .NET, como resultado solo se cargarán las hojas de cálculo visibles de una hoja de cálculo dada. Por favor, revise el [artículo detallado](/cells/es/net/different-ways-to-open-files/) sobre este tema.

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

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
## **APIs obsoletas**
### **Método Worksheet.CopyConditionalFormatting Obsoleto**
Como alternativa al método Worksheet.CopyConditionalFormatting, se recomienda utilizar cualquiera de los métodos Cells.CopyRows o Range.Copy.
### **Propiedad Cells.End Obsoleta**
Por favor, utilice la propiedad Cells.LastCell como alternativa a la propiedad Cells.End.
{{< app/cells/assistant language="csharp" >}}
