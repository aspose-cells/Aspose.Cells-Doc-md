---
title: Cambios en la API Pública en Aspose.Cells 8.3.2
type: docs
weight: 120
url: /es/net/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.3.1 hasta la 8.3.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, [clases añadidas, etc.](/cells/es/net/public-api-changes-in-aspose-cells-8-3-2/) y [clases eliminadas, etc.](/cells/es/net/public-api-changes-in-aspose-cells-8-3-2/), sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Mecanismo para Establecer la Posición Absoluta de un Elemento de un Informe de Tabla Dinámica**
Para proporcionar la característica [Posicionamiento Absoluto del Elemento de Informe de Tabla Dinámica](/cells/es/net/specifying-the-absolute-position-of-the-pivot-item/), el Aspose.Cells for .NET 8.3.2 ha expuesto una serie de propiedades y métodos auxiliares como se listan a continuación.

- La propiedad PivotItem.Position puede ser utilizada para especificar el índice de posición en todos los PivotItems independientemente del nodo padre.
- La propiedad PivotItem.PositionInSameParentNode puede ser utilizada para especificar el índice de posición en los PivotItems bajo el mismo nodo padre.
- El método PivotItem.Move(int count, bool isSameParent) puede ser utilizado para mover el elemento hacia arriba o hacia abajo basándose en el valor del recuento, donde el recuento es el número de posiciones para mover el PivotItem hacia arriba o hacia abajo. Si el valor del recuento es menor que cero, el elemento se moverá hacia arriba, mientras que si el valor del recuento es mayor que cero, el PivotItem se moverá hacia abajo, el parámetro tipo Booleano isSameParent especifica si la operación de movimiento debe realizarse en el mismo nodo padre o no.

{{% alert color="primary" %}} 

Por favor, tenga en cuenta que es necesario llamar a los métodos PivotTable.RefreshData y PivotTable.CalculateData antes de usar las propiedades PivotItem.Position, PivotItem.PositionInSameParentNode y el método PivotItem.Move(int count, bool isSameParent).

{{% /alert %}} 
### **Clase SignatureLine Agregada**
Aspose.Cells for .NET 8.3.2 proporciona soporte para la Línea de Firma para imitar la característica equivalente de MS Excel. Esta versión de Aspose.Cells for .NET ha expuesto la clase SignatureLine y la propiedad Picture.SignatureLine para este propósito.

El siguiente código de ejemplo agrega una Línea de Firma utilizando la propiedad Picture.SignatureLine al libro de trabajo.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.Worksheets[0].Pictures.Add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.Worksheets[0].Pictures[index];

//Create signature line object

SignatureLine s = new SignatureLine();

s.Signer = "John Doe";

s.Title = "Development Lead";

s.Email = "john.doe@aspose.com";

//Assign the signature line object to Picture.SignatureLine property

pic.SignatureLine = s;

{{< /highlight >}}


### **Añadido el Método Chart.HasAxis**
Con el lanzamiento de v8.3.2, la API de Aspose.Cells ha proporcionado el método Chart.HasAxis(AxisType axisType, bool isPrimary) para determinar si el gráfico tiene un eje particular o no.

El siguiente código de muestra demuestra el uso del método Chart.HasAxis para determinar si el gráfico de muestra tiene ejes Primario, Secundario y de Valor.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the chart

Chart chart = worksheet.Charts[0];

//Determine which axis exists in chart

bool ret = chart.HasAxis(AxisType.Category, true);

