---
title: Offentlig API Ändringar i Aspose.Cells 8.6.1
type: docs
weight: 200
url: /sv/net/public-api-changes-in-aspose-cells-8-6-1/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.6.0 till 8.6.1 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda klasser, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Stöd för HTML-länkmåltyp**
Den här utgåvan av Aspose.Cells for .NET API har avslöjat en uppräkning nämligen HtmlLinkTargetType tillsammans med en ny egenskap HtmlSaveOptions.LinkTargetType som tillsammans tillåter att[ställ in måltypen för länkarna i kalkylbladet vid konvertering till HTML-format](/cells/sv/net/change-the-html-link-target-type/). De möjliga värdena för HtmlLinkTargetType-uppräkningen följer där standardvärdet är Self.

1. HtmlLinkTargetType.Blank: Öppnar det länkade dokumentet/sidan i ett nytt fönster eller flik.
1. HtmlLinkTargetType.Parent: Öppnar det länkade dokumentet/sidan i den överordnade ramen.
1. HtmlLinkTargetType.Self: Öppnar det länkade dokumentet/sidan i samma ram där länken klirrades.
1. HtmlLinkTargetType.Top: Öppnar det länkade dokumentet/sidan i hela fönstret.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.LinkTargetType = HtmlLinkTargetType.Blank;

//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.Save(outputFilePath, options);

{{< /highlight >}}


### **Metod VbaModuleCollection.Remove tillagd**
Aspose.Cells for .NET 8.6.1 har avslöjat ytterligare en överbelastning av metoden VbaModuleCollection.Remove som nu kan acceptera en instans av Worksheet för att ta bort alla VBA-moduler som är associerade med det angivna arbetsbladet.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.VbaProject.Modules;

//Remove the VBA modules from specific Worksheet

modules.Remove(workbook.Worksheets[0]);

{{< /highlight >}}


### **Metod RangeCollection.Add tillagd**
Aspose.Cells for .NET 8.6.1 har exponerat metoden RangeCollection.Add som kan användas för att lägga till Range-objekt till samlingen av intervall för ett visst kalkylblad.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.Worksheets[0].Cells;

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.Ranges;

//Add another range to the collection

ranges.Add(cells.CreateRange("A1:B4"));

{{< /highlight >}}


### **Metod Cell.SetCharacters tillagd**
 Metoden Cell.SetCharacters kan användas för att[uppdatera delarna av den rika texten](/cells/sv/net/access-and-update-the-portions-of-rich-text-of-cell/) av ett givet Cell objekt. Metoden Cell.GetCharacters ska användas för att komma åt delarna av texten och sedan kan ändringar göras med metoden Cell.SetCharacters medan**Skaffa sig** metod returnerar en uppsättning FontSetting-objekt som kan manipuleras för att ställa in olika egenskaper typsnittsnamn, teckensnittsfärg, fetstil etc.**Uppsättning** metod kan användas för att tillämpa ändringarna.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.Worksheets[0];

//Access the cells containing the Rich Text

Cell cell = worksheet.Cells["A1"];

//Retrieve the array of FontSetting from the cell

FontSetting[]settings = cell.GetCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].Font.Name = "Arial";

//Set the updated FontSetting

cell.SetCharacters(settings);

{{< /highlight >}}


### **Egenskapen VbaProject.IsSigned tillagd**
 Aspose.Cells for .NET 8.6.1 har exponerat egenskapen VbaProject.IsSigned som kan användas för att[testa om ett VbaProject i en arbetsbok är signerat eller inte](/cells/sv/net/check-if-vba-project-in-a-workbook-is-signed/). Boolesk typ egenskap returnerar true om projektet är signerat.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VbaProject from the Workbook

VbaProject project = workbook.VbaProject;

//Test if VbaProject is signed

if (project.IsSigned)

{

    Console.WriteLine("VBA Project is Signed");

}

else

{

    Console.WriteLine("VBA Project is not Signed");

}

{{< /highlight >}}
## **Ändrade API:er**
### **Metod Cell.GetFormatConditions Modified**
Med lanseringen av v8.6.1 har Aspose.Cells for .NET API ändrat returtypen för metoden Cell.GetFormatConditions som nu returnerar en array av typen FormatConditionCollection.
## **Föråldrade API:er**
### **Metod Workbook.CheckWriteProtectedPassword föråldrat**
Med lanseringen av v8.6.1 har metoden Workbook.CheckWriteProtectedPassword markerats som avskriven. Det rekommenderas att använda metoden WorkbookSettings.WriteProtection.ValidatePassword som kan acceptera ett strängvärde som parameter och returnerar booleskt om lösenordet matchar det förinställda lösenordet för kalkylarket.
