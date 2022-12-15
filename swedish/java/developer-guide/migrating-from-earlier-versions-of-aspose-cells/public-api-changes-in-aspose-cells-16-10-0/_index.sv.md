---
title: Offentlig API Ändringar i Aspose.Cells 16.10.0
type: docs
weight: 350
url: /sv/java/public-api-changes-in-aspose-cells-16-10-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 9.0.0 till 16.10.0 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Stöd för reflektionseffekter**
Aspose.Cells 16.10.0 har exponerat klassen ReflectionEffect tillsammans med egenskapen Shape.Reflection för att kontrollera reflektionseffekterna för ett Shape-objekt. Klassen ReflectionEffect har följande egenskaper.

- ReflectionEffect.Blur: Hämtar/ställer in oskärpa radien i punktenhet.
- ReflectionEffect.Direction: Hämtar/ställer in riktningen för alfagradientrampen i förhållande till själva formen.
- ReflectionEffect.Distance: Får/ställer in avståndet för reflektionen i punktenheter.
- ReflectionEffect.FadeDirection: Hämtar/ställer in riktningen för att förskjuta reflektionen.
- ReflectionEffect.RotWithShape: Får/ställer in om reflektionen ska rotera med formen.
- ReflectionEffect.Size: Hämtar/ställer in slutpositionen (längs alfagradientrampen) för slutalfavärdet i procentenhet .
- ReflectionEffect.Transparency: Hämtar/ställer in graden av startreflektionstransparens som ett värde från 0,0 (opak) till 1,0 (clear).
- ReflectionEffect.Type: Hämtar/ställer in den förinställda reflektionseffekten.

Här är ett enkelt användningsscenario för Shape.Reflection-egenskapen.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Arbeta med reflektionseffekter](/cells/sv/java/working-with-the-reflection-effect-of-shape-or-chart/)

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
### **Stöd för skuggeffekter**
Aspose.Cells 16.10.0 har exponerat egenskapen Shape.ShadowEffect tillsammans med klassen ShadowEffect som tillsammans tillåter att ställa in skuggeffekten på ett Shape-objekt. Klassen ShadowEffect har följande egenskaper.

- ShadowEffect.Angle: Hämtar/ställer in belysningsvinkeln från 0 till 359,9 grader.
- ShadowEffect.Blur: Får och ställer in oskärpan för skuggan från 0 till 100 punkter.
- ShadowEffect.Color: Hämtar/ställer in skuggans färg.
- ShadowEffect.Distance: Hämtar/ställer in avståndet för skuggan från 0 till 200 punkter.
- ShadowEffect.PresetType: Hämtar/ställer in den förinställda skuggtypen för skuggan.
- ShadowEffect.Size: Hämtar/ställer in storleken på skuggan från 0 till 2,0. Det kommer att vara meningslöst i händelse av inre skugga.
- ShadowEffect.Transparency: Hämtar/ställer in graden av genomskinlighet för skuggan från 0,0 (opak) till 1,0 (klar).

Här är ett enkelt användningsscenario för ovannämnda egendom.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Arbeta med skuggeffekter](/cells/sv/java/working-with-the-shadow-effect-of-shape-or-chart/)

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
### **Stöd för Glow Effects**
Aspose.Cells 16.10.0 har exponerat egenskapen Shape.Glow tillsammans med klassen GlowEffect som tillsammans tillåter att ställa in glödeffekten för ett Shape-objekt. Klassen GlowEffect anger en glödeffekt, där en suddig färgkontur läggs till utanför objektets kanter med hjälp av följande egenskaper.

- GlowEffect.Size: Hämtar/ställer in strålens radie i poängenhet.
- GlowEffect.Transparency: Hämtar/ställer in graden av transparens för glödeffekten från 0,0 (opak) till 1,0 (klar).

Här är ett enkelt användningsscenario för Shape.Glow-egenskapen.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Arbeta med Glow Effect](/cells/sv/java/working-with-the-glow-effect-of-shape-or-chart/)

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
### **Stöd för 3D-format**
Aspose.Cells 16.10.0 har exponerat egenskapen Shape.ThreeDFormat tillsammans med klassen ThreeDFormat som tillsammans kan användas för att styra 3D-formateringen av Shape-objektet. Klassen ThreeDFormat representerar en forms tredimensionella formatering och har följande egenskaper.

