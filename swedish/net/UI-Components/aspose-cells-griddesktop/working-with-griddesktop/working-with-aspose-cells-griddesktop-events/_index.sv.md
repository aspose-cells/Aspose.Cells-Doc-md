---
title: Arbetar med Aspose.Cells.GridDesktop Events
type: docs
weight: 30
url: /sv/net/working-with-aspose-cells-griddesktop-events/
---
{{% alert color="primary" %}} 

Händelser används för att skicka meddelanden när en förändring sker i en kontroll eller klass. Aspose.Cells.GridDesktop har flera händelser som används för att utföra specifika uppgifter när vissa ändringar sker i kontrollen. Det här ämnet ger en introduktion till alla händelser som stöds av Aspose.Cells.GridDesktop-kontrollen och förklarar hur man kan hantera dessa händelser.

{{% /alert %}} 
## **Introduktion**
Kontrollen Aspose.Cells.GridDesktop stöder flera händelser som ger mer kontroll för att utföra operationer när specifika händelser utlöses. Nedan finns en komplett lista över händelser som stöds av Aspose.Cells.GridDesktop-kontrollen.

{{% alert color="primary" %}} 

Den här listan inkluderar inte de händelser som ärvs av Aspose.Cells.GridDesktop från klassen Control.

{{% /alert %}} 

|**evenemang**|**Beskrivning**|
|:- |:- |
|Före Beräkna|Förekommer före beräkna formeln i arbetsboken.|
|BeforeLoadFile|Uppstår innan arbetsboken laddas från filen.|
|ColumnHeaderKlicka|Uppstår när kolumnrubriken klickas.|
|ColumnHeaderDoubleClick|Uppstår när kolumnrubriken dubbelklickas.|
|CellDataChanged|Uppstår när data eller värde i en rutnätscell ändras. Denna händelse kan också utlösas om en cells värde ändras programmatiskt med hjälp av egenskapen Value eller metoden SetCellValue för en GridCell.|
|CellButtonClick|Uppstår när cellknappen klickas.|
|CellCheckedChanged|Uppstår när kryssrutan Checked-egenskapen för cell ändras.|
|CellSelectedIndexChanged|Uppstår när egenskapen SelectedIndex för cellkombinationsrutan ändras.|
|CellClick|Uppstår när en rutnätscell klickas.|
|CellDoubleClick|Uppstår när en rutnätscell dubbelklickas.|
|CellKeyPressed|Uppstår när en tangent trycks ned medan en cell har fokus. Om du vill skapa en händelsehanterare för CellKeyPressed-händelsen ställer du in Handled-egenskapen för CellKeyEventArgs-argumentet till true för att förhindra GridDesktop-kontrollen från att hantera nyckelhändelsen.|
|AfterInsertColumns|Uppstår när en kolumn infogas. Du kan få kolumnindex genom att använda Aspose.Cells.GridDesktop.WorksheetEventArgs argumentets Index-egenskap.|
|AfterInsertRows|Uppstår när en rad infogas. Du kan få radindexet genom att använda Aspose.Cells.GridDesktop.WorksheetEventArgs argumentets Index-egenskap.|
|FailLoadFile|Uppstår när det inte går att läsa in arbetsboken.|
|Avsluta Beräkna|Uppstår efter beräkna formeln i arbetsboken.|
|FinishLoadFile|Uppstår när arbetsboken laddas.|
|FocusedCellChanged|Uppstår närhelst en cells fokus ändras.|
|RowHeaderClick|Uppstår när radhuvudet klickas.|
|RowHeaderDoubleClick|Uppstår när radhuvudet dubbelklickas.|
|RowColumnHiddenChanged|Uppstår när radens eller kolumns dolda status ändras.|
|SelectedSheetIndexChanged|Uppstår när en användare väljer ett nytt kalkylblad, det vill säga när det valda bladet ändras från ett kalkylblad till ett annat. Den här händelsen kan också utlösas programmatiskt om GridDesktop-kontrollens ActiveSheetIndex-egenskap ändras.|
## **Hantering av Grid Events**
För att utföra en specifik operation när en specifik händelse utlöses, skapa en händelsehanterare. En händelsehanterare utför en viss uppgift när en viss händelse utlöses. Nedan är en händelsehanterare inställd för att hantera en enkel Grid-händelse med Visual Studio.NET.

**Steg 1: Välj en händelse av Aspose.Cells.GridDesktop Control**

1.  Visual Studio, välj Aspose.Cells.GridDesktop-kontrollen och öppna dess**Egenskaper**dialog.
1.  Klicka på**evenemang** flik.
1.  Välj en händelse. (för det här exemplet**CellClick** händelse är vald).

**Steg 2: Skapa en händelsehanterare**

1.  Dubbelklicka på en vald händelse i**Egenskaper**dialog.
1. När händelsen dubbelklickas skapas en händelsehanterare av Visual Studio.NET. Följande är designergenererad kod som visar att en händelse skapas för GridControl Control.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents.Designer-DesignerGeneratedCode.cs" >}}


 Lägg nu till kod för att utföra önskad operation i händelsehanteraren. För det här exemplet har vi lagt till en kodrad som visar en meddelanderuta för aviseringar.
Ta en titt på händelsehanteraren som visual Studio har lagt till i GridDesktop-kontrollens CellClick-händelse. Det kommer att se ut ungefär som koden nedan.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents-ClickEvent.cs" >}}


**Steg 3: Kör applikationen**

1. Bygg och kör applikationen.
1. När en rutnätscell klickas visas en meddelanderuta med meddelandet "Cell är klickad".
