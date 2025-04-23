---
title: Cambios en la API pública en Aspose.Cells 16.10.0
type: docs
weight: 350
url: /es/java/public-api-changes-in-aspose-cells-16-10-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 9.0.0 hasta la 16.10.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, clases añadidas y eliminadas, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Soporte para efectos de reflexión**
Aspose.Cells 16.10.0 ha expuesto la clase ReflectionEffect junto con la propiedad Shape.Reflection para controlar los efectos de reflexión de un objeto Shape. La clase ReflectionEffect tiene las siguientes propiedades.

- ReflectionEffect.Blur: Obtiene/establece el radio de desenfoque en unidades de puntos.
- ReflectionEffect.Direction: Obtiene/establece la dirección de la rampa de degradado alfa en relación con la forma misma.
- ReflectionEffect.Distance: Obtiene/establece la distancia de la reflexión en unidades de puntos.
- ReflectionEffect.FadeDirection: Obtiene/establece la dirección para desplazar la reflexión.
- ReflectionEffect.RotWithShape: Obtiene/establece si la reflexión debe rotar con la forma.
- ReflectionEffect.Size: Obtiene/establece la posición final (a lo largo de la rampa de degradado alfa) del valor alfa final en unidades de porcentaje.
- ReflectionEffect.Transparency: Obtiene/establece el grado de transparencia inicial de la reflexión como un valor de 0.0 (opaco) a 1.0 (transparente).
- ReflectionEffect.Type: Obtiene/establece el efecto de reflexión preestablecido.

