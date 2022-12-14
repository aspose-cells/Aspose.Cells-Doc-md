---
title: Öffentlich API Änderungen in Aspose.Cells 16.10.0
type: docs
weight: 340
url: /de/net/public-api-changes-in-aspose-cells-16-10-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 9.0.0 bis 16.10.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Unterstützung für Reflexionseffekte**
Aspose.Cells 16.10.0 hat die ReflectionEffect-Klasse zusammen mit der Shape.Reflection-Eigenschaft verfügbar gemacht, um die Reflexionseffekte eines Shape-Objekts zu steuern. Die ReflectionEffect-Klasse hat die folgenden Eigenschaften.

- ReflectionEffect.Blur: Ermittelt/setzt den Unschärferadius in Punkteinheiten.
- ReflectionEffect.Direction: Ermittelt/legt die Richtung der Alpha-Gradientenrampe relativ zur Form selbst fest.
- ReflectionEffect.Distance: Ermittelt/setzt die Entfernung der Reflexion in Punkteinheiten.
- ReflectionEffect.FadeDirection: Ermittelt/legt die Richtung fest, um die Reflexion auszugleichen.
- ReflectionEffect.RotWithShape: Ermittelt/setzt, ob sich die Reflexion mit der Form drehen soll.
- ReflectionEffect.Size: Ermittelt/setzt die Endposition (entlang der Alpha-Gradientenrampe) des Alpha-Endwerts in Prozenteinheit.
- ReflectionEffect.Transparency: Liest/legt den Grad der anfänglichen Reflexionstransparenz als Wert von 0,0 (deckend) bis 1,0 (klar) fest.
- ReflectionEffect.Type: Holt/setzt den voreingestellten Reflexionseffekt.

Hier ist ein einfaches Verwendungsszenario der Shape.Reflection-Eigenschaft.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Arbeiten mit Reflexionseffekten](/cells/de/net/working-with-the-reflection-effect-of-shape-or-chart/)

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


### **Unterstützung für Schatteneffekte**
Aspose.Cells 16.10.0 hat die Shape.ShadowEffect-Eigenschaft zusammen mit der ShadowEffect-Klasse verfügbar gemacht, die es zusammen ermöglicht, den Schatteneffekt für ein Shape-Objekt festzulegen. Die ShadowEffect-Klasse hat die folgenden Eigenschaften.

- ShadowEffect.Angle: Ermittelt/legt den Beleuchtungswinkel im Bereich von 0 bis 359,9 Grad fest.
- ShadowEffect.Blur: Ruft die Unschärfe des Schattens im Bereich von 0 bis 100 Punkten ab und legt sie fest.
- ShadowEffect.Color: Holt/setzt die Farbe des Schattens.
- ShadowEffect.Distance: Ermittelt/setzt die Entfernung des Schattens im Bereich von 0 bis 200 Punkten.
- ShadowEffect.PresetType: Holt/setzt den voreingestellten Schattentyp des Schattens.
- ShadowEffect.Size: Holt/setzt die Größe des Schattens im Bereich von 0 bis 2,0. Im Falle eines inneren Schattens wird es bedeutungslos sein.
- ShadowEffect.Transparency: Liest/setzt den Grad der Transparenz des Schattens im Bereich von 0,0 (deckend) bis 1,0 (klar).

Hier ist ein einfaches Nutzungsszenario der oben genannten Eigenschaft.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Arbeiten mit Schatteneffekten](/cells/de/net/working-with-the-shadow-effect-of-shape-or-chart/)

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


### **Unterstützung für Leuchteffekte**
Aspose.Cells 16.10.0 hat die Shape.Glow-Eigenschaft zusammen mit der GlowEffect-Klasse verfügbar gemacht, die es zusammen ermöglicht, den Glüheffekt eines Shape-Objekts festzulegen. Die GlowEffect-Klasse gibt einen Glüheffekt an, bei dem mithilfe der folgenden Eigenschaften ein farblich unscharfer Umriss außerhalb der Kanten des Objekts hinzugefügt wird.

- GlowEffect.Size: Ermittelt/setzt den Radius des Glühens in Punkteinheiten.
- GlowEffect.Transparency: Ermittelt/legt den Transparenzgrad des Glow-Effekts im Bereich von 0,0 (undurchsichtig) bis 1,0 (klar) fest.

Hier ist ein einfaches Anwendungsszenario der Shape.Glow-Eigenschaft.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Arbeiten mit Glow-Effekt](/cells/de/net/working-with-the-glow-effect-of-shape-or-chart/)

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


### **Unterstützung für 3D-Format**
Aspose.Cells 16.10.0 hat die Shape.ThreeDFormat-Eigenschaft zusammen mit der ThreeDFormat-Klasse verfügbar gemacht, die zusammen verwendet werden können, um die 3D-Formatierung des Shape-Objekts zu steuern. Die ThreeDFormat-Klasse stellt die dreidimensionale Formatierung einer Form dar und verfügt über die folgenden Eigenschaften.

