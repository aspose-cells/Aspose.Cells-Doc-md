---
title: Visa eller dölj flikar i Aspose.Cells
type: docs
weight: 80
url: /sv/net/display-or-hide-tabs-in-aspose-cells/
---
{{% alert color="primary" %}} 

Om du tittar noga på botten av en Microsoft Excel-fil kommer du att se ett antal kontroller. Dessa inkluderar:

- Bladflikar.
- Tabbrullningsknappar.

Bladflikar representerar kalkylbladen i Excel-filen. Klicka på valfri flik för att växla till det kalkylbladet. Ju fler kalkylblad i arbetsboken, desto fler flikar finns det. Om Excel-filen har ett stort antal kalkylblad behöver du knappar för att navigera genom dem. Så, Microsoft Excel tillhandahåller flikrullningsknappar för att rulla igenom arkflikarna.

**Bladflikar & flikrullningsknappar** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_1.png)

Med hjälp av Aspose.Cells kan utvecklare styra synligheten för arkflikar och flikars rullningsknappar i Excel-filer.

{{% /alert %}} 

Nedan är ett komplett exempel som öppnar en Excel-fil (book1.xls), gömmer dess flikar och sparar den ändrade filen som output.xls.

Du kan se att filen Book1.xls innehåller flikar i figuren nedan. Efter att exempelkoden har körts är flikarna dolda, som du kan se från skärmdumpen av filen output.xls nedan.

**book1.xls: Excel-fil före eventuella ändringar** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_2.png)

**output.xls: Excel-fil efter modifiering** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_3.png)

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

//Opening the Excel file

Workbook workbook = new Workbook("book1.xls");

//Hiding the tabs of the Excel file

workbook.Settings.ShowTabs = false;

//Saving the modified Excel file

workbook.Save("output.xls");



{{< /highlight >}}
## **Styra flikfältets bredd**
**C#**

{{< highlight "csharp" >}}

 //Adjusting the sheet tab bar width

workbook.Worksheets.SheetTabBarWidth = 800;



{{< /highlight >}}
## **Ladda ner Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Tabs)
## **Ladda ner provkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
