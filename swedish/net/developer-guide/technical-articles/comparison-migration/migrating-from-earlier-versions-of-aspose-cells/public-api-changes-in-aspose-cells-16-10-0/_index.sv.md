---
title: Ändringar i offentligt API i Aspose.Cells 16.10.0
type: docs
weight: 340
url: /sv/net/public-api-changes-in-aspose-cells-16-10-0/
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

Kolla in den detaljerade artikeln om [Arbete med reflektionseffekter](/cells/sv/net/arbete-med-formens-eller-diagrammets-reflektionseffekt/)

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

Kolla in den detaljerade artikeln om [Arbetet med skugga effekter](/cells/sv/net/arbete-med-formens-eller-diagrammets-skugga-effekt/)

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


### **Stöd för glödeffekter**
Aspose.Cells 16.10.0 har exponerat egenskapen Shape.Glow tillsammans med klassen GlowEffect som tillsammans möjliggör att ställa in glödeffekten för ett Shape-objekt. Klassen GlowEffect specifierar en glödeffekt, där en färgoskarp kontur läggs till utanför objektets kanter med hjälp av följande egenskaper.

- GlowEffect.Size: Hämtar/ställer in radien för glöden i punktenheter.
- GlowEffect.Transparency: Hämtar/ställer in graden av genomskinlighet för glödeffekten som sträcker sig från 0,0 (opak) till 1,0 (genomskinlig).

Här är ett enkelt användningscenario för egenskapen Shape.Glow.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Att arbeta med Glödeffekt](/cells/sv/net/working-with-the-glow-effect-of-shape-or-chart/)

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

Kontrollera den detaljerade artikeln om [Arbeta med 3D-formatering](/cells/sv/net/working-with-the-threedformat-of-shape-or-chart/)

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


### **Stöd för WordArt-stilar i formens text**
Aspose.Cells 16.10.0 har exponerat FontSettingCollection.SetWordArtStyle- & FontSetting.SetWordArtStyle-metoderna för att ställa in den förinställda WordArt-stilen på formens textobjekt.

Här finns ett enkelt användningsscenario för ovanstående metoder.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Arbete med WordArt-stilar](/cells/sv/net/set-preset-wordart-style-to-the-text-of-the-shape/)

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


### **Stöd för inbyggda WordArt-stilar**
Aspose.Cells 16.10.0 har exponerat ShapeCollection.AddWordArt-metoden tillsammans med PresetWordArtStyle-uppräkningen för att tillhandahålla stöd för att lägga till förinställda WordArt-objekt sedan Excel 2007.

Här finns ett enkelt användningsscenario för ShapeCollection.AddWordArt-metoden.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Lägg till WordArt med inbyggda stilar](/cells/sv/net/add-word-art-text-with-built-in-styles/)

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


### **Tillagd XmlMapCollection.Add-metod**
Aspose.Cells har exponerat XmlMapCollection.Add-metoden som gör det möjligt att lägga till Xml-map till ett kalkylblad. Här finns ett enkelt användningsscenario för XmlMapCollection.Add-metoden.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Lägg till XML-karta till kalkylbladet](/cells/sv/net/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Add xml map from the sample.xml to the workbook

book.Worksheets.XmlMaps.Add("sample.xml");

{{< /highlight >}}


### **Tillagd Cells.LinkToXmlMap-metod**
Aspose.Cells har nu exponerat Cells.LinkToXmlMap-metoden för att länka cellerna med XML-kartelementen.

Här finns ett enkelt användningsscenario för Cells.LinkToXmlMap-metoden.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Länka celler till XML-kartelement](/cells/sv/net/link-cells-to-xml-map-elements/)

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


### **Tillagd ListColumn.Formula-egenskap**
Aspose.Cells 16.10.0 har exponerat ListColumn.Formula-egenskapen för att automatiskt sprida formeln till nyligen infogade rader.

Här finns ett enkelt användningsscenario för ListColumn.Formula-egenskapen.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Automatisk spridning av formel i listobjekt](/cells/sv/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

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


### **Stöd för beräkning av anpassade funktioner med GridWeb**
Aspose.Cells.GridWeb 16.10.0 har exponerat GridWeb.CustomCalculationEngine-egenskapen tillsammans med GridAbstractCalculationEngine-klassen vilket tillsammans möjliggör att definiera och beräkna anpassade funktioner från inom GridWeb-komponenten.

Här finns ett enkelt användningsscenario för ovanstående API:er.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Beräkning av anpassade funktioner med GridWeb](/cells/sv/net/calculate-custom-functions-in-gridweb/)

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
