---
title: Ändringar i offentligt API i Aspose.Cells 16.10.0
type: docs
weight: 350
url: /sv/java/public-api-changes-in-aspose-cells-16-10-0/
---

{{% alert color="primary" %}} 

Dokumentet beskriver ändringarna i Aspose.Cells API från version 9.0.0 till 16.10.0 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser, osv., utan även en beskrivning av eventuella ändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Stöd för reflektionseffekter**
Aspose.Cells 16.10.0 har exponerat ReflectionEffect-klassen tillsammans med Shape.Reflection-egenskapen för att styra reflektionseffekterna på en Shape-objekt. ReflectionEffect-klassen har följande egenskaper.

- ReflectionEffect.Blur: Hämtar/ställer in oskärpan i enheten punkter.
- ReflectionEffect.Direction: Hämtar/ställer in riktningen för alfavärdets gradientram p.v. formen själv.
- ReflectionEffect.Distance: Hämtar/ställer in avståndet i enheten punkter.
- ReflectionEffect.FadeDirection: Hämtar/ställer in riktningen för att förskjuta reflektionen.
- ReflectionEffect.RotWithShape: Hämtar/ställer in om reflektionen ska rotera med formen.
- ReflectionEffect.Size: Hämtar/ställer in slutpositionen (längs alfavärdets gradientram) för slutalfavärdet i enheten procent .
- ReflectionEffect.Transparency: Hämtar/ställer in graden av startreflektionens transparens som ett värde från 0,0 (täckande) till 1,0 (klar).
- ReflectionEffect.Type: Hämtar/ställer in förinställd reflektionseffekt.

Här är ett enkelt användningsscenario för Shape.Reflection-egenskapen.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Arbeta med reflektionseffekter](/cells/sv/java/working-with-the-reflection-effect-of-shape-or-chart/)

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
### **Stöd för skuggaeffekter**
Aspose.Cells 16.10.0 har exponerat egenskapen Shape.ShadowEffect tillsammans med ShadowEffect-klassen, vilket tillsammans möjliggör att sätta skuggaeffekten på en Shape-objekt. ShadowEffect-klassen har följande egenskaper.

- ShadowEffect.Angle: Hämtar/ställer in ljusvinkeln som sträcker sig från 0 till 359,9 grader.
- ShadowEffect.Blur: Hämtar och ställer oskärpan för skuggan som sträcker sig från 0 till 100 punkter.
- ShadowEffect.Color: Hämtar/ställer in skuggans färg.
- ShadowEffect.Distance: Hämtar/ställer avståndet för skuggan som sträcker sig från 0 till 200 punkter.
- ShadowEffect.PresetType: Hämtar/ställer in förinställd skuggtyp för skuggan.
- ShadowEffect.Size: Hämtar/ställer in storleken på skuggan som sträcker sig från 0 till 2,0. Det blir meningslöst i fall av inre skugga.
- ShadowEffect.Transparency: Hämtar/ställer graden av transparens för skuggan som sträcker sig från 0,0 (täckande) till 1,0 (klar).

Här är ett enkelt användningsscenario för ovanstående egenskap.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Arbeta med skugga effekter](/cells/sv/java/working-with-the-shadow-effect-of-shape-or-chart/)

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
### **Stöd för glödeffekter**
Aspose.Cells 16.10.0 har exponerat egenskapen Shape.Glow tillsammans med klassen GlowEffect som tillsammans möjliggör att ställa in glödeffekten för ett Shape-objekt. Klassen GlowEffect specifierar en glödeffekt, där en färgoskarp kontur läggs till utanför objektets kanter med hjälp av följande egenskaper.

- GlowEffect.Size: Hämtar/ställer in radien för glöden i punktenheter.
- GlowEffect.Transparency: Hämtar/ställer in graden av genomskinlighet för glödeffekten som sträcker sig från 0,0 (opak) till 1,0 (genomskinlig).

Här är ett enkelt användningscenario för egenskapen Shape.Glow.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Arbeta med glödande effekt](/cells/sv/java/working-with-the-glow-effect-of-shape-or-chart/)

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
### **Stöd för 3D-formatering**
Aspose.Cells 16.10.0 har exponerat egenskapen Shape.ThreeDFormat tillsammans med klassen ThreeDFormat som tillsammans kan användas för att kontrollera 3D-formateringen av ett Shape-objekt. Klassen ThreeDFormat representerar en shapes tredimensionella formatering och har följande egenskaper.

