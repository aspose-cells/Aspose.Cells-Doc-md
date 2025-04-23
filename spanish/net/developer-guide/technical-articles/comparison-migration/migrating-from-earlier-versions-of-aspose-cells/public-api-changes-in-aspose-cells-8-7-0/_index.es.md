---
title: Cambios en la API Pública en Aspose.Cells 8.7.0
type: docs
weight: 230
url: /es/net/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.6.3 hasta la 8.7.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Soporte para Firma Digital, Detección y Extracción de Proyectos VBA**
Esta versión de Aspose.Cells for .NET ha expuesto algunas nuevas propiedades y métodos para ayudar a los usuarios en tareas como firmar digitalmente un proyecto VBA, detectar si un proyecto VBA está firmado y es válido. Además, la nueva API permite extraer el certificado como datos sin procesar de un proyecto VBA firmado digitalmente en un libro de trabajo.
###### **Firmar Digitalmente un Proyecto VBA**
Aspose.Cells for .NET 8.7.0 ha expuesto el método VbaProject.Sign que se puede utilizar para [firmar digitalmente el proyecto VBA en un libro de trabajo](/cells/es/net/digitally-sign-a-vba-code-project-with-certificate/). El mencionado método acepta una instancia de la clase DigitalSignature que reside en el espacio de nombres Aspose.Cells.DigitalSignatures.

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Sign the VbaProject using the X509Certificate

vbaProject.Sign(new DigitalSignature(new System.Security.Cryptography.X509Certificates.X509Certificate2(cert), "Comments", DateTime.Now));

{{< /highlight >}}


###### **Detección de Proyecto VBA Firmado Digitalmente**
La nueva propiedad VbaProject.IsSigned expuesta puede usarse para [detectar si el proyecto VBA en un libro de trabajo está firmado digitalmente](/cells/es/net/check-if-vba-code-is-signed/). La propiedad VbaProject.IsSigned es de tipo booleano, que devuelve true si el proyecto VBA está firmado digitalmente y viceversa.

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

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


###### **Extracción de Firma Digital de Proyecto VBA**
Esta revisión de la API también ha expuesto la propiedad VbaProject.CertRawData que permite [extraer los datos sin procesar del certificado digital del proyecto VBA](/cells/es/net/export-vba-certificate-to-file-or-stream/). La propiedad VbaProject.CertRawData es de tipo matriz de bytes, que contendrá los datos sin procesar del certificado si el proyecto VBA está firmado digitalmente; de lo contrario, dicha propiedad será nula.

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Extract digital signature in an array of bytes

var cert = vbaProject.CertRawData;

{{< /highlight >}}


###### **Validar la Firma Digital del Proyecto VBA**
Otra adición a la API pública es la propiedad VbaProject.IsValidSigned que podría ser útil para [validar la firma digital del proyecto VBA](/cells/es/net/check-if-digital-signature-of-vba-code-is-valid/). Dicha propiedad devuelve true si la firma digital es válida y false si la firma es inválida.

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

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


### **Agregado el Método Protection.VerifyPassword**
Aspose.Cells for .NET 8.7.0 ha expuesto el método Protection.VerifyPassword que se puede utilizar para [verificar la contraseña utilizada para proteger la hoja de cálculo](/cells/es/net/verify-password-used-to-protect-the-worksheet/). Este método acepta una instancia de cadena como parámetro y devuelve true si la contraseña especificada coincide con la contraseña utilizada para proteger la hoja de cálculo.

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

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


### **Agregada la Propiedad Protection.IsProtectedWithPassword**
Esta versión de Aspose.Cells for .NET API también ha expuesto la propiedad Protection.IsProtectedWithPassword que puede ser útil para [detectar si una hoja de cálculo está protegida con contraseña o no](/cells/es/net/detect-if-worksheet-is-password-protected/).

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

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


### **Propiedad Added ColorScale.Is3ColorScale**
Aspose.Cells for .NET 8.7.0 ha expuesto la propiedad ColorScale.Is3ColorScale que puede usarse para crear formato condicional de Escala de 2 Colores. Dicha propiedad es de tipo Boolean con un valor predeterminado de true, lo que significa que el formato condicional será de Escala de 3 Colores por defecto. Sin embargo, cambiar la propiedad ColorScale.Is3ColorScale a false [generará un formato condicional de Escala de 2 Colores](/cells/es/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/).

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

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


### **Propiedad Agregada TxtLoadOptions.HasFormula**
Aspose.Cells for .NET 8.7.0 ha proporcionado soporte para [identificar y analizar fórmulas mientras se cargan archivos CSV/TXT con datos delimitados](/cells/es/net/load-or-import-csv-file-with-formulas/). La propiedad recién expuesta TxtLoadOptions.HasFormula, cuando se establece en true, indica a la API que analice las fórmulas del archivo delimitado de entrada y las establezca en las celdas relevantes sin requerir ningún procesamiento adicional.

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

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


### **Propiedad DataLabels.IsResizeShapeToFitText agregada**
Otra característica útil que Aspose.Cells for .NET 8.7.0 ha expuesto es la propiedad DataLabels.IsResizeShapeToFitText que puede habilitar la función [Redimensionar forma para ajustar el texto](/cells/es/net/resize-chart-s-data-label-shape-to-fit-text/) de la aplicación Excel para las etiquetas de datos del gráfico.

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

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


### **Propiedad PdfSaveOptions.OptimizationType agregada**
Aspose.Cells for .NET 8.7.0 ha expuesto la propiedad PdfSaveOptions.OptimizationType junto con la enumeración PdfOptimizationType para facilitar a los usuarios [elegir el algoritmo de optimización deseado al exportar hojas de cálculo a formato PDF](/cells/es/net/save-excel-into-pdf-with-standard-or-minimum-size/). Hay 2 valores posibles para la propiedad PdfSaveOptions.OptimizationType como se detalla a continuación:

1. PdfOptimizationType.MinimumSize: La calidad se ve comprometida por el tamaño del archivo resultante.
2. PdfOptimizationType.Standard: La calidad no se ve comprometida, por lo que el tamaño del archivo resultante será grande.

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

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
## **APIs Eliminadas**
### **Propiedad Workbook.SaveOptions eliminada**
La propiedad Workbook.SaveOptions fue marcada como obsoleta hace algún tiempo. Con esta versión, ha sido completamente eliminada de la API pública, por lo tanto, se recomienda utilizar el método Workbook.Save(Stream, SaveOptions) o Workbook.Save(string, SaveOptions) como alternativa.
{{< app/cells/assistant language="csharp" >}}
