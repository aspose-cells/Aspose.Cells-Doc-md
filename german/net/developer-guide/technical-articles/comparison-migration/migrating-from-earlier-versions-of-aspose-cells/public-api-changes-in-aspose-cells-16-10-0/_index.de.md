---
title: Öffentliche API Änderungen in Aspose.Cells 16.10.0
type: docs
weight: 340
url: /de/net/public-api-changes-in-aspose-cells-16-10-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells API von Version 9.0.0 bis 16.10.0, die für Modul-/Anwendungs-Entwickler interessant sein können. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte & entfernte Klassen usw., sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Unterstützung für Reflexionseffekte**
Aspose.Cells 16.10.0 hat die Klasse ReflectionEffect zusammen mit der Eigenschaft Shape.Reflection freigegeben, um die Reflexionseffekte eines Shape-Objekts zu steuern. Die ReflectionEffect-Klasse hat die folgenden Eigenschaften.

- ReflectionEffect.Blur: Ruft den Unschärferadius in Einheit von Punkten ab oder legt diesen fest.
- ReflectionEffect.Direction: Ruft die Richtung des Alphagradients relativ zur Form selbst ab oder legt diese fest.
- ReflectionEffect.Distance: Ruft die Entfernung der Reflexion in Einheit von Punkten ab oder legt diese fest.
- ReflectionEffect.FadeDirection: Ruft die Richtung zum Verschieben der Reflexion ab oder legt diese fest.
- ReflectionEffect.RotWithShape: Ruft ab oder legt fest, ob sich die Reflexion mit der Form drehen soll.
- ReflectionEffect.Size: Ruft die Endposition (entlang des Alphagradients) des Endalphawertes in Einheit von Prozenten ab oder legt diese fest.
- ReflectionEffect.Transparency: Ruft den Grad der Startreflexionstransparenz als Wert von 0,0 (undurchsichtig) bis 1,0 (klar) ab oder legt diesen fest.
- ReflectionEffect.Type: Ruft den voreingestellten Reflexionseffekt ab oder legt diesen fest.

