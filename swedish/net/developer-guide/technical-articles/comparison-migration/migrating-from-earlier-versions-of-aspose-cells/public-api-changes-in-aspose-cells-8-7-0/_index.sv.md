---
title: Offentliga API ändringar i Aspose.Cells 8.7.0
type: docs
weight: 230
url: /sv/net/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringarna i Aspose.Cells API från version 8.6.3 till 8.7.0 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade publika metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Stöd för digital signering, upptäckt och extrahering av VBA-projekt**
Denna version av Aspose.Cells for .NET har exponerat några nya egenskaper och metoder för att hjälpa användarna med uppgifter som att digitalt signera ett VBA-projekt, upptäcka om ett VBA-projekt är signerat och giltigt. Dessutom tillåter det nya API:et att extrahera certifikatet som rådata från digitalt signerat VBA-projekt i Workbook.
###### **Digitalt signera VBA-projekt**
Aspose.Cells for .NET 8.7.0 har exponerat VbaProject.Sign-metoden som kan användas för att [digitalt signera VBA-projektet i en Workbook](/cells/sv/net/digitally-sign-a-vba-code-project-with-certificate/). Sagda metod accepterar en instans av DigitalSignature-klassen som ligger i Aspose.Cells.DigitalSignatures-utrymmet.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Sign the VbaProject using the X509Certificate

vbaProject.Sign(new DigitalSignature(new System.Security.Cryptography.X509Certificates.X509Certificate2(cert), "Comments", DateTime.Now));

{{< /highlight >}}


###### **Upptäckt av digitalt signerat VBA-projekt**
Nyexponerad VbaProject.IsSigned-egenskap kan användas för att [upptäcka om VBA-projektet i en Workbook är digitalt signerat](/cells/sv/net/check-if-vba-code-is-signed/). VbaProject.IsSigned-egenskapen är av typen Boolean, vilket returnerar true om VBA-projektet är digitalt signerat och vice versa.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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


###### **Extrahering av digital signatur från VBA-projekt**
Denna revision av API:et har också exponerat VbaProject.CertRawData-egenskapen som tillåter att [extrahera det digitala certifikatets rådata från VBA-projektet](/cells/sv/net/export-vba-certificate-to-file-or-stream/). VbaProject.CertRawData-egenskapen är av typen byte array, vilken kommer att innehålla rå certifikatdata om VBA-projektet är digitalt signerat, annars kommer sagda egenskap att vara null.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Extract digital signature in an array of bytes

var cert = vbaProject.CertRawData;

{{< /highlight >}}


###### **Validera den digitala signaturen av VBA-projektet**
Ett annat tillägg till den offentliga API:n är VbaProject.IsValidSigned-egenskapen som kan vara användbar för [validering av den digitala signaturen av VBA-projektet](/cells/sv/net/check-if-digital-signature-of-vba-code-is-valid/). Sagda egenskap returnerar true om den digitala signaturen är giltig och false om signaturen är ogiltig.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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


### **Lagt till Protection.VerifyPassword-metod**
Aspose.Cells for .NET 8.7.0 har exponerat Protection.VerifyPassword-metoden som kan användas för att [verifiera lösenordet som används för att skydda Worksheet](/cells/sv/net/verify-password-used-to-protect-the-worksheet/). Denna metod accepterar en instans av sträng som parameter och returnerar true om det angivna lösenordet matchar med lösenordet som används för att skydda Worksheet.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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


### **Lagt till Protection.IsProtectedWithPassword-egenskap**
Denna version av Aspose.Cells for .NET API har också exponerat Protection.IsProtectedWithPassword-egenskapen som kan vara användbar för [att upptäcka om en Worksheet är lösenordsskyddad eller inte](/cells/sv/net/detect-if-worksheet-is-password-protected/).

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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


### **Tillagt ColorScale.Is3ColorScale-egenskap**
Aspose.Cells for .NET 8.7.0 har exponerat ColorScale.Is3ColorScale-egenskapen som kan användas för att skapa 2-färgs-skala villkorlig formatering. Sagda egenskap är av typen Boolean med standardvärdet true vilket innebär att den villkorliga formateringen kommer att vara av 3-färgs-skala som standard. Att ändra ColorScale.Is3ColorScale-egenskapen till false kommer dock att [generera en 2-färgs-skala villkorlig formatering](/cells/sv/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/).

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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


### **Tillagt TxtLoadOptions.HasFormula-egenskap**
Aspose.Cells for .NET 8.7.0 har tillhandahållit stöd för [identifiering & tolkning av formler vid inläsning av CSV/TXT-filer med avgränsade vanliga data](/cells/sv/net/load-or-import-csv-file-with-formulas/). Nyexponerad TxtLoadOptions.HasFormula Egenskap styr API: n att tolka formler från den indatadelade filen och ange dem till relevanta celler utan att behöva någon ytterligare bearbetning.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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


### **Lagt till DataLabels.IsResizeShapeToFitText Egenskap**
En annan användbar funktion Aspose.Cells for .NET 8.7.0 har exponerat är DataLabels.IsResizeShapeToFitText Egenskapen som kan aktivera [Ändra storlek på formen för att passa text](/cells/sv/net/resize-chart-s-data-label-shape-to-fit-text/) Excel applikationens funktion för diagramdataetiketter.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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


### **Lagt till PdfSaveOptions.OptimizationType Egenskap**
Aspose.Cells for .NET 8.7.0 har exponerat PdfSaveOptions.OptimizationType egenskap tillsammans med PdfOptimizationType uppräkning för att underlätta för användarna att [välja önskad optimeringsalgoritm vid export av kalkylblad till PDF-format](/cells/sv/net/save-excel-into-pdf-with-standard-or-minimum-size/). Det finns 2 möjliga värden för PdfSaveOptions.OptimizationType egenskapen enligt nedan.

1. PdfOptimizationType.MinimumSize: Kvalitet kompromissas för den resulterande filstorleken.
1. PdfOptimizationType.Standard: Kvaliteten kompromissas inte så den resulterande filstorleken kommer att vara stor.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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
## **Borttagen API:er**
### **Egenskap Arbetsbok.SparaAlternativ Borttagen**
Egenskapen Arbetsbok.SparaAlternativ markerades som föråldrad för en tid sedan. Med denna version har den tagits bort helt från den offentliga API: n och det rekommenderas därför att använda Arbetsbok.Spara(Ström, SparaAlternativ) eller Arbetsbok.Spara(sträng, SparaAlternativ) -metoden som ett alternativ.
