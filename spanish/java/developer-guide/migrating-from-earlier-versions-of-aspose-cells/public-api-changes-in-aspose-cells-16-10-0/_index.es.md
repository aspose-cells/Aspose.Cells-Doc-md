---
title: Público API Cambios en Aspose.Cells 16.10.0
type: docs
weight: 350
url: /es/java/public-api-changes-in-aspose-cells-16-10-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 9.0.0 a la 16.10.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Compatibilidad con efectos de reflexión**
Aspose.Cells 16.10.0 ha expuesto la clase ReflectionEffect junto con la propiedad Shape.Reflection para controlar los efectos de reflexión de un objeto Shape. La clase ReflectionEffect tiene las siguientes propiedades.

- ReflectionEffect.Blur: Obtiene/establece el radio de desenfoque en unidades de puntos.
- ReflectionEffect.Direction: Obtiene/establece la dirección de la rampa de degradado alfa en relación con la forma en sí.
- ReflectionEffect.Distance: Obtiene/establece la distancia del reflejo en unidades de puntos.
- ReflectionEffect.FadeDirection: Obtiene/establece la dirección para compensar el reflejo.
- ReflectionEffect.RotWithShape: Obtiene/establece si el reflejo debe rotar con la forma.
- ReflectionEffect.Size: Obtiene/establece la posición final (a lo largo de la rampa de gradiente alfa) del valor alfa final en unidades de porcentaje.
- ReflectionEffect.Transparency: Obtiene/establece el grado de transparencia de reflexión inicial como un valor de 0,0 (opaco) a 1,0 (transparente).
- ReflectionEffect.Type: Obtiene/establece el efecto de reflejo predeterminado.

