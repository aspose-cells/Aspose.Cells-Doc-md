---
title: Cambios en la API Pública en Aspose.Cells 8.8.1
type: docs
weight: 270
url: /es/net/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.8.0 hasta la 8.8.1 que pueden interesar a los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, clases añadidas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escenas en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Filtrar los Datos para Cargar**
Aspose.Cells for .NET 8.8.1 ha expuesto la enumeración LoadDataFilterOptions junto con la propiedad LoadOptions.LoadDataFilterOptions que se puede usar para especificar el tipo de dato que se debe cargar al construir el libro de trabajo a partir de un archivo de plantilla. Filtrar los datos cargados puede mejorar el rendimiento para fines especiales, especialmente al utilizar las APIs de LightCells.

La enumeración LoadDataFilterOptions proporciona las siguientes selecciones.

1. Todo para cargar todo desde la hoja de cálculo.
1. Nada para no cargar nada desde la hoja de cálculo.
1. CellBlank carga las celdas cuyos valores están en blanco.
1. CellBool carga celdas cuyos valores son booleanos.
1. CellData carga datos de las celdas incluyendo valores, fórmulas y formato.
1. CellError carga celdas cuyos valores son errores.
1. CellNumeric carga celdas cuyos valores son numéricos (incluyendo Fecha y Hora).
1. CellString carga celdas cuyos valores son texto/cadena.
1. CellValue carga solo valores de celda (todos los tipos).
1. Chart carga solo gráficos.
1. ConditionalFormatting carga solo reglas de formato condicional.
1. DataValidation carga solo reglas de validación de datos.
1. DocumentProperties carga solo propiedades de documento.
1. Formula carga fórmulas incluyendo nombres definidos.
1. MergedArea carga solo celdas combinadas.
1. PivotTable carga Tablas Dinámicas.
1. Settings carga solo configuraciones de libro y hoja de cálculo.
1. Shape carga solo formas.
1. Style carga formato de celdas.
1. Table carga tablas de Excel/Objetos de Lista.

{{% alert color="primary" %}} 

Para obtener más detalles sobre esta característica, por favor revise el artículo detallado sobre [Filtrar Datos para Cargar](/cells/es/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

var options = new LoadOptions(LoadFormat.Xlsx);

//Set LoadDataFilterOptions to load only shapes

options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

var book = new Workbook(filePath, options);

{{< /highlight >}}


### **Convertir directamente el gráfico a PDF**
Las APIs de Aspose.Cells ya han proporcionado la facilidad de renderizar gráficos a PDF utilizando el método Chart.ToPdf. Con esta versión, la API ha expuesto otra versión sobrecargada de dicho método que puede aceptar una instancia de Stream, permitiendo a los usuarios guardar el PDF del gráfico en una instancia de MemoryStream.

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

var workbook = new Workbook(filePath);

//Access first worksheet containing a chart

var worksheet = workbook.Worksheets[0];

//Access first chart from the worksheet

var chart = worksheet.Charts[0];

//Save the chart to PDF as Stream

using (MemoryStream stream = new MemoryStream())

{

    chart.ToPdf(stream);

}

{{< /highlight >}}


### **Añadida la propiedad WorkbookSettings.PaperSize**
Aspose.Cells for .NET 8.8.1 ha expuesto la propiedad WorkbookSettings.PaperSize para establecer el tamaño de papel de impresión predeterminado para toda la hoja de cálculo. La propiedad WorkbookSettings.PaperSize acepta un valor de la enumeración PaperSizeType que contiene los tamaños predefinidos para los tipos de papel de impresión más utilizados.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access WorkbookSettings from the Workbook

var settings = book.Settings;

//Set the default printing paper size for the Workbook

settings.PaperSize = PaperSizeType.PaperA4;

{{< /highlight >}}


### **Añadida la propiedad Shape.TextBody**
Esta versión de la API Aspose.Cells for .NET ha expuesto la propiedad Shape.TextBody para manipular los aspectos del texto en formas. El siguiente fragmento de código utiliza dicha propiedad para establecer el efecto de sombra en el texto en un cuadro de texto.

{{% alert color="primary" %}} 

Para más detalles sobre esta funcionalidad, por favor revise el artículo detallado sobre [Configuración del efecto de sombra para texto](/cells/es/net/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

var book = new Workbook();

//Access first worksheet of the Workbook

var sheet = book.Worksheets[0];

//Add a TextBox to the ShapeCollection

var textBox = sheet.Shapes.AddTextBox(2, 0, 2, 0, 100, 400);

//Set the text of the TextBox

textBox.Text = "This text has the following settings.\n\nText Effects > Shadow > Offset Bottom";

//Set shadow effect for text

for (int i = 0; i < textBox.TextBody.Count; i++)

{

    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;

}

{{< /highlight >}}


### **Agregado el método Worksheet.CalculateFormula(string formula, CalculationOptions opts)**
Aspose.Cells for .NET 8.8.1 ha expuesto otra sobrecarga para el método CalculateFormula que proporciona la capacidad de calcular una fórmula dada directamente con opciones personalizadas.

{{% alert color="primary" %}} 

Para más detalles sobre esta funcionalidad, por favor revise el artículo detallado sobre [Cálculo directo de función personalizada](/cells/es/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **Agregado el método GridCell.CreateValidation**
Aspose.Cells.GridWeb ha proporcionado la capacidad de agregar directamente la regla de validación a una celda individual mediante el método GridCell.CreateValidation. Dicho método requiere 2 parámetros. El primero es de tipo GridValidationType que determina el tipo de validación, mientras que el segundo parámetro (isRequired) es de tipo Booleano.



**C#**

{{< highlight csharp >}}

 //Access first worksheet

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B3

GridCell cell = sheet.Cells["B3"];

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.CreateValidation(GridValidationType.WholeNumber, true);

val.Formula1 = "=20";

val.Formula2 = "=40";

val.Operator = GridOperatorType.Between;

val.ShowError = true;

val.ShowInput = true;

{{< /highlight >}}


### **Agregado el método GridCell.RemoveValidation**
Aspose.Cells.GridWeb también ha proporcionado la capacidad de eliminar la regla de validación de datos de una GridCell mediante el método GridCell.RemoveValidation.
## **APIs obsoletas**
### **Propiedad Shape.TextFrame obsoleta**
Se recomienda utilizar la propiedad Shape.TextBody.TextAlignment en su lugar.
{{< app/cells/assistant language="csharp" >}}