- ThreeDFormat.BottomBevelHeight: Ermittelt/legt die Höhe der unteren Abschrägung oder wie weit in die Form hinein sie angewendet wird, in der Einheit von Points.
- ThreeDFormat.BottomBevelType: Erhält/legt den Typ der unteren Abschrägung oder wie weit in die Form hinein sie angewendet wird, in der Einheit von Points.
- ThreeDFormat.BottomBevelWidth: Ermittelt/legt die Breite der unteren Abschrägung oder wie weit in die Form hinein sie angewendet wird, in der Einheit von Points.
- ThreeDFormat.ContourColor: Ermittelt/setzt die Konturfarbe einer Form.
- ThreeDFormat.ContourWidth: Ermittelt/legt die Konturbreite der Form in der Einheit von Points fest.
- ThreeDFormat.ExtrusionColor: Ruft die Extrusionsfarbe einer Form ab.
- ThreeDFormat.ExtrusionHeight: Ermittelt/legt die Extrusionshöhe der auf die Form angewendeten in der Einheit von Points fest.
- ThreeDFormat.LightAngle: Ermittelt/legt den Winkel der Extrusionslichter fest.
- ThreeDFormat.Lighting: Holt/legt den Typ des Lichtrigs fest.
- ThreeDFormat.LightingDirection: Ermittelt/setzt die Richtung, aus der die Lichtanlage in Bezug auf die Szene ausgerichtet ist.
- ThreeDFormat.Material: Stellt das voreingestellte Material dar, das mit den Beleuchtungseigenschaften kombiniert wird, um einer Form das endgültige Erscheinungsbild zu verleihen.
- ThreeDFormat.Perspective: Ermittelt/legt den Winkel fest, in dem ein ThreeDFormat-Objekt angezeigt werden kann.
- ThreeDFormat.PresetCameraType: Ruft die voreingestellte Extrusionskamera ab/legt sie fest.
- ThreeDFormat.RotationX: Ermittelt/legt die Rotation der extrudierten Form um die X-Achse in Gradeinheiten fest.
- ThreeDFormat.RotationY: Ermittelt/legt die Rotation der extrudierten Form um die Y-Achse in Gradeinheiten fest.
- ThreeDFormat.RotationZ: Liest/legt die Rotation der extrudierten Form um die Z-Achse in Gradeinheit fest.
- ThreeDFormat.TopBevelHeight: Erhält/legt die Höhe der oberen Abschrägung oder wie weit in die Form hinein sie angewendet wird, in der Einheit von Points.
- ThreeDFormat.TopBevelType: Erhält/legt den Typ der oberen Abschrägung oder wie weit in die Form hinein sie angewendet wird, in der Einheit von Points.
- ThreeDFormat.TopBevelWidth: Ermittelt/legt die Breite der oberen Abschrägung oder wie weit in die Form hinein sie angewendet wird, in der Einheit von Points.
- ThreeDFormat.Z: Definiert den Abstand vom Boden für die 3D-Form.

Im Folgenden ist das einfache Verwendungsszenario der Shape.ThreeDFormat-Eigenschaft dargestellt.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Arbeiten mit 3D-Formatierung](/cells/de/net/working-with-the-threedformat-of-shape-or-chart/)

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


### **Unterstützung für WordArt-Stile im Text von Shape**
Aspose.Cells 16.10.0 hat die Methoden FontSettingCollection.SetWordArtStyle und FontSetting.SetWordArtStyle verfügbar gemacht, um den voreingestellten WordArt-Stil auf den Text des Shape-Objekts festzulegen.

Hier ist ein einfaches Anwendungsszenario der oben genannten Methoden.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Arbeiten mit WordArt-Stilen](/cells/de/net/set-preset-wordart-style-to-the-text-of-the-shape/)

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


### **Unterstützung für integrierte WordArt-Stile**
Aspose.Cells 16.10.0 hat die ShapeCollection.AddWordArt-Methode zusammen mit der PresetWordArtStyle-Enumeration verfügbar gemacht, um die Unterstützung für das Hinzufügen voreingestellter WordArt-Objekte seit Excel 2007 bereitzustellen.

Hier ist ein einfaches Verwendungsszenario der ShapeCollection.AddWordArt-Methode.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Fügen Sie WordArt mit integrierten Stilen hinzu](/cells/de/net/add-word-art-text-with-built-in-styles/)

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


### **XmlMapCollection.Add-Methode hinzugefügt**
Aspose.Cells hat die XmlMapCollection.Add-Methode verfügbar gemacht, die es ermöglicht, einer Tabelle eine XML-Karte hinzuzufügen. Hier ist ein einfaches Verwendungsszenario der XmlMapCollection.Add-Methode.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[XML-Zuordnung zur Tabelle hinzufügen](/cells/de/net/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Workbook();

// Add xml map from the sample.xml to the workbook

book.Worksheets.XmlMaps.Add("sample.xml");

{{< /highlight >}}


### **Cells.LinkToXmlMap-Methode hinzugefügt**
Aspose.Cells hat nun die Methode Cells.LinkToXmlMap exponiert, um die Zellen mit den XML-Map-Elementen zu verknüpfen.

Hier ist ein einfaches Nutzungsszenario der Methode Cells.LinkToXmlMap.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Link Cells zu XML-Kartenelementen](/cells/de/net/link-cells-to-xml-map-elements/)

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


### **ListColumn.Formula-Eigenschaft hinzugefügt**
Aspose.Cells 16.10.0 hat die ListColumn.Formula-Eigenschaft verfügbar gemacht, um die Formel automatisch an neu eingefügte Zeilen weiterzugeben.

Hier ist ein einfaches Verwendungsszenario der ListColumn.Formula-Eigenschaft.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Formel automatisch im Listenobjekt weitergeben](/cells/de/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

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


### **Unterstützung für die Berechnung benutzerdefinierter Funktionen mit GridWeb**
Aspose.Cells.GridWeb 16.10.0 hat die GridWeb.CustomCalculationEngine-Eigenschaft zusammen mit der GridAbstractCalculationEngine-Klasse verfügbar gemacht, die es insgesamt ermöglicht, die benutzerdefinierten Funktionen innerhalb der GridWeb-Komponente zu definieren und zu berechnen.

Hier ist ein einfaches Nutzungsszenario der oben genannten APIs.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Berechnen von benutzerdefinierten Funktionen mit GridWeb](/cells/de/net/calculate-custom-functions-in-gridweb/)

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
