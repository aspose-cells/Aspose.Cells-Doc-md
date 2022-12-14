---
title: Offentliga API-ändringar i Aspose.Cells 8.1.1
type: docs
weight: 50
url: /sv/net/public-api-changes-in-aspose-cells-8-1-1/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringar av Aspose.Cells API från version 8.1.0 till 8.1.1, som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **HtmlSaveOptions.PresentationPreference Property har lagts till**
Klassen HtmlSaveOptions har exponerat egenskapen PresentationPreference som kan användas för att rendera resultaten med bättre layout vid export av kalkylblad till HTML eller MHTML. Standardvärdet är falskt. medan om satt till sant, kommer Aspose.Cells API att exportera kalkylbladets innehåll med bättre presentation.

{{% alert color="primary" %}} 

 Vänligen kontrollera den detaljerade artikeln om[Använd PresentationPreference Option för bättre layout](/cells/sv/net/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}}
## **Tillagt stöd för arbetsbladsscenarier**
 Ett scenario kallas vad-om-modellen som inkluderar variabla indataceller länkade samman med en eller flera formler i enlighet därmed. Aspose.Cells API har exponerat egendomen Worksheet.Scenarios tillsammans med följande klasser för att underlätta för användarna att skapa, manipulera och ta bort scenarier från kalkylblad,

1. Scenario: Representerar ett individuellt scenario.
1. ScenarioCollection: Representerar en samling scenarier.
1. ScenarioInputCellCollection: Representerar en lista med indataceller för ett visst scenario.
1. ScenarioInputCell: Representerar en ingångscell från samlingen av indataceller för ett visst scenario.

{{% alert color="primary" %}} 

 Vänligen kontrollera den detaljerade artikeln om[Hur man skapar, manipulerar eller tar bort scenarier från arbetsblad](/cells/sv/net/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
