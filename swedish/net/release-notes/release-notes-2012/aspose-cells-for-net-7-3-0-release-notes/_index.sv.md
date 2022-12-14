---
title: Aspose.Cells för .NET 7.3.0 Release Notes
type: docs
weight: 50
url: /sv/net/aspose-cells-for-net-7-3-0-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 7.3.0](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-7.3.0/)

{{% /alert %}} 

 Vi är glada att kunna meddela Aspose.Cells för .NETv7.3.0 för användarna!



\1) Aspose.Cells 



 Nya egenskaper

 40701 - Stöd för läsning och skrivning av MHT-filer

- Stöd XML-kartor



 Förbättringar

- Problem med version som stöds av mono
- Kan inte använda formeln som parameter för
- Kan anpassade funktioner returnera intervall som kan användas för att SUMMA på
- Tillämpa teman på diagram
- Problem med att formeln refererar till en bild



 Undantag

- Delsumma genererar Runtime-fel
- Undantag görs när du anropar Cell.GetPrecedents()-metoden
- Undantaget "Ogiltigt startradindex" vid delsummor



 Buggar

- Problem med SheetRenders XPS och anpassade nummerformat
- Diagrammets legendobjekt lindas när du sparar som en bild
- Bugg sheets diagram visas inte
- Ett problem med metoden Cells.ExportDataTableAsString() och anpassad formatering
- Ett allvarligt problem med pivottabellen
- Använder metoden Workbook.CalculateFormula() på flera arbetsböcker på flygives #VALUE
- PDF-rendering av affärsformer (text inuti) är inte trevligt
- Problem med XLS innehållsförteckning baserat på antalet utskrivna sidor

 - PDF-konverteringen missar värdena för de namngivna områdena

- Att referera till celler med värden från matrisformler fungerar inte

 -Cells Formateringsproblem

- Problem med formeln som refererar till en bild
- Matrisformler i SpreadsheetML överförs inte vid konvertering till XLSX
- Förlorar namngivna intervall bugg i XLSM



 \2) Aspose.Cells.GridWeb



 Buggar

- Ett problem med CellCommand-hyperlänkar
- Cell.Validation skickar en InvalidOperationException-regression
- Aspose.Cells.GridWeb-kontroll kraschar för en Excel-fil


