---
title: Cambios en la API pública en Aspose.Cells 9.0.0
type: docs
weight: 340
url: /es/java/public-api-changes-in-aspose-cells-9-0-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.9.2 hasta la 9.0.0 que pueden interesar a los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases añadidas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento interno de Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Propiedad Shape.TextOptions agregada**
Aspose.Cells for Java ha expuesto la propiedad TextOptions para la clase Shape con el fin de controlar la apariencia de las partes de texto de una forma.

Aquí hay un escenario de uso simple de la propiedad Shape.TextOptions.

**Java**

{{< highlight csharp >}}

 //Initialize an instance of Workbook

Workbook book = new Workbook();

//Get the default Worksheet from the Workbook

Worksheet sheet = book.getWorksheets().get(0);

//Add a TextBox to the collection

int textboxIndex = sheet.getTextBoxes().add(2, 1, 160, 200);

//Get the TextBox object

TextBox textbox = sheet.getTextBoxes().get(textboxIndex);

//Add text to the TextBox

textbox.setText("Hello Aspose!");

//Format the textual contents

textbox.getTextOptions().setColor(Color.getRed());

textbox.getTextOptions().setItalic(true);

textbox.getTextOptions().setBold(true);

{{< /highlight >}}
### **Agregada la propiedad ChartPoint.IsInSecondaryPlot.**
Aspose.Cells for Java ha expuesto la propiedad ChartPoint.IsInSecondaryPlot la cual puede ser usada para detectar si un ChartPoint reside en un segundo gráfico de un gráfico de torta o de barras.

Aquí hay un escenario de uso simple de la propiedad Shape.Line.

{{% alert color="primary" %}} 

Consulta el artículo detallado en [Encontrar un DataPoint que reside en el Segundo Gráfico](/cells/es/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Load an existing spreadsheet containing a Pie chart

Workbook book = new Workbook(dir + "PieBar.xlsx");

//Load the Worksheet at 0 index

Worksheet sheet = book.getWorksheets().get(0);

//Load the first chart from the collection

Chart chart = sheet.getCharts().get(0);

//Calculate the chart before accessing its properties

chart.calculate();

//Accessing chart's first series

Series series = chart.getNSeries().get(0);

//Loop over the ChartPoint collection

for(int p = 0 ; p < series.getPoints().getCount(); p++)

{

	ChartPoint point = series.getPoints().get(p);



	//Detect if ChartPoint resides on secondary plot

	System.out.println(point.isInSecondaryPlot());

}

{{< /highlight >}}
### **Agregada la propiedad OleObject.ClassIdentifier.**
Aspose.Cells for Java ha expuesto la propiedad OleObject.ClassIdentifier la cual puede ser usada para especificar el comportamiento de la aplicación para cargar un OleObject. Por ejemplo, un archivo PPT se puede incrustar en una hoja de cálculo con 2 vistas diferentes, es decir; vista de presentación o vista de diapositiva, mientras que ambas vistas tienen valores de identificación de clase diferentes.

A continuación se muestra el escenario de uso simple de la propiedad OleObject.ClassIdentifier.

{{% alert color="primary" %}} 

Consulta el artículo detallado en [Usando OleObject.ClassIdentifier](https://docs.aspose.com/cells/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet containing a presentation as OleObject

Workbook book = new Workbook(dir + "embeddedPresentation.xls");

//Initialize variables to store properties of OleObject

int upperLeftRow = 0;

int upperLeftColumn = 0;

int height = 0;

int width = 0;

byte[] imageData = null;

int x = 0;

int y = 0;

byte[] objData = null;

String progID = "";

int fileFormatType = 0;

String sourceFullName = "";

Boolean isDisplayAsIcon = false;

byte[] classId = null;

//Get the first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Get the first OleObject from the collection

OleObject frame = sheet.getOleObjects().get(0);

//Store the properties in variables

upperLeftRow = frame.getUpperLeftRow();

upperLeftColumn = frame.getUpperLeftColumn();

height = frame.getHeight();

width = frame.getWidth();

imageData = frame.getImageData();

x = frame.getX();

y = frame.getY();

objData = frame.getObjectData();

progID = frame.getProgID();

fileFormatType = frame.getFileFormatType();

sourceFullName = frame.getObjectSourceFullName();

isDisplayAsIcon = frame.getDisplayAsIcon();

classId = frame.getClassIdentifier();

//Initialize a new Workbook instance

book = new Workbook();

//Access first worksheet from the collection

sheet = book.getWorksheets().get(0);

//Insert the OleObject to the worksheet

int oleNumber = sheet.getOleObjects().add(upperLeftRow, upperLeftColumn, height, width, imageData);

//Access newly inserted OleObject

OleObject embeddedObject = sheet.getOleObjects().get(oleNumber);

//Assign previously stored properties to new OleObject

embeddedObject.setX(x);

embeddedObject.setY(y);

embeddedObject.setObjectData(objData);

embeddedObject.setProgID(progID);

embeddedObject.setFileFormatType(fileFormatType);

embeddedObject.setDisplayAsIcon(isDisplayAsIcon);

embeddedObject.setObjectSourceFullName(sourceFullName);

embeddedObject.setAutoSize(false);

if (classId != null)

{

	embeddedObject.setClassIdentifier(classId);

}

{{< /highlight >}}
## **APIs obsoletas**
### **Método Obsoleto Worksheet.setBackground**
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
### **Método Worksheet.copyConditionalFormatting eliminado**
### **Método Workbook.checkWriteProtectedPassword eliminado**
## **APIs renombradas**
### **Método Workbook.removeDigitallySign renombrado**
El método Workbook.removeDigitallySign ha sido renombrado a Workbook.removeDigitalSignature.
{{< app/cells/assistant language="java" >}}
