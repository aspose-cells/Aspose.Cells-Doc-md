---
title: Öffentlich API Änderungen in Aspose.Cells 16.10.0
type: docs
weight: 350
url: /de/java/public-api-changes-in-aspose-cells-16-10-0/
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

 Überprüfen Sie den ausführlichen Artikel auf[Arbeiten mit Reflexionseffekten](/cells/de/java/working-with-the-reflection-effect-of-shape-or-chart/)

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

 Überprüfen Sie den ausführlichen Artikel auf[Arbeiten mit Schatteneffekten](/cells/de/java/working-with-the-shadow-effect-of-shape-or-chart/)

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
### **Unterstützung für Leuchteffekte**
Aspose.Cells 16.10.0 hat die Shape.Glow-Eigenschaft zusammen mit der GlowEffect-Klasse verfügbar gemacht, die es zusammen ermöglicht, den Glüheffekt eines Shape-Objekts festzulegen. Die GlowEffect-Klasse gibt einen Glüheffekt an, bei dem mithilfe der folgenden Eigenschaften ein farblich unscharfer Umriss außerhalb der Kanten des Objekts hinzugefügt wird.

- GlowEffect.Size: Ermittelt/setzt den Radius des Glühens in Punkteinheiten.
- GlowEffect.Transparency: Ermittelt/legt den Transparenzgrad des Glow-Effekts im Bereich von 0,0 (undurchsichtig) bis 1,0 (klar) fest.

Hier ist ein einfaches Anwendungsszenario der Shape.Glow-Eigenschaft.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Arbeiten mit Glow-Effekt](/cells/de/java/working-with-the-glow-effect-of-shape-or-chart/)

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

 Überprüfen Sie den ausführlichen Artikel auf[Arbeiten mit 3D-Formatierung](/cells/de/java/working-with-the-threedformat-of-shape-or-chart/)

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
### **Unterstützung für WordArt-Stile im Text von Shape**
Aspose.Cells 16.10.0 hat die Methoden FontSettingCollection.SetWordArtStyle und FontSetting.SetWordArtStyle verfügbar gemacht, um den voreingestellten WordArt-Stil auf den Text des Shape-Objekts festzulegen.

Hier ist ein einfaches Anwendungsszenario der oben genannten Methoden.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Arbeiten mit WordArt-Stilen](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/)

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
### **Unterstützung für integrierte WordArt-Stile**
Aspose.Cells 16.10.0 hat die ShapeCollection.AddWordArt-Methode zusammen mit der PresetWordArtStyle-Enumeration verfügbar gemacht, um die Unterstützung für das Hinzufügen voreingestellter WordArt-Objekte seit Excel 2007 bereitzustellen.

Hier ist ein einfaches Verwendungsszenario der ShapeCollection.AddWordArt-Methode.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Fügen Sie WordArt mit integrierten Stilen hinzu](/cells/de/java/add-word-art-text-with-built-in-styles/)

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
### **XmlMapCollection.Add-Methode hinzugefügt**
Aspose.Cells hat die XmlMapCollection.Add-Methode verfügbar gemacht, die es ermöglicht, einer Tabelle eine XML-Karte hinzuzufügen. Hier ist ein einfaches Verwendungsszenario der XmlMapCollection.Add-Methode.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[XML-Zuordnung zur Tabelle hinzufügen](/cells/de/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **Cells.LinkToXmlMap-Methode hinzugefügt**
Aspose.Cells hat nun die Methode Cells.LinkToXmlMap exponiert, um die Zellen mit den XML-Map-Elementen zu verknüpfen. Hier ist ein einfaches Nutzungsszenario der Methode Cells.LinkToXmlMap.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Link Cells zu XML-Kartenelementen](/cells/de/java/link-cells-to-xml-map-elements/)

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
### **ListColumn.Formula-Eigenschaft hinzugefügt**
Aspose.Cells 16.10.0 hat die ListColumn.Formula-Eigenschaft verfügbar gemacht, um die Formel automatisch an neu eingefügte Zeilen weiterzugeben.

Hier ist ein einfaches Verwendungsszenario der ListColumn.Formula-Eigenschaft.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Formel automatisch im Listenobjekt weitergeben](/cells/de/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

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
