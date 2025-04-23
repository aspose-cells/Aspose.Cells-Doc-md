---
title: Ändringar i offentlig API i Aspose.Cells 8.6.1
type: docs
weight: 200
url: /sv/net/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna i Aspose.Cells API från version 8.6.0 till 8.6.1 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda klasser, utan också en beskrivning av eventuella ändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Stöd för HTML Länk Måltyp**
Denna release av Aspose.Cells for .NET API har exponerat en uppräkning, nämligen HtmlLinkTargetType tillsammans med en ny egenskap HtmlSaveOptions.LinkTargetType som tillsammans möjliggör att [sätta måltypen för länkar i kalkylarket vid konvertering till HTML-format](/cells/sv/net/change-the-html-link-target-type/). De möjliga värdena av HtmlLinkTargetType-uppräkningen är följande där standardvärdet är Self.

1. HtmlLinkTargetType.Blank: Öppnar det länkade dokumentet/sidan i ett nytt fönster eller flik.
1. HtmlLinkTargetType.Parent: Öppnar det länkade dokumentet/sidan i föräldrame.
1. HtmlLinkTargetType.Self: Öppnar det länkade dokumentet/sidan i samma ram där länken klickades.
1. HtmlLinkTargetType.Top: Öppnar det länkade dokumentet/sidan i hela fönstrets kropp.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.LinkTargetType = HtmlLinkTargetType.Blank;

//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.Save(outputFilePath, options);

{{< /highlight >}}


### **Tillagd VbaModuleCollection.Remove-metod**
Aspose.Cells for .NET 8.6.1 har exponerat en annan överbelastning av VbaModuleCollection.Remove-metoden som nu kan acceptera en instans av Worksheet för att ta bort alla VBA-moduler som är associerade med den angivna Worksheet.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.VbaProject.Modules;

//Remove the VBA modules from specific Worksheet

modules.Remove(workbook.Worksheets[0]);

{{< /highlight >}}


### **Tillagd RangeCollection.Add-metod**
Aspose.Cells for .NET 8.6.1 har exponerat RangeCollection.Add-metoden som kan användas för att lägga till Range-objekt till samlingen av intervall för en specifik Worksheet.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.Worksheets[0].Cells;

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.Ranges;

//Add another range to the collection

ranges.Add(cells.CreateRange("A1:B4"));

{{< /highlight >}}


### **Tillagd Cell.SetCharacters-metod**
Cell.SetCharacters-metoden kan användas för att [uppdatera delarna av den rika texten](/cells/sv/net/access-and-update-the-portions-of-rich-text-of-cell/) i en given Cell-objekt. Cell.GetCharacters-metoden ska användas för att komma åt delarna av texten och sedan kan ändringar göras med Cell.SetCharacters-metoden medan **Get**-metoden returnerar en array av FontSetting-objekt som kan manipuleras för att ställa in olika egenskaper, till exempel fontnamn, fontfärg, fetstil osv, och **Set**-metoden kan användas för att tillämpa ändringarna.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.Worksheets[0];

//Access the cells containing the Rich Text

Cell cell = worksheet.Cells["A1"];

//Retrieve the array of FontSetting from the cell

FontSetting[] settings = cell.GetCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].Font.Name = "Arial";

//Set the updated FontSetting

cell.SetCharacters(settings);

{{< /highlight >}}


### **Tillagd VbaProject.IsSigned-egenskap**
Aspose.Cells for .NET 8.6.1 har exponerat VbaProject.IsSigned-egenskapen som kan användas för att [testa om ett VbaProject i en arbetsbok är signerat eller ej](/cells/sv/net/check-if-vba-project-in-a-workbook-is-signed/). Boolesk typ egenskap returnerar true om projektet är signerat.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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
## **Modifierade API:er**
### **Modifierad Cell.GetFormatConditions-metod**
Med släppet av v8.6.1 har Aspose.Cells for .NET API:et modifierat returtypen för Cell.GetFormatConditions-metoden som nu returnerar en array av typ FormatConditionCollection.
## **Obsoletterade API:er**
### **Föråldrad Workbook.CheckWriteProtectedPassword-metod**
Med släppet av v8.6.1 har Workbook.CheckWriteProtectedPassword-metoden markerats som föråldrad. Det rekommenderas att använda WorkbookSettings.WriteProtection.ValidatePassword-metoden som kan acceptera en sträng som parameter och returnerar Boolesk om lösenordet matchar det förinställda lösenordet för kalkylarket.
{{< app/cells/assistant language="csharp" >}}
