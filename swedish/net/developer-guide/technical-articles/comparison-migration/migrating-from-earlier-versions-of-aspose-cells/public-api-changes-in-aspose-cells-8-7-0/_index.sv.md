---
title: Offentlig API Ändringar i Aspose.Cells 8.7.0
type: docs
weight: 230
url: /sv/net/public-api-changes-in-aspose-cells-8-7-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.6.3 till 8.7.0 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Stöd för VBA Project Digital Signing, Detection & Extraction**
Den här utgåvan av Aspose.Cells for .NET har avslöjat några nya egenskaper och metoder för att hjälpa användarna i uppgifter som att digitalt signera ett VBA-projekt, upptäcka om ett VBA-projekt är signerat och giltigt. Dessutom tillåter den nya API att extrahera certifikatet som rådata från digitalt signerade VBA-projekt i Workbook.
###### **Signera VBA-projekt digitalt**
 Aspose.Cells for .NET 8.7.0 har exponerat metoden VbaProject.Sign som kan användas för att[signera VBA-projektet digitalt i en arbetsbok](/cells/sv/net/digitally-sign-a-vba-code-project-with-certificate/). Den nämnda metoden accepterar en instans av klassen DigitalSignature som finns i namnområdet Aspose.Cells.DigitalSignatures.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Sign the VbaProject using the X509Certificate

vbaProject.Sign(new DigitalSignature(new System.Security.Cryptography.X509Certificates.X509Certificate2(cert), "Comments", DateTime.Now));

{{< /highlight >}}


###### **Detektering av digitalt signerat VBA-projekt**
 Nyligen exponerad VbaProject.IsSigned-egenskap kan användas för att in[upptäcka om VBA-projektet i en arbetsbok är digitalt signerat](/cells/sv/net/check-if-vba-code-is-signed/). Egenskapen VbaProject.IsSigned är av typen Boolean, som returnerar sant om VBA-projektet är digitalt signerat och vice versa.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Check if VbaProject is digitally signed

if (vbaProject.IsSigned)

{

    Console.WriteLine("VbaProject is digitally signed");

}

else

{

    Console.WriteLine("VbaProject is not digitally signed");

}

{{< /highlight >}}


###### **Extrahering av digital signatur från VBA Project**
Denna revidering av API har också avslöjat egenskapen VbaProject.CertRawData som tillåter att[extrahera det digitala certifikatets rådata från VBA-projektet](/cells/sv/net/export-vba-certificate-to-file-or-stream/). Egenskapen VbaProject.CertRawData är av typen byte array, som kommer att innehålla råcertifikatdata om VBA-projektet är digitalt signerat, annars kommer nämnda egenskap att vara null.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Extract digital signature in an array of bytes

var cert = vbaProject.CertRawData;

{{< /highlight >}}


###### **Validera den digitala signaturen för VBA-projektet**
 Ett annat tillägg till allmänheten API är egenskapen VbaProject.IsValidSigned som kan vara användbar i[validering av VBA-projektets digitala signatur](/cells/sv/net/check-if-digital-signature-of-vba-code-is-valid/). Den nämnda egenskapen returnerar true om den digitala signaturen är giltig och falsk om signaturen är ogiltig.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Check if VbaProject is digitally signed

if (vbaProject.IsSigned)

{

    //Check if signature is valid

    if (vbaProject.IsValidSigned)

    {

        Console.WriteLine("VbaProject is digitally signed & signature is valid");

    }

}

{{< /highlight >}}


### **Metod Protection.VerifyPassword har lagts till**
 Aspose.Cells for .NET 8.7.0 har exponerat metoden Protection.VerifyPassword som kan användas för att[verifiera lösenordet som används för att skydda arbetsbladet](/cells/sv/net/verify-password-used-to-protect-the-worksheet/)Den här metoden accepterar en instans av sträng som parameter och returnerar true om det angivna lösenordet matchar lösenordet som används för att skydda arbetsbladet.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

var sheet = book.Worksheets[0];

//Access Protection module of desired Worksheet

var protection = sheet.Protection;

//Verify the password for Worksheet

if (protection.VerifyPassword(password))

{

    Console.WriteLine("Password has matched");

}

else

{

    Console.WriteLine("Password did not match");

}

{{< /highlight >}}


### **Property Protection.IsProtectedWithPassword Added**
 Den här utgåvan av Aspose.Cells for .NET API har också avslöjat egenskapen Protection.IsProtectedWithPassword som kan vara användbar i[upptäcka om ett arbetsblad är lösenordsskyddat eller inte](/cells/sv/net/detect-if-worksheet-is-password-protected/).

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

var sheet = book.Worksheets[0];

//Access Protection module of desired Worksheet

var protection = sheet.Protection;

//Check if Worksheet is password protected

if (protection.IsProtectedWithPassword)

{

    Console.WriteLine("Worksheet is password protected");

}

else

{

    Console.WriteLine("Worksheet is not password protected");

}

{{< /highlight >}}


