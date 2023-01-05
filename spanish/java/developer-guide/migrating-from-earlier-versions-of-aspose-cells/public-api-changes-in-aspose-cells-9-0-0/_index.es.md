---
title: Público API Cambios en Aspose.Cells 9.0.0
type: docs
weight: 340
url: /es/java/public-api-changes-in-aspose-cells-9-0-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.9.2 a la 9.0.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Se agregó la propiedad Shape.TextOptions**
Aspose.Cells for Java ha expuesto la propiedad TextOptions para la clase Shape para controlar la apariencia de las partes textuales de una forma.

Aquí hay un escenario de uso simple de la propiedad Shape.TextOptions.

**Java**

{{< highlight "csharp" >}}

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
### **Se agregó la propiedad ChartPoint.IsInSecondaryPlot**
Aspose.Cells for Java ha expuesto la propiedad ChartPoint.IsInSecondaryPlot que se puede usar para detectar si un ChartPoint reside en un gráfico secundario de un gráfico circular o de barras.

Aquí hay un escenario de uso simple de la propiedad Shape.Line.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Encontrar un punto de datos reside en la segunda parcela](/cells/es/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Cargar una hoja de cálculo existente que contenga un gráfico circular

Libro de trabajo libro = nuevo Libro de trabajo (dir + "PieBar.xlsx");

//Cargar la hoja de trabajo en el índice 0

hoja de trabajo = book.getWorksheets().get(0);

//Cargar el primer gráfico de la colección

Gráfico gráfico = hoja.getCharts().get(0);

//Calcular el gráfico antes de acceder a sus propiedades

gráfico.calcular();

//Accediendo a la primera serie del gráfico

Serie serie = chart.getNSeries().get(0);

//Recorre la colección ChartPoint

 para(int p = 0 ; p< series.getPoints().getCount(); p++)

{

	ChartPoint point = series.getPoints().get(p);



	//Detect if ChartPoint resides on secondary plot

	System.out.println(point.isInSecondaryPlot());

}

{{< /highlight >}}
### **Se agregó la propiedad OleObject.ClassIdentifier**
Aspose.Cells for Java 9.0.0 ha expuesto la propiedad OleObject.ClassIdentifier que se puede usar para especificar el comportamiento de la aplicación para cargar un OleObject. Por ejemplo, un archivo PPT se puede incrustar en una hoja de cálculo con 2 vistas diferentes, es decir; vista de presentación o vista de diapositivas, mientras que ambas vistas tienen diferentes valores de identificador de clase.

El siguiente es el escenario de uso simple de la propiedad OleObject.ClassIdentifier.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Uso de OleObject.ClassIdentifier](https://docs.aspose.com/cells/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet containing a presentation as OleObject

Workbook book = new Workbook(dir + "embeddedPresentation.xls");

//Initialize variables to store properties of OleObject

int upperLeftRow = 0;

int upperLeftColumn = 0;

int height = 0;

int width = 0;

byte[]imageData = null;

int x = 0;

int y = 0;

byte[]objData = null;

String progID = "";

int fileFormatType = 0;

String sourceFullName = "";

Boolean isDisplayAsIcon = false;

byte[]classId = null;

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
## **API obsoletas**
### **Método Worksheet.setBackground obsoleto**
Utilice la propiedad Worksheet.BackgroundImage en su lugar.
### **Propiedades LineShape.BeginArrowheadStyle y ArcShape.BeginArrowheadStyle obsoletas**
Utilice la propiedad Shape.Line.BeginArrowheadStyle como alternativa.
### **Propiedades LineShape.EndArrowheadStyle y ArcShape.EndArrowheadStyle obsoletas**
Utilice la propiedad Shape.Line.EndArrowheadStyle como alternativa.
### **Propiedades LineShape.BeginArrowheadWidth y ArcShape.BeginArrowheadWidth obsoletas**
Utilice la propiedad Shape.Line.BeginArrowheadWidth como alternativa.
### **Propiedades LineShape.BeginArrowheadLength y ArcShape.BeginArrowheadLength obsoletas**
Utilice la propiedad Shape.Line.BeginArrowheadLength en su lugar.
### **Propiedades LineShape.EndArrowheadWidth y ArcShape.EndArrowheadWidth obsoletas**
Utilice la propiedad Shape.Line.EndArrowheadWidth en su lugar.
### **Propiedades LineShape.EndArrowheadLength y ArcShape.EndArrowheadLength obsoletas**
Utilice la propiedad Shape.Line.EndArrowheadLength en su lugar.
## **API eliminadas**
### **Hoja de trabajo eliminada. Método de formato de copia condicional**
### **Método Workbook.checkWriteProtectedPassword eliminado**
## **API renombradas**
### **Método Workbook.removeDigitallySign renombrado**
Se ha cambiado el nombre del método Workbook.removeDigitallySign a Workbook.removeDigitalSignature.
