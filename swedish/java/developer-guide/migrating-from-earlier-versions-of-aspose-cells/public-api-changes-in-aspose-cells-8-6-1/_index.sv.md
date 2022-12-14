---
title: Offentliga API-ändringar i Aspose.Cells 8.6.1
type: docs
weight: 210
url: /sv/java/public-api-changes-in-aspose-cells-8-6-1/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.6.0 till 8.6.1 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda klasser, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Stöd för HTML-länkmåltyp**
Den här versionen av Aspose.Cells för Java API har avslöjat en uppräkning nämligen HtmlLinkTargetType tillsammans med en ny egenskap HtmlSaveOptions.LinkTargetType som tillsammans gör det möjligt att[ställ in måltypen för länkarna i kalkylbladet vid konvertering till HTML-format](/cells/sv/java/change-the-html-link-target-type/). De möjliga värdena för HtmlLinkTargetType-uppräkningen följer där standardvärdet är SELF.

1. HtmlLinkTargetType.BLANK: Öppnar det länkade dokumentet/sidan i ett nytt fönster eller en ny flik.
1. HtmlLinkTargetType.PARENT: Öppnar det länkade dokumentet/sidan i den överordnade ramen.
1. HtmlLinkTargetType.SELF: Öppnar det länkade dokumentet/sidan i samma ram där länken klirrades.
1. HtmlLinkTargetType.TOP: Öppnar det länkade dokumentet/sidan i hela fönstret.

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.setLinkTargetType(HtmlLinkTargetType.BLANK);


//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.save(outputFilePath, options);

{{< /highlight >}}
### **Metod VbaModuleCollection.remove Tillagd**
Aspose.Cells för Java 8.6.1 har avslöjat ytterligare en överbelastning av metoden VbaModuleCollection.remove som nu kan acceptera en instans av Worksheet för att ta bort alla VBA-moduler som är associerade med det angivna arbetsbladet.

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from specific Worksheet

modules.remove(workbook.getWorksheets().get(0));

{{< /highlight >}}
### **Metod RangeCollection.add tillagd**
Aspose.Cells för Java 8.6.1 har avslöjat metoden RangeCollection.Add som kan användas för att lägga till Range-objekt till samlingen av intervall för ett visst kalkylblad.

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.getWorksheets().get(0).getCells();

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.getRanges();

//Add another range to the collection

ranges.add(cells.createRange("A1:B4"));

{{< /highlight >}}
### **Metod Cell.setCharacters tillagd**
 Metoden Cell.setCharacters kan användas för att[uppdatera delarna av den rika texten](/cells/sv/java/access-and-update-the-portions-of-rich-text-of-cell/) av ett givet Cell objekt. Metoden Cell.getCharacters ska användas för att komma åt delarna av texten och sedan kan ändringar göras med metoden Cell.setCharacters medan**skaffa sig** metod returnerar en uppsättning FontSetting-objekt som kan manipuleras för att ställa in olika egenskaper typsnittsnamn, teckensnittsfärg, fetstil etc.**uppsättning** metod kan användas för att tillämpa ändringarna.

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cells containing the Rich Text

Cell cell = worksheet.getCells().get("A1");

//Retrieve the array of FontSetting from the cell

FontSetting[]settings = cell.getCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].getFont().setName("Arial");

//Set the updated FontSetting

cell.setCharacters(settings);

{{< /highlight >}}
### **Egenskapen VbaProject.isSignad tillagd**
 Aspose.Cells för Java 8.6.1 har exponerat egenskapen VbaProject.isSigned som kan användas för att[testa om ett VbaProject i en arbetsbok är signerat eller inte](/cells/sv/java/check-if-vba-project-in-a-workbook-is-signed/). Boolesk typ egenskap returnerar true om projektet är signerat.

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VbaProject from the Workbook

VbaProject project = workbook.getVbaProject();

//Test if VbaProject is signed

if (project.isSigned())

{

    System.out.println("VBA Project is Signed");

}

else

{

	System.out.println("VBA Project is not Signed");

}

{{< /highlight >}}
## **Ändrade API:er**
### **Metod Cell.getFormatConditions Modified**
Med lanseringen av v8.6.1 har API:et Aspose.Cells för Java ändrat returtypen för metoden Cell.getFormatConditions som nu returnerar en array av typen FormatConditionCollection.
## **Föråldrade API:er**
### **Metod Workbook.checkWriteProtectedPassword föråldrat**
Med lanseringen av v8.6.1 har metoden Workbook.checkWriteProtectedPassword markerats som avskriven. Det rekommenderas att använda metoden WorkbookSettings.WriteProtection.validatePassword som kan acceptera ett strängvärde som parameter och returnerar booleskt om lösenordet matchar det förinställda lösenordet för kalkylarket.