- ThreeDFormat.BottomBevelHeight: Hämtar/ställer in höjden på bottenfasen eller hur långt in i formen den tillämpas, i punktenheter.
- ThreeDFormat.BottomBevelType: Hämtar/ställer in typen av bottenfasen eller hur långt in i formen den tillämpas, i punktenheter.
- ThreeDFormat.BottomBevelWidth: Hämtar/ställer in bredden på bottenfasen eller hur långt in i formen den tillämpas, i punktenheter.
- ThreeDFormat.ContourColor: Hämtar/ställer in konturfärgen på en form.
- ThreeDFormat.ContourWidth: Hämtar/ställer in konturbredden på formen, i punktenheter.
- ThreeDFormat.ExtrusionColor: Hämtar extrusionsfärgen på en form.
- ThreeDFormat.ExtrusionHeight: Hämtar/ställer in extrusionshöjden som tillämpas på formen, i punktenheter.
- ThreeDFormat.LightAngle: Hämtar/ställer in vinkeln för extrusionsljus.
- ThreeDFormat.Lighting: Hämtar/ställer in typ av ljuskonstruktion.
- ThreeDFormat.LightingDirection: Hämtar/ställer in riktningen från vilken ljuskonstruktionen är riktad i förhållande till scenen.
- ThreeDFormat.Material: Representerar det förinställda materialet som kombineras med ljusegenskaperna för att ge slutlig utseende och känsla av en form.
- ThreeDFormat.Perspective: Hämtar/ställer in vinkeln vid vilken ett ThreeDFormat-objekt kan ses.
- ThreeDFormat.PresetCameraType: Hämtar/ställer in förinställt kamera för extrusionen.
- ThreeDFormat.RotationX: Hämtar/ställer in rotationen av den extruderade formen runt X-axeln i gradenheter.
- ThreeDFormat.RotationY: Hämtar/ställer in rotationen av den extruderade formen runt Y-axeln i gradenheter.
- ThreeDFormat.RotationZ: Hämtar/ställer in rotationen av den extruderade formen runt Z-axeln i gradenheter.
- ThreeDFormat.TopBevelHeight: Hämtar/ställer in höjden på toppfasen eller hur långt in i formen den tillämpas, i punktenheter.
- ThreeDFormat.TopBevelType: Hämtar/ställer in typen av toppfasen eller hur långt in i formen den tillämpas, i punktenheter.
- ThreeDFormat.TopBevelWidth: Hämtar/ställer in bredden på toppfasen eller hur långt in i formen den tillämpas, i punktenheter.
- ThreeDFormat.Z: Definierar avståndet från marken för 3D-formen.

Följande är det enkla användningsscenario för egenskapen Shape.ThreeDFormat.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Arbeta med 3D-format](/cells/sv/java/working-with-the-threedformat-of-shape-or-chart/)

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
### **Stöd för WordArt-stilar i formens text**
Aspose.Cells 16.10.0 har exponerat FontSettingCollection.SetWordArtStyle- & FontSetting.SetWordArtStyle-metoderna för att ställa in den förinställda WordArt-stilen på formens textobjekt.

Här finns ett enkelt användningsscenario för ovanstående metoder.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Arbeta med WordArt-stilar](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/)

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
### **Stöd för inbyggda WordArt-stilar**
Aspose.Cells 16.10.0 har exponerat ShapeCollection.AddWordArt-metoden tillsammans med PresetWordArtStyle-uppräkningen för att tillhandahålla stöd för att lägga till förinställda WordArt-objekt sedan Excel 2007.

Här finns ett enkelt användningsscenario för ShapeCollection.AddWordArt-metoden.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Lägga till WordArt med inbyggda stilar](/cells/sv/java/add-word-art-text-with-built-in-styles/)

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
### **Tillagd XmlMapCollection.Add-metod**
Aspose.Cells har exponerat XmlMapCollection.Add-metoden som gör det möjligt att lägga till Xml-map till ett kalkylblad. Här finns ett enkelt användningsscenario för XmlMapCollection.Add-metoden.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Lägga till XML-mapning till kalkylbladet](/cells/sv/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **Tillagd Cells.LinkToXmlMap-metod**
Aspose.Cells har nu exponerat Cells.LinkToXmlMap-metoden för att länka cellerna med XML-kartelementen. Här är ett enkelt användningsscenario för Cells.LinkToXmlMap-metoden.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Länka celler till XML-mapelement](/cells/sv/java/link-cells-to-xml-map-elements/)

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
### **Tillagd ListColumn.Formula-egenskap**
Aspose.Cells 16.10.0 har exponerat ListColumn.Formula-egenskapen för att automatiskt sprida formeln till nyligen infogade rader.

Här finns ett enkelt användningsscenario för ListColumn.Formula-egenskapen.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Automatiskt sprida formel i listobjekt](/cells/sv/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

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