Hier ist ein einfaches Anwendungsszenario der Eigenschaft Shape.Reflection.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zu [Arbeiten mit Reflexeffekten](/cells/de/net/working-with-the-reflection-effect-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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
Aspose.Cells 16.10.0 hat die Eigenschaft Shape.ShadowEffect zusammen mit der Klasse ShadowEffect freigegeben, die es ermöglicht, den Schatteneffekt auf ein Shape-Objekt zu setzen. Die ShadowEffect-Klasse hat die folgenden Eigenschaften.

- ShadowEffect.Angle: Ruft den Beleuchtungswinkel von 0 bis 359,9 Grad ab oder legt diesen fest.
- ShadowEffect.Blur: Ruft den Unschärfeeffekt des Schattens von 0 bis 100 Punkten ab oder legt diesen fest.
- ShadowEffect.Color: Ruft die Farbe des Schattens ab oder legt diese fest.
- ShadowEffect.Distance: Ruft die Entfernung des Schattens von 0 bis 200 Punkten ab oder legt diese fest.
- ShadowEffect.PresetType: Ruft den voreingestellten Schattentyp des Schattens ab oder legt diesen fest.
- ShadowEffect.Size: Ruft die Größe des Schattens von 0 bis 2,0 ab oder legt diese fest. Im Falle eines inneren Schattens ist dies bedeutungslos.
- ShadowEffect.Transparency: Ruft den Grad der Transparenz des Schattens ab/setzt ihn, der von 0,0 (undurchsichtig) bis 1,0 (klar) reicht.

Hier ist ein einfaches Anwendungsszenario der oben genannten Eigenschaft.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zu [Arbeiten mit Schatteneffekten](/cells/de/net/working-with-the-shadow-effect-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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
Aspose.Cells 16.10.0 hat die Shape.Glow-Eigenschaft zusammen mit der GlowEffect-Klasse freigegeben, was es zusammen ermöglicht, den Leuchteffekt eines Shape-Objekts zu setzen. Die GlowEffect-Klasse spezifiziert einen Leuchteffekt, bei dem eine Farbkante außerhalb der Kanten des Objekts mit den folgenden Eigenschaften hinzugefügt wird.

- GlowEffect.Size: Ruft den Radius des Leuchteffekts in Einheiten von Punkten ab/setzt ihn.
- GlowEffect.Transparency: Ruft den Grad der Transparenz des Leuchteffekts ab/setzt ihn, der von 0,0 (undurchsichtig) bis 1,0 (klar) reicht.

Hier ist ein einfaches Anwendungsszenario der Shape.Glow-Eigenschaft.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zu [Arbeiten mit Glow-Effekt](/cells/de/net/working-with-the-glow-effect-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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
Aspose.Cells 16.10.0 hat die Shape.ThreeDFormat-Eigenschaft zusammen mit der ThreeDFormat-Klasse freigegeben, die gemeinsam zur Steuerung der 3D-Formatierung des Shape-Objekts verwendet werden kann. Die ThreeDFormat-Klasse stellt die dreidimensionale Formatierung einer Form dar und hat die folgenden Eigenschaften.

- ThreeDFormat.BottomBevelHeight: Ruft die Höhe der unteren Fase oder wie weit sie in die Form hinein angewendet wird, in Einheiten von Punkten ab/setzt sie.
- ThreeDFormat.BottomBevelType: Ruft den Typ der unteren Fase oder wie weit er in die Form hinein angewendet wird, in Einheiten von Punkten ab/setzt ihn.
- ThreeDFormat.BottomBevelWidth: Ruft die Breite der unteren Fase oder wie weit sie in die Form hinein angewendet wird, in Einheiten von Punkten ab/setzt sie.
- ThreeDFormat.ContourColor: Ruft die Umrandungsfarbe einer Form ab/setzt sie.
- ThreeDFormat.ContourWidth: Ruft die Umrandungsbreite auf der Form ab/setzt sie, in Einheiten von Punkten.
- ThreeDFormat.ExtrusionColor: Ruft die Extrusionsfarbe auf einer Form ab.
- ThreeDFormat.ExtrusionHeight: Ruft die Höhe der Extrusion ab/setzt sie, die auf die Form angewendet wird, in Einheiten von Punkten.
- ThreeDFormat.LightAngle: Ruft den Winkel der Extrusionslichter ab/setzt ihn.
- ThreeDFormat.Lighting: Ruft den Typ des Licht-Rigs ab/setzt ihn.
- ThreeDFormat.LightingDirection: Ermöglicht das Festlegen der Richtung, aus der das Lichtgitter in Bezug auf die Szene orientiert ist.
- ThreeDFormat.Material: Stellt das voreingestellte Material dar, das mit den Beleuchtungseigenschaften kombiniert wird, um das endgültige Erscheinungsbild einer Form zu erhalten.
- ThreeDFormat.Perspective: Ermöglicht das Festlegen des Winkels, unter dem ein ThreeDFormat-Objekt betrachtet werden kann.
- ThreeDFormat.PresetCameraType: Ermöglicht das Festlegen der voreingestellten Kamera für die Extrusion.
- ThreeDFormat.RotationX: Ermöglicht das Festlegen der Rotation der extrudierten Form um die X-Achse in Grad.
- ThreeDFormat.RotationY: Ermöglicht das Festlegen der Rotation der extrudierten Form um die Y-Achse in Grad.
- ThreeDFormat.RotationZ: Ermöglicht das Festlegen der Rotation der extrudierten Form um die Z-Achse in Grad.
- ThreeDFormat.TopBevelHeight: Ermöglicht das Festlegen der Höhe des oberen Schrägschnitts oder wie weit sie in die Form angewendet wird, in Einheiten von Punkten.
- ThreeDFormat.TopBevelType: Ermöglicht das Festlegen des Typs des oberen Schrägschnitts oder wie weit er in die Form angewendet wird, in Einheiten von Punkten.
- ThreeDFormat.TopBevelWidth: Ermöglicht das Festlegen der Breite des oberen Schrägschnitts oder wie weit er in die Form angewendet wird, in Einheiten von Punkten.
- ThreeDFormat.Z: Definiert die Entfernung vom Boden für die 3D-Form.

Folgendes ist das einfache Anwendungsszenario der Eigenschaft Shape.ThreeDFormat.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zu [Arbeiten mit 3D-Formatierung](/cells/de/net/working-with-the-threedformat-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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


### **Unterstützung für WordArt-Stile im Text der Form**
Aspose.Cells 16.10.0 hat die Methoden FontSettingCollection.SetWordArtStyle & FontSetting.SetWordArtStyle freigegeben, um den voreingestellten WordArt-Stil für den Text des Shape-Objekts festzulegen.

Hier ist ein einfaches Anwendungsszenario für die oben genannten Methoden.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zu [Arbeiten mit WordArt-Stilen](/cells/de/net/set-preset-wordart-style-to-the-text-of-the-shape/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create workbook object

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Create a TextBox with some text

var textBox = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 700);

textBox.Text = "Aspose File Format APIs";

textBox.Font.Size = 44;

// Set preset WordArt style to the text of the shape

FontSetting fntSetting = textBox.GetCharacters()[0] as FontSetting;

fntSetting.SetWordArtStyle(PresetWordArtStyle.WordArtStyle3);

{{< /highlight >}}


### **Unterstützung für integrierte WordArt-Stile**
Aspose.Cells 16.10.0 hat die Methode ShapeCollection.AddWordArt zusammen mit der Aufzählung PresetWordArtStyle freigegeben, um die Unterstützung zum Hinzufügen voreingestellter WordArt-Objekte seit Excel 2007 bereitzustellen.

Hier ist ein einfaches Anwendungsszenario der Methode ShapeCollection.AddWordArt.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zu [Hinzufügen von WordArt mit integrierten Stilen](/cells/de/net/add-word-art-text-with-built-in-styles/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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


### **Hinzugefügter XmlMapCollection.Add Methode**
Aspose.Cells hat die XmlMapCollection.Add Methode freigegeben, um eine XML-Mappe zu einer Tabellenkalkulation hinzuzufügen. Hier ist ein einfaches Anwendungsbeispiel der XmlMapCollection.Add Methode.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zu [Xml-Map zur Tabellenkalkulation hinzufügen](/cells/de/net/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Add xml map from the sample.xml to the workbook

book.Worksheets.XmlMaps.Add("sample.xml");

{{< /highlight >}}


### **Hinzugefügte Cells.LinkToXmlMap Methode**
Aspose.Cells hat nun die Cells.LinkToXmlMap-Methode freigegeben, um die Zellen mit den XML-Map-Elementen zu verknüpfen.

Hier finden Sie ein einfaches Anwendungsszenario der Cells.LinkToXmlMap-Methode.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zu [Verknüpfung von Zellen mit XML-Map-Elementen](/cells/de/net/link-cells-to-xml-map-elements/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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


### **Hinzugefügte ListColumn.Formula Eigenschaft**
Aspose.Cells 16.10.0 hat die ListColumn.Formula Eigenschaft freigegeben, um die Formel automatisch auf neu eingefügte Zeilen zu propagieren.

Hier ist ein einfaches Anwendungsbeispiel der ListColumn.Formula Eigenschaft.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zu [Automatische Propagierung der Formel in List Object](/cells/de/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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

listObject.ListColumns[1].Formula = "=[Column A] + 1";

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **Unterstützung für das Berechnen benutzerdefinierter Funktionen mit GridWeb**
Aspose.Cells.GridWeb 16.10.0 hat die GridWeb.CustomCalculationEngine-Eigenschaft zusammen mit der GridAbstractCalculationEngine-Klasse freigelegt, um benutzerdefinierte Funktionen innerhalb des GridWeb-Komponenten zu definieren und zu berechnen.

Hier ist ein einfaches Beispiel für die oben genannten APIs.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zu [Berechnen benutzerdefinierter Funktionen mit GridWeb](/cells/de/net/calculate-custom-functions-in-gridweb/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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
