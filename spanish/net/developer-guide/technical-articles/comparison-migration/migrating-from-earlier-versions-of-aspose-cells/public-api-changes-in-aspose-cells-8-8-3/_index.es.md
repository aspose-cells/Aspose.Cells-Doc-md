---
title: Cambios en la API pública en Aspose.Cells 8.8.3
type: docs
weight: 290
url: /es/net/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.8.2 a la 8.8.3 que pueden interesar a los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Soporte para controles ActiveX**
Aspose.Cells for .NET 8.8.3 ha expuesto el método AddActiveXControl que permite agregar un control ActiveX a la ShapeCollection. El método mencionado requiere 7 parámetros para especificar el tipo de control, la ubicación para colocar el control y el tamaño del control. El tipo puede especificarse utilizando la enumeración ControlType con los siguientes valores posibles.

1. ControlType.CheckBox
1. ControlType.ComboBox
1. ControlType.CommandButton
1. ControlType.Image
1. ControlType.Label
1. ControlType.ListBox
1. ControlType.RadioButton
1. ControlType.ScrollBar
1. ControlType.SpinButton
1. ControlType.TextBox
1. ControlType.ToggleButton
1. ControlType.Unknown

{{% alert color="primary" %}} 

Para más detalles sobre esta característica, consulte el artículo detallado sobre [Agregar controles ActiveX a la hoja de cálculo](/cells/es/net/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Add Toggle Button ActiveX Control to the ShapeCollection at specified location

var shape = sheet.Shapes.AddActiveXControl(ControlType.ToggleButton, 4, 0, 4, 0, 100, 30);

// Access the ActiveX Control object and set its linked cell property

ActiveXControl control = shape.ActiveXControl;

control.LinkedCell = "A1";

// Save the result on disc

book.Save(dir + "output.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}


### **Agregado el método LoadOptions.SetPaperSize**
Aspose.Cells for .NET 8.8.3 permite establecer el tamaño de papel de impresión predeterminado desde la configuración de la impresora predeterminada al utilizar el método expuesto recientemente LoadOptions.SetPaperSize tal como se muestra a continuación. Por favor, tenga en cuenta que el parámetro de entrada para dicho método es el valor de la enumeración PaperSizeType que contiene los tamaños de papel predefinidos.

{{% alert color="primary" %}} 

Para más detalles sobre esta función, por favor revise el artículo detallado sobre [Cargar Hojas de Cálculo con Tamaño de Papel Especificado](/cells/es/net/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions

var loadOptions = new LoadOptions();

// Set the PaperSize property to appropriate value

loadOptions.SetPaperSize(PaperSizeType.PaperA4);

// Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}


### **Agregado el método Cell.GetCharacters(flag)**
Las APIs de Aspose.Cells permiten obtener los objetos de caracteres en forma de una matriz de FontSetting mediante el uso del método Cell.GetCharacters. Con esta versión, la API Aspose.Cells for .NET ha expuesto una versión sobrecargada de Cell.GetCharacters que puede aceptar un Booleano como parámetro, indicando si el estilo de tabla debe aplicarse en la celda si la celda es parte de un ListObject.

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access cells collection of the first worksheet

var cells = sheet.Cells;

// Access particular cell from a ListObject

// Assuming A1 resides in a ListObject

var cell = cells["A1"];

// Get all Characters objects from the cell

var characters = cell.GetCharacters(true);

{{< /highlight >}}


### **Añadida propiedad OleObject.AutoLoad**
Aspose.Cells for .NET 8.8.3 ha expuesto la propiedad OleObject.AutoLoad que permite refrescar la imagen del OleObject si el contenido/datos del objeto subyacente han cambiado. Cuando la mencionada propiedad se establece en true, obliga a la aplicación de Excel a refrescar la imagen del OleObject cuando se carga la hoja de cálculo resultante.

{{% alert color="primary" %}} 

Para más detalles sobre esta función, por favor revise el artículo detallado sobre [Actualizar Automáticamente los OleObjects](/cells/es/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access OleObjectCollection from first worksheet

var oleObjects = sheet.OleObjects;

// Access a OleObject from the collection

var oleObject = oleObjects[0];

// Set AutoLoad to true

oleObject.AutoLoad = true;

{{< /highlight >}}


### **Añadida propiedad HTMLLoadOptions.SupportDivTag**
Aspose.Cells for .NET 8.8.3 ha expuesto la propiedad HTMLLoadOptions.SupportDivTag que permite analizar las etiquetas DIV incrustadas en las etiquetas TD mientras se cargan archivos/fracciones de HTML en el modelo de objeto Aspose.Cells. La propiedad de tipo Booleano tiene un valor predeterminado de false.

{{% alert color="primary" %}} 

Para más detalles sobre esta función, por favor revise el artículo detallado sobre [Soporte de Etiquetas DIV Internas al Cargar HTML](/cells/es/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 // Store the HTML snippet in a variable

var export_html = @"

<html>

<body>

    <table>

        <tr>

            <td>

                <div>This is some Text.</div>

                <div>

                    <div>

                        <span>This is some more Text</span>

                    </div>

                    <div>

                        <span>abc@abc.com</span>

                    </div>

                    <div>

                        <span>1234567890</span>

                    </div>

                    <div>

                        <span>ABC DEF</span>

                    </div>

                </div>

                <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>

            </td>

            <td>

                <img src='ASpose_logo_100x100.png' />

            </td>

        </tr>

    </table>

</body>

</html>";

// Create an instance of MemoryStream and load the contents of the HTML

using (var stream = new MemoryStream(System.Text.Encoding.UTF8.GetBytes(export_html)))

{

    // Create an instance of HTMLLoadOptions

    var loadOptions = new HTMLLoadOptions(LoadFormat.Html);

    // Set SupportDivTag property to true

    loadOptions.SupportDivTag = true;

    // Create workbook object from the HTML using load options

    var book = new Workbook(stream, loadOptions);

    // Auto fit rows and columns of first worksheet

    var sheet = book.Worksheets[0];

    sheet.AutoFitRows();

    sheet.AutoFitColumns();

    // Save the spreadsheet on disc

    book.Save(dir + "output.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}


### **Agregada la propiedad HtmlSaveOptions.ExportGridLines**
Aspose.Cells for .NET 8.8.3 ha expuesto la propiedad HtmlSaveOptions.ExportGridLines que permite renderizar las líneas de la cuadrícula al exportar la hoja de cálculo en formato HTML. La propiedad de tipo Booleano tiene un valor predeterminado de false, sin embargo, cuando se establece en true, la API renderiza las líneas de la cuadrícula para el rango de datos disponible en formato HTML.

{{% alert color="primary" %}} 

Para más detalles sobre esta función, por favor revise el artículo detallado sobre [Renderizar Líneas de Cuadrícula en HTML](/cells/es/net/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set ExportGridLines to true

options.ExportGridLines = true;

// Save the result in HTML format

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **Agregada la propiedad ListObject.Comment**
Las APIs de Aspose.Cells ahora permiten obtener y establecer los comentarios para una instancia de ListObject. Para proporcionar la característica anteriormente mencionada, las APIs de Aspose.Cells han expuesto la propiedad ListObject.Comment.

{{% alert color="primary" %}} 

Para más detalles sobre esta característica, por favor revise el artículo detallado sobre [Agregar comentarios a ListObjects](/cells/es/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first ListObject from the collection of ListObjects

var listObject = sheet.ListObjects[0];

// Set comments for the ListObject

listObject.Comment = "Comments";

// Save the result on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Añadida la propiedad GridWeb.SessionStorePath**
Aspose.Cells.GridWeb para .NET 8.8.3 ha expuesto la propiedad SessionStorePath que permite obtener o configurar la ruta de almacenamiento de sesión cuando el Modo de Sesión es ViewState. La mencionada propiedad obtiene o establece la ruta relativa al Directorio Base de la aplicación web actual.

{{% alert color="primary" %}} 

Para más detalles sobre esta característica, por favor revise el artículo detallado sobre [Especificar la ruta para los archivos temporales de sesión](/cells/es/net/specify-the-path-where-gridweb-stores-temporary-session-files/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.
## **APIs Eliminadas**
### **Método Workbook.Decrypt Eliminado**
La mencionada propiedad fue marcada como obsoleta hace algún tiempo. Esta versión la ha eliminado por completo de la API pública. Se recomienda establecer la propiedad WorkbookSettings.Password en nulo para lograr el mismo objetivo.
{{< app/cells/assistant language="csharp" >}}
