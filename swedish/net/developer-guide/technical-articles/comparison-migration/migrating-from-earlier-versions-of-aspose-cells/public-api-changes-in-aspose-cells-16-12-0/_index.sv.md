---
title: Offentliga API-ändringar i Aspose.Cells 16.12.0
type: docs
weight: 360
url: /sv/net/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 16.11.0 till 16.12.0 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Filtrera objekt vid laddningstid**
Aspose.Cells 16.12.0 har exponerat klassen LoadFilter tillsammans med egenskapen LoadOptions.LoadFilter som tillsammans kan styra vilken typ av data som ska laddas samtidigt som en instans av Workbook initialiseras från en mallfil.

Här är ett enkelt användningsscenario för att bara ladda dokumentegenskaperna från en mallfil.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class

// Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.DocumentProperties);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Följande utdrag läser in allt från ett befintligt kalkylblad förutom diagrammen.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to the constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.All & ~Aspose.Cells.LoadDataFilterOptions.Chart);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Följande kod laddar endast celldata (tillsammans med formler) och formatering från ett befintligt kalkylblad.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.CellData);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Klassen LoadFilter tillåter också att anpassa laddningsprocessen enligt egenskaperna för kalkylbladet. För att anpassa laddningsprocessen enligt kalkylbladet måste man åsidosätta metoden LoadFilter.StartSheet som visas nedan.

**C#**

{{< highlight "csharp" >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}



Följande kodavsnitt använder klassen CustomFilter som definieras ovan.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **Lade till FileFormatType.OTS Enumeration**
Aspose.Cells 16.12.0 har lagt till OTS-post till FileFormatType-uppräkningen för att upptäcka formatet på OTS-filer.

Följande kodavsnitt använder FileFormatType.OTS.

**C#**

{{< highlight "csharp" >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **Lade till FontConfigs.PreferSystemFontSubstitutes Property**
Aspose.Cells 16.12.0 har exponerat egenskapen PreferSystemFontSubstitutes för FontConfigs-klassen. Egenskapen FontConfigs.PreferSystemFontSubstitutes är av typen Boolean, vilket indikerar om API:et ska använda systemets teckensnittsersättningsmekanism först, om ett obligatoriskt teckensnitt inte finns och ingen ersättning för det specifika teckensnittet har definierats. Standardvärdet för egenskapen FontConfigs.PreferSystemFontSubstitutes är falskt.
### **Lade till egenskapen BuiltInDocumentPropertyCollection.ScaleCrop**
Aspose.Cells 16.12.0 har lagt till egenskapen ScaleCrop till klassen BuiltInDocumentPropertyCollection. ScaleCrop indikerar visningsläget för dokumentminiatyren. Om du ställer in det här elementet på sant möjliggör skalning av dokumentminiatyrbilden enligt visningen, medan om du ställer in den på false kan du beskära dokumentminiatyren för att visa avsnittet som passar skärmen.
### **Lade till egenskapen BuiltInDocumentPropertyCollection.LinksUpToDate**
Aspose.Cells 16.12.0 har också exponerat LinksUpToDate-egenskapen för klassen BuiltInDocumentPropertyCollection. Egenskapen LinksUpToDate anger om hyperlänkarna i ett dokument är uppdaterade.
### **Lade till Workbook.ExportXml Method**
Aspose.Cells 16.12.0 har avslöjat metoden Workbook.ExportXml som gör det möjligt att lagra XML-kartdata till angiven filsökväg. Metoden Workbook.ExportXml accepterar 2 parametrar där den första parametern av typen sträng ska vara XML-mappnamnet och den andra parametern ska vara filsökvägen för att lagra XML-data.
### **Lade till WorksheetCollection.CreateRange Method**
Aspose.Cells 16.12.0 har lagt till metoden WorksheetCollection.CreateRange som gör det möjligt att skapa intervall baserat på en adress (cellområdesreferens) & kalkylbladsindex.

Följande utdrag använder metoden WorksheetCollection.CreateRange för att skapa ett cellintervall som spänner över A1 till A2 i det första (standard) kalkylbladet.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

{{< /highlight >}}
## **Föråldrade API:er**
### **Föråldrad LoadOptions.LoadDataOptions-egenskap**
Använd egenskapen LoadOptions.LoadFilter som ett alternativ.
### **Föråldrad LoadOptions.LoadDataFilterOptions-egenskap**
Använd egenskapen LoadOptions.LoadFilter istället.
### **Föråldrade LoadOptions.OnlyLoadDocumentProperties-egenskap**
Använd egenskapen LoadOptions.LoadFilter som ett alternativ.
### **Föråldrad LoadOptions.LoadDataAndFormatting Property**
Använd egenskapen LoadOptions.LoadFilter istället.

{{% alert color="primary" %}} 

Kodavsnitt för alla föråldrade API:er har delats ovan.

{{% /alert %}}
## **Borttagna API:er**
### **Raderade DataLabels.Rotation Property**
Använd egenskapen DataLabels.RotationAngle istället.
### **Raderad Title.Rotation Property**
Använd egenskapen Title.RotationAngle som ett alternativ.
### **Borttagen DataLabels.Background-egenskap**
Det rekommenderas att använda egenskapen DataLabels.BackgroundMode istället.
### **Raderad DisplayUnitLabel.Rotation-egenskap**
Överväg att använda egenskapen DisplayUnitLabel.RotationAngle för att uppnå samma mål.
