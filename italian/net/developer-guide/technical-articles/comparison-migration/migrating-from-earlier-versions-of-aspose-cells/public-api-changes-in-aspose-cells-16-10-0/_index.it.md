---
title: Pubblico API Modifiche Aspose.Cells 16.10.0
type: docs
weight: 340
url: /it/net/public-api-changes-in-aspose-cells-16-10-0/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 9.0.0 alla 16.10.0 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per effetti di riflessione**
Aspose.Cells 16.10.0 ha esposto la classe ReflectionEffect insieme alla proprietà Shape.Reflection per controllare gli effetti di riflessione di un oggetto Shape. La classe ReflectionEffect ha le seguenti proprietà.

- ReflectionEffect.Blur: ottiene/imposta il raggio di sfocatura in unità di punti.
- ReflectionEffect.Direction: Ottiene/imposta la direzione della rampa del gradiente alfa relativa alla forma stessa.
- ReflectionEffect.Distance: ottiene/imposta la distanza del riflesso in unità di punti.
- ReflectionEffect.FadeDirection: Ottiene/imposta la direzione per l'offset del riflesso.
- ReflectionEffect.RotWithShape: Ottiene/imposta se il riflesso deve ruotare con la forma.
- ReflectionEffect.Size: Ottiene/imposta la posizione finale (lungo la rampa del gradiente alfa) del valore alfa finale in unità di percentuale .
- ReflectionEffect.Transparency: Ottiene/imposta il grado di trasparenza del riflesso iniziale come valore compreso tra 0,0 (opaco) e 1,0 (trasparente).
- ReflectionEffect.Type: Ottiene/imposta l'effetto riflesso preimpostato.

Ecco un semplice scenario di utilizzo della proprietà Shape.Reflection.

{{% alert color="primary" %}} 

 Controlla l'articolo dettagliato su[Lavorare con gli effetti di riflessione](/cells/it/net/working-with-the-reflection-effect-of-shape-or-chart/)

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


### **Supporto per effetti ombra**
Aspose.Cells 16.10.0 ha esposto la proprietà Shape.ShadowEffect insieme alla classe ShadowEffect che tutti insieme consentono di impostare l'effetto ombra su un oggetto Shape. La classe ShadowEffect ha le seguenti proprietà.

- ShadowEffect.Angle: ottiene/imposta l'angolo di illuminazione compreso tra 0 e 359,9 gradi.
- ShadowEffect.Blur: ottiene e imposta la sfocatura dell'ombra compresa tra 0 e 100 punti.
- ShadowEffect.Color: ottiene/imposta il colore dell'ombra.
- ShadowEffect.Distance: ottiene/imposta la distanza dell'ombra compresa tra 0 e 200 punti.
- ShadowEffect.PresetType: Ottiene/imposta il tipo di ombra preimpostato dell'ombra.
- ShadowEffect.Size: Ottiene/imposta la dimensione dell'ombra compresa tra 0 e 2,0. Non avrà senso in caso di ombra interiore.
- ShadowEffect.Transparency: Ottiene/imposta il grado di trasparenza dell'ombra compreso tra 0.0 (opaco) e 1.0 (chiaro).

Ecco un semplice scenario di utilizzo della suddetta proprietà.

{{% alert color="primary" %}} 

 Controlla l'articolo dettagliato su[Lavorare con gli effetti ombra](/cells/it/net/working-with-the-shadow-effect-of-shape-or-chart/)

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


### **Supporto per effetti luminosi**
Aspose.Cells 16.10.0 ha esposto la proprietà Shape.Glow insieme alla classe GlowEffect che tutti insieme consentono di impostare l'effetto bagliore di un oggetto Shape. La classe GlowEffect specifica un effetto bagliore, in cui un contorno sfocato di colore viene aggiunto all'esterno dei bordi dell'oggetto utilizzando le seguenti proprietà.

- GlowEffect.Size: Ottiene/imposta il raggio del bagliore in unità di punti.
- GlowEffect.Transparency: Ottiene/imposta il grado di trasparenza dell'effetto bagliore compreso tra 0,0 (opaco) e 1,0 (trasparente).

Ecco un semplice scenario di utilizzo della proprietà Shape.Glow.

{{% alert color="primary" %}} 

 Controlla l'articolo dettagliato su[Lavorare con l'effetto bagliore](/cells/it/net/working-with-the-glow-effect-of-shape-or-chart/)

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


### **Supporto per il formato 3D**
Aspose.Cells 16.10.0 ha esposto la proprietà Shape.ThreeDFormat insieme alla classe ThreeDFormat che insieme possono essere utilizzate per controllare la formattazione 3D dell'oggetto Shape. La classe ThreeDFormat rappresenta la formattazione tridimensionale di una forma e ha le seguenti proprietà.

