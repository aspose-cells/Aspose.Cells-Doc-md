---
title: Público API Cambios en Aspose.Cells 8.6.3
type: docs
weight: 230
url: /es/java/public-api-changes-in-aspose-cells-8-6-3/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.6.2 a la 8.6.3 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Compatibilidad con el análisis HTML durante la importación de datos**
Esta versión de Aspose.Cells for Java API ha expuesto el atributo ImportTableOptions.setHtmlString que indica a API que analice las etiquetas HTML al importar datos en la hoja de trabajo y establezca el resultado analizado como valor de celda. Tenga en cuenta que las API Aspose.Cells ya proporcionan el atributo Cell.setHtmlString para realizar esta tarea para una sola celda; sin embargo, al importar datos de forma masiva, el atributo ImportTableOptions.setHtmlString (cuando se establece en verdadero) intenta analizar todas las etiquetas y conjuntos HTML admitidos los resultados analizados a las celdas correspondientes.

Este es el escenario de uso más simple.

**Java**

{{< highlight "csharp" >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **Método Workbook.createBuiltinStyle agregado**
 Aspose.Cells for Java 8.6.3 ha expuesto el método Workbook.createBuiltinStyle que se puede usar para crear un objeto de la clase Style que corresponde a uno de los[estilos integrados ofrecidos por la aplicación Excel](/cells/es/java/using-built-in-styles/)El método Workbook.createBuiltinStyle acepta una constante de la enumeración BuiltinStyleType. Tenga en cuenta que con las versiones anteriores de las API Aspose.Cells, la misma tarea se podía realizar a través del método StyleCollection.createBuiltinStyle, pero como las versiones recientes de las API Aspose.Cells han eliminado la clase StyleCollection, por lo tanto, el método Workbook.createBuiltinStyle recientemente expuesto se puede considerar como un enfoque alternativo para lograr lo mismo.

El siguiente es el escenario de uso simple.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **Propiedad LoadDataOption.OnlyVisibleWorksheet agregada**
Aspose.Cells for Java 8.6.3 ha expuesto la propiedad LoadDataOption.OnlyVisibleWorksheet que, al establecerse en verdadero, influirá en el mecanismo de carga de Aspose.Cells for Java API, como resultado, solo se cargarán las hojas de trabajo visibles de una hoja de cálculo determinada.

El siguiente es el escenario de uso simple.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadDataOption

LoadDataOption loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.setOnlyVisibleWorksheet(true);

//Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.setLoadDataOptions(loadDataOptions);

//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

Workbook book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **API obsoletas**
### **Método Worksheet.copyConditionalFormatting Obsoleto**
Como alternativa al método Worksheet.copyConditionalFormatting, se recomienda utilizar cualquiera de los métodos Cells.copyRows o Range.copy.
### **Propiedad Cells. Fin obsoleto**
Utilice la propiedad Cells.LastCell como alternativa a la propiedad Cells.End.