Aquí hay un escenario de uso simple de la propiedad Shape.Reflection.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Trabajar con efectos de reflexión](/cells/es/java/working-with-the-reflection-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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
### **Soporte para efectos de sombra**
Aspose.Cells 16.10.0 ha expuesto la propiedad Shape.ShadowEffect junto con la clase ShadowEffect que, en conjunto, permite establecer el efecto de sombra en un objeto Shape. La clase ShadowEffect tiene las siguientes propiedades.

- ShadowEffect.Angle: Obtiene/establece el ángulo de iluminación que va de 0 a 359,9 grados.
- ShadowEffect.Blur: Obtiene y establece el desenfoque de la sombra que va de 0 a 100 puntos.
- ShadowEffect.Color: Obtiene/establece el color de la sombra.
- ShadowEffect.Distance: Obtiene/establece la distancia de la sombra que va de 0 a 200 puntos.
- ShadowEffect.PresetType: Obtiene/establece el tipo de sombra preestablecido de la sombra.
- ShadowEffect.Size: Obtiene/establece el tamaño de la sombra que va de 0 a 2,0. No tendrá sentido en caso de sombra interior.
- ShadowEffect.Transparency: Obtiene/establece el grado de transparencia de la sombra que va de 0,0 (opaco) a 1,0 (claro).

Aquí hay un escenario de uso simple de la propiedad antes mencionada.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Trabajar con efectos de sombra](/cells/es/java/working-with-the-shadow-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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
### **Compatibilidad con efectos de brillo**
Aspose.Cells 16.10.0 ha expuesto la propiedad Shape.Glow junto con la clase GlowEffect que, en conjunto, permite establecer el efecto de brillo de un objeto Shape. La clase GlowEffect especifica un efecto de brillo, en el que se agrega un contorno borroso de color fuera de los bordes del objeto usando las siguientes propiedades.

- GlowEffect.Size: Obtiene/establece el radio del resplandor en unidades de puntos.
- GlowEffect.Transparency: Obtiene/establece el grado de transparencia del efecto de brillo que va de 0,0 (opaco) a 1,0 (transparente).

Aquí hay un escenario de uso simple de la propiedad Shape.Glow.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Trabajando con Efecto Resplandor](/cells/es/java/working-with-the-glow-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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
### **Soporte para formato 3D**
Aspose.Cells 16.10.0 ha expuesto la propiedad Shape.ThreeDFormat junto con la clase ThreeDFormat que juntas se pueden usar para controlar el formato 3D del objeto Shape. La clase ThreeDFormat representa el formato tridimensional de una forma y tiene las siguientes propiedades.

- ThreeDFormat.BottomBevelHeight: Obtiene/establece la altura del bisel inferior o qué tan lejos se aplica en la forma, en unidades de Puntos.
- ThreeDFormat.BottomBevelType: Obtiene/establece el tipo de bisel inferior o hasta qué punto se aplica en la forma, en unidades de Puntos.
- ThreeDFormat.BottomBevelWidth: Obtiene/establece el ancho del bisel inferior o cuánto se aplica en la forma, en unidades de Puntos.
- ThreeDFormat.ContourColor: Obtiene/establece el color del contorno de una forma.
- ThreeDFormat.ContourWidth: Obtiene/establece el ancho del contorno de la forma, en unidades de Puntos.
- ThreeDFormat.ExtrusionColor: Obtiene el color de extrusión en una forma.
- ThreeDFormat.ExtrusionHeight: Obtiene/establece la altura de extrusión del aplicado a la forma, en unidades de Puntos.
- ThreeDFormat.LightAngle: Obtiene/establece el ángulo de las luces de extrusión.
- ThreeDFormat.Lighting: Obtiene/establece el tipo de plataforma de iluminación.
- ThreeDFormat.LightingDirection: Obtiene/establece la dirección desde la que se orienta el equipo de iluminación en relación con la escena.
- ThreeDFormat.Material: representa el material preestablecido que se combina con las propiedades de iluminación para dar la apariencia final de una forma.
- ThreeDFormat.Perspective: Obtiene/establece el ángulo en el que se puede ver un objeto ThreeDFormat.
- ThreeDFormat.PresetCameraType: Obtiene/establece la cámara preestablecida de extrusión.
- ThreeDFormat.RotationX: Obtiene/establece la rotación de la forma extruida alrededor del eje X en unidades de Grados.
- ThreeDFormat.RotationY: Obtiene/establece la rotación de la forma extruida alrededor del eje Y en unidades de Grados.
- ThreeDFormat.RotationZ: Obtiene/establece la rotación de la forma extruida alrededor del eje Z en unidades de Grados.
- ThreeDFormat.TopBevelHeight: Obtiene/establece la altura del bisel superior o qué tan lejos se aplica en la forma, en unidades de Puntos.
- ThreeDFormat.TopBevelType: Obtiene/establece el tipo de bisel superior o hasta qué punto se aplica en la forma, en unidades de Puntos.
- ThreeDFormat.TopBevelWidth: Obtiene/establece el ancho del bisel superior o cuánto se aplica en la forma, en unidades de Puntos.
- ThreeDFormat.Z: Define la distancia desde el suelo para la forma 3D.

El siguiente es el escenario de uso simple de la propiedad Shape.ThreeDFormat.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Trabajar con formato 3D](/cells/es/java/working-with-the-threedformat-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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
### **Compatibilidad con estilos de WordArt en el texto de Shape**
Aspose.Cells 16.10.0 ha expuesto los métodos FontSettingCollection.SetWordArtStyle y FontSetting.SetWordArtStyle para establecer el estilo predeterminado de WordArt en el texto del objeto Shape.

Aquí hay un escenario de uso simple de los métodos antes mencionados.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Trabajar con estilos de WordArt](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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
### **Compatibilidad con estilos integrados de WordArt**
Aspose.Cells 16.10.0 ha expuesto el método ShapeCollection.AddWordArt junto con la enumeración PresetWordArtStyle para brindar soporte para agregar objetos de WordArt preestablecidos desde Excel 2007.

Aquí hay un escenario de uso simple del método ShapeCollection.AddWordArt.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Agregue WordArt con estilos incorporados](/cells/es/java/add-word-art-text-with-built-in-styles/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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
### **Se agregó el método XmlMapCollection.Add**
Aspose.Cells ha expuesto el método XmlMapCollection.Add que permite agregar Xml Map a una hoja de cálculo. Este es un escenario de uso simple del método XmlMapCollection.Add.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Agregar mapa XML a la hoja de cálculo](/cells/es/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **Se agregó Cells. Método LinkToXmlMap**
Aspose.Cells ahora ha expuesto el método Cells.LinkToXmlMap para vincular las celdas con los elementos del mapa XML. Aquí hay un escenario de uso simple del método Cells.LinkToXmlMap.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Enlace Cells a elementos del mapa XML](/cells/es/java/link-cells-to-xml-map-elements/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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
### **Se agregó la propiedad ListColumn.Formula**
Aspose.Cells 16.10.0 ha expuesto la propiedad ListColumn.Formula para propagar automáticamente la fórmula a las filas recién insertadas.

Aquí hay un escenario de uso simple de la propiedad ListColumn.Formula.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Propaga automáticamente la fórmula en el objeto de la lista](/cells/es/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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

listObject.getListColumns().get(1).setFormula("=[Column A]+ 1");

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