Aquí hay un escenario simple de uso de la propiedad Shape.Reflection.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Cómo trabajar con efectos de reflexión](/cells/es/java/working-with-the-reflection-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet containing a shape

//Alternatively create a new spreadsheet and add a shape

Workbook book = new Workbook("sample.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first shape from the collection

Shape shape = sheet.getShapes().get(0);

//Get the instance of ReflectionEffect from the Shape object

ReflectionEffect reflection = shape.getReflection();

//Set its Blur, Size, Transparency and Distance properties

reflection.setBlur(30);

reflection.setSize(90);

reflection.setTransparency(0.5);

reflection.setDistance(80);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **Soporte para Efectos de Sombra**
Aspose.Cells 16.10.0 ha expuesto la propiedad Shape.ShadowEffect junto con la clase ShadowEffect que, en conjunto, permite establecer el efecto de sombra en un objeto Shape. La clase ShadowEffect tiene las siguientes propiedades.

- ShadowEffect.Angle: Obtiene/establece el ángulo de iluminación que varía de 0 a 359.9 grados.
- ShadowEffect.Blur: Obtiene y establece el desenfoque de la sombra que varía de 0 a 100 puntos.
- ShadowEffect.Color: Obtiene/establece el color de la sombra.
- ShadowEffect.Distance: Obtiene/establece la distancia de la sombra que varía de 0 a 200 puntos.
- ShadowEffect.PresetType: Obtiene/establece el tipo de sombra preestablecido de la sombra.
- ShadowEffect.Size: Obtiene/establece el tamaño de la sombra que varía de 0 a 2.0. Será carente de sentido en caso de sombra interna.
- ShadowEffect.Transparency: Obtiene o establece el grado de transparencia de la sombra que va desde 0.0 (opaco) a 1.0 (transparente).

Aquí hay un escenario de uso simple de la propiedad mencionada anteriormente.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Trabajar con Efectos de Sombra](/cells/es/java/working-with-the-shadow-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet containing a shape

//Alternatively create a new spreadsheet and add a shape

Workbook book = new Workbook("sample.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first shape from the collection

Shape shape = sheet.getShapes().get(0);

//Get the instance of ShadowEffect from the Shape object

ShadowEffect shadow = shape.getShadowEffect();

//Set its Angle, Blur, Size, Transparency and Distance properties

shadow.setAngle(150);

shadow.setBlur(30);

shadow.setSize(90);

shadow.setTransparency(0.5);

shadow.setDistance(80);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **Soporte para Efectos de Resplandor**
Aspose.Cells 16.10.0 ha expuesto la propiedad Shape.Glow junto con la clase GlowEffect, que en conjunto permiten establecer el efecto de resplandor de un objeto Shape. La clase GlowEffect especifica un efecto de resplandor, en el que se agrega un contorno borroso de color fuera de los bordes del objeto usando las siguientes propiedades.

- GlowEffect.Size: Obtiene o establece el radio del resplandor en unidades de puntos.
- GlowEffect.Transparency: Obtiene o establece el grado de transparencia del efecto de resplandor que va desde 0.0 (opaco) a 1.0 (transparente).

Aquí hay un escenario de uso simple de la propiedad Shape.Glow.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Trabajar con el Efecto de Resplandor](/cells/es/java/working-with-the-glow-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet containing a shape

//Alternatively create a new spreadsheet and add a shape

Workbook book = new Workbook("sample.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first shape from the collection

Shape shape = sheet.getShapes().get(0);

//Get the instance of GlowEffect from the Shape object

GlowEffect glow = shape.getGlow();

//Set its Size & Transparency properties

glow.setSize(90);

glow.setTransparency(0.5);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **Soporte para Formato 3D**
Aspose.Cells 16.10.0 ha expuesto la propiedad Shape.ThreeDFormat junto con la clase ThreeDFormat, que juntas se pueden utilizar para controlar el formato 3D del objeto Shape. La clase ThreeDFormat representa el formato tridimensional de una forma y tiene las siguientes propiedades.

- ThreeDFormat.BottomBevelHeight: Obtiene o establece la altura del bisel inferior o qué tan lejos se aplica en la forma, en unidades de puntos.
- ThreeDFormat.BottomBevelType: Obtiene o establece el tipo de bisel inferior o qué tan lejos se aplica en la forma, en unidades de puntos.
- ThreeDFormat.BottomBevelWidth: Obtiene o establece el ancho del bisel inferior o qué tan lejos se aplica en la forma, en unidades de puntos.
- ThreeDFormat.ContourColor: Obtiene o establece el color de contorno de una forma.
- ThreeDFormat.ContourWidth: Obtiene o establece el ancho del contorno en la forma, en unidades de puntos.
- ThreeDFormat.ExtrusionColor: Obtiene el color de extrusión en una forma.
- ThreeDFormat.ExtrusionHeight: Obtiene o establece la altura de extrusión aplicada a la forma, en unidades de puntos.
- ThreeDFormat.LightAngle: Obtiene/establece el ángulo de las luces de extrusión.
- ThreeDFormat.Lighting: Obtiene/establece el tipo de configuración de luces.
- ThreeDFormat.LightingDirection: Obtiene/establece la dirección desde la que está orientada la configuración de luces en relación a la escena.
- ThreeDFormat.Material: Representa el material preestablecido que se combina con las propiedades de iluminación para dar el aspecto final de una forma.
- ThreeDFormat.Perspective: Obtiene/establece el ángulo desde el cual se puede ver un objeto ThreeDFormat.
- ThreeDFormat.PresetCameraType: Obtiene/establece la cámara preestablecida para la extrusión.
- ThreeDFormat.RotationX: Obtiene/establece la rotación de la forma extruida alrededor del eje X en grados.
- ThreeDFormat.RotationY: Obtiene/establece la rotación de la forma extruida alrededor del eje Y en grados.
- ThreeDFormat.RotationZ: Obtiene/establece la rotación de la forma extruida alrededor del eje Z en grados.
- ThreeDFormat.TopBevelHeight: Obtiene/establece la altura del bisel superior o la distancia hasta la cual se aplica en la forma, en puntos.
- ThreeDFormat.TopBevelType: Obtiene/establece el tipo de bisel superior o la distancia hasta la cual se aplica en la forma, en puntos.
- ThreeDFormat.TopBevelWidth: Obtiene/establece el ancho del bisel superior o la distancia hasta la cual se aplica en la forma, en puntos.
- ThreeDFormat.Z: Define la distancia desde el suelo para la forma 3D.

A continuación se muestra un escenario de uso sencillo de la propiedad Shape.ThreeDFormat.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Trabajar con el Formato 3D](/cells/es/java/working-with-the-threedformat-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet containing a shape

//Alternatively create a new spreadsheet and add a shape

Workbook book = new Workbook("sample.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first shape from the collection

Shape shape = sheet.getShapes().get(0);

//Get the instance of ThreeDFormat from the Shape object

ThreeDFormat threeD = shape.getThreeDFormat();

//Set its ContourWidth & ExtrusionHeight properties

threeD.setContourWidth(15);

threeD.setExtrusionHeight(30);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **Soporte para Estilos WordArt en el texto de una forma**
Aspose.Cells 16.10.0 ha expuesto los métodos FontSettingCollection.SetWordArtStyle y FontSetting.SetWordArtStyle para establecer el estilo predefinido de WordArt en el texto del objeto Shape.

Aquí hay un escenario de uso simple de los mencionados métodos.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Trabajar con los Estilos WordArt](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Create a TextBox with some text

int index = sheet.getTextBoxes().add(0, 0, 100, 700);

TextBox textBox = (TextBox)sheet.getShapes().get(index);

textBox.setText("Aspose File Format APIs");

textBox.getFont().setSize(44);

//Set preset WordArt style to the text of the shape

FontSetting fntSetting = (FontSetting)textBox.getCharacters().get(0);

fntSetting.setWordArtStyle(PresetWordArtStyle.WORD_ART_STYLE_15);

{{< /highlight >}}
### **Soporte para estilos integrados de WordArt**
Aspose.Cells 16.10.0 ha expuesto el método ShapeCollection.AddWordArt junto con la enumeración PresetWordArtStyle para brindar soporte para agregar objetos WordArt preestablecidos desde Excel 2007.

Aquí hay un escenario de uso simple del método ShapeCollection.AddWordArt.

{{% alert color="primary" %}} 

Consulte el artículo detallado en [Agregar WordArt con estilos integrados](/cells/es/java/add-word-art-text-with-built-in-styles/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access ShapeCollection of first worksheet

ShapeCollection shapes = sheet.getShapes();

//Add WordArt with built-in styles

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_1, "Aspose File Format APIs", 00, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_2, "Aspose File Format APIs", 10, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_3, "Aspose File Format APIs", 20, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_4, "Aspose File Format APIs", 30, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_5, "Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **Método XmlMapCollection.Add agregado**
Aspose.Cells ha expuesto el método XmlMapCollection.Add que permite agregar un mapa XML a una hoja de cálculo. Aquí hay un escenario de uso simple del método XmlMapCollection.Add.

{{% alert color="primary" %}} 

Consulte el artículo detallado en [Agregar mapa XML a hoja de cálculo](/cells/es/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **Método Cells.LinkToXmlMap agregado**
Aspose.Cells ha expuesto el método Cells.LinkToXmlMap para enlazar las celdas con los elementos del mapa XML. Aquí hay un escenario de uso simple del método Cells.LinkToXmlMap.

{{% alert color="primary" %}} 

Consulte el artículo detallado en [Enlazar celdas a elementos de mapa XML](/cells/es/java/link-cells-to-xml-map-elements/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook("sample.xlsx");

//Access the XML Map from the spreadsheet

XmlMap map = book.getWorksheets().getXmlMaps().get(0);

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Map FIELD1 and FIELD2 to cell A1 and B2

sheet.getCells().linkToXmlMap(map.getName(), 0, 0, "/root/row/FIELD1");

sheet.getCells().linkToXmlMap(map.getName(), 1, 1, "/root/row/FIELD2");

//Map FIELD4 and FIELD5 to cell C3 and D4

sheet.getCells().linkToXmlMap(map.getName(), 2, 2, "/root/row/FIELD4");

sheet.getCells().linkToXmlMap(map.getName(), 3, 3, "/root/row/FIELD5");

//Map FIELD7 and FIELD8 to cell E5 and F6

sheet.getCells().linkToXmlMap(map.getName(), 4, 4, "/root/row/FIELD7");

sheet.getCells().linkToXmlMap(map.getName(), 5, 5, "/root/row/FIELD8");

{{< /highlight >}}
### **Propiedad Formula de ListColumn agregada**
Aspose.Cells 16.10.0 ha expuesto la propiedad ListColumn.Formula para propagar automáticamente la fórmula a las filas recién insertadas.

Aquí hay un escenario de uso simple de la propiedad ListColumn.Formula.

{{% alert color="primary" %}} 

Consulte el artículo detallado en [Propagar automáticamente la fórmula en objeto de lista](/cells/es/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Add column headings in cell A1 and B1

sheet.getCells().get(0, 0).putValue("Column A");

sheet.getCells().get(0, 1).putValue("Column B");

//Add list object, set its name and style

ListObject listObject = sheet.getListObjects().get(sheet.getListObjects().add(0, 0, 1, sheet.getCells().getMaxColumn(), true));

listObject.setTableStyleType(TableStyleType.TABLE_STYLE_MEDIUM_14);

listObject.setDisplayName("Table");

//Set the formula of second column so that it could automatically propagate to new rows while entering data

listObject.getListColumns().get(1).setFormula("=[Column A] + 1");

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
