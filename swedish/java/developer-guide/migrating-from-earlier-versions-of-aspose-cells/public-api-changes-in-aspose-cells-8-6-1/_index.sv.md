---
title: Ändringar i offentlig API i Aspose.Cells 8.6.1
type: docs
weight: 210
url: /sv/java/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna i Aspose.Cells API från version 8.6.0 till 8.6.1 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda klasser, utan också en beskrivning av eventuella ändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Stöd för HTML Länk Måltyp**
Denna release av Aspose.Cells for Java API har exponerat en uppräkning, nämligen HtmlLinkTargetType tillsammans med en ny egenskap HtmlSaveOptions.LinkTargetType som tillsammans möjliggör att [sätta måltypen för länkarna i kalkylblad vid konvertering till HTML-format](/cells/sv/java/change-the-html-link-target-type/). De möjliga värdena för uppräkningen HtmlLinkTargetType är följande där standardvärdet är SELF.

1. HtmlLinkTargetType.BLANK: Öppnar det länkade dokumentet/sidan i ett nytt fönster eller flik.
1. HtmlLinkTargetType.PARENT: Öppnar det länkade dokumentet/sidan i föräldrarfönstret.
1. HtmlLinkTargetType.SELF: Öppnar det länkade dokumentet/sidan i samma fönster där länken klickades.
1. HtmlLinkTargetType.TOP: Öppnar det länkade dokumentet/sidan i hela fönstrets kropp.

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.setLinkTargetType(HtmlLinkTargetType.BLANK);


//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.save(outputFilePath, options);

{{< /highlight >}}
### **Tillagd VbaModuleCollection.remove Metod**
Aspose.Cells for Java 8.6.1 har exponerat en annan överbelastning av VbaModuleCollection.remove-metoden som nu kan acceptera en instans av Worksheet för att ta bort alla VBA-moduler som är associerade med den angivna Worksheet.

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from specific Worksheet

modules.remove(workbook.getWorksheets().get(0));

{{< /highlight >}}
### **Lade till RangeCollection.add-metoden**
Aspose.Cells for Java 8.6.1 har exponerat RangeCollection.Add-metoden som kan användas för att lägga till Range-objekt i samlingen av intervall för en specifik Worksheet.

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.getWorksheets().get(0).getCells();

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.getRanges();

//Add another range to the collection

ranges.add(cells.createRange("A1:B4"));

{{< /highlight >}}
### **Lade till Cell.setCharacters-metoden**
Cell.setCharacters-metoden kan användas för att [uppdatera delar av den rika texten](/cells/sv/java/access-and-update-the-portions-of-rich-text-of-cell/) för en given Cell-objekt. Cell.getCharacters-metoden ska användas för att komma åt delar av texten och sedan kan ändringar göras med Cell.setCharacters-metoden, medan **get**-metoden returnerar en matris av FontSetting-objekt som kan manipuleras för att ställa in olika egenskaper som teckensnittsnamn, teckenfärg, fetstil osv och **set**-metoden kan användas för att tillämpa ändringarna.

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cells containing the Rich Text

Cell cell = worksheet.getCells().get("A1");

//Retrieve the array of FontSetting from the cell

FontSetting[] settings = cell.getCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].getFont().setName("Arial");

//Set the updated FontSetting

cell.setCharacters(settings);

{{< /highlight >}}
### **Lade till VbaProject.isSigned-egenskapen**
Aspose.Cells for Java 8.6.1 har exponerat VbaProject.isSigned-egenskapen som kan användas för att [testa om ett VbaProject i en Workbook är signerat eller inte](/cells/sv/java/check-if-vba-project-in-a-workbook-is-signed/). Boolesk typegenskap returnerar true om projektet är signerat.

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

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
## **Modifierade API:er**
### **Modifierade Cell.getFormatConditions-metoden**
Med utgåvan av v8.6.1 har Aspose.Cells for Java API modifierat returtypen för Cell.getFormatConditions-metoden som nu returnerar en matris av typ FormatConditionCollection.
## **Obsoletterade API:er**
### **Obsolet Workbook.checkWriteProtectedPassword-metod**
Med utgåvan av v8.6.1 har Workbook.checkWriteProtectedPassword-metoden markerats som föråldrad. Det rekommenderas att använda WorkbookSettings.WriteProtection.validatePassword-metoden som kan acceptera en String-värde som parameter och returnerar Boolean om lösenordet matchar det förinställda lösenordet för kalkylbladet.
