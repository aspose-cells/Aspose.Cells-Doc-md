---
title: Público API Cambios en Aspose.Cells 8.7.0
type: docs
weight: 230
url: /es/net/public-api-changes-in-aspose-cells-8-7-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.6.3 a la 8.7.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Compatibilidad con la firma, detección y extracción digital del proyecto VBA**
Esta versión de Aspose.Cells for .NET ha expuesto algunas propiedades y métodos nuevos para ayudar a los usuarios en tareas como la firma digital de un proyecto de VBA, la detección de si un proyecto de VBA está firmado y es válido. Además, el nuevo API permite extraer el certificado como datos sin procesar del proyecto VBA firmado digitalmente en Workbook.
###### **Firmar digitalmente el proyecto VBA**
 Aspose.Cells for .NET 8.7.0 ha expuesto el método VbaProject.Sign que se puede utilizar para[firmar digitalmente el proyecto VBA en un libro de trabajo](/cells/es/net/digitally-sign-a-vba-code-project-with-certificate/). Dicho método acepta una instancia de la clase DigitalSignature que reside en el espacio de nombres Aspose.Cells.DigitalSignatures.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Sign the VbaProject using the X509Certificate

vbaProject.Sign(new DigitalSignature(new System.Security.Cryptography.X509Certificates.X509Certificate2(cert), "Comments", DateTime.Now));

{{< /highlight >}}


###### **Detección de proyecto VBA firmado digitalmente**
 La propiedad VbaProject.IsSigned recién expuesta se puede usar para[detectar si el proyecto de VBA en un libro de trabajo está firmado digitalmente](/cells/es/net/check-if-vba-code-is-signed/). La propiedad VbaProject.IsSigned es de tipo booleano, que devuelve verdadero si el proyecto de VBA está firmado digitalmente y viceversa.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Check if VbaProject is digitally signed

if (vbaProject.IsSigned)

{

    Console.WriteLine("VbaProject is digitally signed");

}

else

{

    Console.WriteLine("VbaProject is not digitally signed");

}

{{< /highlight >}}


###### **Extracción de Firma Digital del Proyecto VBA**
Esta revisión de API también ha expuesto la propiedad VbaProject.CertRawData que permite[extraer los datos sin procesar del certificado digital del proyecto VBA](/cells/es/net/export-vba-certificate-to-file-or-stream/). La propiedad VbaProject.CertRawData es de tipo matriz de bytes, que contendrá los datos del certificado sin procesar si el proyecto VBA está firmado digitalmente; de lo contrario, dicha propiedad será nula.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Extract digital signature in an array of bytes

var cert = vbaProject.CertRawData;

{{< /highlight >}}


###### **Validar la Firma Digital del Proyecto VBA**
 Otra adición al público API es la propiedad VbaProject.IsValidSigned que podría ser útil en[validando la firma digital del proyecto VBA](/cells/es/net/check-if-digital-signature-of-vba-code-is-valid/). Dicha propiedad devuelve verdadero si la firma digital es válida y falso si la firma no es válida.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Check if VbaProject is digitally signed

if (vbaProject.IsSigned)

{

    //Check if signature is valid

    if (vbaProject.IsValidSigned)

    {

        Console.WriteLine("VbaProject is digitally signed & signature is valid");

    }

}

{{< /highlight >}}


### **Método Protection.VerifyPassword agregado**
 Aspose.Cells for .NET 8.7.0 ha expuesto el método Protection.VerifyPassword que se puede utilizar para[verificar la contraseña utilizada para proteger la hoja de trabajo](/cells/es/net/verify-password-used-to-protect-the-worksheet/)Este método acepta una instancia de cadena como parámetro y devuelve verdadero si la contraseña especificada coincide con la contraseña utilizada para proteger la hoja de trabajo.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

var sheet = book.Worksheets[0];

//Access Protection module of desired Worksheet

var protection = sheet.Protection;

//Verify the password for Worksheet

if (protection.VerifyPassword(password))

{

    Console.WriteLine("Password has matched");

}

else

{

    Console.WriteLine("Password did not match");

}

{{< /highlight >}}


### **Protección de propiedad. IsProtectedWithPassword agregado**
 Esta versión de Aspose.Cells for .NET API también ha expuesto la propiedad Protection.IsProtectedWithPassword que puede ser útil en[detectar si una hoja de trabajo está protegida con contraseña o no](/cells/es/net/detect-if-worksheet-is-password-protected/).

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

var sheet = book.Worksheets[0];

//Access Protection module of desired Worksheet

var protection = sheet.Protection;

//Check if Worksheet is password protected

if (protection.IsProtectedWithPassword)

{

    Console.WriteLine("Worksheet is password protected");

}

else

{

    Console.WriteLine("Worksheet is not password protected");

}

{{< /highlight >}}


