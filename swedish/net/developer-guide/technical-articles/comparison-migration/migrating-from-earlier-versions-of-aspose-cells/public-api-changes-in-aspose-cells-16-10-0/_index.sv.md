---
title: Offentlig API Ändringar i Aspose.Cells 16.10.0
type: docs
weight: 340
url: /sv/net/public-api-changes-in-aspose-cells-16-10-0/
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

 Kolla den detaljerade artikeln om[Arbeta med reflektionseffekter](/cells/sv/net/working-with-the-reflection-effect-of-shape-or-chart/)

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

 Kolla den detaljerade artikeln om[Arbeta med skuggeffekter](/cells/sv/net/working-with-the-shadow-effect-of-shape-or-chart/)

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


### **Stöd för Glow Effects**
Aspose.Cells 16.10.0 har exponerat egenskapen Shape.Glow tillsammans med klassen GlowEffect som tillsammans tillåter att ställa in glödeffekten för ett Shape-objekt. Klassen GlowEffect anger en glödeffekt, där en suddig färgkontur läggs till utanför objektets kanter med hjälp av följande egenskaper.

- GlowEffect.Size: Hämtar/ställer in strålens radie i poängenhet.
- GlowEffect.Transparency: Hämtar/ställer in graden av transparens för glödeffekten från 0,0 (opak) till 1,0 (klar).

Här är ett enkelt användningsscenario för Shape.Glow-egenskapen.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Arbeta med Glow Effect](/cells/sv/net/working-with-the-glow-effect-of-shape-or-chart/)

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
- ThreeDFormat.RotationX: Hämtar/ställer in rotationen av den extruderade formen runt X-axeln i graderenhet.
- ThreeDFormat.RotationY: Hämtar/ställer in rotationen av den extruderade formen runt Y-axeln i graderenhet.
- ThreeDFormat.RotationZ: Hämtar/ställer in rotationen av den extruderade formen runt Z-axeln i grader.
- ThreeDFormat.TopBevelHeight: Får/ställer in höjden på den övre avfasningen eller hur långt in i formen den appliceras, i poängenhet.
- ThreeDFormat.TopBevelType: Hämtar/ställer in typen av den övre avfasningen eller hur långt in i formen den appliceras, i poängenhet.
- ThreeDFormat.TopBevelWidth: Hämtar/ställer in bredden på den övre avfasningen eller hur långt in i formen den appliceras, i poängenhet.
- ThreeDFormat.Z: Definierar avståndet från marken för 3D-formen.

Följande är det enkla användningsscenariot för egenskapen Shape.ThreeDFormat.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Arbeta med 3D-formatering](/cells/sv/net/working-with-the-threedformat-of-shape-or-chart/)

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


### **Stöd för WordArt-stilar i Shapes text**
Aspose.Cells 16.10.0 har exponerat metoderna FontSettingCollection.SetWordArtStyle och FontSetting.SetWordArtStyle för att ställa in den förinställda WordArt-stilen till texten i Shape-objektet.

Här är ett enkelt användningsscenario för ovannämnda metoder.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Arbeta med WordArt-stilar](/cells/sv/net/set-preset-wordart-style-to-the-text-of-the-shape/)

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


### **Stöd för WordArt inbyggda stilar**
Aspose.Cells 16.10.0 har exponerat metoden ShapeCollection.AddWordArt tillsammans med PresetWordArtStyle-uppräkning för att ge stöd för att lägga till förinställda WordArt-objekt sedan Excel 2007.

Här är ett enkelt användningsscenario för metoden ShapeCollection.AddWordArt.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Lägg till WordArt med inbyggda stilar](/cells/sv/net/add-word-art-text-with-built-in-styles/)

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


### **Lade till XmlMapCollection.Add Method**
Aspose.Cells har avslöjat metoden XmlMapCollection.Add som gör det möjligt att lägga till Xml Map till ett kalkylblad. Här är ett enkelt användningsscenario för XmlMapCollection.Add-metoden.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Lägg till XML-karta till kalkylblad](/cells/sv/net/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Workbook();

// Add xml map from the sample.xml to the workbook

book.Worksheets.XmlMaps.Add("sample.xml");

{{< /highlight >}}


### **Lade till Cells.LinkToXmlMap Method**
Aspose.Cells har nu exponerat metoden Cells.LinkToXmlMap för att länka cellerna med XML-kartelementen.

Här är ett enkelt användningsscenario för Cells.LinkToXmlMap-metoden.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Länka Cells till XML Map Elements](/cells/sv/net/link-cells-to-xml-map-elements/)

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


### **Tillagd ListColumn.Formula Property**
Aspose.Cells 16.10.0 har exponerat egenskapen ListColumn.Formula för att automatiskt sprida formeln till nyinfogade rader.

Här är ett enkelt användningsscenario för ListColumn.Formula-egenskapen.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Sprid automatiskt formel i listobjekt](/cells/sv/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

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


### **Stöd för beräkning av anpassade funktioner med GridWeb**
Aspose.Cells.GridWeb 16.10.0 har exponerat egenskapen GridWeb.CustomCalculationEngine tillsammans med klassen GridAbstractCalculationEngine som tillsammans tillåter att definiera och beräkna anpassade funktioner från GridWeb-komponenten.

Här är ett enkelt användningsscenario för ovannämnda API:er.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Beräkna anpassade funktioner med GridWeb](/cells/sv/net/calculate-custom-functions-in-gridweb/)

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
