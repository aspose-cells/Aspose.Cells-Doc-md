---
title: Cambios en la API pública en Aspose.Cells 9.0.0
type: docs
weight: 330
url: /es/net/public-api-changes-in-aspose-cells-9-0-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.9.2 hasta la 9.0.0 que pueden interesar a los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases añadidas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento interno de Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Propiedad Shape.TextOptions agregada**
Aspose.Cells for .NET ha expuesto la propiedad TextOptions para la clase Shape con el fin de controlar la apariencia de las partes textuales de una forma.

Aquí hay un escenario de uso simple de la propiedad Shape.TextOptions.

**C#**

{{< highlight csharp >}}

 // Initialize an instance of Workbook

var book = new Workbook();

// Get the default Worksheet from the Workbook

var sheet = book.Worksheets[0];

// Add a TextBox to the collection

var textboxIndex = sheet.TextBoxes.Add(2, 1, 160, 200);

// Get the TextBox object

var textbox = sheet.TextBoxes[textboxIndex];

// Add text to the TextBox

textbox.Text = "Hello Aspose!";

// Format the textual contents

textbox.TextOptions.Color = System.Drawing.Color.Red;

textbox.TextOptions.IsItalic = true;

{{< /highlight >}}


### **Agregada la propiedad LoadOptions.CultureInfo**
Aspose.Cells for .NET 9.0.0 ha expuesto la propiedad LoadOptions.CultureInfo que permite inyectar una instancia de CultureInfo al cargar un documento en una instancia de Workbook.

Aquí hay un escenario de uso simple de las propiedades mencionadas.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Cargar la hoja de cálculo con información específica de la cultura](/cells/es/net/load-the-workbook-with-specific-system-culture-info/).

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of CultureInfo and populate its properties

var culture = new CultureInfo("en-GB");

culture.NumberFormat.NumberDecimalSeparator = ",";

culture.DateTimeFormat.DateSeparator = "-";

culture.DateTimeFormat.ShortDatePattern = "dd-MM-yyyy";

// Create an instance of LoadOptions and set the CultureInfo property

var options = new LoadOptions(LoadFormat.Html);

options.CultureInfo = culture;

// Load a HTML or TXT file in an instance of Workbook with instance of  LoadOptions

var book = new Workbook(dir + "input.html", options);

{{< /highlight >}}


### **Agregada la propiedad ChartPoint.IsInSecondaryPlot.**
Aspose.Cells for .NET ha expuesto la propiedad ChartPoint.IsInSecondaryPlot que se puede usar para detectar si un ChartPoint reside en un segundo trazado de un gráfico de sectores o de barras.

Aquí hay un escenario de uso simple de la propiedad Shape.Line.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Encontrar si un punto de datos reside en el segundo trazado](/cells/es/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/).

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load an existing spreadsheet containing a Pie chart

var book = new Workbook(dir + "PieBar.xlsx");

// Load the Worksheet at 0 index

var sheet = book.Worksheets[0];

// Load the first chart from the collection

var chart = sheet.Charts[0];

// Calculate the chart before accessing its properties

chart.Calculate();

// Accessing chart's first series

var series = chart.NSeries[0];

// Loop over the ChartPoint collection

foreach (ChartPoint point in series.Points)

{

    // Detect if ChartPoint resides on secondary plot

    Console.WriteLine(point.IsInSecondaryPlot);

}

{{< /highlight >}}


### **Agregada la propiedad OleObject.ClassIdentifier.**
Aspose.Cells for .NET 9.0.0 ha expuesto la propiedad OleObject.ClassIdentifier que se puede utilizar para especificar el comportamiento de la aplicación para cargar un OleObject. Por ejemplo, un archivo PPT puede ser incrustado en una hoja de cálculo con 2 vistas diferentes, es decir, vista de presentación o vista de diapositiva, mientras que ambas vistas tienen valores de identificador de clase diferentes.

A continuación se muestra el escenario de uso simple de la propiedad OleObject.ClassIdentifier.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Usar OleObject.ClassIdentifier](/cells/es/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/).

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load a spreadsheet containing a presentation as OleObject

