---
title: Imprimir hojas de cálculo
type: docs
weight: 20
url: /es/net/print-spreadsheets/
---
Los ajustes de configuración de página también proporcionan varias opciones de impresión (también denominadas opciones de hoja) que permiten a los usuarios controlar las páginas impresas de las hojas de trabajo. Estas opciones de impresión permiten a los usuarios:

- Seleccione un área de impresión específica de la hoja de trabajo
- Imprimir títulos
- Imprimir líneas de cuadrícula
- Imprimir encabezados de fila/columna
- Lograr calidad de borrador
- Imprimir comentarios
- Imprimir Cell Errores
- Definir el orden de las páginas
  **Configuración de las opciones de impresión/hoja**

Aspose.Cells admite todas estas opciones de impresión y los desarrolladores pueden configurar fácilmente estas opciones para sus hojas de trabajo deseadas utilizando las diversas propiedades que ofrece la clase PageSetup. El uso de estas propiedades de la clase PageSetup se analiza a continuación con más detalle.
## **Establecer área de impresión**
De forma predeterminada, solo se selecciona el área de impresión que incorpora toda el área de la hoja de trabajo, que contiene datos, pero los desarrolladores también pueden establecer un área de impresión específica de la hoja de trabajo según su deseo.

 Para seleccionar un área de impresión específica, los desarrolladores pueden usar set**Área de impresión** metodo de la**Configuración de página** clase. Puede proporcionar el rango de celdas del área de impresión a este método como argumento.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **Establecer títulos de impresión**
 Aspose.Cells le permite designar encabezados de fila y columna que desea que se repitan en todas las páginas de su hoja de trabajo impresa. Para hacerlo, los desarrolladores pueden usar set**ImprimirTítuloColumnas** y**setPrintTitleRows** métodos de la**Configuración de página** clase.

Las filas o columnas (que se repetirán en todas las páginas de la hoja de trabajo impresa) se definen pasando sus números de fila o columna. Por ejemplo, las filas se definen como \ $1: \ $2 y las columnas se definen como \ $A: \ $B.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

Aspose.Cells.PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows = "$1:$2";

{{< /highlight >}}
## **Establecer otras opciones de impresión**
**Configuración de página** La clase también proporciona varios otros métodos para configurar las opciones generales de impresión de la siguiente manera:

- **método setPrintGridline s** , se pasa un parámetro booleano a este método que define si imprimir o no las líneas de cuadrícula
- **método setPrintHeadings** se pasa un parámetro booleano a este método que define si imprimir encabezados de fila y columna o no
- **método setBlackAndWhite** , se pasa un parámetro booleano a este método que define si imprimir la hoja de trabajo en modo blanco y negro o no
- **método setPrintComments** , define si mostrar los comentarios de impresión en la hoja de trabajo o al final de la hoja de trabajo
- **método setPrintDraft** , se pasa un parámetro booleano a este método que define si imprimir la hoja de trabajo en calidad de borrador o no
- **método setPrintErrors** , define si imprimir los errores de celda como se muestra, en blanco, guión o N/A

 Para usar conjunto**ImprimirComentarios** y establecer**Errores de impresión** métodos, Aspose.Cells también proporciona dos enumeraciones, PrintCommentsType y PrintErrorsType que contienen valores predefinidos que se pasan a parámetros para configurar los métodos PrintComments y PrintErrors respectivamente.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Allowing to print gridlines

pageSetup.PrintGridlines = true;

//Allowing to print row/column headings

pageSetup.PrintHeadings = true;

//Allowing to print worksheet in black & white mode

pageSetup.BlackAndWhite = true;

//Allowing to print comments as displayed on worksheet

pageSetup.PrintComments = PrintCommentsType.PrintInPlace;

//Allowing to print worksheet with draft quality

pageSetup.PrintDraft = true;

//Allowing to print cell errors as N/A

pageSetup.PrintErrors = PrintErrorsType.PrintErrorsNA;

{{< /highlight >}}
## **Establecer orden de página**
**Configuración de página**La clase proporciona un método de orden establecido que se usa para ordenar que se impriman varias páginas de su hoja de trabajo. Hay dos posibilidades para ordenar las páginas de la siguiente manera:

Abajo y luego encima, por lo tanto, imprimirá todas las páginas hacia abajo antes de imprimir las páginas hacia la derecha.
Luego hacia abajo, imprimirá las páginas de izquierda a derecha antes de imprimir las páginas a continuación.
Aspose.Cells proporciona una enumeración, PrintOrderType, que contiene todos los tipos de pedidos predefinidos que se asignarán al método setPage Order.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down

pageSetup.Order = PrintOrderType.OverThenDown;

{{< /highlight >}}
## **Descargar código de muestra**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
