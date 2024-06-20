---
title: Modifiche all API pubblica in Aspose.Cells 16.10.0
type: docs
weight: 350
url: /it/java/public-api-changes-in-aspose-cells-16-10-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 9.0.0 a 16.10.0 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali modifiche nel comportamento del dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto agli effetti di riflessione**
Aspose.Cells 16.10.0 ha esposto la classe ReflectionEffect insieme alla proprietà Shape.Reflection per controllare gli effetti di riflessione di un oggetto Shape. La classe ReflectionEffect ha le seguenti proprietà.

- ReflectionEffect.Blur: Ottiene/imposta il raggio di sfocatura in unità di punti.
- ReflectionEffect.Direction: Ottiene/imposta la direzione della rampa del gradiente alfa rispetto alla forma stessa.
- ReflectionEffect.Distance: Ottiene/imposta la distanza della riflessione in unità di punti.
- ReflectionEffect.FadeDirection: Ottiene/imposta la direzione per spostare la riflessione.
- ReflectionEffect.RotWithShape: Ottiene/imposta se la riflessione deve ruotare con la forma.
- ReflectionEffect.Size: Ottiene/imposta la posizione finale (lungo la rampa del gradiente alfa) del valore finale alfa in percentuale.
- ReflectionEffect.Transparency: Ottiene/imposta il grado di trasparenza iniziale della riflessione come valore da 0,0 (opaco) a 1,0 (trasparente).
- ReflectionEffect.Type: Ottiene/imposta l'effetto di riflessione preimpostato.

Ecco un semplice scenario di utilizzo della proprietà Shape.Reflection.

{{% alert color="primary" %}} 

Consulta l'articolo dettagliato su [Working with Reflection Effects](/cells/it/java/working-with-the-reflection-effect-of-shape-or-chart/)

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
### **Supporto agli effetti d'ombra**
Aspose.Cells 16.10.0 ha esposto la proprietà Shape.ShadowEffect insieme alla classe ShadowEffect che permette di impostare l'effetto d'ombra su un oggetto Shape. La classe ShadowEffect ha le seguenti proprietà.

- ShadowEffect.Angle: Ottiene/imposta l'angolo di illuminazione che va da 0 a 359,9 gradi.
- ShadowEffect.Blur: Ottiene e imposta la sfocatura dell'ombra che va da 0 a 100 punti.
- ShadowEffect.Color: Ottiene/imposta il colore dell'ombra.
- ShadowEffect.Distance: Ottiene/imposta la distanza dell'ombra compresa tra 0 e 200 punti.
- ShadowEffect.PresetType: Ottiene/imposta il tipo di ombra predefinito dell'ombra.
- ShadowEffect.Size: Ottiene/imposta le dimensioni dell'ombra comprese tra 0 e 2.0. Sarà insignificante in caso di ombra interna.
- ShadowEffect.Transparency: Ottiene/imposta il grado di trasparenza dell'ombra compreso tra 0.0 (opaco) e 1.0 (trasparente).

Ecco un semplice scenario di utilizzo della proprietà sopra citata.

{{% alert color="primary" %}} 

Controlla l'articolo dettagliato su [Lavorare con gli effetti ombra](/cells/it/java/working-with-the-shadow-effect-of-shape-or-chart/)

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
### **Supporto per gli effetti luminosi**
Aspose.Cells 16.10.0 ha esposto la proprietà Shape.Glow insieme alla classe GlowEffect che permette di impostare l'effetto di bagliore di un oggetto Shape. La classe GlowEffect specifica un effetto di bagliore, in cui un contorno sfocato del colore è aggiunto all'esterno dei bordi dell'oggetto utilizzando le seguenti proprietà.

- GlowEffect.Size: Ottiene/imposta il raggio del bagliore in unità di punti.
- GlowEffect.Transparency: Ottiene/imposta il grado di trasparenza dell'effetto di bagliore compreso tra 0.0 (opaco) e 1.0 (trasparente).

Ecco un semplice scenario di utilizzo della proprietà Shape.Glow.

{{% alert color="primary" %}} 

Controlla l'articolo dettagliato su [Lavorare con l'effetto di bagliore](/cells/it/java/working-with-the-glow-effect-of-shape-or-chart/)

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
### **Supporto per il formato 3D**
Aspose.Cells 16.10.0 ha esposto la proprietà Shape.ThreeDFormat insieme alla classe ThreeDFormat che insieme possono essere utilizzate per controllare la formattazione 3D dell'oggetto Shape. La classe ThreeDFormat rappresenta la formattazione tridimensionale di una forma e ha le seguenti proprietà.

