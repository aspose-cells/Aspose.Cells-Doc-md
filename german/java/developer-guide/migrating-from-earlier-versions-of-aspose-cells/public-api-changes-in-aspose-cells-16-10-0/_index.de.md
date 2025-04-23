---
title: Öffentliche API Änderungen in Aspose.Cells 16.10.0
type: docs
weight: 350
url: /de/java/public-api-changes-in-aspose-cells-16-10-0/
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

Weitere Informationen finden Sie im ausführlichen Artikel zu [Arbeiten mit Reflexionseffekten](/cells/de/java/working-with-the-reflection-effect-of-shape-or-chart/)

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

Überprüfen Sie den detaillierten Artikel zu [Arbeiten mit Schatten-Effekten](/cells/de/java/working-with-the-shadow-effect-of-shape-or-chart/)

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
### **Unterstützung für Leuchteffekte**
Aspose.Cells 16.10.0 hat die Shape.Glow-Eigenschaft zusammen mit der GlowEffect-Klasse freigegeben, was es zusammen ermöglicht, den Leuchteffekt eines Shape-Objekts zu setzen. Die GlowEffect-Klasse spezifiziert einen Leuchteffekt, bei dem eine Farbkante außerhalb der Kanten des Objekts mit den folgenden Eigenschaften hinzugefügt wird.

- GlowEffect.Size: Ruft den Radius des Leuchteffekts in Einheiten von Punkten ab/setzt ihn.
- GlowEffect.Transparency: Ruft den Grad der Transparenz des Leuchteffekts ab/setzt ihn, der von 0,0 (undurchsichtig) bis 1,0 (klar) reicht.

Hier ist ein einfaches Anwendungsszenario der Shape.Glow-Eigenschaft.

{{% alert color="primary" %}} 

Überprüfen Sie den detaillierten Artikel zu [Arbeiten mit Glanzeffekt](/cells/de/java/working-with-the-glow-effect-of-shape-or-chart/)

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

Überprüfen Sie den ausführlichen Artikel zu [Arbeiten mit 3D-Formatierung](/cells/de/java/working-with-the-threedformat-of-shape-or-chart/)

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
### **Unterstützung für WordArt-Stile im Text der Form**
Aspose.Cells 16.10.0 hat die Methoden FontSettingCollection.SetWordArtStyle & FontSetting.SetWordArtStyle freigegeben, um den voreingestellten WordArt-Stil für den Text des Shape-Objekts festzulegen.

Hier ist ein einfaches Anwendungsszenario für die oben genannten Methoden.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zu [Arbeiten mit WordArt-Stilen](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/)

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
### **Unterstützung für integrierte WordArt-Stile**
Aspose.Cells 16.10.0 hat die Methode ShapeCollection.AddWordArt zusammen mit der Aufzählung PresetWordArtStyle freigegeben, um die Unterstützung zum Hinzufügen voreingestellter WordArt-Objekte seit Excel 2007 bereitzustellen.

Hier ist ein einfaches Anwendungsszenario der Methode ShapeCollection.AddWordArt.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zu [WordArt mit integrierten Stilen hinzufügen](/cells/de/java/wordart-mit-integrierten-stilen-hinzufügen/)

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
### **Hinzugefügter XmlMapCollection.Add Methode**
Aspose.Cells hat die XmlMapCollection.Add Methode freigegeben, um eine XML-Mappe zu einer Tabellenkalkulation hinzuzufügen. Hier ist ein einfaches Anwendungsbeispiel der XmlMapCollection.Add Methode.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zu [Hinzufügen einer XML-Mappe zur Tabellenkalkulation](/cells/de/java/hinzufügen-einer-xml-mappe-in-die-arbeitsmappe-mit-der-xmlmapcollection-add-methode/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **Hinzugefügte Cells.LinkToXmlMap Methode**
Aspose.Cells hat nun die Cells.LinkToXmlMap Methode freigegeben, um die Zellen mit den XML-Mappelementen zu verknüpfen. Hier ist ein einfaches Anwendungsbeispiel der Cells.LinkToXmlMap Methode.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zu [Zellen mit XML-Mappelementen verknüpfen](/cells/de/java/zellen-mit-xml-mappelementen-verknüpfen/)

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
### **Hinzugefügte ListColumn.Formula Eigenschaft**
Aspose.Cells 16.10.0 hat die ListColumn.Formula Eigenschaft freigegeben, um die Formel automatisch auf neu eingefügte Zeilen zu propagieren.

Hier ist ein einfaches Anwendungsbeispiel der ListColumn.Formula Eigenschaft.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zum [Automatischen Propagieren der Formel in einer Listenobjekt](/cells/de/java/formel-in-tabelle-oder-listenobjekt-automatisch-propagieren-während-das-eingeben-von-daten-in-neuen-zeilen/)

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
