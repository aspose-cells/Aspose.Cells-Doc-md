---
title: Aspose.Cells för .NET 7.3.4 Release Notes
type: docs
weight: 10
url: /sv/net/aspose-cells-for-net-7-3-4-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 7.3.4](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-7.3.4/)

{{% /alert %}} 

 Vi är glada att kunna meddela Aspose.Cells för .NET v7.3.4!



\1) Aspose.Cells 



 Nya egenskaper

- Stöd för Open Office 3D-diagram
- Beräkna vägt medelvärde på delsummaraden mellan två kolumner (SmartMarkers)
- Upptäck vertikal eller horisontell datakälla för ett diagram



 Förbättringar

- Hitta och ersätt inre texter



 Prestanda

- Arbetsbokens CalculateFormula-metod tar 30+ sekunder
- Prestandaförsämring för Office 2007 jämfört med 2003

 -CalculateFormula tar cirka 3 minuter på 8 Core-maskin

- Aspose Cell ersätter Excel Wrapper
- Att spara ett Excel-dokument tar mer än en minut



 Undantag

- Undantaget "Ogiltig formel" när du öppnar en XLSX-fil
- Aspose.Cells kastar "ArgumentNullException" undantag när en mallfil öppnas
- Att spara en MHtml-fil, läsa in Aspose.Cells är ett problem



 Buggar

- Formeln är inte korrekt beräknad
- ActiveX-kontroller skadar en arbetsbok
- 4 Kalkylblad kunde inte skrivas om
- Excel-diagram är låsta efter spara
- Fel vid kopiering av arbetsblad

 -Fylld radargrafbild renderad med dolda Axis Tick-markeringar via metoden Chart.ToImage

 - Problem med formatering av dataetiketter

- Problem med att beräkna Excel-diagram
- Problem med ett kolumndiagram med båda axlarna
- Flera beräknade pivotfält resulterar i en oläsbar fil.
- Problem med anpassade XML-delar
- Den här filen är skadad efter att ha sparats

 -Konvertering av XLS till XLSX och tillbaka skapar en dålig XLS-fil

 -Konvertering av XLS till XLSX skapar ett dåligt dokument

- Att rendera en MS Excel-fil till PDF-dokument har ett problem med innehållet



 \2) GridWeb



 Buggar

 40838 - GridWeb - Formateringen har inte sparats korrekt

 41140 - Problem när du använder alternativet "Lägg till rad".

 41152 - När du redigerar Aspose.Cells.GridWeb, hoppar cell runt när den är markerad

 41154 - Renderingsproblem på GridWeb-kontroll

 41149 - Markera problem med GridWeb-kontroll

41183 - 

 41126 - GridWeb Cells stil BorderWidth-problem



 \3) GridDesktop



 Buggar

40709 - GridDesktops renderingsproblem

41098 - Cell Skydds-/låsningsproblem med GridDesktop
