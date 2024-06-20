---
title: Offentliga API ändringar i Aspose.Cells 8.7.0
type: docs
weight: 240
url: /sv/java/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringarna i Aspose.Cells API från version 8.6.3 till 8.7.0 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade publika metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Stöd för PDF-optimering**
Aspose.Cells API:er tillhandahåller redan funktionen att konvertera kalkylblad till PDF. Med denna version av API:et kan användare nu också [optimera den resulterande PDF-storleken](/cells/sv/java/save-excel-into-pdf-with-standard-or-minimum-size/). Aspose.Cells for Java 8.7.0 har exponerat egenskapen PdfSaveOptions.OptimizationType tillsammans med uppräkningen PdfOptimizationType för att underlätta för användarna att välja önskad optimeringsalgoritm vid export av kalkylblad till PDF-format. Det finns 2 möjliga värden för egenskapen PdfSaveOptions.OptimizationType enligt nedan. 

1. PdfOptimizationType.MINIMUM_SIZE: Kvaliteten äventyras för filstorleken.
1. PdfOptimizationType.STANDARD: Kvaliteten äventyras inte så filstorleken blir stor.

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

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
### **Upptäckt av digitalt signerat VBA-projekt**
Nyexponerade egenskapen VbaProject.isSigned kan användas för att [upptäcka om VBA-projektet i en arbetsbok är digitalt signerat](/cells/sv/java/check-if-vba-code-is-signed/). Egenskapen VbaProject.isSigned är av typen Boolean och returnerar true om VBA-projektet är digitalt signerat och vice versa.

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

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
### **Tillagd Protection.verifyPassword-metod**
Aspose.Cells API:er har förbättrat Protection-klassen genom att införa verifyPassword-metoden som tillåter att specificera ett lösenord som en instans av String och [kontrollerar om samma lösenord har använts för att skydda kalkylbladet](/cells/sv/java/verify-password-used-to-protect-the-worksheet/). Metoden Protection.verifyPassword returnerar true om det angivna lösenordet matchar det lösenord som användes för att skydda det angivna kalkylbladet, och false om det angivna lösenordet inte matchar. Följande kod använder Protection.verifyPassword-metoden i samarbete med Protection.isProtectedWithPassword-fältet för att upptäcka lösenordsskyddet och verifierar lösenordet.

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

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
### **Tillagt Protection.isProtectedWithPassword-egenskap**
Denna version av Aspose.Cells for Java har också exponerat Protection.isProtectedWithPassword-fältet som kan vara användbart för [att upptäcka om ett kalkylblad är lösenordsskyddat eller inte](/cells/sv/java/detect-if-worksheet-is-password-protected/).

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

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
### **Tillagt ColorScale.Is3ColorScale-egenskap**
Aspose.Cells for Java 8.7.0 har exponerat ColorScale.Is3ColorScale-egenskapen som kan användas för att [skapa 2-färgskaliga villkorlig formatering](/cells/sv/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/). Den angivna egenskapen är av typen Boolean med standardvärdet true, vilket innebär att den villkorliga formateringen standardmässigt kommer att vara av 3-färgskalatypen. Dock kommer att ändra ColorScale.Is3ColorScale-egenskapen till false att generera en 2-färgskalig villkorlig formatering.

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

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
### **Tillagt TxtLoadOptions.HasFormula-egenskap**
Aspose.Cells for Java 8.7.0 har gett stöd för att [identifiera & tolka formler vid inläsning av CSV/TXT-filer med delimiterad plandata](/cells/sv/java/load-or-import-csv-file-with-formulas/). Nyexponerade TxtLoadOptions.HasFormula-egenskapen när den är inställd på true dirigerar API:et att tolka formlerna från den inspelade filen med avgränsare och ställa in dem i relevanta celler utan att kräva någon ytterligare bearbetning.

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

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
### **Tillagt DataLabels.ResizeShapeToFitText-egenskap**
En annan användbar funktion som Aspose.Cells for Java 8.7.0 har exponerat är DataLabels.ResizeShapeToFitText-egenskapen som kan aktivera [ändra storlek på formen för att passa text](/cells/sv/java/resize-chart-s-data-label-shape-to-fit-text/) för Excels tillämpning av diagramdataetiketter.

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

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
## **Borttagen API:er**
### **Borttagen Workbook.SaveOptions-egenskap**
Workbook.SaveOptions-egenskapen markerades som föråldrad för en tid sedan. Med denna version har den helt tagits bort från den offentliga API:n, och därför rekommenderas det att använda Workbook.save(Stream, SaveOptions) eller Workbook.save(string, SaveOptions)-metoden som alternativ.
