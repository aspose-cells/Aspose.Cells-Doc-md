---
title: Visa eller dölj flikar i Aspose.Cells
type: docs
weight: 80
url: /sv/net/display-or-hide-tabs-in-aspose-cells/
---

{{% alert color="primary" %}} 

Om du tittar noga längst ner i en Microsoft Excel-fil, kommer du att se ett antal kontroller. Dessa inkluderar:

- Arkflikar.
- Flikbläddringsknappar.

Arkflikar representerar arbetsbladen i Excel-filen. Klicka på vilken flik som helst för att växla till det arbetsbladet. Ju fler arbetsblad i arbetsboken, desto fler arkflikar finns det. Om Excel-filen har ett bra antal arbetsblad behöver du knappar för att navigera genom dem. Så tillhandahåller Microsoft Excel flikbläddringsknappar för att bläddra igenom arkflikarna.

**Arkflikar & flikbläddringsknappar** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_1.png)

Genom att använda Aspose.Cells kan utvecklare kontrollera synligheten av arkflikar och flikbläddringsknappar i Excel-filer. 

{{% /alert %}} 

Här nedan följer ett komplett exempel som öppnar en Excel-fil (book1.xls), gömmer dess flikar och sparar den modifierade filen som output.xls.

Du kan se att filen Book1.xls innehåller flikar i figuren nedan. Efter att exempelkoden har utförts göms flikarna, som du kan se på skärmbilden av filen output.xls nedan.

**book1.xls: Excel-fil innan någon modifiering** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_2.png)

**output.xls: Excel-fil efter modifiering** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_3.png)

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

//Opening the Excel file

Workbook workbook = new Workbook("book1.xls");

//Hiding the tabs of the Excel file

workbook.Settings.ShowTabs = false;

//Saving the modified Excel file

workbook.Save("output.xls");



{{< /highlight >}}
## **Styra fliken Bredd**
**C#**

{{< highlight csharp >}}

 //Adjusting the sheet tab bar width

workbook.Worksheets.SheetTabBarWidth = 800;



{{< /highlight >}}
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Tabs)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
