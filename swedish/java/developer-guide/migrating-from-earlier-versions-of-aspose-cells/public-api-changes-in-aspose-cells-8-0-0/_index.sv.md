---
title: Offentliga API ändringar i Aspose.Cells 8.0.0
type: docs
weight: 20
url: /sv/java/public-api-changes-in-aspose-cells-8-0-0/
---

{{% alert color="primary" %}} 

Denna sida listar offentliga API-ändringar som introducerades i Aspose.Cells 8.0.0. Den inkluderar inte bara nya och inaktuella offentliga metoder, utan också en beskrivning av eventuella ändringar i beteendet bakom kulisserna i Aspose.Cells som kan påverka befintlig kod.

{{% /alert %}} 
## **Tillagt MemorySetting till LoadOptions & WorkbookSettings**
Från och med v8.0.0 av Aspose.Cells for Java har vi tillhandahållit minnesanvändningsalternativ för prestandahänsyn. MemorySetting-egenskapen är nu tillgänglig i LoadOptions- och WorkbookSettings-klasserna.
### **Exempel**
Visar hur man läser in en Excel-fil (med stor storlek) i optimerat läge.

**Java**

{{< highlight csharp >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Visar hur man skriver in ett stort Dataset till en arbetsbok i optimerat läge.

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

Vänligen kontrollera den detaljerade artikeln om [Optimering av minne vid arbete med stora filer](/cells/sv/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}
## **Implementeringar av Rad & Cell har ändrats**
I tidigare versioner hölls Rad- och Cell-objekt i minnet för att representera motsvarande rad och cell i en arbetsbok. Samma instans returnerades när **RowCollection[int index]** eller **Cells[int row, int column]** hämtades. Av prestandaskäl kommer endast egenskaper och data hos Rad och Cell att hållas i minnet från och med nu. Därför har Rad- och Cell-objekten blivit omslutare för ovan nämnda egenskaper.
### **Exempel**
Visar hur man jämför Cell- och Rad-objekt från och med nu.

**Java**

{{< highlight csharp >}}

 //..

row1.equals(row2);


cell1.equals(cell2);

//..

{{< /highlight >}}

Eftersom Rad- och Cell-objekten instansieras enligt anrop kommer de inte att hållas och hanteras i minnet av Cells-komponenten. Därför kan rad- och kolumnindexen efter vissa infogningar och borttagningar inte uppdateras eller ännu värre, dessa objekt blir ogiltiga.
### **Exempel**
Till exempel kommer följande kodsnutt att returnera ogiltiga resultat med version 8.0.0 och senare.

**Java**

{{< highlight csharp >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

Med den nya versionen kommer Cell-objektet att bli ogiltigt eller hänvisa till A2 med något oönskat värde. För att undvika en sådan situation, hämta Rad- eller Cell-objekten igen från cellkollektionen för att hämta det korrekta resultatet.

**Java**

{{< highlight csharp >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells.get("A3");

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

{{% alert color="primary" %}} 

RadCollection är inteververar CollectionBase längre eftersom det inte finns något Rad-objekt i dess inre lista.

{{% /alert %}}
## **Cell.StringValue Beteende Ändrat**
I tidigare versioner ignorerades speciellt mönstret _ vid formatering av cellvärden, medan det speciella tecknet * alltid producerade ett tecken i det formaterade resultatet. Från och med denna version har vi ändrat logiken för att hantera speciella tecken _ och * för att göra det formaterade resultatet samma som i Excel-applikationen. Till exempel innebar det anpassade cellformatet "_(\$* #,##0.00_)" för att representera värdet 123 att resultatet producerades som "$ 123.00". Med nya versioner kommer Cell.StringValue att innehålla resultatet som "$123.00" vilket är samma beteende som Excel-applikationen uppvisar när cellen kopieras till text eller exporteras till CSV.
## **Tillagt CreatedTime till PdfSaveOptions**
Nu kan användare få eller ställa in PDF-skapandetiden när de sparar kalkylbladet som PDF med PdfSaveOptions-klassen.
## **Tillagt ShowFormulas till Arbetsblad**
Från och med nu kan användare använda Boolesk egenskap VisaFormler som erbjuds av Arbetsblad för att växla vyn mellan formel och värde för ett givet arbetsblad.
## **Tillagt Ooxml till FileFormatType**
En ny konstant Ooxml har lagts till klassen FileFormatType för att representera krypterad Office Open XML-fil såsom XLSX, DOCX, PPTX och mer.
## **Obsoletade FilterColumnCollection av AutoFilter**
Med Aspose.Cells for Java har getFilterColumnCollection-metoden markerats som föråldrad. Det föreslås att istället använda AuotFilter.getFilterColumns-metoden.
## **Ersatt SeriesCollection.SecondCatergoryData med SeriesCollection.SecondCategoryData**
Vi har i princip rättat till stavfel i metodnamnet för SeriesCollection.getSecondCatergoryData. Du kan använda SeriesCollection.getSecondCategoryData-metoden från och med nu, medan den ursprungliga metoden SeriesCollection.getSecondCatergoryData har markerats som föråldrad.
{{< app/cells/assistant language="java" >}}
