---
title: Offentliga API ändringar i Aspose.Cells 16.12.0
type: docs
weight: 360
url: /sv/net/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringar i Aspose.Cells API från version 16.11.0 till 16.12.0 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser osv., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Filterobjekt vid inläsning**
Aspose.Cells 16.12.0 har exponerat klassen LoadFilter tillsammans med egenskapen LoadOptions.LoadFilter som tillsammans kan kontrollera vilken typ av data som ska laddas vid initialisering av en instans av Workbook från en mallfil.

Här är ett enkelt användningsscenariot för att endast ladda dokumentegenskaper från en mallfil.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class

// Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.DocumentProperties);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Följande utdrag laddar allt från en befintlig kalkylblad förutom diagrammen.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to the constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.All & ~Aspose.Cells.LoadDataFilterOptions.Chart);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Följande kod laddar endast celldata (tillsammans med formler) och formatering från en befintlig kalkylblad.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.CellData);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Klassen LoadFilter tillåter också att anpassa laddningsprocessen enligt egenskaperna för arket. För att anpassa laddningsprocessen enligt kalkylblad måste en person överväga metoden LoadFilter.StartSheet enligt nedanstående exempel.

**C#**

{{< highlight csharp >}}

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



Följande kodsnutt använder CustomFilter-klassen som definierats ovan.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **Tillagd FileFormatType.OTS Uppräkning**
Aspose.Cells 16.12.0 har lagt till OTS-posten till uppräkningen FileFormatType för att upptäcka formatet av OTS-filer.

Följande kodsnutt använder FileFormatType.OTS.

**C#**

{{< highlight csharp >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **Tillagd egenskapen FontConfigs.PreferSystemFontSubstitutes**
Aspose.Cells 16.12.0 har exponerat egenskapen PreferSystemFontSubstitutes för FontConfigs-klassen. Egenskapen FontConfigs.PreferSystemFontSubstitutes är av typen Boolean och indikerar om API:en ska använda systemets fontsubstitutionsmekanism först, om en nödvändig font inte är närvarande och ingen ersättning för den särskilda fonten har definierats. Standardvärdet för egenskapen FontConfigs.PreferSystemFontSubstitutes är falskt.
### **Tillagd egenskapen BuiltInDocumentPropertyCollection.ScaleCrop**
Aspose.Cells 16.12.0 har lagt till egenskapen ScaleCrop till BuiltInDocumentPropertyCollection-klassen. ScaleCrop anger visningsläget för dokumentets miniatyrbild. Att sätta det här elementet till sann aktiverar skalningen av dokumentets miniatyrbild enligt visning medan att sätta det till falskt aktiverar beskärningen av dokumentets miniatyrbild för att visa avsnittet som passar visningen.
### **Tillagd egenskapen BuiltInDocumentPropertyCollection.LinksUpToDate**
Aspose.Cells 16.12.0 har också exponerat egenskapen LinksUpToDate för BuiltInDocumentPropertyCollection-klassen. Egenskapen LinksUpToDate indikerar om hyperlänkar i en dokument är uppdaterade.
### **Tillagd Workbook.ExportXml Metoden**
Aspose.Cells 16.12.0 har exponerat metoden Workbook.ExportXml som tillåter att lagra XML-kartdata till angiven filväg. Workbook.ExportXml metoden accepterar 2 parametrar där den första parametern av typen string ska vara XML-kartnamnet och den andra parametern ska vara filvägsplatsen för att lagra XML-data.
### **Tillagd WorksheetCollection.CreateRange Metoden**
Aspose.Cells 16.12.0 har lagt till metoden WorksheetCollection.CreateRange som tillåter att skapa ett område baserat på en adress (cellområdens referens) & Arkindex.

Följande kodsnutt använder WorksheetCollection.CreateRange-metoden för att skapa ett område med celler som sträcker sig över A1 till A2 i första (standard) kalkylblad.

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

{{< /highlight >}}
## **Obsoletterade API:er**
### **Obsoletterad LoadOptions.LoadDataOptions Egenskap**
Använd istället LoadOptions.LoadFilter egenskapen som ett alternativ.
### **Obsoletterad LoadOptions.LoadDataFilterOptions Egenskap**
Använd istället LoadOptions.LoadFilter egenskapen istället.
### **Obsoletterad LoadOptions.OnlyLoadDocumentProperties Egenskap**
Använd istället LoadOptions.LoadFilter egenskapen som ett alternativ.
### **Obsoletterad LoadOptions.LoadDataAndFormatting Egenskap**
Använd istället LoadOptions.LoadFilter egenskapen istället.

{{% alert color="primary" %}} 

Kodsnutten för alla obsoletterade API:er har delats ovan.

{{% /alert %}}
## **Raderade API:er**
### **Raderad DataLabels.Rotation Egenskap**
Använd istället DataLabels.RotationAngle egenskapen istället.
### **Borttagen titel.Rotationsattribut**
Vänligen använd Title.RotationAngle-egendom som ett alternativ.
### **Borttagen DataLabels.Background Egendom**
Det rekommenderas att använda DataLabels.BackgroundMode-egendomen istället.
### **Borttagen DisplayUnitLabel.Rotation-egendom**
Överväg att använda DisplayUnitLabel.RotationAngle-egendom för att uppnå samma mål.
{{< app/cells/assistant language="csharp" >}}
