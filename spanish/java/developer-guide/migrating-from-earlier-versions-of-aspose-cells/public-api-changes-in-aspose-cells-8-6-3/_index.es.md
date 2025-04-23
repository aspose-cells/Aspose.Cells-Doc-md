---
title: Cambios en la API pública en Aspose.Cells 8.6.3
type: docs
weight: 230
url: /es/java/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.6.2 a la 8.6.3 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, clases añadidas, sino también una descripción de cualquier cambio en el comportamiento tras bastidores de Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Soporte para Análisis HTML al Importar Datos**
Esta versión de la API Aspose.Cells for Java ha expuesto el atributo ImportTableOptions.setHtmlString que dirige a la API a analizar las etiquetas HTML al importar datos en la Hoja de Cálculo y establecer el resultado analizado como valor de la celda. Por favor, tenga en cuenta que las APIs de Aspose.Cells ya proporcionan el atributo Cell.setHtmlString para realizar esta tarea para una sola celda, sin embargo, al importar datos en masa, el atributo ImportTableOptions.setHtmlString (cuando se establece en true) intenta analizar todas las etiquetas HTML admitidas y establece los resultados analizados en las celdas correspondientes.

Aquí se presenta el escenario de uso más simple.

**Java**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **Método Workbook.createBuiltinStyle Añadido**
Aspose.Cells for Java 8.6.3 ha expuesto el método Workbook.createBuiltinStyle que puede ser usado para crear un objeto de la clase Style que corresponde a uno de los [estilos integrados ofrecidos por la aplicación Excel](/cells/es/java/using-built-in-styles/). El método Workbook.createBuiltinStyle acepta una constante de la enumeración BuiltinStyleType. Por favor tenga en cuenta, con las versiones anteriores de las APIs de Aspose.Cells, la misma tarea se podía lograr a través del método StyleCollection.createBuiltinStyle, pero como las versiones recientes de las APIs de Aspose.Cells han eliminado la clase StyleCollection, por lo tanto, el método Workbook.createBuiltinStyle recién expuesto puede ser considerado como un enfoque alternativo para lograr lo mismo.

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **Propiedad LoadDataOption.OnlyVisibleWorksheet Añadida**
Aspose.Cells for Java 8.6.3 ha expuesto la propiedad LoadDataOption.OnlyVisibleWorksheet la cual, al establecerse en true, influirá en el mecanismo de carga de la API Aspose.Cells for Java, como resultado solo las hojas de cálculo visibles de una hoja de cálculo dada se cargarán.

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

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
## **APIs obsoletas**
### **Método Worksheet.copyConditionalFormatting Obsoleto**
Como alternativa al método Worksheet.copyConditionalFormatting, se recomienda utilizar cualquiera de los métodos Cells.copyRows o Range.copy.
### **Propiedad Cells.End Obsoleta**
Por favor, utilice la propiedad Cells.LastCell como alternativa a la propiedad Cells.End.
{{< app/cells/assistant language="java" >}}
