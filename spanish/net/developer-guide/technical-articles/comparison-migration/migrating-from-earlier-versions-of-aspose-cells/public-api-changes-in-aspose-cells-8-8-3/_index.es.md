---
title: Público API Cambios en Aspose.Cells 8.8.3
type: docs
weight: 290
url: /es/net/public-api-changes-in-aspose-cells-8-8-3/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.8.2 a la 8.8.3 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Compatibilidad con controles ActiveX**
Aspose.Cells for .NET 8.8.3 ha expuesto el método AddActiveXControl que permite agregar un control ActiveX a ShapeCollection. El método mencionado requiere 7 parámetros para especificar el tipo de control, la ubicación para colocar el control y el tamaño del control. El tipo se puede especificar mediante la enumeración ControlType con los siguientes valores posibles.

1. ControlType.CheckBox
1. ControlType.ComboBox
1. ControlType.CommandButton
1. ControlType.Imagen
1. ControlType.Label
1. ControlType.ListBox
1. ControlType.RadioButton
1. ControlType.ScrollBar
1. ControlType.SpinButton
1. ControlType.TextBox
1. ControlType.ToggleButton
1. ControlType.Desconocido

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Adición de controles ActiveX a la hoja de trabajo](/cells/es/net/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

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


### **Se agregó el método LoadOptions.SetPaperSize**
Aspose.Cells for .NET 8.8.3 permite configurar el tamaño de papel de impresión predeterminado a partir de la configuración predeterminada de la impresora mientras se usa el método LoadOptions.SetPaperSize recientemente expuesto, como se muestra a continuación. Tenga en cuenta que el parámetro de entrada del método mencionado anteriormente es el valor de la enumeración PaperSizeType que contiene los tamaños de papel predefinidos.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Cargar hojas de cálculo con el tamaño de papel especificado](/cells/es/net/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions

var loadOptions = new LoadOptions();

// Set the PaperSize property to appropriate value

loadOptions.SetPaperSize(PaperSizeType.PaperA4);

// Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}


### **Se agregó el método Cell.GetCharacters(flag)**
Las API Aspose.Cells permiten obtener los objetos de caracteres en forma de matriz FontSetting utilizando el método Cell.GetCharacters. Con esta versión, Aspose.Cells for .NET API ha expuesto una versión sobrecargada de Cell.GetCharacters que podría aceptar Boolean como parámetro, indicando si el estilo de tabla debe aplicarse en la celda si la celda es parte de ListObject.

**C#**

{{< highlight "csharp" >}}

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


### **Se agregó la propiedad OleObject.AutoLoad**
Aspose.Cells for .NET 8.8.3 ha expuesto la propiedad OleObject.AutoLoad que permite actualizar la imagen de OleObject si se han cambiado los contenidos/datos del objeto subyacente. La propiedad mencionada anteriormente, cuando se establece en verdadero, obliga a la aplicación de Excel a actualizar la imagen de OleObject cuando se carga la hoja de cálculo resultante.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Actualizar automáticamente OleObjects](/cells/es/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

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


### **Se agregó la propiedad HTMLLoadOptions.SupportDivTag**
Aspose.Cells for .NET 8.8.3 ha expuesto la propiedad HTMLLoadOptions.SupportDivTag que permite analizar las etiquetas DIV incrustadas en las etiquetas TD al cargar archivos/fragmentos HTML en el modelo de objetos Aspose.Cells. La propiedad de tipo booleano tiene el valor predeterminado falso.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Admite etiquetas DIV internas al cargar HTML](/cells/es/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

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


### **Se agregó la propiedad HtmlSaveOptions.ExportGridLines**
Aspose.Cells for .NET 8.8.3 ha expuesto la propiedad HtmlSaveOptions.ExportGridLines que permite representar las líneas de la cuadrícula mientras se exporta la hoja de cálculo a formato HTML. La propiedad de tipo booleano tiene el valor predeterminado falso; sin embargo, cuando se establece en verdadero, API representa las líneas de cuadrícula para el rango de datos disponible en formato HTML.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Renderizar líneas de cuadrícula a HTML](/cells/es/net/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set ExportGridLines to true

options.ExportGridLines = true;

// Save the result in HTML format

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **Propiedad ListObject.Comment añadida**
Aspose.Cells Las API ahora permiten obtener y configurar los comentarios para una instancia de ListObject. Para proporcionar la función antes mencionada, las API Aspose.Cells han expuesto la propiedad ListObject.Comment.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Adición de comentarios para ListObjects](/cells/es/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/).

{{% /alert %}} 

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

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


### **Se agregó la propiedad GridWeb.SessionStorePath**
Aspose.Cells.GridWeb for .NET 8.8.3 ha expuesto la propiedad SessionStorePath que permite obtener o establecer la ruta del almacenamiento de la sesión cuando el modo de sesión es ViewState. La propiedad antes mencionada obtiene o establece la ruta relativa al directorio base de la aplicación web actual.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Especifique la ruta para los archivos de sesión temporales](/cells/es/net/specify-the-path-where-gridweb-stores-temporary-session-files/).

{{% /alert %}} 

El siguiente es el escenario de uso simple.
## **API eliminadas**
### **Libro de trabajo eliminado. Método de descifrado**
Dicha propiedad fue marcada como obsoleta hace algún tiempo. Esta versión lo ha eliminado por completo del público API. Se recomienda establecer la propiedad WorkbookSettings.Password en nulo para lograr el mismo objetivo.
