---
title: Público API Cambios en Aspose.Cells 8.8.1
type: docs
weight: 270
url: /es/net/public-api-changes-in-aspose-cells-8-8-1/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.8.0 a la 8.8.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Filtrar los datos para cargar**
Aspose.Cells for .NET 8.8.1 ha expuesto la enumeración LoadDataFilterOptions junto con la propiedad LoadOptions.LoadDataFilterOptions que se puede usar para especificar el tipo de datos que se debe cargar al crear el libro de trabajo a partir de un archivo de plantilla. Filtrar los datos cargados puede mejorar el rendimiento para propósitos especiales, especialmente cuando se usan las API de LightCells.

La enumeración LoadDataFilterOptions proporciona las siguientes selecciones.

1. Todo para cargar todo desde la hoja de cálculo.
1. Ninguno para cargar nada desde la hoja de cálculo.
1. CellBlank carga las celdas cuyos valores están en blanco.
1. CellBool carga celdas cuyos valores son booleanos.
1. CellData carga datos de celdas, incluidos valores, fórmulas y formato.
1. CellError carga celdas cuyos valores son erróneos.
1. CellNumeric carga celdas cuyos valores son numéricos (incluidas la fecha y la hora).
1. CellString carga celdas cuyos valores son texto/cadena.
1. CellValue carga solo valores de celda (todos los tipos).
1. Gráfico carga solo gráficos.
1. ConditionalFormatting solo carga reglas de formato condicional.
1. DataValidation solo carga reglas de validación de datos.
1. DocumentProperties carga solo las propiedades del documento.
1. Fórmula carga fórmulas que incluyen nombres definidos.
1. MergedArea carga solo celdas combinadas.
1. PivotTable carga tablas dinámicas.
1. La configuración carga solo la configuración del libro y la hoja de trabajo.
1. Shape carga solo formas.
1. El estilo carga el formato de las celdas.
1. Tabla carga tablas de Excel/Lista de objetos.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Filtrar datos para cargar](/cells/es/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

var options = new LoadOptions(LoadFormat.Xlsx);

//Set LoadDataFilterOptions to load only shapes

options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

var book = new Workbook(filePath, options);

{{< /highlight >}}


### **Convertir directamente el gráfico a PDF**
Las API Aspose.Cells ya han brindado la posibilidad de representar gráficos en PDF al usar el método Chart.ToPdf. Con este lanzamiento, el API ha expuesto otra versión sobrecargada de dicho método que podría aceptar una instancia de Stream, lo que permite a los usuarios guardar el gráfico PDF en una instancia de MemoryStream.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

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


### **Se agregó la propiedad WorkbookSettings.PaperSize**
Aspose.Cells for .NET 8.8.1 ha expuesto la propiedad WorkbookSettings.PaperSize para establecer el tamaño de papel de impresión predeterminado para toda la hoja de cálculo. La propiedad WorkbookSettings.PaperSize acepta un valor de la enumeración PaperSizeType que contiene los tamaños predefinidos para los tipos de papel de impresión más utilizados.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access WorkbookSettings from the Workbook

var settings = book.Settings;

//Set the default printing paper size for the Workbook

settings.PaperSize = PaperSizeType.PaperA4;

{{< /highlight >}}


### **Se agregó la propiedad Shape.TextBody**
Esta versión de Aspose.Cells for .NET API ha expuesto Shape.TextBody para manipular los aspectos del texto en formas. El siguiente fragmento usa dicha propiedad para establecer el efecto de sombra del texto en un cuadro de texto.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Configuración del efecto de sombra para el texto](/cells/es/net/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 //Crear una instancia de Workbook

var libro = nuevo libro de trabajo ();

// Acceder a la primera hoja de trabajo del Libro de trabajo

var hoja = libro.Hojas de trabajo[0];

//Añadir un TextBox a la ShapeCollection

var textBox = hoja.Formas.AddTextBox(2, 0, 2, 0, 100, 400);

//Establecer el texto del cuadro de texto

textBox.Text = "Este texto tiene la siguiente configuración.\n\nEfectos de texto > Sombra > Fondo desplazado";

//Establecer efecto de sombra para el texto

 para (int i = 0; i< textBox.TextBody.Count; i++)

{

    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;

}

{{< /highlight >}}


### **Se agregó el método Worksheet.CalculateFormula (fórmula de cadena, Opciones de cálculo)**
Aspose.Cells for .NET 8.8.1 ha expuesto otra sobrecarga para el método CalculateFormula que brinda la capacidad de calcular una fórmula determinada directamente con opciones personalizadas.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Cálculo directo de la función personalizada](/cells/es/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **Se agregó el método GridCell.CreateValidation**
Aspose.Cells.GridWeb ha brindado la capacidad de agregar directamente la regla de validación a una sola celda mientras se usa el método GridCell.CreateValidation. Dicho método requiere 2 parámetros. El primero es de tipo GridValidationType que determina el tipo de validación, mientras que el segundo parámetro (isRequied) es de tipo booleano.



**C#**

{{< highlight "csharp" >}}

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


### **Se agregó el método GridCell.RemoveValidation**
Aspose.Cells.GridWeb también ha brindado la capacidad de eliminar la regla de validación de datos de GridCell mientras se usa el método GridCell.RemoveValidation.
## **API obsoletas**
### **Propiedad Shape.TextFrame obsoleta**
Se recomienda utilizar la propiedad Shape.TextBody.TextAlignment en su lugar.