- ThreeDFormat.BottomBevelHeight: Får/ställer in höjden på den nedre avfasningen eller hur långt in i formen den appliceras, i poängenhet.
- ThreeDFormat.BottomBevelType: Hämtar/ställer in typen av den nedre avfasningen eller hur långt in i formen den appliceras, i poängenhet.
- ThreeDFormat.BottomBevelWidth: Hämtar/ställer in bredden på den nedre avfasningen eller hur långt in i formen den appliceras, i poängenhet.
- ThreeDFormat.ContourColor: Hämtar/ställer in konturfärgen för en form.
- ThreeDFormat.ContourWidth: Hämtar/ställer in konturbredden på formen, i poängenhet.
- ThreeDFormat.ExtrusionColor: Får extruderingsfärgen på en form.
- ThreeDFormat.ExtrusionHeight: Hämtar/ställer in extruderingshöjden för den applicerade formen, i poängenhet.
- ThreeDFormat.LightAngle: Hämtar/ställer in vinkeln på extruderingsljusen.
- ThreeDFormat.Lighting: Får/ställer in typ av ljusrigg.
- ThreeDFormat.LightingDirection: Får/ställer in riktningen från vilken ljusriggen är orienterad i förhållande till scenen.
- ThreeDFormat.Material: Representerar det förinställda materialet som kombineras med ljusegenskaperna för att ge det slutliga utseendet och känslan av en form.
- ThreeDFormat.Perspective: Hämtar/ställer in vinkeln vid vilken ett ThreeDFormat-objekt kan ses.
- ThreeDFormat.PresetCameraType: Hämtar/ställer in den förinställda extruderingskameran.
- ThreeDFormat.RotationX: Hämtar/ställer in rotationen av den extruderade formen runt X-axeln i grader.
- ThreeDFormat.RotationY: Hämtar/ställer in rotationen av den extruderade formen runt Y-axeln i graderenhet.
- ThreeDFormat.RotationZ: Hämtar/ställer in rotationen av den extruderade formen runt Z-axeln i grader.
- ThreeDFormat.TopBevelHeight: Får/ställer in höjden på den övre avfasningen eller hur långt in i formen den appliceras, i poängenhet.
- ThreeDFormat.TopBevelType: Hämtar/ställer in typen av den övre avfasningen eller hur långt in i formen den appliceras, i poängenhet.
- ThreeDFormat.TopBevelWidth: Hämtar/ställer in bredden på den övre avfasningen eller hur långt in i formen den appliceras, i poängenhet.
- ThreeDFormat.Z: Definierar avståndet från marken för 3D-formen.

Följande är det enkla användningsscenariot för egenskapen Shape.ThreeDFormat.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Arbeta med 3D-formatering](/cells/sv/java/working-with-the-threedformat-of-shape-or-chart/)

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
### **Stöd för WordArt-stilar i Shapes text**
Aspose.Cells 16.10.0 har exponerat metoderna FontSettingCollection.SetWordArtStyle och FontSetting.SetWordArtStyle för att ställa in den förinställda WordArt-stilen till texten i Shape-objektet.

Här är ett enkelt användningsscenario för ovannämnda metoder.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Arbeta med WordArt-stilar](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/)

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
### **Stöd för WordArt inbyggda stilar**
Aspose.Cells 16.10.0 har exponerat metoden ShapeCollection.AddWordArt tillsammans med PresetWordArtStyle-uppräkning för att ge stöd för att lägga till förinställda WordArt-objekt sedan Excel 2007.

Här är ett enkelt användningsscenario för metoden ShapeCollection.AddWordArt.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Lägg till WordArt med inbyggda stilar](/cells/sv/java/add-word-art-text-with-built-in-styles/)

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
### **Lade till XmlMapCollection.Add Method**
Aspose.Cells har avslöjat metoden XmlMapCollection.Add som gör det möjligt att lägga till Xml Map till ett kalkylblad. Här är ett enkelt användningsscenario för XmlMapCollection.Add-metoden.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Lägg till XML-karta till kalkylblad](/cells/sv/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **Lade till Cells.LinkToXmlMap Method**
Aspose.Cells har nu exponerat metoden Cells.LinkToXmlMap för att länka cellerna med XML-kartelementen. Här är ett enkelt användningsscenario för Cells.LinkToXmlMap-metoden.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Länka Cells till XML Map Elements](/cells/sv/java/link-cells-to-xml-map-elements/)

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
### **Tillagd ListColumn.Formula Property**
Aspose.Cells 16.10.0 har exponerat egenskapen ListColumn.Formula för att automatiskt sprida formeln till nyinfogade rader.

Här är ett enkelt användningsscenario för ListColumn.Formula-egenskapen.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Sprid automatiskt formel i listobjekt](/cells/sv/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

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
