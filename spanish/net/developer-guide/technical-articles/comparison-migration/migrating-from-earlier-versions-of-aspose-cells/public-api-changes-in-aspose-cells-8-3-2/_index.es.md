---
title: Público API Cambios en Aspose.Cells 8.3.2
type: docs
weight: 120
url: /es/net/public-api-changes-in-aspose-cells-8-3-2/
---
{{% alert color="primary" %}} 

 Este documento describe los cambios al Aspose.Cells API de la versión 8.3.1 a la 8.3.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados,[Clases añadidas, etc.](/cells/es/net/public-api-changes-in-aspose-cells-8-3-2/) y[clases eliminadas, etc.](/cells/es/net/public-api-changes-in-aspose-cells-8-3-2/), pero también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Mecanismo para establecer la posición absoluta de PivotItem**
 Para proporcionar la función[Posicionamiento absoluto de PivotItem](/cells/es/net/specifying-the-absolute-position-of-the-pivot-item/)el Aspose.Cells for .NET 8.3.2 ha expuesto una serie de propiedades y métodos de ayuda que se enumeran a continuación.

- La propiedad PivotItem.Position se puede usar para especificar el índice de posición en todos los PivotItems, independientemente del nodo principal.
- La propiedad PivotItem.PositionInSameParentNode se puede usar para especificar el índice de posición en PivotItems en el mismo nodo principal.
- El método PivotItem.Move(int count, bool isSameParent) se puede usar para mover el elemento hacia arriba o hacia abajo en función del valor de conteo, donde count es el número de posición para mover el PivotItem hacia arriba o hacia abajo. Si el valor de conteo es menor que cero, el elemento se moverá hacia arriba donde, como si el valor de conteo fuera mayor que cero, PivotItem se moverá hacia abajo, el parámetro de tipo booleano isSameParent especifica si la operación de movimiento debe realizarse en el mismo nodo principal O no.

{{% alert color="primary" %}} 

Tenga en cuenta que es necesario llamar a los métodos PivotTable.RefreshData y PivotTable.CalculateData antes de usar las propiedades PivotItem.Position, PivotItem.PositionInSameParentNode y el método PivotItem.Move(int count, bool isSameParent).

{{% /alert %}} 
### **Línea de firma de clase agregada**
Aspose.Cells for .NET 8.3.2 proporciona soporte para Signature Line para imitar la función equivalente de MS Excel. Esta versión de Aspose.Cells for .NET ha expuesto la clase SignatureLine y la propiedad Picture.SignatureLine para este fin.

El siguiente código de ejemplo agrega una línea de firma mediante la propiedad Picture.SignatureLine al libro de trabajo.

**C#**

{{< highlight "csharp" >}}

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


### **Método Chart.HasAxis agregado**
Con el lanzamiento de v8.3.2, Aspose.Cells API proporcionó el método Chart.HasAxis(AxisType axisType, bool isPrimary) para determinar si el gráfico tiene un eje en particular o no.

El siguiente código de ejemplo demuestra el uso del método Chart.HasAxis para determinar si el gráfico de ejemplo tiene eje principal, secundario y de valor.

**C#**

{{< highlight "csharp" >}}

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


### **Método WorkbookSettings.CheckWriteProtectedPassword agregado**
El método WorkbookSettings.CheckWriteProtectedPassword permite a los desarrolladores verificar si una contraseña dada para modificar la hoja de cálculo es correcta o no.

**C#**

