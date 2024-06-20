---
title: Arbeta med Aspose.Cells.GridDesktop händelser
type: docs
weight: 30
url: /sv/net/aspose-cells-griddesktop/work-with-aspose-cells-griddesktop-events/
keywords: GridDesktop, händelse, händelser
description: Den här artikeln introducerar hur man använder händelser i GridDesktop.
---

{{% alert color="primary" %}} 

Händelser används för att skicka meddelanden när en förändring sker i en kontroll eller klass. Aspose.Cells.GridDesktop har flera händelser som används för att utföra specifika uppgifter när vissa förändringar inträffar i kontrollen. Det här ämnet ger en introduktion till alla händelser som stöds av Aspose.Cells.GridDesktop-kontrollen och förklarar hur man hanterar dessa händelser.

{{% /alert %}} 
## **Introduktion**
Aspose.Cells.GridDesktop-kontrollen stöder flera händelser som ger mer kontroll för att utföra operationer när specifika händelser utlöses. Nedan följer en komplett lista över händelser som stöds av Aspose.Cells.GridDesktop-kontrollen.

{{% alert color="primary" %}} 

Denna lista inkluderar inte händelser som är ärvt av Aspose.Cells.GridDesktop från Control-klassen.

{{% /alert %}} 

|**Händelser**|**Beskrivning**|
| :- | :- |
|BeforeCalculate| Uppstår före beräkna formel i kalkylblad.|
|BeforeLoadFile| Uppstår innan arbetsbok laddas från fil.|
|ColumnHeaderClick| Uppstår när kolumnrubriken klickas på.|
|ColumnHeaderDoubleClick| Uppstår när kolumnrubriken dubbelklickas på.|
|CellDataChanged| Uppstår när datan eller värdet i en gridcell ändras. Denna händelse kan också utlösas om en cells värde ändras programmatiskt med hjälp av Value-egenskapen eller SetCellValue-metoden i en GridCell.|
|CellButtonClick| Uppstår när cellknappen klickas på.|
|CellCheckedChanged| Uppstår när Checked-egenskapen för cellens kryssruta ändras.|
|CellSelectedIndexChanged| Uppstår när SelectedIndex-egenskapen för cellens kombinationsruta ändras.|
|CellClick| Uppstår när en gridcell klickas på.|
|CellDoubleClick|Uppstår när en gridcell dubbelklickas på.|
|CellKeyPressed| Uppstår när en tangent trycks ned medan en cell har fokus. Om du vill skapa en händelsehanterare för CellKeyPressed-händelsen, ställ in Handled-egenskapen för CellKeyEventArgs-argumentet till true för att förhindra att GridDesktop-kontrollen hanterar tangenthändelsen.|
|AfterInsertColumns| Uppstår när en kolumn infogas. Du kan få kolumnindexet genom att använda Index-egenskapen i Aspose.Cells.GridDesktop.WorksheetEventArgs-argumentet.|
|AfterInsertRows| Uppstår när en rad infogas. Du kan få radindexet genom att använda Index-egenskapen i Aspose.Cells.GridDesktop.WorksheetEventArgs-argumentet.|
|FailLoadFile| Uppstår när det misslyckas att ladda arbetsboken.|
|FinishCalculate| Uppstår efter beräkna formel i arbetsboken.|
|FinishLoadFile| Uppstår när arbetsboken laddas.|
|FocusedCellChanged| Uppstår när en cells fokus ändras.|
|RowHeaderClick| Uppstår när radrubriken klickas på.|
|RowHeaderDoubleClick| Uppstår när radrubriken dubbelklickas på.|
|RowColumnHiddenChanged| Uppstår när radens eller kolumnens dolda status ändras.|
|SelectedSheetIndexChanged| Uppstår när en användare väljer ett nytt kalkylblad, det vill säga när det valda kalkylarket ändras från ett kalkylblad till ett annat. Denna händelse kan också utlösas programmatiskt om GridDesktop-kontrollens ActiveSheetIndex-egenskap ändras.|
## **Hantering av rutnätshändelser**
För att utföra en specifik operation när en specifik händelse inträffar, skapa en händelsehanterare. En händelsehanterare utför en viss uppgift när en viss händelse inträffar. Nedan är en händelsehanterare inställd för att hantera en enkel Grid-händelse med hjälp av Visual Studio.NET.

**Steg 1: Välja en händelse av Aspose.Cells.GridDesktop Control**

1. I Visual Studio, välj Aspose.Cells.GridDesktop kontrollen och öppna dess **Egenskaper** dialogruta.
1. Klicka på fliken **Händelser**.
1. Välj en händelse. (för detta exempel är händelsen **CellClick** vald).

**Steg 2: Skapa en händelsehanterare**

1. Dubbelklicka på en vald händelse i **Egenskaper** dialogrutan.
1. När händelsen dubbelklickas skapas en händelsehanterare av Visual Studio.NET. Följande är kod som genererats av designern som visar att en händelse skapas för GridControl Control.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents.Designer-DesignerGeneratedCode.cs" >}}


Lägg nu till kod för att utföra den önskade operationen i händelsehanteraren. För detta exempel har vi lagt till en rad kod som visar en meddelandefruta för aviseringar. 
Ta en titt på händelsehanteraren som visual Studio har lagt till i GridDesktop kontrollens CellClick-händelse. Det kommer att se ut ungefär som koden nedan.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents-ClickEvent.cs" >}}


**Steg 3: Kör applikationen**

1. Bygg och kör applikationen.
1. Varje gång en cell i rutan klickas visas en meddelandefruta med meddelandet "Cell is Clicked".
