---
title: Público API Cambios en Aspose.Cells 8.4.0
type: docs
weight: 130
url: /es/net/public-api-changes-in-aspose-cells-8-4-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.3.2 a la 8.4.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados,[Clases añadidas, etc.](/cells/es/net/public-api-changes-in-aspose-cells-8-4-0/) y[clases eliminadas, etc.](/cells/es/net/public-api-changes-in-aspose-cells-8-4-0/), pero también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Mecanismo para modificar el código VBA/macro en hojas de cálculo**
 Con el fin de proporcionar la característica de[Manipulación de código VBA/macro](/cells/es/net/modifying-vba-or-macro-code-using-aspose-cells/), el Aspose.Cells for .NET 8.4.0 ha expuesto una serie de nuevas clases y propiedades en el espacio de nombres Aspose.Cells.Vba. Algunos de los detalles importantes de estas nuevas clases son los siguientes.

- La clase VbaProject se puede usar para obtener el proyecto VBA de una hoja de cálculo determinada.
- La clase VbaModuleCollection representa la colección de módulos de VBA que forman parte de un VbaProject determinado.
- La clase VbaModule representa un único módulo de VbaModuleCollection.

El siguiente fragmento de código muestra cómo modificar dinámicamente los segmentos de código VBA.

**C#**

{{< highlight "csharp" >}}

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


### **Capacidad para eliminar la tabla dinámica**
Aspose.Cells for .NET 8.4.0 ha expuesto dos métodos para PivotTableCollection para proporcionar la función de eliminación de tabla dinámica de una hoja de cálculo determinada. Los detalles de los métodos mencionados son los siguientes.

- El método PivotTableCollection.Remove acepta un objeto de PivotTable y lo elimina de la colección.
- El método PivotTableCollection.RemoveAt acepta un valor entero basado en índice cero y quita la tabla dinámica particular de la colección.

El siguiente fragmento de código muestra cómo eliminar la tabla dinámica utilizando los dos métodos mencionados anteriormente.

**C#**

{{< highlight "csharp" >}}

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


### **Compatibilidad con diferentes diseños de tablas dinámicas**
Aspose.Cells for .NET 8.4.0 proporciona soporte para diferentes diseños predefinidos para tablas dinámicas. Para proporcionar esta función, las API Aspose.Cells han expuesto tres métodos para la clase de tabla dinámica, como se detalla a continuación.

- El método PivotTable.ShowInCompactForm representa la tabla dinámica en un diseño compacto.
- El método PivotTable.ShowInOutlineForm representa la tabla dinámica en el diseño de esquema.
- El método PivotTable.ShowInTabularForm representa la tabla dinámica en un diseño tabular.

{{% alert color="primary" %}} 

Es importante llamar a PivotTable.RefreshData & PivotTable.CalculateData después de configurar cualquiera de los diseños mencionados anteriormente.

{{% /alert %}} 

El siguiente código de ejemplo establece diferentes diseños para una tabla dinámica y almacena el resultado en el disco.

**C#**

{{< highlight "csharp" >}}

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


### **Clase TxtLoadStyleStrategy y propiedad TxtLoadOptions.LoadStyleStrategy agregado**
Aspose.Cells for .NET 8.4.0 ha expuesto la clase TxtLoadStyleStrategy y la propiedad TxtLoadOptions.LoadStyleStrategy para especificar la estrategia para formatear los valores analizados al convertir el valor de cadena en número o fecha y hora.
### **Método DataBar.ToImage agregado**
Con el lanzamiento de v8.4.0, Aspose.Cells API ha proporcionado el método DataBar.ToImage para guardar las barras de datos con formato condicional en formato de imagen. El método {DataBar.ToImage}} acepta dos parámetros como se detalla a continuación.

- El primer parámetro es del tipo Aspose.Cells.Cell al que se le ha aplicado formato condicional.
- El segundo parámetro es del tipo Aspose.Cells.Rendering.ImageOrPrintOptions para establecer diferentes parámetros de la imagen resultante.

El siguiente código de ejemplo demuestra el uso del método DataBar.ToImage para representar el DataBar en formato de imagen.

**C#**

{{< highlight "csharp" >}}

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

byte[]imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **Propiedad Border.ThemeColor agregado**
Aspose.Cells Las API permiten extraer datos de formato relacionados con el tema de las hojas de cálculo. Con el lanzamiento de Aspose.Cells for .NET 8.4.0, API ha expuesto la propiedad Border.ThemeColor que se puede usar para recuperar los atributos de color del tema de los bordes Cell.
### **Propiedad DrawObject.ImageBytes agregada**
Aspose.Cells for .NET 8.4.0 ha expuesto la propiedad DrawObject.ImageBytes para obtener los datos de imagen de Chart o Shape.
### **Propiedad HtmlSaveOptions.ExportBogusRowData agregado**
Aspose.Cells for .NET 8.4.0 ha proporcionado la propiedad {HtmlSaveOptions.ExportBogusRowData}}. La propiedad de tipo booleano determina si API inyectará datos falsos en la fila inferior al exportar la hoja de cálculo al formato HTML.

{{% alert color="primary" %}} 

El valor por defecto es verdadero.

{{% /alert %}} 

El siguiente código de ejemplo ilustra el uso de dicha propiedad.

**C#**

{{< highlight "csharp" >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Propiedad HtmlSaveOptions.CellCssPrefix agregado**
La propiedad recién agregada HtmlSaveOptions.CellCssPrefix permite establecer el prefijo para los archivos CSS al exportar hojas de cálculo al formato HTML.

{{% alert color="primary" %}} 

El valor predeterminado es una cadena vacía).

{{% /alert %}}
## **API obsoletas**
### **Métodos Cells.GetCellByIndex & Row.GetCellByIndex Obsoletos**
Utilice el método GetEnumerator para iterar todas las celdas en su lugar.
### **Propiedad DrawObject.Image obsoleta**
Utilice la propiedad DrawObject.ImageBytes para obtener datos de imagen en su lugar.
