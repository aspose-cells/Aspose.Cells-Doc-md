---
title: Público API Cambios en Aspose.Cells 8.3.2
type: docs
weight: 130
url: /es/java/public-api-changes-in-aspose-cells-8-3-2/
---
{{% alert color="primary" %}} 

 Este documento describe los cambios al Aspose.Cells API de la versión 8.3.1 a la 8.3.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados,[Clases añadidas, etc.](/cells/es/java/public-api-changes-in-aspose-cells-8-3-2/) y[clases eliminadas, etc.](/cells/es/java/public-api-changes-in-aspose-cells-8-3-2/), pero también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Mecanismo para establecer la posición absoluta de PivotItem**
 Para proporcionar la característica[Posicionamiento absoluto de PivotItem](/cells/es/java/specifying-the-absolute-position-of-the-pivot-item/), el Aspose.Cells for Java 8.3.2 ha expuesto una serie de propiedades y un método como se indica a continuación.

- PivotItem.setPosition se puede usar para establecer el índice de posición en todos los PivotItems independientemente del nodo principal.
- PivotItem.setPositionInSameParentNode se puede usar para establecer el índice de posición en PivotItems en el mismo nodo principal.
- El método PivotItem.move(int count, bool isSameParent) se puede usar para mover el elemento hacia arriba o hacia abajo en función del valor de conteo, donde count es el número de posición para mover el PivotItem hacia arriba o hacia abajo. Si el valor de conteo es menor que cero, el elemento se moverá hacia arriba donde, como si el valor de conteo fuera mayor que cero, PivotItem se moverá hacia abajo, el parámetro de tipo booleano isSameParent especifica si la operación de movimiento debe realizarse en el mismo nodo principal O no.

{{% alert color="primary" %}} 

Tenga en cuenta que es necesario llamar a los métodos PivotTable.refreshData y PivotTable.calculateData antes de usar las propiedades PivotItem.setPosition, PivotItem.setPositionInSameParentNode y el método PivotItem.move(int count, bool isSameParent).

{{% /alert %}} 
### **Línea de firma de clase agregada**
Aspose.Cells 8.3.2 proporciona soporte para Signature Line para imitar la función equivalente de MS Excel. Esta versión ha expuesto la clase SignatureLine y la propiedad Picture.SignatureLine para este propósito.

El siguiente código de ejemplo agrega una línea de firma mediante la propiedad Picture.SignatureLine al libro de trabajo.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.getWorksheets().get(0).getPictures().add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.getWorksheets().get(0).getPictures().get(index);

//Create signature line object

SignatureLine s = new SignatureLine();

s.setSigner("John Doe");

s.setTitle("Development Lead");

s.setEmail("john.doe@aspose.com");

//Assign the signature line object to Picture.SignatureLine property

pic.setSignatureLine(s);

{{< /highlight >}}
### **Método Chart.hasAxis agregado**
Con el lanzamiento de v8.3.2, Aspose.Cells API ha proporcionado el método Chart.hasAxis(AxisType axisType, bool isPrimary) para determinar si el gráfico tiene un eje en particular o no.

El siguiente código de ejemplo demuestra el uso del método Chart.hasAxis para determinar si el gráfico de ejemplo tiene eje primario, secundario y de valor.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart

Chart chart = worksheet.getCharts().get(0);

//Determine which axis exists in chart

boolean ret = chart.hasAxis(AxisType.CATEGORY, true);

