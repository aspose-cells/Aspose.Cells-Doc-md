---
title: Imprimir hojas de cálculo
type: docs
weight: 20
url: /es/net/print-spreadsheets/
---

La configuración de la página también proporciona varias Opciones de impresión (también llamadas Opciones de hoja) que permiten a los usuarios controlar las páginas impresas de sus hojas de cálculo. Estas opciones de impresión permiten a los usuarios:

- Seleccionar un área de impresión específica de la hoja de cálculo
- Imprimir títulos
- Imprimir líneas de cuadrícula
- Imprimir encabezados de fila/columna
- Lograr calidad de borrador
- Imprimir comentarios
- Imprimir errores de celda
- Definir el orden de las páginas
  **Configuración de Opciones de Impresión/Hoja**

Aspose.Cells admite todas estas opciones de impresión y los desarrolladores pueden configurar fácilmente estas opciones para sus hojas de cálculo deseadas utilizando las diversas propiedades ofrecidas por la clase PageSetup. El uso de estas propiedades de la clase PageSetup se discute a continuación con más detalle.
## **Establecer Área de Impresión**
Por defecto, solo se selecciona el área de impresión que incorpora todo el área de la hoja de cálculo que contiene datos, pero los desarrolladores también pueden establecer un área de impresión específica de la hoja según su deseo.

Para seleccionar un área de impresión específica, los desarrolladores pueden utilizar el método **setPrintArea** de la clase **PageSetup**. Puedes proporcionar el rango de celdas del área de impresión a este método como argumento.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **Establecer Títulos de Impresión**
Aspose.Cells te permite designar los encabezados de fila y columna que quieres que se repitan en todas las páginas de tu hoja de cálculo impresa. Para hacerlo, los desarrolladores pueden utilizar los métodos **setPrintTitleColumns** y **setPrintTitleRows** de la clase **PageSetup**.

Las filas o columnas (que se repetirán en todas las páginas de la hoja de cálculo impresa) se definen pasando sus números de fila o columna. Por ejemplo, las filas se definen como \ $1: \ $2 y las columnas se definen como \ $A: \ $B.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

Aspose.Cells.PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows = "$1:$2";

{{< /highlight >}}
## **Establecer Otras Opciones de Impresión**
La clase **PageSetup** también proporciona varios otros métodos para establecer opciones generales de impresión de la siguiente manera:

- **método setPrintGridline s**, se pasa un parámetro booleano a este método que define si imprimir o no las líneas de cuadrícula
- **método setPrintHeadings**, se pasa un parámetro booleano a este método que define si imprimir o no los encabezados de fila y columna
- **método setBlackAndWhite**, se pasa un parámetro booleano a este método que define si imprimir la hoja de cálculo en modo blanco y negro o no
- **método setPrintComments**, define si mostrar los comentarios de impresión en la hoja de cálculo o al final de la hoja de cálculo
- **método setPrintDraft**, se pasa un parámetro booleano a este método que define si imprimir la hoja de cálculo en calidad de borrador o no
- **método setPrintErrors**, define si imprimir errores de celda tal como se muestran, en blanco, guion o N/A

Para utilizar los métodos **setPrintComments** y **setPrintErrors**, Aspose.Cells también proporciona dos enumeraciones, PrintCommentsType y PrintErrorsType que contienen valores predefinidos para ser pasados como parámetros a los métodos setPrintComments y setPrintErrors respectivamente.

{{< highlight csharp >}}

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
## **Establecer Orden de Páginas**
La clase **PageSetup** proporciona el método set Order que se utiliza para ordenar las múltiples páginas de tu hoja de cálculo a imprimir. Hay dos posibilidades para ordenar las páginas de la siguiente manera:

Primero abajo y luego a la derecha, por lo que imprimirá todas las páginas hacia abajo antes de imprimir las páginas hacia la derecha
Primero de arriba abajo, luego se imprimirán las páginas de izquierda a derecha antes de imprimir las páginas debajo
Aspose.Cells proporciona una enumeración, PrintOrderType, que contiene todos los tipos de orden predefinidos para asignar al método setPage Order.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down

pageSetup.Order = PrintOrderType.OverThenDown;

{{< /highlight >}}
## **Descargar Código de Ejemplo**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
