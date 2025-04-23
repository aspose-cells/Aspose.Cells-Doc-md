---
title: Offentliga API förändringar i Aspose.Cells 8.1.1
type: docs
weight: 60
url: /sv/java/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringar av Aspose.Cells API från version 8.1.0 till 8.1.1, som kan vara av intresse för modul- och applikationsutvecklare. Det inkluderar inte bara [nya och uppdaterade offentliga metoder](/cells/sv/java/public-api-changes-in-aspose-cells-8-1-1/), utan också en beskrivning av eventuella [förändringar i beteendet](/cells/sv/java/public-api-changes-in-aspose-cells-8-1-1/) bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda egenskaper och funktioner**
### **Tillagt HtmlSaveOptions.PresentationPreference-egenskapen**
HtmlSaveOptions-klassen har exponerat getter/setter för PresentationPreference-egenskapen som kan användas för att rendera resultaten med bättre layout vid export av kalkylblad till HTML eller MHTML. Standardvärdet är false. om det sätts till true, exporterar Aspose.Cells API kalkylbladens innehåll med bättre presentation.

{{% alert color="primary" %}} 

Vänligen kontrollera den detaljerade artikeln om [Använd PresentationPreference-alternativet för bättre layout](/cells/sv/java/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}} 
### **Tillagt stöd för kalkylblads-scenarier**
Ett scenario är en vad-om-modell som inkluderar variabla ingångsceller länkade tillsammans av en eller flera formler. Aspose.Cells har exponerat en getter och setter för Arbetsblad.Scenarios-egenskapen tillsammans med följande klasser för att hjälpa utvecklare att skapa, manipulera och ta bort scenarier.

1. Scenario: Representerar ett individuellt scenario.
1. ScenarioCollection: Representerar en samling scenarier.
1. ScenarioInputCellCollection: Representerar en lista med inmatningsceller för ett visst scenario.
1. ScenarioInputCell: Representerar en inmatningscell från samlingen av inmatningsceller för ett visst scenario.

{{% alert color="primary" %}} 

Vänligen kontrollera den detaljerade artikeln om [Hur man skapar, manipulerar eller tar bort scenarier från arbetsblad](/cells/sv/java/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
## **Ändring av beteende för CellsException**
Med tidigare versioner av Aspose.Cells for Java API, när en eventuellt skadad kalkyl laddades i en instans av Arbetsbok, tenderade API:et att kasta ett generiskt meddelande utan att ange var problemet kunde finnas. Vi har ändrat detta beteende för 8.1.1 så att API:et kastar ett undantag med ett meningsfullt meddelande som pekar ut var (vilken cell) och vad (formeluttryck) som orsakar undantaget när mallfilen läses.
{{< app/cells/assistant language="java" >}}