- ThreeDFormat.BottomBevelHeight: Ottiene/imposta l'altezza della smussatura inferiore o la distanza di applicazione nella forma, in unità di punti.
- ThreeDFormat.BottomBevelType: Ottiene/imposta il tipo di smusso inferiore o la distanza in cui viene applicato nella forma, in unità di punti.
- ThreeDFormat.BottomBevelWidth: Ottiene/imposta la larghezza della smussatura inferiore o la distanza nella forma a cui viene applicata, in unità di punti.
- ThreeDFormat.ContourColor: ottiene/imposta il colore del contorno di una forma.
- ThreeDFormat.ContourWidth: ottiene/imposta la larghezza del contorno sulla forma, in unità di punti.
- ThreeDFormat.ExtrusionColor: ottiene il colore di estrusione su una forma.
- ThreeDFormat.ExtrusionHeight: ottiene/imposta l'altezza di estrusione applicata alla forma, in unità di punti.
- ThreeDFormat.LightAngle: Ottiene/imposta l'angolo delle luci di estrusione.
- ThreeDFormat.Lighting: ottiene/imposta il tipo di impianto luci.
- ThreeDFormat.LightingDirection: Ottiene/imposta la direzione da cui è orientato l'impianto luci rispetto alla scena.
- ThreeDFormat.Material: rappresenta il materiale preimpostato che viene combinato con le proprietà di illuminazione per dare l'aspetto finale di una forma.
- ThreeDFormat.Perspective: Ottiene/imposta l'angolo di visualizzazione di un oggetto ThreeDFormat.
- ThreeDFormat.PresetCameraType: Ottiene/imposta la telecamera preimpostata di estrusione.
- ThreeDFormat.RotationX: Ottiene/imposta la rotazione della forma estrusa attorno all'asse X in unità di gradi.
- ThreeDFormat.RotationY: Ottiene/imposta la rotazione della forma estrusa attorno all'asse Y in unità di gradi.
- ThreeDFormat.RotationZ: Ottiene/imposta la rotazione della forma estrusa attorno all'asse Z in unità di gradi.
- ThreeDFormat.TopBevelHeight: Ottiene/imposta l'altezza della smussatura superiore o la distanza nella forma a cui viene applicata, in unità di punti.
- ThreeDFormat.TopBevelType: Ottiene/imposta il tipo di smusso superiore o la distanza di applicazione nella forma, in unità di punti.
- ThreeDFormat.TopBevelWidth: Ottiene/imposta la larghezza della smussatura superiore o la distanza nella forma a cui viene applicata, in unità di punti.
- ThreeDFormat.Z: definisce la distanza dal suolo per la forma 3D.

Di seguito è riportato il semplice scenario di utilizzo della proprietà Shape.ThreeDFormat.

{{% alert color="primary" %}} 

 Controlla l'articolo dettagliato su[Lavorare con la formattazione 3D](/cells/it/net/working-with-the-threedformat-of-shape-or-chart/)

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


### **Supporto per gli stili WordArt nel testo di Shape**
Aspose.Cells 16.10.0 ha esposto i metodi FontSettingCollection.SetWordArtStyle & FontSetting.SetWordArtStyle per impostare lo stile WordArt preimpostato sul testo dell'oggetto Shape.

Ecco un semplice scenario di utilizzo dei metodi di cui sopra.

{{% alert color="primary" %}} 

 Controlla l'articolo dettagliato su[Lavorare con gli stili WordArt](/cells/it/net/set-preset-wordart-style-to-the-text-of-the-shape/)

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


### **Supporto per gli stili incorporati di WordArt**
Aspose.Cells 16.10.0 ha esposto il metodo ShapeCollection.AddWordArt insieme all'enumerazione PresetWordArtStyle per fornire il supporto per l'aggiunta di oggetti WordArt preimpostati da Excel 2007.

Ecco un semplice scenario di utilizzo del metodo ShapeCollection.AddWordArt.

{{% alert color="primary" %}} 

 Controlla l'articolo dettagliato su[Aggiungi WordArt con stili incorporati](/cells/it/net/add-word-art-text-with-built-in-styles/)

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


### **Aggiunto il metodo XmlMapCollection.Add**
Aspose.Cells ha esposto il metodo XmlMapCollection.Add che permette di aggiungere Xml Map ad un foglio di calcolo. Ecco un semplice scenario di utilizzo del metodo XmlMapCollection.Add.

{{% alert color="primary" %}} 

 Controlla l'articolo dettagliato su[Aggiungi mappa XML al foglio di calcolo](/cells/it/net/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Workbook();

// Add xml map from the sample.xml to the workbook

book.Worksheets.XmlMaps.Add("sample.xml");

{{< /highlight >}}


### **Aggiunto il metodo Cells.LinkToXmlMap**
Aspose.Cells ha ora esposto il metodo Cells.LinkToXmlMap per collegare le celle con gli elementi della mappa XML.

Ecco un semplice scenario di utilizzo del metodo Cells.LinkToXmlMap.

{{% alert color="primary" %}} 

 Controlla l'articolo dettagliato su[Collega Cells agli elementi della mappa XML](/cells/it/net/link-cells-to-xml-map-elements/)

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


### **Aggiunta proprietà ListColumn.Formula**
Aspose.Cells 16.10.0 ha esposto la proprietà ListColumn.Formula per propagare automaticamente la formula alle righe appena inserite.

Ecco un semplice scenario di utilizzo della proprietà ListColumn.Formula.

{{% alert color="primary" %}} 

 Controlla l'articolo dettagliato su[Propaga automaticamente la formula nell'oggetto elenco](/cells/it/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

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


### **Supporto per il calcolo di funzioni personalizzate con GridWeb**
Aspose.Cells.GridWeb 16.10.0 ha esposto la proprietà GridWeb.CustomCalculationEngine insieme alla classe GridAbstractCalculationEngine che tutti insieme consentono di definire e calcolare le funzioni personalizzate dall'interno del componente GridWeb.

Ecco un semplice scenario di utilizzo delle suddette API.

{{% alert color="primary" %}} 

 Controlla l'articolo dettagliato su[Calcolo delle funzioni personalizzate con GridWeb](/cells/it/net/calculate-custom-functions-in-gridweb/)

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
