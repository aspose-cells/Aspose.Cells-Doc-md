---
title: Ställ in Shared Formula i Aspose.Cells
type: docs
weight: 110
url: /sv/net/setting-shared-formula-in-aspose-cells/
---
{{% alert color="primary" %}} 

Anta att du har ett kalkylblad fyllt med data.

 Du vill lägga till en funktion i B2 som kommer att beräkna momsen för den första raden med data. Skatten är**9%** Formeln som beräknar momsen är:**"=A2*0,09"**. Den här artikeln förklarar hur du använder den här formeln med Aspose.Cells.

{{% /alert %}} 

Aspose.Cells låter dig ange en formel med egenskapen Cell.Formula.

Det finns två alternativ för att lägga till formler till de andra cellerna (B3, B4, B5, och så vidare) i kolumnen.

Gör antingen som du gjorde för den första cellen, ställ in formeln för varje cell och uppdatera cellreferensen därefter (A3*0,09, A4*0,09, A5*0,09 och så vidare). Detta kräver att cellreferenserna för varje rad uppdateras. Det kräver också Aspose.Cells för att analysera varje formel individuellt, vilket kan vara tidskrävande för stora kalkylblad och komplexa formler. Det lägger också till extra rader med koder även om loopar kan skära ner dem något.

 Ett annat tillvägagångssätt är att använda en**delad formel**. Med en delad formel uppdateras formlerna automatiskt för cellreferenserna i varje rad så att skatten skulle beräknas korrekt. Metoden Cell.SetSharedFormula är mer effektiv än den första metoden.

Följande exempel visar hur man använder det.

**C#**

{{< highlight "csharp" >}}

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
## **Ladda ner exempelkod**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Shared%20Formula)
## **Ladda ner körningsexempel**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