var book = new Workbook(dir + "embeddedPresentation.xls");

// Initialize variables to store properties of OleObject

int upperLeftRow = 0;

int upperLeftColumn = 0;

int height = 0;

int width = 0;

byte[] imageData = null;

int x = 0;

int y = 0;

byte[] objData = null;

string progID = "";

FileFormatType fileFormatType = FileFormatType.Unknown;

string sourceFullName = "";

bool isDisplayAsIcon = false;

byte[] classId = null;

// Get the first worksheet from the collection

var sheet = book.Worksheets[0];

// Get the first OleObject from the collection

var frame = sheet.OleObjects[0];

// Store the properties in variables

upperLeftRow = frame.UpperLeftRow;

upperLeftColumn = frame.UpperLeftColumn;

height = frame.Height;

width = frame.Width;

imageData = frame.ImageData;

x = frame.X;

y = frame.Y;

objData = frame.ObjectData;

progID = frame.ProgID;

fileFormatType = frame.FileFormatType;

sourceFullName = frame.ObjectSourceFullName;

isDisplayAsIcon = frame.DisplayAsIcon;

classId = frame.ClassIdentifier;

// Initialize a new Workbook instance

book = new Workbook();

// Access first worksheet from the collection

sheet = book.Worksheets[0];

// Insert the OleObject to the worksheet

int oleNumber = sheet.OleObjects.Add(upperLeftRow, upperLeftColumn, height, width, imageData);

// Access newly inserted OleObject

var embeddedObject = sheet.OleObjects[oleNumber];

// Assign previously stored properties to new OleObject

embeddedObject.X = x;

embeddedObject.Y = y;

embeddedObject.ObjectData = objData;

embeddedObject.ProgID = progID;

embeddedObject.FileFormatType = fileFormatType;

embeddedObject.DisplayAsIcon = isDisplayAsIcon;

embeddedObject.ObjectSourceFullName = sourceFullName;

embeddedObject.IsAutoSize = false;

if (classId != null)

{

    embeddedObject.ClassIdentifier = classId;

}

// Save the resultant spreadsheet

book.Save(dir  + "output.xls");

{{< /highlight >}}
## **APIs obsoletas**
### **Método Obsoleto Worksheet.SetBackground**
Por favor, utiliza en su lugar la propiedad Worksheet.BackgroundImage.
### **Propiedades Obsoletas LineShape.BeginArrowheadStyle & ArcShape.BeginArrowheadStyle**
Por favor, utiliza la propiedad Shape.Line.BeginArrowheadStyle como alternativa.
### **Propiedades Obsoletas LineShape.EndArrowheadStyle & ArcShape.EndArrowheadStyle**
Por favor, utiliza la propiedad Shape.Line.EndArrowheadStyle como alternativa.
### **Propiedades LineShape.BeginArrowheadWidth y ArcShape.BeginArrowheadWidth obsoletas**
Por favor, utilice la propiedad Shape.Line.BeginArrowheadWidth como alternativa.
### **Propiedades LineShape.BeginArrowheadLength y ArcShape.BeginArrowheadLength obsoletas**
Por favor, utilice la propiedad Shape.Line.BeginArrowheadLength en su lugar.
### **Propiedades LineShape.EndArrowheadWidth y ArcShape.EndArrowheadWidth obsoletas**
Por favor, utilice la propiedad Shape.Line.EndArrowheadWidth en su lugar.
### **Propiedades LineShape.EndArrowheadLength y ArcShape.EndArrowheadLength obsoletas**
Por favor, utilice la propiedad Shape.Line.EndArrowheadLength en su lugar.
## **APIs eliminadas**
### **Método Eliminado Worksheet.CopyConditionalFormatting**
### **Método Eliminado Workbook.CheckWriteProtectedPassword**
## **APIs renombradas**
### **Método Renombrado Workbook.RemoveDigitallySign**
El método Workbook.RemoveDigitallySign ha sido renombrado a Workbook.RemoveDigitalSignature.
{{< app/cells/assistant language="csharp" >}}
