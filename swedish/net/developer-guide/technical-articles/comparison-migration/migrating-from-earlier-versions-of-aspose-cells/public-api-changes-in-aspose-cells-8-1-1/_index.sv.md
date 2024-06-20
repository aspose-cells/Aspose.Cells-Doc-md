---
title: Offentliga API förändringar i Aspose.Cells 8.1.1
type: docs
weight: 50
url: /sv/net/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringar av Aspose.Cells API från version 8.1.0 till 8.1.1, som kan vara av intresse för modul/apputvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagd HtmlSaveOptions.PresentationPreference Egenskap**
HtmlSaveOptions-klassen har exponerat PresentationPreference-egenskapen som kan användas för att rendera resultaten med bättre layout vid export av kalkylblad till HTML eller MHTML. Standardvärdet är false. om det är inställt på true, kommer Aspose.Cells API att exportera kalkylbladets innehåll med bättre presentation.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Använd PresentationPreference-alternativ för bättre layout](/cells/sv/net/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}}
## **Tillagt stöd för kalkylblads-scenarier**
Ett scenario är en s.k. om-prov-modell som inkluderar variabla inmatningsceller kopplade av ett eller flera formler. Aspose.Cells API har exponerat Worksheet.Scenarios-egenskapen tillsammans med följande klasser för att underlätta användarna att skapa, manipulera och ta bort scenarier från kalkylblad, 

1. Scenario: Representerar ett individuellt scenario.
1. ScenarioCollection: Representerar en samling scenarier.
1. ScenarioInputCellCollection: Representerar en lista med inmatningsceller för ett specifikt scenario.
1. ScenarioInputCell: Representerar en inmatningscell från samlingen med inmatningsceller för ett specifikt scenario.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Hur man skapar, manipulerar eller tar bort scenarier från kalkylblad](/cells/sv/net/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