### **Egenskapen ColorScale.Is3ColorScale tillagd**
 Aspose.Cells for .NET 8.7.0 har exponerat egenskapen ColorScale.Is3ColorScale som kan användas för att skapa villkorsformat för 2-färgskala. Den nämnda egenskapen är av typen Boolean med standardvärdet true vilket betyder att det villkorliga formatet kommer att vara i 3-färgsskala som standard. Ändrar dock egenskapen ColorScale.Is3ColorScale till falsk vilja[generera ett villkorligt format med 2-färgsskala](/cells/sv/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/).

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the Worksheet to which conditional formatting rule has to be added

var sheet = book.Worksheets[0];

//Add FormatConditions to the collection

int index = sheet.ConditionalFormattings.Add();

//Access newly added formatConditionCollection via its index

var formatConditionCollection = sheet.ConditionalFormattings[index];

//Create a CellArea on which conditional formatting rule will be applied

var cellArea = CellArea.CreateCellArea("A1", "A5");

//Add conditional formatted cell range

formatConditionCollection.AddArea(cellArea);

//Add format condition of type ColorScale

index = formatConditionCollection.AddCondition(FormatConditionType.ColorScale);

//Access newly added format condition via its index

var formatCondition = formatConditionCollection[index];

//Set Is3ColorScale to false in order to generate a 2-Color Scale format

formatCondition.ColorScale.Is3ColorScale = false;

//Set other necessary properties

{{< /highlight >}}


### **Property TxtLoadOptions.HasFormula Added**
 Aspose.Cells for .NET 8.7.0 har tillhandahållit support till[identifiera och analysera formlerna medan du laddar CSV/TXT-filer med avgränsad vanlig data](/cells/sv/net/load-or-import-csv-file-with-formulas/). Den nyligen exponerade egenskapen TxtLoadOptions.HasFormula när den är satt till true dirigerar API att tolka formlerna från den indataavgränsade filen och ställa in dem på relevanta celler utan att kräva ytterligare bearbetning.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of TxtLoadOptions

var options = new TxtLoadOptions();

//Set HasFormula property to true

options.HasFormula = true;

//Set the Separator property as desired

options.Separator = ',';

//Load the CSV/TXT file using the instance of TxtLoadOptions

var book = new Workbook(inFilePath, options);

//Calculate formulas in order to get the calculated values of formula in CSV

book.CalculateFormula();

//Write result in any of the supported formats

book.Save(outFilePath);

{{< /highlight >}}


### **Egenskap DataLabels.IsResizeShapeToFitText tillagd**
 En annan användbar funktion som Aspose.Cells for .NET 8.7.0 har exponerat är egenskapen DataLabels.IsResizeShapeToFitText som kan aktivera[Ändra storlek på form för att passa text](/cells/sv/net/resize-chart-s-data-label-shape-to-fit-text/)funktion i Excel-applikationen för diagrammets dataetiketter.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook containing the Chart

var book = new Workbook(inFilePath);

//Access the Worksheet that contains the Chart

var sheet = book.Worksheets[0];

//Access the desired Chart via its index or name

var chart = sheet.Charts[0];

//Access the DataLabels of desired NSeries

var labels = chart.NSeries[0].DataLabels;

//Set ResizeShapeToFitText property to true

labels.IsResizeShapeToFitText = true;

//Calculate Chart

chart.Calculate();

{{< /highlight >}}


### **Egenskap PdfSaveOptions.OptimizationType tillagd**
Aspose.Cells for .NET 8.7.0 har exponerat egenskapen PdfSaveOptions.OptimizationType tillsammans med PdfOptimizationType-uppräkningen för att underlätta för användarna att[välj önskad optimeringsalgoritm när du exporterar kalkylblad till formatet PDF](/cells/sv/net/save-excel-into-pdf-with-standard-or-minimum-size/). Det finns två möjliga värden för egenskapen PdfSaveOptions.OptimizationType enligt beskrivningen nedan.

1. PdfOptimizationType.MinimumSize: Kvaliteten äventyras för den resulterande filstorleken.
1. PdfOptimizationType.Standard: Kvaliteten äventyras inte så den resulterande filstorleken blir stor.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of PdfSaveOptions

var pdfSaveOptions = new PdfSaveOptions();

//Set the OptimizationType property to desired value

pdfSaveOptions.OptimizationType = PdfOptimizationType.MinimumSize;

//Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook(inFilePath);

//Save the spreadsheet in PDF format while passing the instance of PdfSaveOptions

book.Save(outFilePath, pdfSaveOptions);

{{< /highlight >}}
## **Borttagna API:er**
### **Egenskapsarbetsbok.Sparaalternativ har tagits bort**
Egenskapen Workbook.SaveOptions markerades som föråldrad för en tid sedan. Med den här utgåvan har den tagits bort helt från den offentliga API, därför rekommenderas att använda metoden Workbook.Save(Stream, SaveOptions) eller Workbook.Save(string, SaveOptions) som alternativ.
