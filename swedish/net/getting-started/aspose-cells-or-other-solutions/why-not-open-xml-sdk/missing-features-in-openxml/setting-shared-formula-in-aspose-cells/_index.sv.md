---
title: Ange delad formel i Aspose.Cells
type: docs
weight: 110
url: /sv/net/setting-shared-formula-in-aspose-cells/
---

{{% alert color="primary" %}} 

Anta att du har ett kalkylblad fyllt med data.

Du vill lägga till en funktion i B2 som kommer att beräkna momsen för den första dataraden. Skatten är **9%**. Formeln som beräknar momsen är: **"=A2*0.09"**. Den här artikeln förklarar hur man tillämpar denna formel med Aspose.Cells.

{{% /alert %}} 

Aspose.Cells låter dig specificera en formel med hjälp av Cell.Formula-egenskapen.

Det finns två alternativ för att lägga till formler i de andra cellerna (B3, B4, B5, och så vidare) i kolumnen.

Antingen göra som du gjorde för den första cellen, vilket effektivt anger formeln för varje cell och uppdaterar cellreferensen därefter (A3*0.09, A4*0.09, A5*0.09 och så vidare). Detta kräver att cellreferenserna för varje rad uppdateras. Det kräver också att Aspose.Cells tolkar varje formel individuellt, vilket kan ta tid för stora kalkylblad och komplexa formler. Det lägger också till extra rader kod även om loopar kan minska dem något.

Ett annat tillvägagångssätt är att använda en **delad formel**. Med en delad formel uppdateras formulären automatiskt för cellreferenserna i varje rad så att momsen beräknas korrekt. Metoden Cell.SetSharedFormula är mer effektiv än den första metoden.

Följande exempel visar hur du använder den.

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Shared Formula.xlsx";

//Instantiate a Workbook from existing file

Workbook workbook = new Workbook(FileName);

//Get the cells collection in the first worksheet

Aspose.Cells.Cells cells = workbook.Worksheets[0].Cells;

//Apply the shared formula in the range i.e.., B2:B14

cells["B2"].SetSharedFormula("=A2*0.09", 13, 1);

//Save the excel file

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **Ladda ned provkoden**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Shared%20Formula)
## **Ladda ner exempel på körning**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
