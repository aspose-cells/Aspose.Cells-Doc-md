---
title: Modifiche all'API pubblica in Aspose.Cells 16.10.0
type: docs
weight: 350
url: /it/java/public-api-changes-in-aspose-cells-16-10-0/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 9.0.0 alla 16.10.0 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per effetti di riflessione**
Aspose.Cells 16.10.0 ha esposto la classe ReflectionEffect insieme alla proprietà Shape.Reflection per controllare gli effetti di riflessione di un oggetto Shape. La classe ReflectionEffect ha le seguenti proprietà.

- ReflectionEffect.Blur: ottiene/imposta il raggio di sfocatura in unità di punti.
- ReflectionEffect.Direction: Ottiene/imposta la direzione della rampa del gradiente alfa rispetto alla forma stessa.
- ReflectionEffect.Distance: ottiene/imposta la distanza del riflesso in unità di punti.
- ReflectionEffect.FadeDirection: Ottiene/imposta la direzione per l'offset del riflesso.
- ReflectionEffect.RotWithShape: Ottiene/imposta se il riflesso deve ruotare con la forma.
- ReflectionEffect.Size: Ottiene/imposta la posizione finale (lungo la rampa del gradiente alfa) del valore alfa finale in unità di percentuale .
- ReflectionEffect.Transparency: Ottiene/imposta il grado di trasparenza del riflesso iniziale come valore compreso tra 0,0 (opaco) e 1,0 (trasparente).
- ReflectionEffect.Type: Ottiene/imposta l'effetto riflesso preimpostato.

Ecco un semplice scenario di utilizzo della proprietà Shape.Reflection.

{{% alert color="primary" %}} 

 Controlla l'articolo dettagliato su[Lavorare con gli effetti di riflessione](/cells/it/java/working-with-the-reflection-effect-of-shape-or-chart/)

{{% /alert %}} 

**Giava**

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

 Controlla l'articolo dettagliato su[Lavorare con gli effetti ombra](/cells/it/java/working-with-the-shadow-effect-of-shape-or-chart/)

{{% /alert %}} 

**Giava**

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
### **Supporto per effetti luminosi**
Aspose.Cells 16.10.0 ha esposto la proprietà Shape.Glow insieme alla classe GlowEffect che tutti insieme consentono di impostare l'effetto bagliore di un oggetto Shape. La classe GlowEffect specifica un effetto bagliore, in cui un contorno sfocato di colore viene aggiunto all'esterno dei bordi dell'oggetto utilizzando le seguenti proprietà.

- GlowEffect.Size: Ottiene/imposta il raggio del bagliore in unità di punti.
- GlowEffect.Transparency: Ottiene/imposta il grado di trasparenza dell'effetto bagliore compreso tra 0,0 (opaco) e 1,0 (trasparente).

Ecco un semplice scenario di utilizzo della proprietà Shape.Glow.

{{% alert color="primary" %}} 

 Controlla l'articolo dettagliato su[Lavorare con l'effetto bagliore](/cells/it/java/working-with-the-glow-effect-of-shape-or-chart/)

{{% /alert %}} 

**Giava**

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

 Controlla l'articolo dettagliato su[Lavorare con la formattazione 3D](/cells/it/java/working-with-the-threedformat-of-shape-or-chart/)

{{% /alert %}} 

**Giava**

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
### **Supporto per gli stili WordArt nel testo di Shape**
Aspose.Cells 16.10.0 ha esposto i metodi FontSettingCollection.SetWordArtStyle & FontSetting.SetWordArtStyle per impostare lo stile WordArt preimpostato sul testo dell'oggetto Shape.

Ecco un semplice scenario di utilizzo dei metodi di cui sopra.

{{% alert color="primary" %}} 

 Controlla l'articolo dettagliato su[Lavorare con gli stili WordArt](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/)

{{% /alert %}} 

**Giava**

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
### **Supporto per gli stili incorporati di WordArt**
Aspose.Cells 16.10.0 ha esposto il metodo ShapeCollection.AddWordArt insieme all'enumerazione PresetWordArtStyle per fornire il supporto per l'aggiunta di oggetti WordArt preimpostati da Excel 2007.

Ecco un semplice scenario di utilizzo del metodo ShapeCollection.AddWordArt.

{{% alert color="primary" %}} 

 Controlla l'articolo dettagliato su[Aggiungi WordArt con stili incorporati](/cells/it/java/add-word-art-text-with-built-in-styles/)

{{% /alert %}} 

**Giava**

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
### **Aggiunto il metodo XmlMapCollection.Add**
Aspose.Cells ha esposto il metodo XmlMapCollection.Add che permette di aggiungere Xml Map ad un foglio di calcolo. Ecco un semplice scenario di utilizzo del metodo XmlMapCollection.Add.

{{% alert color="primary" %}} 

 Controlla l'articolo dettagliato su[Aggiungi mappa XML al foglio di calcolo](/cells/it/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**Giava**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **Aggiunto il metodo Cells.LinkToXmlMap**
Aspose.Cells ha ora esposto il metodo Cells.LinkToXmlMap per collegare le celle con gli elementi della mappa XML. Ecco un semplice scenario di utilizzo del metodo Cells.LinkToXmlMap.

{{% alert color="primary" %}} 

 Controlla l'articolo dettagliato su[Collega Cells agli elementi della mappa XML](/cells/it/java/link-cells-to-xml-map-elements/)

{{% /alert %}} 

**Giava**

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
### **Aggiunta proprietà ListColumn.Formula**
Aspose.Cells 16.10.0 ha esposto la proprietà ListColumn.Formula per propagare automaticamente la formula alle righe appena inserite.

Ecco un semplice scenario di utilizzo della proprietà ListColumn.Formula.

{{% alert color="primary" %}} 

 Controlla l'articolo dettagliato su[Propaga automaticamente la formula nell'oggetto elenco](/cells/it/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

{{% /alert %}} 

**Giava**

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
