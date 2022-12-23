---
title: Offentlig API Ändringar i Aspose.Cells 8.7.0
type: docs
weight: 240
url: /sv/java/public-api-changes-in-aspose-cells-8-7-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.6.3 till 8.7.0 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Stöd för PDF Optimering**
 Aspose.Cells API:er tillhandahåller redan funktionen att konvertera kalkylblad till PDF. Med denna version av API kan användare nu[optimera den resulterande PDF-storleken](/cells/sv/java/save-excel-into-pdf-with-standard-or-minimum-size/)också. Aspose.Cells for Java 8.7.0 har exponerat egenskapen PdfSaveOptions.OptimizationType tillsammans med PdfOptimizationType-uppräkningen för att underlätta för användarna att välja önskad optimeringsalgoritm när de exporterar kalkylblad till formatet PDF. Det finns två möjliga värden för egenskapen PdfSaveOptions.OptimizationType enligt beskrivningen nedan.

1. PdfOptimizationType.MINIMUM_SIZE: Kvaliteten äventyras för den resulterande filstorleken.
1. PdfOptimizationType.STANDARD: Kvaliteten äventyras inte så den resulterande filstorleken blir stor.

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of PdfSaveOptions

PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();

//Set the OptimizationType property to desired value

pdfSaveOptions.setOptimizationType(PdfOptimizationType.MINIMUM_SIZE);

//Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Save the spreadsheet in PDF format while passing the instance of PdfSaveOptions

book.save(outFilePath, pdfSaveOptions);

{{< /highlight >}}
### **Detektering av digitalt signerat VBA-projekt**
 Nyligen exponerad egendom VbaProject.isSigned kan användas för att in[upptäcka om VBA-projektet i en arbetsbok är digitalt signerat](/cells/sv/java/check-if-vba-code-is-signed/). Egenskapen VbaProject.isSigned är av typen Boolean, som returnerar true om VBA-projektet är digitalt signerat och vice versa.

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

VbaProject vbaProject = book.getVbaProject();

//Check if VbaProject is digitally signed

if (vbaProject.isSigned())

{

	System.out.println("VbaProject is digitally signed");

}

else

{

	System.out.println("VbaProject is not digitally signed");

}

{{< /highlight >}}
### **Metod Protection.verifyPassword har lagts till**
Aspose.Cells API:er har förbättrat skyddsklassen genom att introducera metoden verifyPassword som gör det möjligt att ange ett lösenord som en instans av String och[verifierar om samma lösenord har använts för att skydda arbetsbladet](/cells/sv/java/verify-password-used-to-protect-the-worksheet/). Metoden Protection.verifyPassword returnerar true om det angivna lösenordet matchar lösenordet som används för att skydda det givna kalkylbladet, och false om det angivna lösenordet inte stämmer överens. Följande kodbit använder metoden Protection.verifyPassword i kombination med fältet Protection.isProtectedWithPassword för att upptäcka lösenordsskyddet och verifierar lösenordet.

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load a spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the protected Worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Check if Worksheet is password protected

if (sheet.getProtection().isProtectedWithPassword())

{

  //Verify the password used to protect the Worksheet

  if (sheet.getProtection().verifyPassword("password"))

  {

	  System.out.println("Specified password has matched");

  }

  else

  {

	  System.out.println("Specified password has not matched");

  }

}

{{< /highlight >}}
### **Property Protection.isProtectedWithPassword har lagts till**
 Denna utgåva av Aspose.Cells for Java har också exponerat fältet Protection.isProtectedWithPassword som kan vara användbart i[upptäcka om ett arbetsblad är lösenordsskyddat eller inte](/cells/sv/java/detect-if-worksheet-is-password-protected/).

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

Worksheet sheet = book.getWorksheets().get(0);

//Access Protection module of desired Worksheet

Protection protection = sheet.getProtection();

//Check if Worksheet is password protected

if (protection.isProtectedWithPassword())

{

	System.out.println("Worksheet is password protected");

}

else

