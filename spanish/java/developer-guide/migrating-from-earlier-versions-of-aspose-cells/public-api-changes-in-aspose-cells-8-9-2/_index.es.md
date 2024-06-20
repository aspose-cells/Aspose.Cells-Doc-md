---
title: Cambios en la API pública en Aspose.Cells 8.9.2
type: docs
weight: 330
url: /es/java/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.9.1 hasta la 8.9.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento en segundo plano de Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

También consulte los [Cambios en la API pública introducidos en Aspose.Cells for Java 8.9.1](http://aspose.com/docs/display/cellsjava/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **APIs Añadidas**
### **Clase TextOptions y propiedad FontSettings.TextOptions agregadas**
Aspose.Cells for Java ha expuesto la clase TextOptions junto con la propiedad FontSettings.TextOptions para controlar la apariencia de las partes de texto de una forma.

Aquí hay un escenario de uso simple de la propiedad FontSettings.TextOptions.

**Java**

{{< highlight csharp >}}

 //Initialize Workbook instance

Workbook book = new Workbook();

//Access first worksheet from collection

Worksheet sheet = book.getWorksheets().get(0);

//Add a Shape of type TextBox to the collection 

Shape shape = sheet.getShapes().addShape(MsoDrawingType.TEXT_BOX, 0, 0, 0, 0, 100, 200);

//Add text to Shape

shape.setText("Aspose");

//Access TextOptions of Shape

TextOptions textOptions =  ((FontSetting)shape.getCharacters().get(0)).getTextOptions();

{{< /highlight >}}
### **Propiedad de relleno, contorno y sombra TextOptions agregadas**
Aspose.Cells for Java 8.9.2 ha expuesto las propiedades TextOptions.Fill, TextOptions.Outline y TextOptions.Shadow que permiten controlar los aspectos de los contenidos de texto de la forma, como el relleno, la sombra y el contorno respectivamente. 

Aquí hay un escenario de uso simple de las propiedades mencionadas.

**Java**

{{< highlight csharp >}}

 //Initialize Workbook instance

Workbook book = new Workbook();

//Access first worksheet from collection

Worksheet sheet = book.getWorksheets().get(0);

//Add a Shape of type TextBox to the collection 

Shape shape = sheet.getShapes().addShape(MsoDrawingType.TEXT_BOX, 0, 0, 0, 0, 100, 200);

//Add text to Shape

shape.setText("Aspose");

//Access TextOptions of Shape

TextOptions textOptions =  ((FontSetting)shape.getCharacters().get(0)).getTextOptions();

//Set shadow 

textOptions.getShadow().setPresetType(PresetShadowType.BELOW);

//Set fill color

textOptions.getFill().setFillType(FillType.SOLID);

textOptions.getFill().getSolidFill().setColor(Color.getRed());

//Set outline color

textOptions.getOutline().setOneColorGradient(Color.getBlue(), 0.3, GradientStyleType.HORIZONTAL, 2);

{{< /highlight >}}
### **Propiedad Shape.Line agregada**
Aspose.Cells for Java ha expuesto la propiedad Shape.Line que devuelve una instancia de LineFormat para controlar la apariencia de los contornos de una forma.

Aquí hay un escenario de uso simple de la propiedad Shape.Line.

**Java**

{{< highlight csharp >}}

 //Initialize Workbook instance

Workbook book = new Workbook();

//Access first worksheet from collection

Worksheet sheet = book.getWorksheets().get(0);

//Add a Shape of type TextBox to the collection 

Shape shape = sheet.getShapes().addShape(MsoDrawingType.TEXT_BOX, 0, 0, 0, 0, 100, 200);

//Access LineFormat of Shape

LineFormat line = shape.getLine();

//Set weight of line

line.setWeight(4);

{{< /highlight >}}
### **Propiedad Shape.Fill agregada**
Aspose.Cells for Java La versión 8.9.2 ha expuesto la propiedad Shape.Fill que devuelve una instancia de FillFormat para controlar los diferentes aspectos del área de la forma.

A continuación se muestra el escenario de uso simple de la propiedad Shape.Fill.

**Java**

{{< highlight csharp >}}

 //Initialize Workbook instance

Workbook book = new Workbook();

//Access first worksheet from collection

Worksheet sheet = book.getWorksheets().get(0);

//Add a Shape of type TextBox to the collection 

Shape shape = sheet.getShapes().addShape(MsoDrawingType.TEXT_BOX, 0, 0, 0, 0, 100, 200);

//Access FillFormat of Shape

FillFormat fill = shape.getFill();

//Set color for fill

fill.setFillType(FillType.SOLID);

fill.getSolidFill().setColor(Color.getBlue());

{{< /highlight >}}
## **APIs obsoletas**
### **Clase ShapeFont obsoleta**
Por favor, utilice la clase TextOptions en su lugar.
### **Clase ShapeFormat obsoleta**
Por favor, utilice directamente las propiedades Shape.Fill y Shape.Line.
### **Propiedad Shape.Format obsoleta**
Por favor, utilice directamente las propiedades Shape.Fill y Shape.Line.
### **Propiedad Shape.LineFormat obsoleta**
Por favor, utilice la propiedad Shape.Line en su lugar.
### **Propiedad Shape.FillFormat obsoleta**
Por favor, utilice la propiedad Shape.Fill en su lugar.
### **Propiedad FontSetting.ShapeFont obsoleta**
Por favor, utilice la propiedad FontSetting.TextOptions en su lugar.
