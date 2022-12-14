---
title: Público API Cambios en Aspose.Cells 8.5.2
type: docs
weight: 180
url: /es/net/public-api-changes-in-aspose-cells-8-5-2/
---
{{% alert color="primary" %}} 

 Este documento describe los cambios al Aspose.Cells API de la versión 8.5.1 a la 8.5.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados,[Clases añadidas, etc.](/cells/es/net/public-api-changes-in-aspose-cells-8-5-2/), pero también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Renderizar la hoja de trabajo al contexto gráfico**
 Esta versión de Aspose.Cells for .NET API ha expuesto dos nuevas sobrecargas del método SheetRender.ToImage que ahora permite aceptar una instancia de la clase System.Drawing.Graphics para[renderizar en contexto de gráficos](/cells/es/net/render-worksheet-to-graphic-context/). Las firmas de los métodos recién agregados son las siguientes.

1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)
1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Create empty Bitmap

Bitmap bmp = new Bitmap(800, 800);

//Create Graphics Context

Graphics g = Graphics.FromImage(bmp);

g.Clear(Color.Blue);

//Set one page per sheet to true in image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.OnePagePerSheet = true;

//Render worksheet to graphics context

SheetRender sr = new SheetRender(worksheet, opts);

sr.ToImage(0, g, 0, 0);

//Save the graphics context image in Png format

bmp.Save("test.png", ImageFormat.Png);

{{< /highlight >}}


### **Método PivotTable.GetCellByDisplayName agregado**
 Aspose.Cells for .NET 8.5.2 ha expuesto el método PivotTable.GetCellByDisplayName que se puede usar para[recuperar el objeto Cell por el nombre de PivotField](/cells/es/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Este método podría ser útil en escenarios en los que desea resaltar o formatear el encabezado PivotField.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first pivot table inside the worksheet

PivotTable pivotTable = worksheet.PivotTables[0];

//Access cell by display name of 2nd data field of the pivot table

Cell cell = pivotTable.GetCellByDisplayName(pivotTable.DataFields[1].DisplayName);

//Access cell style and set its fill color and font color

Style style = cell.GetStyle();

style.ForegroundColor = Color.LightBlue;

style.Font.Color = Color.Black;

//Set the style of the cell

pivotTable.Format(cell.Row, cell.Column, style);

//Save workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Propiedades SaveOptions.MergeAreas añadidas**
Aspose.Cells for .NET 8.5.2 ha expuesto la propiedad SaveOptions.MergeAreas que puede aceptar valores de tipo booleano. El valor predeterminado es falso; sin embargo, si se establece en verdadero, Aspose.Cells for .NET API intenta fusionar el CellArea individual antes de guardar el archivo.

{{% alert color="primary" %}} 

Si una hoja de cálculo tiene demasiadas celdas individuales con validación aplicada, existe la posibilidad de que la hoja de cálculo resultante se dañe. Una posible solución es fusionar las celdas con reglas de validación idénticas o ahora puede usar la propiedad SaveOptions.MergeAreas para indicar al API que fusione automáticamente las CellAreas antes de guardar la operación.

{{% /alert %}} 
### **Propiedad Shape.Geometry.ShapeAdjustValues añadido**
 Con el lanzamiento de v8.5.2, Aspose.Cells API ha expuesto la propiedad Shape.Geometry.ShapeAdjustValues que se puede usar para[realizar cambios en los puntos de ajuste de diferentes formas](/cells/es/net/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

En la interfaz de Excel Microsoft, los puntos de ajuste se muestran como nodos de diamantes amarillos.

{{% /alert %}} 

Por ejemplo,

1. Rectángulo redondeado tiene un ajuste para cambiar el arco
1. Triángulo tiene un ajuste para cambiar la ubicación del punto
1. Trapecio tiene un ajuste para cambiar el ancho de la parte superior
1. Las flechas tienen dos ajustes para cambiar la forma de la cabeza y la cola.

Este es el escenario de uso más simple.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first three shapes of the worksheet

Shape shape1 = worksheet.Shapes[0];

Shape shape2 = worksheet.Shapes[1];

Shape shape3 = worksheet.Shapes[2];

//Change the adjustment values of the shapes

shape1.Geometry.ShapeAdjustValues[0].Value = 0.5d;

shape2.Geometry.ShapeAdjustValues[0].Value = 0.8d;

shape3.Geometry.ShapeAdjustValues[0].Value = 0.5d;

//Save the workbook

workbook.Save("output.xls);

{{< /highlight >}}


### **Consolidación de campos de enumeraciónFunction.DistinctCount agregado**
 Aspose.Cells for .NET 8.5.2 ha expuesto el campo ConsolidationFunction.DistinctCount que se puede usar para[aplicar la función de consolidación Distinct Count](/cells/es/net/consolidation-function/) en el campo de datos de una tabla dinámica.

{{% alert color="primary" %}} 

La función de consolidación Distinct Count solo es compatible con Microsoft Excel 2013.

{{% /alert %}} 
### **Mejor manejo de eventos para GridDesktop**
Esta versión de Aspose.Cells.GridDesktop ha expuesto 4 nuevos eventos. 2 de estos eventos se activan en diferentes estados de carga de archivos de hojas de cálculo en GridDesktop, mientras que los otros 2 se activan al calcular fórmulas.

Los eventos se enumeran a continuación.

1. GridDesktop.BeforeLoadFile
1. GridDesktop.FinishLoadFile
1. GridDesktop.BeforeCalculate
1. GridDesktop.FinishCalculate
