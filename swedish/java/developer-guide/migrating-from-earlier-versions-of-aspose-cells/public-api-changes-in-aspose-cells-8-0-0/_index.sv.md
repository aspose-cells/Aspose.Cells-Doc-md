---
title: Offentlig API Ändringar i Aspose.Cells 8.0.0
type: docs
weight: 20
url: /sv/java/public-api-changes-in-aspose-cells-8-0-0/
---
{{% alert color="primary" %}} 

Den här sidan listar offentliga API ändringar som infördes i Aspose.Cells 8.0.0. Den innehåller inte bara nya och föråldrade offentliga metoder, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells som kan påverka den befintliga koden.

{{% /alert %}} 
## **Lade till MemorySetting till LoadOptions & WorkbookSettings**
Från och med v8.0.0 av Aspose.Cells for Java har vi tillhandahållit minnesanvändningsalternativen för prestandaöverväganden. MemorySetting-egenskapen är nu tillgänglig i klasserna LoadOptions & WorkbookSettings.
### **Exempel**
Demonstrerar hur man läser en Excel-fil (som har stor storlek) i optimerat läge.

**Java**

{{< highlight "csharp" >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Demonstrerar hur man skriver stora datamängder till ett kalkylblad i optimerat läge.

**Java**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

 Vänligen kontrollera den detaljerade artikeln om[Optimera minnet när du arbetar med stora filer](/cells/sv/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)s.

{{% /alert %}}
## **Implementeringarna av Row & Cell har ändrats**
 I tidigare versioner hölls Row- och Cell-objekt i minnet för att representera motsvarande rad och cell i ett kalkylblad. Samma instans returnerades när som helst**RowCollection[int index]** eller**Cells[int rad, int kolumn]** hämtades. Av hänsyn till minnesprestanda kommer endast egenskaper och data för Row och Cell att behållas i minnet nu och framåt. Följaktligen har Row & Cell-objektet blivit omslaget av ovannämnda egenskaper.
### **Exempel**
Demonstrerar hur man jämför objekten Cell och Row från och med nu.

**Java**

{{< highlight "csharp" >}}

 //..

row1.equals(row2);


cell1.equals(cell2);

//..

{{< /highlight >}}

Eftersom Row- och Cell-objekten instansieras enligt anropet kommer de inte att behållas och hanteras i minnet av Cells-komponenten. Därför kan det hända att rad- och kolumnindexen inte uppdateras efter vissa insättnings- och raderingsoperationer, eller ännu värre, dessa objekt blir ogiltiga.
### **Exempel**
Till exempel kommer följande kodavsnitt att returnera ogiltiga resultat med 8.0.0 och högre,

**Java**

{{< highlight "csharp" >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

Med den nya versionen blir objektet Cell ogiltigt eller refererar till A2 med något oönskat värde. För att undvika en sådan situation, hämta Row- eller Cell-objekten igen från cellsamlingen för att hämta rätt resultat.

**Java**

{{< highlight "csharp" >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells.get("A3");

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection ärver inte CollectionBase längre eftersom det inte finns något radobjekt i dess inre lista.

{{% /alert %}}
## **Cell.StringValue Beteende ändrat**
 I tidigare versioner, specialmönster_ignorerades vid formatering av cellvärden, där specialtecknet * alltid producerade ett tecken i det formaterade resultatet. Från den här versionen har vi ändrat logiken för att hantera specialtecken_ och* för att göra det formaterade resultatet samma som i Excel-applikationen. Till exempel det anpassade cellformatet "_(\$* #,##0.00_)" som används för att representera värde 123 gav resultatet som "$ 123.00". Med nya versioner kommer Cell.StringValue att innehålla resultatet som "$123.00", vilket är samma beteende som Excel-applikationen uppvisar när cellen kopieras att sms:a eller exportera till CSV.
## **Lade till CreatedTime till PdfSaveOptions**
Nu kan användare få eller ställa in PDF skapandetid samtidigt som de sparar kalkylarket till PDF medan de använder klassen PdfSaveOptions.
## **Lade till ShowFormulas till arbetsbladet**
Från och med nu kan användare använda den booleska egenskapen ShowFormulas som erbjuds av Worksheet för att växla vyn mellan formel och värde för ett givet kalkylblad.
## **Lade till Ooxml till FileFormatType**
En ny konstant Ooxml har lagts till i klassen FileFormatType för att representera den krypterade Office open XML-filen som XLSX, DOCX, PPTX och mer.
## **Föråldrad FilterColumnCollection av AutoFilter**
Med Aspose.Cells for Java har metoden getFilterColumnCollection markerats som föråldrad. Det rekommenderas att använda metoden AuotFilter.getFilterColumns istället.
## **Ersatte SeriesCollection.SecondCatergoryData med SeriesCollection.SecondCategoryData**
Vi har i princip korrigerat stavfelet i metodnamnet för SeriesCollection.getSecondCatergoryData. Du kan använda SeriesCollection.getSecondCategoryData-metoden nu och framåt, medan den ursprungliga metoden SeriesCollection.getSecondCatergoryData har markerats som föråldrad.
