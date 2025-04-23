---
title: Cambios en la API Pública en Aspose.Cells 8.7.0
type: docs
weight: 240
url: /es/java/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.6.3 hasta la 8.7.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Soporte para Optimización de PDF**
Las APIs de Aspose.Cells ya proporcionan la característica de convertir hojas de cálculo a PDF. Con esta versión de la API, los usuarios ahora pueden [optimizar el tamaño del PDF resultante](/cells/es/java/save-excel-into-pdf-with-standard-or-minimum-size/) también. Aspose.Cells for Java 8.7.0 ha expuesto la propiedad PdfSaveOptions.OptimizationType junto con la enumeración PdfOptimizationType para facilitar a los usuarios elegir el algoritmo de optimización deseado al exportar hojas de cálculo al formato PDF. Existen 2 valores posibles para la propiedad PdfSaveOptions.OptimizationType como se detalla a continuación. 

1. PdfOptimizationType.MINIMUM_SIZE: La calidad se ve comprometida por el tamaño del archivo resultante.
2. PdfOptimizationType.STANDARD: La calidad no se ve comprometida, por lo que el tamaño del archivo resultante será grande.

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of PdfSaveOptions

PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();

//Set the OptimizationType property to desired value

pdfSaveOptions.setOptimizationType(PdfOptimizationType.MINIMUM_SIZE);

//Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Save the spreadsheet in PDF format while passing the instance of PdfSaveOptions

book.save(outFilePath, pdfSaveOptions);

{{< /highlight >}}
### **Detección de Proyecto VBA Firmado Digitalmente**
La propiedad recién expuesta VbaProject.isSigned se puede utilizar para [detectar si el proyecto VBA en un Libro está firmado digitalmente](/cells/es/java/check-if-vba-code-is-signed/). La propiedad VbaProject.isSigned es de tipo Boolean, que devuelve true si el proyecto VBA está firmado digitalmente y viceversa.

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

VbaProject vbaProject = book.getVbaProject();

//Check if VbaProject is digitally signed

if (vbaProject.isSigned())

{

	System.out.println("VbaProject is digitally signed");

}

else

{

	System.out.println("VbaProject is not digitally signed");

}

{{< /highlight >}}
### **Método Protection.verifyPassword Agregado**
Las APIs de Aspose.Cells han mejorado la clase Protection al introducir el método verifyPassword que permite especificar una contraseña como una instancia de String y [verifica si se ha utilizado la misma contraseña para proteger la Hoja de cálculo](/cells/es/java/verify-password-used-to-protect-the-worksheet/). El método Protection.verifyPassword devuelve true si la contraseña especificada coincide con la contraseña utilizada para proteger la hoja de cálculo dada, y false si la contraseña especificada no coincide. El siguiente fragmento de código utiliza el método Protection.verifyPassword en conjunto con el campo Protection.isProtectedWithPassword para detectar la protección con contraseña y verificar la contraseña.

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load a spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the protected Worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Check if Worksheet is password protected

if (sheet.getProtection().isProtectedWithPassword())

{

  //Verify the password used to protect the Worksheet

  if (sheet.getProtection().verifyPassword("password"))

  {

	  System.out.println("Specified password has matched");

  }

  else

  {

	  System.out.println("Specified password has not matched");

  }

}

{{< /highlight >}}
### **Propiedad Protection.isProtectedWithPassword Agregada**
Esta versión de Aspose.Cells for Java también ha expuesto el campo Protection.isProtectedWithPassword que puede ser útil para [detectar si una Hoja de cálculo está protegida con contraseña o no](/cells/es/java/detect-if-worksheet-is-password-protected/).

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

Worksheet sheet = book.getWorksheets().get(0);

//Access Protection module of desired Worksheet

Protection protection = sheet.getProtection();

//Check if Worksheet is password protected

if (protection.isProtectedWithPassword())

{

	System.out.println("Worksheet is password protected");

}

else

{

	System.out.println("Worksheet is not password protected");

}