{

	System.out.println("Worksheet is not password protected");

}

{{< /highlight >}}
### **Egenskapen ColorScale.Is3ColorScale tillagd**
 Aspose.Cells for Java 8.7.0 har exponerat egenskapen ColorScale.Is3ColorScale som kan användas för att[skapa villkorligt format i 2-färgskala](/cells/sv/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/). Den nämnda egenskapen är av typen Boolean med standardvärdet true vilket betyder att det villkorliga formatet kommer att vara i 3-färgsskala som standard. Men om du ändrar egenskapen ColorScale.Is3ColorScale till false genereras ett villkorligt format med 2-färgsskala.

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access the Worksheet to which conditional formatting rule has to be added

Worksheet sheet = book.getWorksheets().get(0);

//Add FormatConditions to the collection

int index = sheet.getConditionalFormattings().add();

//Access newly added formatConditionCollection via its index

FormatConditionCollection formatConditionCollection = sheet.getConditionalFormattings().get(index);

//Create a CellArea on which conditional formatting rule will be applied

CellArea cellArea = CellArea.createCellArea("A1", "A5");

//Add conditional formatted cell range

formatConditionCollection.addArea(cellArea);

//Add format condition of type ColorScale

index = formatConditionCollection.addCondition(FormatConditionType.COLOR_SCALE);

//Access newly added format condition via its index

FormatCondition formatCondition = formatConditionCollection.get(index);

//Set Is3ColorScale to false in order to generate a 2-Color Scale format

formatCondition.getColorScale().setIs3ColorScale(false);

//Set other necessary properties

{{< /highlight >}}
### **Property TxtLoadOptions.HasFormula Added**
 Aspose.Cells for Java 8.7.0 har tillhandahållit support till[identifiera och analysera formlerna medan du laddar CSV/TXT-filer med avgränsad vanlig data](/cells/sv/java/load-or-import-csv-file-with-formulas/). Den nyligen exponerade egenskapen TxtLoadOptions.HasFormula när den är satt till true dirigerar API att tolka formlerna från den indataavgränsade filen och ställa in dem på relevanta celler utan att kräva ytterligare bearbetning.

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of TxtLoadOptions

TxtLoadOptions options = new TxtLoadOptions();

//Set HasFormula property to true

options.setHasFormula(true);

//Set the Separator property as desired

options.setSeparator(',');

//Load the CSV/TXT file using the instance of TxtLoadOptions

Workbook book = new Workbook(inFilePath, options);

//Calculate formulas in order to get the calculated values of formula in CSV

book.calculateFormula();

//Write result in any of the supported formats

book.save(outFilePath);

{{< /highlight >}}
### **Egenskap DataLabels.ResizeShapeToFitText tillagd**
 En annan användbar funktion som Aspose.Cells for Java 8.7.0 har exponerat är egenskapen DataLabels.ResizeShapeToFitText som kan aktivera[ändra storlek på formen så att den passar text](/cells/sv/java/resize-chart-s-data-label-shape-to-fit-text/)funktion i Excel-applikationen för diagrammets dataetiketter.

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook containing the Chart

Workbook book = new Workbook(inFilePath);

//Access the Worksheet that contains the Chart

Worksheet sheet = book.getWorksheets().get(0);

//Access the desired Chart via its index or name

Chart chart = sheet.getCharts().get(0);

//Access the DataLabels of desired NSeries

DataLabels labels = chart.getNSeries().get(0).getDataLabels();

//Set ResizeShapeToFitText property to true

labels.setResizeShapeToFitText(true);

//Calculate Chart

chart.calculate();

{{< /highlight >}}
## **Borttagna API:er**
### **Egenskapsarbetsbok.Sparaalternativ har tagits bort**
Egenskapen Workbook.SaveOptions markerades som föråldrad för en tid sedan. Med den här utgåvan har den tagits bort helt från den offentliga API, därför rekommenderas att använda metoden Workbook.save(Stream, SaveOptions) eller Workbook.save(string, SaveOptions) som alternativ.
