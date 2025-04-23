---
title: Cambios en la API pública en Aspose.Cells 8.4.0
type: docs
weight: 130
url: /es/net/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.3.2 hasta la 8.4.0 que pueden interesar a los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos métodos públicos actualizados, [clases añadidas, etc.](/cells/es/net/cambios-en-la-api-pública-en-aspose-cells-8-4-0/) y [clases eliminadas, etc.](/cells/es/net/cambios-en-la-api-pública-en-aspose-cells-8-4-0/), sino también una descripción de cualquier cambio en el comportamiento interno en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Mecanismo para modificar el código VBA/Macro en hojas de cálculo**
Para proporcionar la función de [Manipulación del código VBA/Macro](/cells/es/net/modificar-codigo-vba-o-macro-usando-aspose-cells/), el Aspose.Cells for .NET 8.4.0 ha expuesto una serie de nuevas clases y propiedades en el espacio de nombres Aspose.Cells.Vba. Algunos detalles importantes de estas nuevas clases son los siguientes.

- La clase VbaProject se puede utilizar para obtener el proyecto VBA de una hoja de cálculo dada.
- La clase VbaModuleCollection representa la colección de módulos VBA que forman parte de un VbaProject dado.
- La clase VbaModule representa un único módulo de la VbaModuleCollection.

El siguiente fragmento de código muestra cómo modificar dinámicamente los segmentos de código VBA.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

foreach (VbaModule module in workbook.VbaProject.Modules)

{

    string code = module.Codes;

    //Replace the original message with the modified message

    if (code.Contains("This is test message."))

    {

        code = code.Replace("This is test message.", "This is Aspose.Cells message.");

        module.Codes = code;

    }

}

//Save the output Excel file

workbook.Save("output.xlsm");

{{< /highlight >}}


### **Capacidad para eliminar una tabla dinámica**
El Aspose.Cells for .NET 8.4.0 ha expuesto dos métodos para la colección PivotTable para proporcionar la función de eliminación de tabla dinámica de una hoja de cálculo dada. Los detalles de los métodos mencionados son los siguientes.

- El método PivotTableCollection.Remove acepta un objeto de PivotTable y lo elimina de la colección.
- El método RemoveAt de PivotTableCollection acepta un valor entero basado en índices cero y elimina la tabla dinámica específica de la colección.

El siguiente fragmento de código muestra cómo eliminar la tabla dinámica utilizando ambos métodos mencionados anteriormente.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the first pivot table object

PivotTable pivotTable = worksheet.PivotTables[0];

//Remove pivot table using pivot table object

worksheet.PivotTables.Remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.PivotTables.RemoveAt(0);

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Soporte para Diferentes Diseños de Tabla Dinámica**
Aspose.Cells for .NET 8.4.0 proporciona soporte para diferentes diseños predefinidos para Tablas Dinámicas. Para ofrecer esta característica, las APIs de Aspose.Cells han expuesto tres métodos para la clase PivotTable como se describe a continuación.

- El método ShowInCompactForm de PivotTable muestra la Tabla Dinámica en diseño Compacto.
- El método ShowInOutlineForm de PivotTable muestra la Tabla Dinámica en diseño de Contorno.
- El método ShowInTabularForm de PivotTable muestra la Tabla Dinámica en diseño Tabular.

{{% alert color="primary" %}} 

Es importante llamar a PivotTable.RefreshData & PivotTable.CalculateData después de establecer cualquiera de los diseños mencionados anteriormente.

{{% /alert %}} 

El siguiente código de muestra establece diferentes diseños para una Tabla Dinámica y guarda el resultado en disco.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first pivot table

PivotTable pivotTable = worksheet.PivotTables[0];

//Render the pivot table in compact form

pivotTable.ShowInCompactForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("CompactForm.xlsx");

//Render the pivot table in outline form

pivotTable.ShowInOutlineForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("OutlineForm.xlsx");

//Render the pivot table in tabular form

pivotTable.ShowInTabularForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("TabularForm.xlsx");

{{< /highlight >}}


### **Se agregó la Clase TxtLoadStyleStrategy y la Propiedad TxtLoadOptions.LoadStyleStrategy**
Aspose.Cells for .NET 8.4.0 ha expuesto la clase TxtLoadStyleStrategy y la propiedad TxtLoadOptions.LoadStyleStrategy para especificar la estrategia para formatear los valores analizados al convertir el valor de cadena a número o fecha.
### **Se agregó el método DataBar.ToImage**
Con el lanzamiento de v8.4.0, la API de Aspose.Cells ha proporcionado el método DataBar.ToImage para guardar las Barras de Datos formateadas condicionalmente en formato de imagen. El método {DataBar.ToImage}} acepta dos parámetros como se detalla a continuación.

- El primer parámetro es de tipo Aspose.Cells.Cell en el que se ha aplicado el formato condicional.
- El segundo parámetro es de tipo Aspose.Cells.Rendering.ImageOrPrintOptions para establecer diferentes parámetros de la imagen resultante.

El siguiente código de ejemplo demuestra el uso del método DataBar.ToImage para mostrar la Barra de Datos en formato de imagen.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.Cells["C1"];

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.GetFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc[0].DataBar;

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.ImageFormat = ImageFormat.Png;

//Get the image bytes of the databar

byte[] imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **Agregada la propiedad Border.ThemeColor.**
Las APIs de Aspose.Cells permiten extraer datos de formato relacionados con el tema de las hojas de cálculo. Con el lanzamiento de Aspose.Cells for .NET 8.4.0, la API ha expuesto la propiedad Border.ThemeColor que se puede utilizar para recuperar los atributos de color de tema de los bordes de celda.
### **Agregada la propiedad DrawObject.ImageBytes.**
Aspose.Cells for .NET 8.4.0 ha expuesto la propiedad DrawObject.ImageBytes para obtener los datos de imagen de Gráfico o Forma.
### **Agregada la propiedad HtmlSaveOptions.ExportBogusRowData.**
Aspose.Cells for .NET 8.4.0 ha proporcionado la propiedad {HtmlSaveOptions.ExportBogusRowData}. La propiedad de tipo booleano determina si la API inyectará datos de fila inferior falsos al exportar la hoja de cálculo al formato HTML.

{{% alert color="primary" %}} 

El valor predeterminado es true.

{{% /alert %}} 

El siguiente código de muestra ilustra el uso de dicha propiedad.

**C#**

{{< highlight csharp >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Agregada la propiedad HtmlSaveOptions.CellCssPrefix.**
La propiedad recién añadida HtmlSaveOptions.CellCssPrefix permite establecer el prefijo para los archivos CSS al exportar hojas de cálculo al formato HTML.

{{% alert color="primary" %}} 

El valor predeterminado es "" (cadena vacía).

{{% /alert %}}
## **APIs obsoletas**
### **Métodos Obsoletos Cells.GetCellByIndex y Row.GetCellByIndex**
Utilice el método GetEnumerator para iterar todas las celdas en su lugar.
### **Propiedad obsoleta DrawObject.Image**
Utilice la propiedad DrawObject.ImageBytes para obtener los datos de la imagen en su lugar.
{{< app/cells/assistant language="csharp" >}}