{{< /highlight >}}
### **Propiedad Added ColorScale.Is3ColorScale**
Aspose.Cells for Java 8.7.0 ha expuesto la propiedad ColorScale.Is3ColorScale que se puede utilizar para [crear formato condicional de escala de 2 colores](/cells/es/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/). La mencionada propiedad es de tipo Boolean con un valor predeterminado de true, lo que significa que el formato condicional será de escala de 3 colores de forma predeterminada. Sin embargo, cambiar la propiedad ColorScale.Is3ColorScale a false generará un formato condicional de escala de 2 colores.

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access the Worksheet to which conditional formatting rule has to be added

Worksheet sheet = book.getWorksheets().get(0);

//Add FormatConditions to the collection

int index = sheet.getConditionalFormattings().add();

//Access newly added formatConditionCollection via its index

FormatConditionCollection formatConditionCollection = sheet.getConditionalFormattings().get(index);

//Create a CellArea on which conditional formatting rule will be applied

CellArea cellArea = CellArea.createCellArea("A1", "A5");

//Add conditional formatted cell range

formatConditionCollection.addArea(cellArea);

//Add format condition of type ColorScale

index = formatConditionCollection.addCondition(FormatConditionType.COLOR_SCALE);

//Access newly added format condition via its index

FormatCondition formatCondition = formatConditionCollection.get(index);

//Set Is3ColorScale to false in order to generate a 2-Color Scale format

formatCondition.getColorScale().setIs3ColorScale(false);

//Set other necessary properties

{{< /highlight >}}
### **Propiedad Agregada TxtLoadOptions.HasFormula**
Aspose.Cells for Java 8.7.0 ha proporcionado soporte para [identificar y analizar las fórmulas al cargar archivos CSV/TXT que contienen datos planos delimitados](/cells/es/java/load-or-import-csv-file-with-formulas/). La propiedad recién expuesta TxtLoadOptions.HasFormula cuando se establece en true dirige a la API para analizar las fórmulas del archivo delimitado de entrada y establecerlas en celdas relevantes sin necesidad de ningún procesamiento adicional.

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of TxtLoadOptions

TxtLoadOptions options = new TxtLoadOptions();

//Set HasFormula property to true

options.setHasFormula(true);

//Set the Separator property as desired

options.setSeparator(',');

//Load the CSV/TXT file using the instance of TxtLoadOptions

Workbook book = new Workbook(inFilePath, options);

//Calculate formulas in order to get the calculated values of formula in CSV

book.calculateFormula();

//Write result in any of the supported formats

book.save(outFilePath);

{{< /highlight >}}
### **Propiedad Agregada DataLabels.ResizeShapeToFitText**
Otra característica útil que Aspose.Cells for Java 8.7.0 ha expuesto es la propiedad DataLabels.ResizeShapeToFitText que puede habilitar la función de [ajustar la forma para que se ajuste al texto](/cells/es/java/resize-chart-s-data-label-shape-to-fit-text/) de la aplicación Excel para las etiquetas de datos del gráfico.

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook containing the Chart

Workbook book = new Workbook(inFilePath);

//Access the Worksheet that contains the Chart

Worksheet sheet = book.getWorksheets().get(0);

//Access the desired Chart via its index or name

Chart chart = sheet.getCharts().get(0);

//Access the DataLabels of desired NSeries

DataLabels labels = chart.getNSeries().get(0).getDataLabels();

//Set ResizeShapeToFitText property to true

labels.setResizeShapeToFitText(true);

//Calculate Chart

chart.calculate();

{{< /highlight >}}
## **APIs Eliminadas**
### **Propiedad Eliminada Workbook.SaveOptions**
La propiedad Workbook.SaveOptions fue marcada como obsoleta hace algún tiempo. Con esta versión, se ha eliminado por completo de la API pública, por lo tanto, se recomienda utilizar el método Workbook.save(Stream, SaveOptions) o Workbook.save(string, SaveOptions) como alternativa.
{{< app/cells/assistant language="java" >}}
