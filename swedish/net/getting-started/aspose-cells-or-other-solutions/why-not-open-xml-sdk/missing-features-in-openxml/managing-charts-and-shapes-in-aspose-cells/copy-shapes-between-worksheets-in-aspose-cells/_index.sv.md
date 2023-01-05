---
title: Kopiera former mellan kalkylblad på Aspose.Cells
type: docs
weight: 30
url: /sv/net/copy-shapes-between-worksheets-in-aspose-cells/
---
{{% alert color="primary" %}} 

Ibland behöver du kopiera element på ett kalkylblad, till exempel bilder, diagram och andra ritobjekt, mellan kalkylblad. Aspose.Cells stöder den här funktionen. Diagram, bilder och andra objekt kan kopieras med högsta precision.

Den här artikeln ger dig en detaljerad förståelse för hur du kopierar former mellan kalkylblad. För att illustrera skapar den en konsolapplikation i Visual Studio.Net, kopierar bilder, diagram och andra ritobjekt mellan kalkylblad med hjälp av Aspose.Cells.

{{% /alert %}} 

Nedan finns koden för att kopiera ett diagram från kalkylblad till ett annat

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Copy Shapes between Worksheets.xlsx";

//Open the template file

Workbook workbook = new Workbook(FileName);

//Get the Chart from the "Chart" worksheet.

Aspose.Cells.Charts.Chart source = workbook.Worksheets["Chart"].Charts[0];

Aspose.Cells.Drawing.ChartShape cshape = source.ChartObject;

//Copy the Chart to the Result Worksheet

workbook.Worksheets["Result"].Shapes.AddCopy(cshape, 20, 0, 2, 0);

//Save the Worksheet

workbook.Save(FileName);



{{< /highlight >}}

**Notera:** För mer information om att kopiera flera former behöver du besöka[här](/cells/sv/net/copy-shapes-between-worksheets/)
## **Ladda ner provkod**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)
## **Ladda ner körningsexempel**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