- ThreeDFormat.BottomBevelHeight: Ottiene/imposta l'altezza della bisellatura inferiore o quanto è profonda nella forma, in unità di punti.
- ThreeDFormat.BottomBevelType: Ottiene/imposta il tipo di bisellatura inferiore o quanto è profonda nella forma, in unità di punti.
- ThreeDFormat.BottomBevelWidth: Ottiene/imposta la larghezza della bisellatura inferiore o quanto è profonda nella forma, in unità di punti.
- ThreeDFormat.ContourColor: Ottiene/imposta il colore del contorno di una forma.
- ThreeDFormat.ContourWidth: Ottiene/imposta la larghezza del contorno sulla forma, in unità di punti.
- ThreeDFormat.ExtrusionColor: Ottiene il colore dell'estrusione su una forma.
- ThreeDFormat.ExtrusionHeight: Ottiene/imposta l'altezza dell'estrusione applicata alla forma, in unità di punti.
- ThreeDFormat.LightAngle: Ottiene/imposta l'angolo delle luci di estrusione.
- ThreeDFormat.Lighting: Ottiene/imposta il tipo di illuminazione.
- ThreeDFormat.LightingDirection: Ottiene/imposta la direzione da cui è orientata la fonte di luce rispetto alla scena.
- ThreeDFormat.Material: Rappresenta il materiale preimpostato combinato con le proprietà di illuminazione per dare il look finale di una forma.
- ThreeDFormat.Perspective: Ottiene/imposta l'angolazione con cui un oggetto ThreeDFormat può essere visualizzato.
- ThreeDFormat.PresetCameraType: Ottiene/imposta la fotocamera preimpostata per l'estrusione.
- ThreeDFormat.RotationX: Ottiene/imposta la rotazione della forma estrusa attorno all'asse X, in unità di gradi.
- ThreeDFormat.RotationY: Ottiene/imposta la rotazione della forma estrusa attorno all'asse Y, in unità di gradi.
- ThreeDFormat.RotationZ: Ottiene/imposta la rotazione della forma estrusa attorno all'asse Z, in unità di gradi.
- ThreeDFormat.TopBevelHeight: Ottiene/imposta l'altezza del bordo superiore o quanto è applicato nella forma, in unità di punti.
- ThreeDFormat.TopBevelType: Ottiene/imposta il tipo del bordo superiore o quanto è applicato nella forma, in unità di punti.
- ThreeDFormat.TopBevelWidth: Ottiene/imposta la larghezza del bordo superiore o quanto è applicato nella forma, in unità di punti.
- ThreeDFormat.Z: Definisce la distanza dal terreno per la forma 3D.

Ecco uno scenario di utilizzo semplice della proprietà Shape.ThreeDFormat.

{{% alert color="primary" %}} 

Controlla l'articolo dettagliato su [Lavorare con la formattazione 3D](/cells/it/java/lavorare-con-il-threedformat-di-shape-or-chart/)

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
### **Supporto per gli stili WordArt nel testo di forma**
Aspose.Cells 16.10.0 ha esposto i metodi FontSettingCollection.SetWordArtStyle & FontSetting.SetWordArtStyle per impostare lo stile WordArt preimpostato sul testo dell'oggetto Shape.

Ecco uno scenario di utilizzo semplice dei metodi menzionati in precedenza.

{{% alert color="primary" %}} 

Consultare l'articolo dettagliato su [Working with WordArt Styles](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/)

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
### **Supporto per gli stili incorporati di WordArt**
Aspose.Cells 16.10.0 ha esposto il metodo ShapeCollection.AddWordArt insieme all'enumerazione PresetWordArtStyle per fornire il supporto per aggiungere oggetti WordArt predefiniti sin da Excel 2007.

Ecco un semplice scenario di utilizzo del metodo ShapeCollection.AddWordArt.

{{% alert color="primary" %}} 

Consultare l'articolo dettagliato su [Aggiungere WordArt con stili incorporati](/cells/it/java/add-word-art-text-with-built-in-styles/)

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
### **Aggiunto il metodo XmlMapCollection.Add**
Aspose.Cells ha esposto il metodo XmlMapCollection.Add che consente di aggiungere una mappa XML a un foglio di calcolo. Ecco un semplice scenario di utilizzo del metodo XmlMapCollection.Add.

{{% alert color="primary" %}} 

Consultare l'articolo dettagliato su [Aggiungere mappa XML al foglio di calcolo](/cells/it/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **Aggiunto il metodo Cells.LinkToXmlMap**
Aspose.Cells ha esposto il metodo Cells.LinkToXmlMap per collegare le celle agli elementi della mappa XML. Ecco un semplice scenario di utilizzo del metodo Cells.LinkToXmlMap.

{{% alert color="primary" %}} 

Consultare l'articolo dettagliato su [Collegare le celle agli elementi della mappa XML](/cells/it/java/link-cells-to-xml-map-elements/)

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
### **Aggiunta la proprietà Formula di ListColumn**
Aspose.Cells 16.10.0 ha esposto la proprietà Formula di ListColumn per propagare automaticamente la formula alle righe appena inserite.

Ecco un semplice scenario di utilizzo della proprietà Formula di ListColumn.

{{% alert color="primary" %}} 

Consultare l'articolo dettagliato su [Propagare automaticamente la formula in un oggetto elenco](/cells/it/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

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