Console.WriteLine("Has Primary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Category, false);

Console.WriteLine("Has Secondary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, true);

Console.WriteLine("Has Primary Value Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, false);

Console.WriteLine("Has Secondary Value Axis: " + ret);

{{< /highlight >}}


### **Añadido el Método WorkbookSettings.CheckWriteProtectedPassword**
El método WorkbookSettings.CheckWriteProtectedPassword permite a los desarrolladores verificar si una contraseña dada para modificar la hoja de cálculo es correcta o no.

**C#**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.Password = "1234";

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

bool ret = workbook.CheckWriteProtectedPassword("567");

Console.WriteLine("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}


### **Métodos de sobrecarga WorkbookRender.ToPrinter y SheetRender.ToPrinter Añadidos**
Aspose.Cells for .NET 8.3.2 ha proporcionado los métodos WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) y SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) para imprimir el rango de páginas del libro de trabajo y la hoja de cálculo respectivamente.

El siguiente código de muestra ilustra cómo utilizar los métodos mencionados anteriormente para imprimir las páginas 2-5 del libro y hoja de cálculo.

**C#**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.ToPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.ToPrinter(printerName, 1, 4);

{{< /highlight >}}


### **Añadido Método Worksheet.RefreshPivotTables**
El método recién añadido Worksheet.RefreshPivotTables permite actualizar todas las tablas dinámicas en una hoja de cálculo dada en una sola llamada.

**C#**

{{< highlight csharp >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **Añadido Método Workbook.GetNamedStyle**
Aspose.Cells for .NET API ha expuesto el método Workbook.GetNamedStyle que acepta una cadena como parámetro y recupera el objeto de estilo basado en el parámetro pasado.
### **Añadido Método Cells.ImportTwoDimensionArray**
Aspose.Cells for .NET API ha hecho posible importar arreglos bidimensionales a celdas de hojas de cálculo mediante la exposición del método Cells.ImportTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions). El método mencionado importa un arreglo de dos dimensiones de datos en una hoja de cálculo con opciones más flexibles definidas en TxtLoadOptions.
### **Se agregaron las propiedades OnePagePerSheet, PageIndex y PageCount**
Aspose.Cells for .NET 8.3.2 ha expuesto las propiedades OnePagePerSheet, PageIndex y PageCount para la clase XpsSaveOptions. El usuario puede ajustar todo el contenido de una hoja de cálculo en una única página de XPS usando la propiedad OnePagePerSheet y/o recuperar el número de páginas a imprimir usando la propiedad PageCount. La propiedad PageIndex obtiene/establece el índice basado en 0 de la primera página que se guardará.
### **Se agregaron las propiedades NumberDecimalSeparator y NumberGroupSeparator**
Aspose.Cells for .NET 8.3.2 ha introducido las propiedades NumberDecimalSeparator y NumberGroupSeparator que pueden obtener/establecer los separadores personalizados utilizados para formatear y analizar los valores numéricos en hojas de cálculo.

El siguiente código de muestra ilustra cómo especificar los separadores personalizados utilizando la API de Aspose.Cells. El siguiente código especifica los separadores decimales y de grupo personalizados como punto y espacio respectivamente.

**C#**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **Añadida Propiedad PdfSaveOptions.IsFontSubstitutionCharGranularity**
Aspose.Cells for .NET 8.3.2 ha expuesto la propiedad PdfSaveOptions.IsFontSubstitutionCharGranularity para superar el problema donde algunos caracteres Unicode no pueden mostrarse utilizando una familia de fuentes específica. Cuando la propiedad PdfSaveOptions.IsFontSubstitutionCharGranularity se establece en true, solo la fuente de un carácter específico que no se puede mostrar cambiará a una fuente mostrable y el resto de la palabra o frase deberá permanecer en la fuente original.

**C#**

{{< highlight csharp >}}

 //Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **APIs Eliminadas**
### **Métodos obsoletos eliminados**
Los siguientes métodos han sido eliminados de la API pública.

- Métodos Workbook.Open y Workbook.Save.
- Método Workbook.SetOleSize.
- Método Workbook.LoadData.
- Métodos WorkbookDesigner.Open y WorkbookDesigner.Save.
- Método WorksheetCollection.DeleteName.
### **Propiedades obsoletas eliminadas**
Las siguientes propiedades han sido eliminadas de la API pública.

- Propiedad Workbook.IsProtected.
- Propiedad Workbook.Language.
- Propiedad Workbook.Region.
- Propiedad WorkbookSettings.ReCalcOnOpen.
- Propiedad WorkbookSettings.Language.
- Propiedad WorkbookSettings.Encoding.
- Propiedad WorkbookSettings.ConvertNumericData.
- Propiedad WorksheetCollection.HidePivotFieldList.
- Propiedad WorksheetCollection.EnableHTTPCompression.
- Propiedad WorksheetCollection.IsMinimized.
- Propiedad WorksheetCollection.IsHidden.
- Propiedad WorksheetCollection.SheetTabBarWidth.
- Propiedad WorksheetCollection.WindowLeft.
- Propiedad WorksheetCollection.WindowLeftInch.
- Propiedad WorksheetCollection.WindowLeftCM.
- Propiedad WorksheetCollection.WindowTop.
- Propiedad WorksheetCollection.WindowTopInch.
- Propiedad WorksheetCollection.WindowTopCM.
- Propiedad WorksheetCollection.WindowWidth.
- Propiedad WorksheetCollection.WindowWidthInch.
- Propiedad WorksheetCollection.WindowWidthCM.
- Propiedad WorksheetCollection.WindowHeight.
- Propiedad WorksheetCollection.WindowHeightInch.
- Propiedad WorksheetCollection.WindowHeightCM.
- Propiedad Worksheet.HPageBreaks.
- Propiedad Worksheet.VPageBreaks.
- Propiedad HtmlSaveOptions.DisplayHTMLCrossString.
- Propiedad HtmlSaveOptions.ExportChartImageFormat.
- Propiedad SaveOptions.ExpCellNameToXLSX.
- Propiedad SaveOptions.DefaultFont.
- Propiedad SaveOptions.Compliance.
- Propiedad SaveOptions.PdfBookmark.
- Propiedad SaveOptions.PdfImageCompression.
- Propiedad TxtSaveOptions.AlwaysQuoted.
## **APIs obsoletas**
### **Propiedad Obsoleta Workbook.SaveOptions**
Se debe pasar un objeto SaveOptions al método Workbook.Save después de configurar las propiedades adecuadas de SaveOptions.
### **Propiedad y clase StyleCollection obsoletas de Workbook.Styles**
Se aconseja utilizar el método Workbook.CreateStyle para crear y manipular estilos para una instancia de Workbook en lugar de crear un Style con el método StyleCollection.Add. Además, se puede usar el método Workbook.GetNamedStyle(string) para obtener un estilo con nombre en lugar de StyleCollection[string].
### **Método PivotItem.Move(int count) obsoleto**
Con el lanzamiento de Aspose.Cells 8.3.2, la API ha introducido otra sobrecarga del método PivotItem.Move que acepta el parámetro entero para el contador y el parámetro booleano para mover un PivotItem dentro del nodo padre.