{{< highlight "csharp" >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.Password = "1234";

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

bool ret = workbook.CheckWriteProtectedPassword("567");

Console.WriteLine("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}


### **Métodos de sobrecarga WorkbookRender.ToPrinter y SheetRender.ToPrinter agregados**
Aspose.Cells for .NET 8.3.2 ha proporcionado los métodos WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) y SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) para imprimir el rango de páginas del libro y la hoja de trabajo respectivamente.

El siguiente código de ejemplo ilustra el uso de los métodos mencionados anteriormente para imprimir las páginas 2 a 5 del libro de trabajo y la hoja de trabajo.

**C#**

{{< highlight "csharp" >}}

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


### **Método Worksheet.RefreshPivotTables añadido**
El método recién agregado Worksheet.RefreshPivotTables permite actualizar todas las tablas dinámicas en una hoja de cálculo determinada en una sola llamada.

**C#**

{{< highlight "csharp" >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **Método Workbook.GetNamedStyle agregado**
Aspose.Cells for .NET API ha expuesto el método Workbook.GetNamedStyle que acepta la cadena como parámetro y recupera el objeto Style según el parámetro pasado.
### **Método Cells. Importar matriz de dos dimensiones agregada**
Aspose.Cells for .NET API ha hecho posible importar matrices bidimensionales a celdas de hojas de cálculo al exponer el método Cells.ImportTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions). Dicho método importa una matriz de datos de dos dimensiones en una hoja de trabajo con opciones más flexibles definidas en TxtLoadOptions.
### **Propiedades OnePagePerSheet, PageIndex y PageCount añadidas**
Aspose.Cells for .NET 8.3.2 ha expuesto las propiedades OnePagePerSheet, PageIndex y PageCount para la clase XpsSaveOptions. El usuario puede ajustar todo el contenido de una hoja de cálculo en una sola página de XPS usando la propiedad OnePagePerSheet y/o recuperar el número de páginas que se imprimirán usando la propiedad PageCount. La propiedad PageIndex obtiene/establece el índice basado en 0 de la primera página que se guardará.
### **Propiedades NumberDecimalSeparator & NumberGroupSeparator añadido**
Aspose.Cells for .NET 8.3.2 ha introducido las propiedades NumberDecimalSeparator y NumberGroupSeparator que pueden obtener/establecer los separadores personalizados utilizados para formatear y analizar los valores numéricos en las hojas de cálculo.

El siguiente código de ejemplo ilustra cómo especificar los separadores personalizados usando Aspose.Cells API. El siguiente código especifica los separadores decimales y de grupo personalizados como punto y espacio respectivamente.

**C#**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **Propiedad PdfSaveOptions.IsFontSubstitutionCharGranularity agregada**
Aspose.Cells for .NET 8.3.2 ha expuesto la propiedad PdfSaveOptions.IsFontSubstitutionCharGranularity para superar el problema en el que algunos caracteres Unicode no se pueden mostrar con una familia de fuentes específica. Cuando la propiedad PdfSaveOptions.IsFontSubstitutionCharGranularity se establece en verdadero, solo la fuente del carácter específico que no se puede mostrar se cambiará a la fuente que se puede mostrar y el resto de la palabra u oración debe permanecer en la fuente original.

**C#**

{{< highlight "csharp" >}}

 //Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **API eliminadas**
### **Métodos obsoletos eliminados**
Los siguientes métodos se han eliminado del Público API.

- Métodos Workbook.Open y Workbook.Save.
- Método Workbook.SetOleSize.
- Método Workbook.LoadData.
- Métodos WorkbookDesigner.Open y WorkbookDesigner.Save.
- Método WorksheetCollection.DeleteName.
### **Propiedades obsoletas eliminadas**
Las siguientes propiedades han sido eliminadas del Público API.

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
## **API obsoletas**
### **Property Workbook.SaveOptions Obsoleto**
Se debe pasar un objeto de SaveOptions al método Workbook.Save después de establecer las propiedades adecuadas de SaveOptions.
### **Property Workbook.Styles & Class StyleCollection Obsoleto**
Se recomienda usar el método Workbook.CreateStyle para crear y manipular el estilo para la instancia de Workbook en lugar de crear un estilo con el método StyleCollection.Add. Además, el método Workbook.GetNamedStyle(string) se puede usar para obtener un estilo con nombre en lugar de StyleCollection[string].
### **Método PivotItem.Move(int count) Obsoleto**
Con el lanzamiento de Aspose.Cells 8.3.2, API introdujo otra sobrecarga del método PivotItem.Move que acepta el parámetro entero para el parámetro de conteo y booleano para mover un PivotItem dentro del nodo principal.
