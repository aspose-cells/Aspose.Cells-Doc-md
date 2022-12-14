---
title: Offentliga API-ändringar i Aspose.Cells 16.12.0
type: docs
weight: 370
url: /sv/java/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 16.11.0 till 16.12.0 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Filtrera objekt vid laddningstid**
Aspose.Cells 16.12.0 har exponerat klassen LoadFilter tillsammans med egenskapen LoadOptions.LoadFilter som tillsammans kan styra vilken typ av data som ska laddas samtidigt som en instans av Workbook initialiseras från en mallfil.

Här är ett enkelt användningsscenario för att bara ladda dokumentegenskaperna från en mallfil.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.DOCUMENT_PROPERTIES);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

Följande utdrag läser in allt från ett befintligt kalkylblad förutom diagrammen.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.CHART);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

Följande kod laddar endast celldata (tillsammans med formler) och formatering från ett befintligt kalkylblad.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.CELL_DATA);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}
### **Lade till FileFormatType.OTS Enumeration**
Aspose.Cells 16.12.0 har lagt till OTS-post till FileFormatType-uppräkningen för att upptäcka formatet på OTS-filer.

Följande kodavsnitt använder FileFormatType.OTS.

**Java**

{{< highlight "csharp" >}}

 //Detect the format of the file

FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");



//Check if stream is of type OTS

if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);

{

	System.out.println("It is an OTS file");

}

{{< /highlight >}}
### **Lade till egenskapen BuiltInDocumentPropertyCollection.ScaleCrop**
Aspose.Cells 16.12.0 har lagt till egenskapen ScaleCrop till klassen BuiltInDocumentPropertyCollection. ScaleCrop indikerar visningsläget för dokumentminiatyren. Om du ställer in det här elementet på sant möjliggör skalning av dokumentminiatyrbilden enligt visningen, medan om du ställer in den på false kan du beskära dokumentminiatyren för att visa avsnittet som passar skärmen.
### **Lade till egenskapen BuiltInDocumentPropertyCollection.LinksUpToDate**
 Aspose.Cells 16.12.0 har också exponerat LinksUpToDate-egenskapen för klassen BuiltInDocumentPropertyCollection. Egenskapen LinksUpToDate anger om hyperlänkarna i ett dokument är uppdaterade.
### **Lade till Workbook.exportXml-metoden**
Aspose.Cells 16.12.0 har exponerat Workbook.exportXml-metoden som gör det möjligt att lagra XML-kartdata till angiven filsökväg. Metoden Workbook.exportXml accepterar 2 parametrar där den första parametern av typen sträng ska vara XML-mappnamnet och den andra parametern ska vara filsökvägen för att lagra XML-data.
### **Lade till WorksheetCollection.createRange Method**
Aspose.Cells 16.12.0 har lagt till metoden WorksheetCollection.createRange som gör det möjligt att skapa intervall baserat på en adress (cellområdesreferens) & kalkylbladsindex.

Följande utdrag använder metoden WorksheetCollection.createRange för att skapa ett cellintervall som sträcker sig över A1 till A2 i det första (standard) kalkylbladet.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access WorksheetCollection from the Workbook

WorksheetCollection sheets = book.getWorksheets();



//Create a range in first worksheet

Range range = sheets.createRange("A1:A2", 0);

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
### **Raderad Title.getCharacters-metod**
Använd metoden Title.characters istället.
