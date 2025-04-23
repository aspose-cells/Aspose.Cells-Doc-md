---
title: Cambios en la API pública en Aspose.Cells 8.8.3
type: docs
weight: 300
url: /es/java/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.8.2 a la 8.8.3 que pueden interesar a los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Soporte para controles ActiveX**
Aspose.Cells for Java 8.8.3 ha expuesto el método addActiveXControl que permite agregar un control ActiveX a ShapeCollection. El mencionado método requiere 7 parámetros para especificar el tipo de control, la ubicación para colocar el control y el tamaño del control. El tipo se puede especificar utilizando la enumeración ControlType con los siguientes valores posibles.

1. ControlType.CHECK_BOX
1. ControlType.COMBO_BOX
1. ControlType.COMMAND_BUTTON
1. ControlType.IMAGE
1. ControlType.LABEL
1. ControlType.LIST_BOX
1. ControlType.RADIO_BUTTON
1. ControlType.SCROLL_BAR
1. ControlType.SPIN_BUTTON
1. ControlType.TEXT_BOX
1. ControlType.TOGGLE_BUTTON
1. ControlType.UNKNOWN

{{% alert color="primary" %}} 

Para obtener más detalles sobre esta característica, revise el artículo detallado sobre [Agregar controles ActiveX a la hoja de cálculo](/cells/es/java/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Add Toggle Button ActiveX Control to the ShapeCollection at specified location

Shape shape = sheet.getShapes().addActiveXControl(ControlType.TOGGLE_BUTTON, 4, 0, 4, 0, 100, 30);

//Access the ActiveX Control object and set its linked cell property

ActiveXControl control = shape.getActiveXControl();

control.setLinkedCell("A1");

//Save the result on disc

book.save(dir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Agregado método LoadOptions.setPaperSize**
Aspose.Cells for Java 8.8.3 permite configurar el tamaño de papel de impresión predeterminado desde la configuración de la impresora predeterminada al utilizar el método recién expuesto LoadOptions.setPaperSize como se muestra a continuación. Tenga en cuenta que el parámetro de entrada al método mencionado es el valor de la enumeración PaperSizeType que contiene los tamaños de papel predefinidos.

{{% alert color="primary" %}} 

Para obtener más detalles sobre esta característica, revise el artículo detallado sobre [Cargar hojas de cálculo con un tamaño de papel especificado](/cells/es/java/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **Añadido método Cell.getCharacters(flag)**
Las APIs de Aspose.Cells permiten obtener los objetos de caracteres en forma de matriz de FontSetting utilizando el método Cell.getCharacters. Con esta versión, la API Aspose.Cells for Java ha expuesto una versión sobrecargada de Cell.getCharacters que podría aceptar un Boolean como parámetro, indicando si se debe aplicar el estilo de tabla en la celda si la celda es parte de un ListObject.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access cells collection of the first worksheet

Cells cells = sheet.getCells();

//Access particular cell from a ListObject

//Assuming A1 resides in a ListObject

Cell cell = cells.get("A1");

//Get all Characters objects from the cell

FontSetting[] characters = cell.getCharacters(true);

{{< /highlight >}}
### **Añadida propiedad OleObject.AutoLoad**
Aspose.Cells for Java 8.8.3 ha expuesto la propiedad OleObject.AutoLoad que permite actualizar la imagen de OleObject si el contenido/datos del objeto subyacente han cambiado. La mencionada propiedad, cuando se establece en true, obliga a la aplicación de Excel a actualizar la imagen del OleObject cuando se carga la hoja de cálculo resultante.

{{% alert color="primary" %}} 

Para obtener más detalles sobre esta característica, revise el artículo detallado sobre [Actualizar automáticamente los OleObjects](/cells/es/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access OleObjectCollection from first worksheet

OleObjectCollection oleObjects = sheet.getOleObjects();

//Access a OleObject from the collection

OleObject oleObject = oleObjects.get(0);

//Set AutoLoad to true

oleObject.setAutoLoad(true);

{{< /highlight >}}
### **Añadida propiedad HTMLLoadOptions.SupportDivTag**
Aspose.Cells for Java 8.8.3 ha expuesto la propiedad HTMLLoadOptions.SupportDivTag que permite analizar las etiquetas DIV incrustadas en las etiquetas TD al cargar archivos/snippets HTML en el modelo de objetos Aspose.Cells. La propiedad de tipo booleano tiene el valor predeterminado de falso.

{{% alert color="primary" %}} 

Para más detalles sobre esta característica, por favor revise el artículo detallado en [Soportar Etiquetas DIV Internas al Cargar HTML](/cells/es/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Store the HTML snippet in a variable

String export_html = "<html>"

\+ "<body>"

\+ " <table>"

\+ "     <tr>"

\+ "         <td>"

\+ "             <div>This is some Text.</div>"

\+ "             <div>"

\+ "                 <div>"

\+ "                     <span>This is some more Text</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>abc@abc.com</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>1234567890</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>ABC DEF</span>"

\+ "                 </div>"

\+ "             </div>"

\+ "             <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>"

\+ "         </td>"

\+ "         <td>"

\+ "             <img src='ASpose_logo_100x100.png' />"

\+ "         </td>"

\+ "     </tr>"

\+ " </table>"

\+ "</body>"

\+ "</html>";

//Convert HTML string to InputStream

InputStream stream = new ByteArrayInputStream(export_html.getBytes(StandardCharsets.UTF_8));

//Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

// Set SupportDivTag property to true

loadOptions.setSupportDivTag(true);

//Create workbook object from the HTML using load options

Workbook book = new Workbook(stream, loadOptions);

//Save the spreadsheet on disc

book.save(dir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Agregada la propiedad HtmlSaveOptions.ExportGridLines**
Aspose.Cells for Java 8.8.3 ha expuesto la propiedad HtmlSaveOptions.ExportGridLines que permite renderizar las líneas de cuadrícula al exportar la hoja de cálculo al formato HTML. La propiedad de tipo booleano tiene el valor predeterminado de falso, sin embargo, cuando se establece en verdadero, la API renderiza las líneas de cuadrícula para el rango de datos disponible en formato HTML.

{{% alert color="primary" %}} 

Para más detalles sobre esta característica, por favor revise el artículo detallado en [Renderizar Líneas de Cuadrícula a HTML](/cells/es/java/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set ExportGridLines to true

options.setExportGridLines(true);

//Save the result in HTML format

book.save(dir + "output.html", options);

{{< /highlight >}}
### **Agregada la propiedad ListObject.Comment**
Las APIs de Aspose.Cells ahora permiten obtener y establecer los comentarios para una instancia de ListObject. Para proporcionar la característica anteriormente mencionada, las APIs de Aspose.Cells han expuesto la propiedad ListObject.Comment.

{{% alert color="primary" %}} 

Para más detalles sobre esta característica, por favor revise el artículo detallado en [Agregar Comentarios para ListObjects](/cells/es/java/set-the-comment-of-table-or-list-object/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first ListObject from the collection of ListObjects

ListObject listObject = sheet.getListObjects().get(0);

//Set comments for the ListObject

listObject.setComment("Comments");

//Save the result on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}
## **APIs Eliminadas**
### **Método Workbook.decrypt Eliminado**
La mencionada propiedad fue marcada como obsoleta hace algún tiempo. Esta versión la ha eliminado por completo de la API pública. Se recomienda establecer la propiedad WorkbookSettings.Password en nulo para lograr el mismo objetivo.
{{< app/cells/assistant language="java" >}}