System.out.println("Has Primary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.CATEGORY, false);

System.out.println("Has Secondary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, true);

System.out.println("Has Primary Value Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, false);

System.out.println("Has Seconary Value Axis: " + ret);

{{< /highlight >}}
### **Método WorkbookSettings.checkWriteProtectedPassword agregado**
El método WorkbookSettings.checkWriteProtectedPassword permite a los desarrolladores verificar si una contraseña dada para modificar la hoja de cálculo es correcta o no.

**Java**

{{< highlight "csharp" >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.setPassword("1234");

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

boolean ret = workbook.checkWriteProtectedPassword("567");

System.out.println("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}
### **Métodos de sobrecarga WorkbookRender.toPrinter y SheetRender.toPrinter agregados**
Aspose.Cells 8.3.2 ha proporcionado los métodos WorkbookRender.toPrinter(string printerName, int printPageIndex, int printPageCount) y SheetRender.toPrinter(string printerName, int printPageIndex, int printPageCount) para imprimir el rango de páginas del libro y la hoja de trabajo respectivamente.

El siguiente código de ejemplo ilustra el uso de los métodos mencionados anteriormente para imprimir las páginas 2 a 5 del libro de trabajo y la hoja de trabajo.

**Java**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.toPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.toPrinter(printerName, 1, 4);

{{< /highlight >}}
### **Método Worksheet.refreshPivotTables añadido**
El método recién agregado Worksheet.refreshPivotTables permite actualizar todas las tablas dinámicas en una hoja de cálculo determinada en una sola llamada.

**Java**

{{< highlight "csharp" >}}

 worksheet.refreshPivotTables();

{{< /highlight >}}
### **Método Workbook.getNamedStyle agregado**
Aspose.Cells 8.3.2 ha expuesto el método Workbook.getNamedStyle que acepta la cadena como parámetro y recupera el objeto Style en función del parámetro pasado.
### **Método Cells.importTwoDimensionArray agregado**
Aspose.Cells API ha hecho posible importar matrices bidimensionales a celdas de hojas de cálculo al exponer el método Cells.importTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions). Dicho método importa una matriz de datos de dos dimensiones en una hoja de trabajo con opciones más flexibles definidas en TxtLoadOptions.
### **Propiedades OnePagePerSheet, PageIndex y PageCount añadidas**
Aspose.Cells for Java 8.3.2 ha expuesto las propiedades OnePagePerSheet, PageIndex y PageCount para la clase XpsSaveOptions. El usuario puede ajustar todo el contenido de una hoja de cálculo en una sola página de XPS usando la propiedad OnePagePerSheet y/o recuperar el número de páginas que se imprimirán usando la propiedad PageCount. La propiedad PageIndex obtiene/establece el índice basado en 0 de la primera página que se guardará.
### **Propiedades NumberDecimalSeparator & NumberGroupSeparator añadido**
Aspose.Cells for Java 8.3.2 ha introducido las propiedades NumberDecimalSeparator y NumberGroupSeparator que pueden obtener/establecer los separadores personalizados utilizados para formatear y analizar los valores numéricos en las hojas de cálculo.

El siguiente código de ejemplo ilustra cómo especificar los separadores personalizados usando Aspose.Cells API. El siguiente código especifica los separadores Decimal y de Grupo personalizados como punto y espacio respectivamente.

**Java**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.getSettings().setNumberDecimalSeparator('.');

workbook.getSettings().setNumberGroupSeparator(' ');

{{< /highlight >}}
### **Propiedad PdfSaveOptions.setFontSubstitutionCharGranularity agregada**
Aspose.Cells for Java 8.3.2 ha expuesto la propiedad PdfSaveOptions.setFontSubstitutionCharGranularity para superar el problema en el que algunos caracteres Unicode no se pueden mostrar con una familia de fuentes específica. Cuando la propiedad PdfSaveOptions.setFontSubstitutionCharGranularity se establece en verdadero, solo la fuente del carácter específico que no se puede mostrar se cambiará a la fuente que se puede mostrar y el resto de la palabra u oración debe permanecer en la fuente original.

**Java**

{{< highlight "csharp" >}}

 //Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity

PdfSaveOptions opts = new PdfSaveOptions();

opts.setFontSubstitutionCharGranularity(true);

{{< /highlight >}}
## **API eliminadas**
### **Métodos obsoletos eliminados**
Los siguientes métodos se han eliminado del Público API.

- Métodos Workbook.open y Workbook.save.
- Método Workbook.setOleSize.
- Método Workbook.loadData.
- Métodos WorkbookDesigner.open y WorkbookDesigner.save.
- Método WorksheetCollection.deleteName.
### **Propiedades obsoletas eliminadas**
Las siguientes propiedades han sido eliminadas del Público API.

- Propiedad Workbook.isProtected.
- Propiedad Workbook.Language.
- Propiedad Workbook.Region.
- Propiedad WorkbookSettings.ReCalcOnOpen.
- Propiedad WorkbookSettings.Language.
- Propiedad WorkbookSettings.Encoding.
- Propiedad WorkbookSettings.ConvertNumericData.
- Propiedad WorksheetCollection.HidePivotFieldList.
- Propiedad WorksheetCollection.EnableHTTPCompression.
- WorksheetCollection.isPropiedad minimizada.
- Propiedad WorksheetCollection.isHidden.
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
### **Propiedad Workbook.saveOptions Obsoleto**
 Se debe pasar un objeto de SaveOptions al método Workbook.Save después de establecer las propiedades adecuadas de SaveOptions.
### **Property Workbook.Styles & Class StyleCollection Obsoleto**
Se recomienda usar el método Workbook.createStyle para crear y manipular el estilo para la instancia de Workbook en lugar de crear un estilo con el método StyleCollection.add. Además, el método Workbook.getNamedStyle(string) se puede usar para obtener un estilo con nombre en lugar de StyleCollection.get(string).
### **Método PivotItem.move(int count) Obsoleto**
 Con el lanzamiento de Aspose.Cells 8.3.2, API introdujo otra sobrecarga del método PivotItem.move que acepta el parámetro entero para el parámetro de conteo y booleano para mover un PivotItem dentro del nodo principal.