### **Propiedad ColorScale.Is3ColorScale agregado**
 Aspose.Cells for .NET 8.7.0 ha expuesto la propiedad ColorScale.Is3ColorScale que se puede usar para crear un formato condicional de escala de 2 colores. Dicha propiedad es de tipo booleano con valor predeterminado de verdadero, lo que significa que el formato condicional será de escala de 3 colores de forma predeterminada. Sin embargo, cambiar la propiedad ColorScale.Is3ColorScale a false[generar un formato condicional de escala de 2 colores](/cells/es/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/).

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the Worksheet to which conditional formatting rule has to be added

var sheet = book.Worksheets[0];

//Add FormatConditions to the collection

int index = sheet.ConditionalFormattings.Add();

//Access newly added formatConditionCollection via its index

var formatConditionCollection = sheet.ConditionalFormattings[index];

//Create a CellArea on which conditional formatting rule will be applied

var cellArea = CellArea.CreateCellArea("A1", "A5");

//Add conditional formatted cell range

formatConditionCollection.AddArea(cellArea);

//Add format condition of type ColorScale

index = formatConditionCollection.AddCondition(FormatConditionType.ColorScale);

//Access newly added format condition via its index

var formatCondition = formatConditionCollection[index];

//Set Is3ColorScale to false in order to generate a 2-Color Scale format

formatCondition.ColorScale.Is3ColorScale = false;

//Set other necessary properties

{{< /highlight >}}


### **Propiedad TxtLoadOptions.HasFormula Agregada**
 Aspose.Cells for .NET 8.7.0 ha proporcionado soporte para[identifique y analice las fórmulas mientras carga archivos CSV/TXT con datos simples delimitados](/cells/es/net/load-or-import-csv-file-with-formulas/). La propiedad TxtLoadOptions.HasFormula recién expuesta cuando se establece en verdadero dirige el API para analizar las fórmulas del archivo delimitado de entrada y establecerlas en celdas relevantes sin requerir ningún procesamiento adicional.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of TxtLoadOptions

var options = new TxtLoadOptions();

//Set HasFormula property to true

options.HasFormula = true;

//Set the Separator property as desired

options.Separator = ',';

//Load the CSV/TXT file using the instance of TxtLoadOptions

var book = new Workbook(inFilePath, options);

//Calculate formulas in order to get the calculated values of formula in CSV

book.CalculateFormula();

//Write result in any of the supported formats

book.Save(outFilePath);

{{< /highlight >}}


### **Propiedad DataLabels.IsResizeShapeToFitText agregado**
 Otra característica útil que ha expuesto Aspose.Cells for .NET 8.7.0 es la propiedad DataLabels.IsResizeShapeToFitText que puede habilitar la[Cambiar el tamaño de la forma para que se ajuste al texto](/cells/es/net/resize-chart-s-data-label-shape-to-fit-text/)característica de la aplicación Excel para las etiquetas de datos del gráfico.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook containing the Chart

var book = new Workbook(inFilePath);

//Access the Worksheet that contains the Chart

var sheet = book.Worksheets[0];

//Access the desired Chart via its index or name

var chart = sheet.Charts[0];

//Access the DataLabels of desired NSeries

var labels = chart.NSeries[0].DataLabels;

//Set ResizeShapeToFitText property to true

labels.IsResizeShapeToFitText = true;

//Calculate Chart

chart.Calculate();

{{< /highlight >}}


### **Propiedad PdfSaveOptions.OptimizationType agregado**
Aspose.Cells for .NET 8.7.0 ha expuesto la propiedad PdfSaveOptions.OptimizationType junto con la enumeración PdfOptimizationType para facilitar a los usuarios[elija el algoritmo de optimización deseado mientras exporta hojas de cálculo al formato PDF](/cells/es/net/save-excel-into-pdf-with-standard-or-minimum-size/). Hay 2 valores posibles para la propiedad PdfSaveOptions.OptimizationType como se detalla a continuación.

1. PdfOptimizationType.MinimumSize: la calidad se ve comprometida por el tamaño del archivo resultante.
1. PdfOptimizationType.Standard: la calidad no se ve comprometida, por lo que el tamaño del archivo resultante será grande.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of PdfSaveOptions

var pdfSaveOptions = new PdfSaveOptions();

//Set the OptimizationType property to desired value

pdfSaveOptions.OptimizationType = PdfOptimizationType.MinimumSize;

//Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook(inFilePath);

//Save the spreadsheet in PDF format while passing the instance of PdfSaveOptions

book.Save(outFilePath, pdfSaveOptions);

{{< /highlight >}}
## **API eliminadas**
### **Propiedad Workbook.SaveOptions Eliminado**
La propiedad Workbook.SaveOptions se marcó como obsoleta hace algún tiempo. Con esta versión, se ha eliminado por completo del público API, por lo que se recomienda utilizar el método Workbook.Save(Stream, SaveOptions) o Workbook.Save(string, SaveOptions) como alternativa.
