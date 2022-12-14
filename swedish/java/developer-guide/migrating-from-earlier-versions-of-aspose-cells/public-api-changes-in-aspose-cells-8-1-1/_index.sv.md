---
title: Offentliga API-ändringar i Aspose.Cells 8.1.1
type: docs
weight: 60
url: /sv/java/public-api-changes-in-aspose-cells-8-1-1/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringar av Aspose.Cells API från version 8.1.0 till 8.1.1, som kan vara av intresse för modul- och applikationsutvecklare. Det inkluderar inte bara[nya och uppdaterade offentliga metoder](/cells/sv/java/public-api-changes-in-aspose-cells-8-1-1/) , men även en beskrivning av ev[förändringar i beteendet](/cells/sv/java/public-api-changes-in-aspose-cells-8-1-1/) bakom kulisserna på Aspose.Cells.

{{% /alert %}} 
## **Tillagda egenskaper och funktioner**
### **Lade till egenskapen HtmlSaveOptions.PresentationPreference**
Klassen HtmlSaveOptions har exponerat getter/setter för PresentationPreference-egenskapen som kan användas för att rendera resultaten med bättre layout vid export av kalkylblad till HTML eller MHTML. Standardvärdet är falskt. medan om satt till sant, exporterar API:et Aspose.Cells kalkylbladets innehåll med bättre presentation.

{{% alert color="primary" %}} 

 Vänligen kontrollera den detaljerade artikeln om[Använd PresentationPreference Option för bättre layout](/cells/sv/java/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}} 
### **Tillagt stöd för arbetsbladsscenarier**
Ett scenario är en vad-om-modell som inkluderar variabla indataceller länkade med en eller flera formler. Aspose.Cells har avslöjat en getter och seter för egenskapen Worksheet.Scenarios tillsammans med följande klasser för att hjälpa utvecklare att skapa, manipulera och ta bort scenarier.

1. Scenario: Representerar ett individuellt scenario.
1. ScenarioCollection: Representerar en samling scenarier.
1. ScenarioInputCellCollection: Representerar en lista med indataceller för ett visst scenario.
1. ScenarioInputCell: Representerar en indatacell från samlingen av indataceller för ett visst scenario.

{{% alert color="primary" %}} 

 Vänligen kontrollera den detaljerade artikeln om[Hur man skapar, manipulerar eller tar bort scenarier från arbetsblad](/cells/sv/java/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
## **Ändring i beteende för CellsException**
Med tidigare versioner av Aspose.Cells för Java API, när ett eventuellt skadat kalkylblad laddades i en instans av Workbook, tenderade API:et att skicka ett allmänt meddelande utan att nämna var problemet kunde vara. Vi har ändrat detta beteende för 8.1.1 så att API:et kastar ett undantag med ett meningsfullt meddelande som pekar ut var (vilken cell) och vad (formeluttryck) som orsakar undantaget vid läsning av mallfilen.
