---
title: Público API Cambios en Aspose.Cells 16.10.0
type: docs
weight: 340
url: /es/net/public-api-changes-in-aspose-cells-16-10-0/
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

 Consulte el artículo detallado sobre[Trabajar con efectos de reflexión](/cells/es/net/working-with-the-reflection-effect-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet containing a shape

// Alternatively create a new spreadsheet and add a shape

var book = new Workbook("sample.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first shape from the collection

var shape = sheet.Shapes[0];

// Get the instance of ReflectionEffect from the Shape object

var reflection = shape.Reflection;

// Set its Blur, Size, Transparency and Distance properties

reflection.Blur = 30;

reflection.Size = 90;

reflection.Transparency = 0.5;

reflection.Distance = 80;

// Save the result in XLSX format

book.Save("output.xlsx");

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

 Consulte el artículo detallado sobre[Trabajar con efectos de sombra](/cells/es/net/working-with-the-shadow-effect-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet containing a shape

// Alternatively create a new spreadsheet and add a shape

var book = new Workbook("sample.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first shape from the collection

var shape = sheet.Shapes[0];

// Get the instance of ShadowEffect from the Shape object

var shadow = shape.ShadowEffect;

// Set its Angle, Blur, Size, Transparency and Distance properties

shadow.Angle = 150;

shadow.Blur = 30;

shadow.Size = 90;

shadow.Transparency = 0.5;

shadow.Distance = 80;

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **Compatibilidad con efectos de brillo**
Aspose.Cells 16.10.0 ha expuesto la propiedad Shape.Glow junto con la clase GlowEffect que, en conjunto, permite establecer el efecto de brillo de un objeto Shape. La clase GlowEffect especifica un efecto de brillo, en el que se agrega un contorno borroso de color fuera de los bordes del objeto usando las siguientes propiedades.

- GlowEffect.Size: Obtiene/establece el radio del resplandor en unidades de puntos.
- GlowEffect.Transparency: Obtiene/establece el grado de transparencia del efecto de brillo que va de 0,0 (opaco) a 1,0 (transparente).

Aquí hay un escenario de uso simple de la propiedad Shape.Glow.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Trabajando con Efecto Resplandor](/cells/es/net/working-with-the-glow-effect-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet containing a shape

// Alternatively create a new spreadsheet and add a shape

var book = new Workbook("sample.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first shape from the collection

var shape = sheet.Shapes[0];

// Get the instance of GlowEffect from the Shape object

var glow = shape.Glow;

// Set its Size & Transparency properties

glow.Size = 90;

glow.Transparency = 0.5;

// Save the result in XLSX format

book.Save("output.xlsx");

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

 Consulte el artículo detallado sobre[Trabajar con formato 3D](/cells/es/net/working-with-the-threedformat-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet containing a shape

// Alternatively create a new spreadsheet and add a shape

var book = new Workbook("sample.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first shape from the collection

var shape = sheet.Shapes[0];

// Get the instance of ThreeDFormat from the Shape object

var threeD = shape.ThreeDFormat;

// Set its ContourWidth & ExtrusionHeight properties

threeD.ContourWidth = 15;

threeD.ExtrusionHeight = 30;

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **Compatibilidad con estilos de WordArt en el texto de Shape**
Aspose.Cells 16.10.0 ha expuesto los métodos FontSettingCollection.SetWordArtStyle y FontSetting.SetWordArtStyle para establecer el estilo predeterminado de WordArt en el texto del objeto Shape.

Aquí hay un escenario de uso simple de los métodos antes mencionados.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Trabajar con estilos de WordArt](/cells/es/net/set-preset-wordart-style-to-the-text-of-the-shape/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Create workbook object

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Create a TextBox with some text

var textBox = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 700);

textBox.Text = "Aspose File Format APIs";

textBox.Font.Size = 44;

// Set preset WordArt style to the text of the shape

FontSetting fntSetting = textBox.GetCharacters()[0]as FontSetting;

fntSetting.SetWordArtStyle(PresetWordArtStyle.WordArtStyle3);

{{< /highlight >}}


### **Compatibilidad con estilos integrados de WordArt**
Aspose.Cells 16.10.0 ha expuesto el método ShapeCollection.AddWordArt junto con la enumeración PresetWordArtStyle para brindar soporte para agregar objetos de WordArt preestablecidos desde Excel 2007.

Aquí hay un escenario de uso simple del método ShapeCollection.AddWordArt.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Agregue WordArt con estilos incorporados](/cells/es/net/add-word-art-text-with-built-in-styles/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access ShapeCollection of first worksheet

var shapes = sheet.Shapes;

// Add WordArt with built-in styles

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle1, "Aspose File Format APIs", 00, 0, 0, 0, 100, 800);

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle2, "Aspose File Format APIs", 10, 0, 0, 0, 100, 800);

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle3, "Aspose File Format APIs", 20, 0, 0, 0, 100, 800);

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle4, "Aspose File Format APIs", 30, 0, 0, 0, 100, 800);

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle5, "Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **Se agregó el método XmlMapCollection.Add**
Aspose.Cells ha expuesto el método XmlMapCollection.Add que permite agregar Xml Map a una hoja de cálculo. Este es un escenario de uso simple del método XmlMapCollection.Add.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Agregar mapa XML a la hoja de cálculo](/cells/es/net/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Workbook();

// Add xml map from the sample.xml to the workbook

book.Worksheets.XmlMaps.Add("sample.xml");

{{< /highlight >}}


### **Se agregó Cells. Método LinkToXmlMap**
Aspose.Cells ahora ha expuesto el método Cells.LinkToXmlMap para vincular las celdas con los elementos del mapa XML.

Este es un escenario de uso simple del método Cells.LinkToXmlMap.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Enlace Cells a elementos del mapa XML](/cells/es/net/link-cells-to-xml-map-elements/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook("sample.xlsx");

// Access the XML Map from the spreadsheet

var map = book.Worksheets.XmlMaps[0];

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Map FIELD1 and FIELD2 to cell A1 and B2

sheet.Cells.LinkToXmlMap(map.Name, 0, 0, "/root/row/FIELD1");

sheet.Cells.LinkToXmlMap(map.Name, 1, 1, "/root/row/FIELD2");

// Map FIELD4 and FIELD5 to cell C3 and D4

sheet.Cells.LinkToXmlMap(map.Name, 2, 2, "/root/row/FIELD4");

sheet.Cells.LinkToXmlMap(map.Name, 3, 3, "/root/row/FIELD5");

// Map FIELD7 and FIELD8 to cell E5 and F6

sheet.Cells.LinkToXmlMap(map.Name, 4, 4, "/root/row/FIELD7");

sheet.Cells.LinkToXmlMap(map.Name, 5, 5, "/root/row/FIELD8");

{{< /highlight >}}


### **Se agregó la propiedad ListColumn.Formula**
Aspose.Cells 16.10.0 ha expuesto la propiedad ListColumn.Formula para propagar automáticamente la fórmula a las filas recién insertadas.

Aquí hay un escenario de uso simple de la propiedad ListColumn.Formula.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Propaga automáticamente la fórmula en el objeto de la lista](/cells/es/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Add column headings in cell A1 and B1

sheet.Cells[0, 0].PutValue("Column A");

sheet.Cells[0, 1].PutValue("Column B");

// Add list object, set its name and style

var listObject = sheet.ListObjects[sheet.ListObjects.Add(0, 0, 1, sheet.Cells.MaxColumn, true)];

listObject.TableStyleType = TableStyleType.TableStyleMedium2;

listObject.DisplayName = "Table";

// Set the formula of second column so that it could automatically propagate to new rows while entering data

listObject.ListColumns[1].Formula = "=[Column A]+ 1";

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **Soporte para calcular funciones personalizadas con GridWeb**
Aspose.Cells.GridWeb 16.10.0 ha expuesto la propiedad GridWeb.CustomCalculationEngine junto con la clase GridAbstractCalculationEngine que, en conjunto, permite definir y calcular las funciones personalizadas desde el componente GridWeb.

Aquí hay un escenario de uso simple de las API antes mencionadas.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Cálculo de funciones personalizadas con GridWeb](/cells/es/net/calculate-custom-functions-in-gridweb/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 private class GridWebCustomCalculationEngine : GridAbstractCalculationEngine

{

    public override void Calculate(GridCalculationData data)

    {

        //  Calculate MYTESTFUNC() with your own logic.

        //For example, you can multiply MYTESTFUNC() parameter with 2 so

        // MYTESTFUNC(3.0) will return 6

        // MYTESTFUNC(4.0) will return 8

        // MYTESTFUNC(5.0) will return 10

        if ("MYTESTFUNC".Equals(data.FunctionName.ToUpper()))

        {

            data.CalculatedValue = (decimal)(2.0 * (double)data.GetParamValue(0));

        }

    }

}


if (Page.IsPostBack == false && GridWeb1.IsPostBack == false)

{

    // Assign your own custom calculation engine to GridWeb

    GridWeb1.CustomCalculationEngine = new GridWebCustomCalculationEngine();

    // Access the active worksheet and add your custom function in cell B3

    GridWorksheet sheet = GridWeb1.ActiveSheet;

    GridCell cell = sheet.Cells["B3"];

    cell.Formula = "=MYTESTFUNC(9.0)";

    // Calculate the GridWeb formula

    GridWeb1.CalculateFormula();

}

{{< /highlight >}}
