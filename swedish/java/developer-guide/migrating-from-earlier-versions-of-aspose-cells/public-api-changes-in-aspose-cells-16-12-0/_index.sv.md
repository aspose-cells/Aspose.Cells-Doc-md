---
title: Offentliga API ändringar i Aspose.Cells 16.12.0
type: docs
weight: 370
url: /sv/java/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringar i Aspose.Cells API från version 16.11.0 till 16.12.0 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser osv., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Filterobjekt vid inläsning**
Aspose.Cells 16.12.0 har exponerat klassen LoadFilter tillsammans med egenskapen LoadOptions.LoadFilter som tillsammans kan kontrollera vilken typ av data som ska laddas vid initialisering av en instans av Workbook från en mallfil.

Här är ett enkelt användningsscenariot för att endast ladda dokumentegenskaper från en mallfil.

**Java**

{{< highlight csharp >}}

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

Följande utdrag laddar allt från en befintlig kalkylblad förutom diagrammen.

**Java**

{{< highlight csharp >}}

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

Följande kod laddar endast celldata (tillsammans med formler) och formatering från en befintlig kalkylblad.

**Java**

{{< highlight csharp >}}

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
### **Tillagd FileFormatType.OTS Uppräkning**
Aspose.Cells 16.12.0 har lagt till OTS-posten till uppräkningen FileFormatType för att upptäcka formatet av OTS-filer.

Följande kodsnutt använder FileFormatType.OTS.

**Java**

{{< highlight csharp >}}

 //Detect the format of the file

FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");



//Check if stream is of type OTS

if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);

{

	System.out.println("It is an OTS file");

}

{{< /highlight >}}
### **Tillagd egenskapen BuiltInDocumentPropertyCollection.ScaleCrop**
Aspose.Cells 16.12.0 har lagt till egenskapen ScaleCrop till BuiltInDocumentPropertyCollection-klassen. ScaleCrop anger visningsläget för dokumentets miniatyrbild. Att sätta det här elementet till sann aktiverar skalningen av dokumentets miniatyrbild enligt visning medan att sätta det till falskt aktiverar beskärningen av dokumentets miniatyrbild för att visa avsnittet som passar visningen.
### **Tillagd egenskapen BuiltInDocumentPropertyCollection.LinksUpToDate**
Aspose.Cells 16.12.0 har också exponerat egenskapen LinksUpToDate för BuiltInDocumentPropertyCollection-klassen. Egenskapen LinksUpToDate indikerar om hyperlänkar i en dokument är uppdaterade. 
### **Lade till Workbook.exportXml-metod**
Aspose.Cells 16.12.0 har exponerat Workbook.exportXml-metoden som tillåter att lagra XML-kartdata till angiven filväg. Workbook.exportXml-metoden accepterar 2 parametrar där den första parametern av typen string ska vara XML-kartans namn och den andra parametern ska vara filvägens plats för att lagra XML-data.
### **Lade till WorksheetCollection.createRange-metod**
Aspose.Cells 16.12.0 har lagt till WorksheetCollection.createRange-metod som tillåter att skapa ett område baserat på en adress (cellområdesreferens) och arbetsbladets index.

Följande kodsnutt använder WorksheetCollection.createRange-metoden för att skapa ett område av celler som sträcker sig över A1 till A2 i det första (standard) arbetsbladet.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access WorksheetCollection from the Workbook

WorksheetCollection sheets = book.getWorksheets();



//Create a range in first worksheet

Range range = sheets.createRange("A1:A2", 0);

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
### **Raderad Title.getCharacters-metod**
Använd vänligen Title.characters-metoden istället.
{{< app/cells/assistant language="java" >}}
